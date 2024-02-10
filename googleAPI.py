reviewsText = []
reviewsRating = []
reviewsAdditionalInformation = []
reviewSentAnalysis = []

reviewed = False

def googleAPIConn(placeName):
    import googlemaps
    from sentiment import sentAnalysis
    from visualization import visua
    from tokenization import tokenization_list
    from vectorization import tfid
    
    print("check")
    gmaps = googlemaps.Client(key="")
    try:
        place_res = gmaps.places(placeName)
        place_id = place_res['results'][0]['place_id']
        place = gmaps.place(place_id=place_id)
        print(place)
        for i in range(len(place['result']['reviews'])):
            textRev = place['result']['reviews'][i]['text']
            ratingRev = place['result']['reviews'][i]['rating']

            reviewsText.append(textRev)
            reviewsRating.append(ratingRev)
        reviewsAdditionalInformation.append({
            'Place_name': placeName,
            'Country': place['result']['address_components'][0]['long_name'],
            'short_country': place['result']['address_components'][0]['short_name'],
            'URL_link': place['result']['url'],
            'Website': place['result']['website']
        })
        for i in range(0,len(place['result']['address_components'])):
            if ( place['result']['address_components'][i]['types'][0] == 'country'):
                    reviewsAdditionalInformation[0]['Country'] = place['result']['address_components'][i]['long_name'];
                    reviewsAdditionalInformation[0]['short_country'] = place['result']['address_components'][i]['short_name'];
        
        print(reviewsAdditionalInformation)
        # for i in range(len(reviews)):
        #     print("review ",i,": ",reviews[i]['rating'])
        # print(reviewsAdditionalInformation[0]['Country'])
        # print(reviewsAdditionalInformation[0]['URL_link'])

        print(reviewsText)
        print(len(reviewsText))
        # token and lemma
        token_lema = tokenization_list(reviewsText)
        #tdif
        print("\n ------\n TIFD\n")
        vector_tfid = tfid(reviewsText)


        print(reviewsAdditionalInformation[0]['Website'])
        print("review ratings ->", reviewsRating)
        visua(sentAnalysis(reviewsText), reviewsRating,reviewsAdditionalInformation[0]['Place_name'], place_id)
        print("after visua")
        
        from export import export
        export(reviewsText,token_lema, vector_tfid, place_id,reviewsAdditionalInformation)
    except googlemaps.exceptions.ApiError:
        print("INVALID REQUEST\n")
    finally:
        print("VISUALIZE\n")


