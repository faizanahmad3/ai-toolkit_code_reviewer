from typing import Dict

from fastapi import HTTPException, APIRouter, Depends

from src.models.format_model import Analyzer
from src.core.auth import get_api_key
from src.config import criteria_lists
from src.services.openai_analyzer import openai_analyzer
from src.utils.logger import setup_logger
from src.utils.utilities import (
    read_code_files,
    report_store,
    score_calculator,
)
import logging

info_logger = setup_logger(__name__, level=logging.INFO)
debug_logger = setup_logger(__name__, level=logging.DEBUG)
error_logger = setup_logger(__name__, level=logging.ERROR)
warning_logger = setup_logger(__name__, level=logging.WARNING)

analyzer_router = APIRouter()


@analyzer_router.post("/analyze_code/", dependencies=[Depends(get_api_key)])
async def analyze_code_files(req: Analyzer) -> Dict:
    try:
        path = req["files_path"]

        if req["python"]:
            criteria_list = criteria_lists.python_criteria_list
            file_extension = (".ts", ".html")
        elif req["angular"]:
            criteria_list = criteria_lists.angular_criteria_list
            file_extension = (".py", ".ipynb")
        elif req["react"]:
            criteria_list = criteria_lists.flutter_criteria_list
            file_extension = (".dart", ".yaml")
        else:
            raise HTTPException(status_code=500, detail="you didn't select any project to be analyze")

        full_code = read_code_files(path, file_extension)

        max_length = 1048570  # Maximum length allowed
        chunks = [
            full_code[i: i + max_length] for i in range(0, len(full_code), max_length)
        ]

        scores = []
        result = []

        for i, chunk in enumerate(chunks):
            for criteria in criteria_list:
                heading = criteria.split(":")[0].strip()
                info_logger.info(f"Generating response for criteria: {heading}")

                response = openai_analyzer(chunk, criteria)
                response["heading"] = f"{heading}"

                result.append(response)
                scores.append(int(response["score"]))

        status = score_calculator(scores)
        info_logger.info(
            f"Code analysis completed successfully for files in '{path}'. Status: {status}."
        )

        report = {"status": status, "detailed_report": result}
        report_store(path, report)

        return report

    except Exception as e:
        error_logger.error(f"Error analyzing code in path '{req}': {e}")
        raise HTTPException(status_code=500, detail="Error analyzing code.")
