from utils.clean import clean_up_sentence
import numpy as np
def bow(nltk,lemmatizer,sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(nltk,lemmatizer,sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))