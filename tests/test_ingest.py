from unittest.mock import patch, MagicMock
from src.ingest import ingest_text

@patch("src.ingest.index")
@patch("src.ingest.embed_text")
def test_ingest_text(mock_embed, mock_index):
    # Mock return values
    mock_embed.return_value = [0.1, 0.2, 0.3]
    
    text = "This is a test document. It has enough content for multiple chunks maybe."
    # With chunk_size=500, it'll likely be one chunk.
    # Let's mock chunk_text as well if we want to be sure of multiple chunks, 
    # but testing the flow is more important.
    
    num_chunks = ingest_text(text, source="test_source")
    
    # Assertions
    assert num_chunks > 0
    assert mock_index.upsert.called
    
    # Check if upsert was called with vectors
    args, kwargs = mock_index.upsert.call_args
    assert "vectors" in kwargs
    vectors = kwargs["vectors"]
    assert len(vectors) == num_chunks
    assert vectors[0]["metadata"]["source"] == "test_source"
    assert vectors[0]["values"] == [0.1, 0.2, 0.3]
