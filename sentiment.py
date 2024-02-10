from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentAnalysis(revText):
    reviewSentAnalysis = []
    percent_Sentiment = 0
    for i in range(len(revText)):
        sa = SentimentIntensityAnalyzer()
        score = sa.polarity_scores(revText[i])
        percent_Sentiment = round(score['compound'], 2)
        reviewSentAnalysis.append(percent_Sentiment)
        
    print("SENTIMENT ANALISIS ->",reviewSentAnalysis) 
    return reviewSentAnalysis