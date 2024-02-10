import matplotlib.pyplot as plt
import os

from visualization import visua


def test_visua():
    input_list_sent = [0.2, -0.5, 0.8, 0.4, -0.1]
    input_list_rating = [4, 2, 5, 4, 3]
    title = "Sample Visualization"
    place_id = "sample_place"

    # Call the function to generate the plot
    visua(input_list_sent, input_list_rating, title, place_id)

    # Verify if the plot file is created
    assert os.path.exists('graphs_result/sample_place.png')

    # Clean up the generated plot file
    os.remove('graphs_result/sample_place.png')
