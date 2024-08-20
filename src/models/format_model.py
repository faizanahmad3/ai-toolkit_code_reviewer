from pydantic import BaseModel, Field


class Format(BaseModel):
    score: str = Field(
        description="give a score to critique based on the provided code, only a digit between 1-10"
    )
    summary: str = Field(
        description="give a summary of why did you give that score to critique of the given code"
    )


class Analyzer(BaseModel):
    files_path: str
    python: bool
    angular: bool
    flutter: bool
