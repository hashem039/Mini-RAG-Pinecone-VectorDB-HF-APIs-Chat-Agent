from unittest.mock import MagicMock, patch
from src.pdf_utils import extract_text_from_pdf

@patch("src.pdf_utils.PdfReader")
def test_extract_text_from_pdf(mock_pdf_reader):
    # Mock page objects
    mock_page1 = MagicMock()
    mock_page1.extract_text.return_value = "Page 1 text"
    
    mock_page2 = MagicMock()
    mock_page2.extract_text.return_value = "Page 2 text"
    
    # Configure mock reader
    mock_reader_instance = mock_pdf_reader.return_value
    mock_reader_instance.pages = [mock_page1, mock_page2]
    
    # Call the function
    result = extract_text_from_pdf("dummy_file_path")
    
    # Check results
    assert "Page 1 text" in result
    assert "Page 2 text" in result
    assert result.count("\n") >= 2
    
    # Ensure it was called for each page
    assert mock_page1.extract_text.called
    assert mock_page2.extract_text.called
