import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def visua(listSent, listRating, title, placeID):

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
