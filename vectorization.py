from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

vector_word = []
def tfid(list):
    vectorizer = TfidfVectorizer(stop_words='english')
    tf_idf_matrix = vectorizer.fit_transform(list)
    
    review_index = 0;
    for review in tf_idf_matrix.toarray():
        argmax = np.argmax(review)
        print("Review Number",review_index+1,": ",vectorizer.get_feature_names_out()[argmax])
        review_index += 1
        vector_word.append(vectorizer.get_feature_names_out()[argmax])

    return vector_word