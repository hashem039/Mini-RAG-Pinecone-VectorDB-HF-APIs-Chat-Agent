from src.rag_pipeline import filter_context, SIMILARITY_THRESHOLD

def test_filter_context_success():
    context = [
        {"score": 0.8, "metadata": {"text": "High score chunk."}},
        {"score": 0.6, "metadata": {"text": "Low score chunk."}},
        {"score": 0.9, "metadata": {"text": "Very high score chunk."}}
    ]
    
    result = filter_context(context)
    
    assert "High score chunk." in result
    assert "Very high score chunk." in result
    assert "Low score chunk." not in result

def test_filter_context_fallback():
    # All scores are below SIMILARITY_THRESHOLD
    context = [
        {"score": 0.1, "metadata": {"text": "Chunk 1"}},
        {"score": 0.2, "metadata": {"text": "Chunk 2"}},
        {"score": 0.3, "metadata": {"text": "Chunk 3"}},
        {"score": 0.4, "metadata": {"text": "Chunk 4"}}
    ]
    
    # filter_context: fallback if nothing passes threshold, take first 3 from context
    result = filter_context(context)
    
    assert "Chunk 1" in result
    assert "Chunk 2" in result
    assert "Chunk 3" in result
    assert "Chunk 4" not in result

def test_filter_context_empty():
    context = []
    result = filter_context(context)
    assert result == ""
