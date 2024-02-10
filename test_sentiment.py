from sentiment import sentAnalysis


def test_sentiment_analysis():
    input_text = ["I love this product!", "It's not that great."]
    expected_output = [0.67, -0.51]

    result = sentAnalysis(input_text)
    assert result == expected_output
