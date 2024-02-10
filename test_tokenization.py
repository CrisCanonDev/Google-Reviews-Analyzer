import pytest
# Assuming there's a tokenize function in your NLP program
from tokenization import tokenization_list


def test_tokenization():
    input_list = ["Hello, how are you?", "I am doing well."]

    result = tokenization_list(input_list)
    assert isinstance(result, list)
    assert len(result) == len(input_list)
    for word in result:
        assert isinstance(word, str)
