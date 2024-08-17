import os
import unittest
from unittest.mock import MagicMock, patch

from src.utils.utilities import (
    create_directories,
    extract_zip,
    read_code_files,
    report_store,
)


class TestUtilityFunctions(unittest.TestCase):

    @patch("os.makedirs")
    @patch(
        "src.utilities.e_var"
    )  # Corrected to use 'src.utilities' instead of 'utility'
    def test_create_directories(self, mock_env, mock_makedirs):
        mock_env.UPLOAD_FOLDER = "/fake/upload"
        mock_env.PROCESSED_FOLDER = "/fake/processed"
        mock_env.REPORT_FOLDER = "/fake/report"
        create_directories()
        mock_makedirs.assert_any_call("/fake/upload", exist_ok=True)
        mock_makedirs.assert_any_call("/fake/processed", exist_ok=True)
        mock_makedirs.assert_any_call("/fake/report", exist_ok=True)

    @patch("zipfile.ZipFile")
    @patch("os.makedirs")
    @patch("src.utilities.e_var.PROCESSED_FOLDER", "/fake/processed")
    def test_extract_zip(self, mock_makedirs, mock_zipfile):
        mock_zipfile_instance = MagicMock()
        mock_zipfile.return_value.__enter__.return_value = mock_zipfile_instance

        result = extract_zip("/path/to/file.zip")

        expected_path = os.path.join("/fake/processed", "file")
        self.assertEqual(result, expected_path)
        mock_makedirs.assert_called_once()
        mock_zipfile_instance.extractall.assert_called_once()

    @patch("builtins.open", new_callable=unittest.mock.mock_open)
    @patch("os.walk")
    def test_read_code_files(self, mock_walk, mock_open):
        mock_walk.return_value = [("/path/to", ("dir",), ("file.ts",))]
        mock_open.return_value.read.return_value = "sample code"
        result = read_code_files("/path")
        self.assertEqual(result, "sample code")

    @patch("json.dump")
    @patch("builtins.open", new_callable=unittest.mock.mock_open)
    @patch("os.makedirs")
    @patch("src.utilities.e_var.REPORT_FOLDER", "/fake/report")
    def test_report_store(self, mock_makedirs, mock_open, mock_json_dump):
        report_store("/path/to/report", {"key": "value"})
        mock_open.assert_called_once_with(
            os.path.join("/fake/report", "report", "report.json"), "w"
        )
        mock_json_dump.assert_called_once()
