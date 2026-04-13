import sys
from unittest.mock import MagicMock

# Mock heavy/missing dependencies before they are imported by src
mock_modules = [
    "sentence_transformers",
    "pinecone",
    "pypdf",
    "streamlit",
    "dotenv",
    "requests",
]

for module_name in mock_modules:
    sys.modules[module_name] = MagicMock()

import pytest

@pytest.fixture
def mock_pinecone_index():
    return MagicMock()

@pytest.fixture
def mock_hf_response():
    return {
        "choices": [
            {
                "message": {
                    "content": "This is a mock answer from Hugging Face."
                }
            }
        ]
    }
