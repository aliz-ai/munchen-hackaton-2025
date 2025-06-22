# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Test cases for the Academic Research Tools."""

import pytest
from unittest.mock import patch, MagicMock

def test_import_download_pdf():
    """Tests that the download_pdf function can be imported."""
    from academic_research.tools import download_pdf
    assert callable(download_pdf)

@patch('requests.get')
def test_download_pdf_success(mock_get):
    """Tests the download_pdf function's success path."""
    # Arrange
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = None
    mock_response.iter_content.return_value = [b'%PDF-1.4\n', b'1 0 obj\n', b'<< /Type /Catalog /Pages 2 0 R >>\n', b'endobj\n']
    mock_get.return_value = mock_response

    # Act
    from academic_research.tools import download_pdf
    result = download_pdf("http://example.com/test.pdf")

    # Assert
    assert result is not None
    assert "file_path" in result
    assert "pdf_content" in result
    assert result["file_path"].endswith("test.pdf")
