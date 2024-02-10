import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# def asign_colorPallete(val, colRange):
#     for range in colRange:
#         if val >= range[0] and val < range[1]:
#             return range[2]
#     return "gray"

# def ratingVal(listOfRating):
# colorRating=[]
# for val in listOfRating:
#     if val == 1:
#         colorRating.append('red')
#     elif val == 2:
#         colorRating.append('orange')
#     elif val == 3:
#         colorRating.append('yellow')
#     elif val == 4:
#         colorRating.append('lime')
#     elif val == 5:
#         colorRating.append('green')
# return colorRating


def visua(listSent, listRating, title, placeID):
    # rangeSentiment = [(-1, -0.6, "red"), (-0.6, -0.2, "orange"), (-0.2, 0.2, "yellow"), (0.2, 0.6, "lime"), (0.6, 1, "green")]
    # colorSent= [asign_colorPallete(val, rangeSentiment) for val in rangeSentiment]
    # colorRating = ratingVal(listRating)
    df = pd.DataFrame({
        "Sentiment Value": listSent,
        "Review Number": list('12345'),
        "Rating": listRating
    })
    figure, axes = plt.subplots(1, 2, sharex=True, figsize=(10, 5))
    figure.suptitle(title)
    axes[0].set_title('SENTIMENT VALUE PER REVIEW')
    axes[1].set_title('RATING PER REVIEW')
    sns.barplot(ax=axes[0], x='Review Number', y='Sentiment Value', data=df)
    sns.barplot(ax=axes[1], x='Review Number', y='Rating', data=df)
    folder_route = 'graphs_result/'
    plot = plt.savefig(folder_route+placeID+".png")
    return plot
