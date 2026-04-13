from src.rag_utils import chunk_text

def test_chunk_text_basic():
    text = "This is a test sentence for chunking."
    chunk_size = 10
    overlap = 2
    chunks = chunk_text(text, chunk_size, overlap)
    
    # "This is a " (10)
    # "s a test s" (10) -> start: 10-2=8. text[8:18] = "a test sen"
    # Actually let's calculate:
    # 0:10 -> "This is a "
    # (10-2)=8:18 -> "a test sen"
    # (18-2)=16:26 -> "sentence f"
    # (26-2)=24:34 -> "e for chun"
    # (34-2)=32:42 -> "hunking."
    
    assert len(chunks) > 0
    assert "".join(chunks).startswith("This")

def test_chunk_text_no_overlap():
    text = "ABCDEFGHIJ"
    chunk_size = 5
    overlap = 0
    chunks = chunk_text(text, chunk_size, overlap)
    
    assert chunks == ["ABCDE", "FGHIJ"]

def test_chunk_text_small_input():
    text = "Short"
    chunk_size = 10
    overlap = 2
    chunks = chunk_text(text, chunk_size, overlap)
    
    assert chunks == ["Short"]

def test_chunk_text_exact_size():
    text = "1234567890"
    chunk_size = 5
    overlap = 0
    chunks = chunk_text(text, chunk_size, overlap)
    
    assert chunks == ["12345", "67890"]
