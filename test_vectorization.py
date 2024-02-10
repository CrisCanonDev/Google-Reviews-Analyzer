from vectorization import tfid


def test_tfidf():
    input_list = ["This is a sample text.", "Another text."]
    expected_output = ["sample", "text"]

    result = tfid(input_list)
    assert result == expected_output
