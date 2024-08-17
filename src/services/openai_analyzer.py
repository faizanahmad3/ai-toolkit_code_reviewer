import tiktoken
from langchain.schema import AIMessage
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from openai import OpenAI

from src.config import settings as e_var
from src.models.format_model import Format
from src.utils.logger import setup_logger
from src.utils.utilities import chunk_code
import logging

info_logger = setup_logger(__name__, level=logging.INFO)
debug_logger = setup_logger(__name__, level=logging.DEBUG)
error_logger = setup_logger(__name__, level=logging.ERROR)
warning_logger = setup_logger(__name__, level=logging.WARNING)
e_var.load_env_vars()

client = OpenAI()


def critique_prompt():
    return """
        Act as a reviewer for Angular where you conduct code review, in a strict and professional manner, as part of a developer interview. You will be reviewing on the following criteria:
        Remember, just focus on the given criteria, and provide a concise critique.

        criteria:
        {criteria}

        Code to review:
        {code}

        critique:
        """


def score_prompt():
    return """
        Based on the following critique of the Angular code, provide a score between 1-10 based on how well the code meets the critique.
        Remember, just score between 1-10.

        critique:
        {critique}

        Code to review:
        {code}
        """


def openai_analyzer(code, criteria):
    try:
        tokenizer = tiktoken.encoding_for_model(e_var.model)
        max_tokens = 15000  # Leave some room for the prompt and criteria
        llm = ChatOpenAI(model_name=e_var.model, temperature=0)

        info_logger.info("Starting OpenAI code analysis.")

        code_chunks = chunk_code(code, max_tokens, tokenizer)
        critiques = []

        for chunk in code_chunks:
            critique_prompt_template = critique_prompt()
            first_prompt = PromptTemplate(
                template=critique_prompt_template,
                input_variables=["code", "criteria"],
            )

            critique_chain = first_prompt | llm
            chunk_critique = critique_chain.invoke(
                {"code": chunk, "criteria": criteria}
            )

            if isinstance(chunk_critique, AIMessage):
                chunk_critique = chunk_critique.content

            critiques.append(chunk_critique)
            info_logger.info(f"Critique generated for a chunk of code.")

        combined_critique = "\n".join(critiques)
        combined_critique_tokens = tokenizer.encode(combined_critique)
        if len(combined_critique_tokens) > max_tokens:
            combined_critique = tokenizer.decode(combined_critique_tokens[:max_tokens])
            warning_logger.warning("Combined critique was too long and was truncated.")

        parser = JsonOutputParser(pydantic_object=Format)
        second_prompt = PromptTemplate(
            template="Response in structure which is given.\n{format_instructions}\ncritique:\n{critique}\ncode:\n{code}\n",
            input_variables=["code", "critique"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        score_and_summary_chain = second_prompt | llm | parser

        code_summary = f"Code summary (total {len(code_chunks)} chunks analyzed)"
        score_and_summary = score_and_summary_chain.invoke(
            {"code": code_summary, "critique": combined_critique}
        )

        info_logger.info("OpenAI code analysis completed successfully.")
        return score_and_summary

    except Exception as e:
        error_logger.error(f"Error during OpenAI analysis: {e}")
        raise
