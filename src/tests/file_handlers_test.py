import asyncio
import unittest
from unittest.mock import AsyncMock, patch

from fastapi import UploadFile

from src.services import file_handlers


class TestFileHandlers(unittest.TestCase):

    @patch("services.file_handlers.create_directories")
    @patch("services.file_handlers.extract_zip", return_value="/extracted/path")
    @patch(
        "services.file_handlers.open", new_callable=unittest.mock.mock_open, create=True
    )
    def test_handle_file_upload(self, mock_open, mock_extract_zip, mock_create_dirs):
        async def run_test():
            mock_file = AsyncMock(spec=UploadFile)
            mock_file.filename = "test.zip"
            mock_file.read = AsyncMock(return_value=b"data")
            result = await file_handlers.handle_file_upload(mock_file)
            self.assertEqual(result, {"files_path": "/extracted/path"})

        asyncio.run(run_test())

    @patch("services.file_handlers.read_code_files", return_value="code")
    @patch("services.file_handlers.openai_analyzer", return_value={"score": "8"})
    @patch("services.file_handlers.score_calculator", return_value="passed")
    @patch("services.file_handlers.report_store")
    def test_analyze_code_files(self, mock_store, mock_score, mock_analyzer, mock_read):
        async def run_test():
            folder_path = {"files_path": "/path/to/files"}
            result = await file_handlers.analyze_code_files(folder_path)
            self.assertIn("status", result)
            self.assertEqual(result["status"], "passed")

        asyncio.run(run_test())


if __name__ == "__main__":
    unittest.main()
