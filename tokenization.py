import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

sentence_token = []
cleaned= []
total_token = []
word_token = []

def get_part_of_speech_tags(token):
     # We are focusing on Verbs, Nouns, Adjectives and Adverbs here.
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    # eg. from [('She', 'PRP')] get P
    tag = nltk.pos_tag([token])[0][1][0].upper()
    return tag_dict.get(tag, wordnet.NOUN)

def tokenization_list(list):
    for item in list:
        print("INDEX ",list.index(item)+1) 
        tokens = item.split()# tokenization
   
        clean_tokens = tokens[:]  # copy the token list
        for token in tokens:  # for each token (word)
            if token.lower() in stopwords.words('english'):  # if it is a stop word
                clean_tokens.remove(token)  # remove it
        # print("CLEAN TOKENS",clean_tokens)
                
   
        current_lemmatize = []
        for token in clean_tokens: #Lematization
            
            lemmatizer = WordNetLemmatizer()
            lemmatisedtoken = lemmatizer.lemmatize(token, get_part_of_speech_tags(token))
            # print("TOKEN- LEMMA",  token, lemmatisedtoken)
            current_lemmatize.append(lemmatisedtoken)
        print("Lema ",current_lemmatize)
        print("Cleaned: ",clean_tokens)
        print("Cleaned LEN: ",len(clean_tokens))
        
    
        freq = nltk.FreqDist(clean_tokens)  #calculate frequency (occurance) of each word
        print(freq)
        maxVal = 0
        maxWord = 0
        for key,val in freq.items():
            if val > maxVal:
                maxVal = val
                maxWord = key
        print("The text is about: ",maxWord)
        word_token.append(maxWord)
    # freq.plot(cumulative=False)
        print("======\n")
        
    return word_token