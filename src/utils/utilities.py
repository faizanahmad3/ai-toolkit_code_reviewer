import json
import os
import zipfile
from typing import List

from fastapi import HTTPException

from src.config import settings as e_var
from src.utils.logger import setup_logger
import logging

info_logger = setup_logger(__name__, level=logging.INFO)
debug_logger = setup_logger(__name__, level=logging.DEBUG)
error_logger = setup_logger(__name__, level=logging.ERROR)
warning_logger = setup_logger(__name__, level=logging.WARNING)


def create_directories():
    try:
        os.makedirs(e_var.UPLOAD_FOLDER, exist_ok=True)
        os.makedirs(e_var.PROCESSED_FOLDER, exist_ok=True)
        os.makedirs(e_var.REPORT_FOLDER, exist_ok=True)
        info_logger.info(
            f"Directories '{e_var.UPLOAD_FOLDER}', '{e_var.PROCESSED_FOLDER}', and '{e_var.REPORT_FOLDER}' created successfully."
        )
    except Exception as e:
        error_logger.error(f"Error creating directories: {e}")
        raise HTTPException(status_code=500, detail="Error creating directories.")


def extract_zip(file_path):
    try:
        base_filename = os.path.basename(file_path).replace(".zip", "")
        extract_to_folder = os.path.join(e_var.PROCESSED_FOLDER, base_filename)
        os.makedirs(extract_to_folder, exist_ok=True)
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall(extract_to_folder)
        info_logger.info(f"Extracted files from '{file_path}' to '{extract_to_folder}'.")
        return extract_to_folder
    except Exception as e:
        error_logger.error(f"Error extracting zip file: {e}")
        raise HTTPException(status_code=500, detail="Error extracting zip file.")


def read_code_files(path: str, file_extension: tuple) -> str:
    code_files = []
    try:
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(file_extension):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as code_file:
                            code_files.append(code_file.read())
                    except UnicodeDecodeError:
                        warning_logger.warning(
                            f"Failed to decode {file} with UTF-8, trying with 'latin-1'."
                        )
                        try:
                            with open(file_path, "r", encoding="latin-1") as code_file:
                                code_files.append(code_file.read())
                        except Exception as e:
                            error_logger.error(
                                f"Failed to read file {file_path} with latin-1 encoding: {e}"
                            )
                            raise
                    except Exception as e:
                        error_logger.error(f"Failed to read file {file_path}: {e}")
                        raise
        full_code = "\n\n".join(code_files)
        return full_code
    except Exception as e:
        error_logger.error(
            f"An error occurred while reading code files from path '{path}': {e}"
        )
        raise


def score_calculator(scores) -> str:
    try:
        average_score = int(sum(scores) / len(scores))
        info_logger.info(f"The average score is: {average_score}")

        if average_score >= 7:
            return "passed"
        elif 5 <= average_score < 7:
            return "needs improvement"
        else:
            return "failed"
    except Exception as e:
        error_logger.error(f"Error calculating score: {e}")
        raise HTTPException(status_code=500, detail="Error calculating score.")


def report_store(path, report):
    try:
        base_filename = os.path.basename(path)
        report_folder_path = os.path.join(e_var.REPORT_FOLDER, base_filename)
        os.makedirs(report_folder_path, exist_ok=True)
        report_file_name = base_filename + ".json"
        report_file_path = os.path.join(report_folder_path, report_file_name)

        with open(report_file_path, "w") as file:
            json.dump(report, file, indent=4)

        info_logger.info(f"Report saved successfully at: {report_file_path}")
    except Exception as e:
        error_logger.error(f"Error saving report: {e}")
        raise HTTPException(status_code=500, detail="Error saving report.")


def chunk_code(code: str, max_tokens: int, tokenizer) -> List[str]:
    try:
        tokens = tokenizer.encode(code)
        chunks = []
        for i in range(0, len(tokens), max_tokens):
            chunk = tokenizer.decode(tokens[i : i + max_tokens])
            chunks.append(chunk)
        info_logger.info(f"Code split into {len(chunks)} chunks for analysis.")
        return chunks
    except Exception as e:
        info_logger.error(f"An error occurred while chunking the code: {e}")
        raise
