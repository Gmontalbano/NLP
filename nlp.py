import spacy

def data(postedData):
        #Step 1 is to read the data
        text1 = postedData["text1"]
        text2 = postedData["text2"]

        return text1, text2

def similarity(text1, text2, language):
    #Calculate edit distance between text1, text2
        if language=="portuguese":
            nlp = spacy.load('pt_core_news_sm')
        elif language=="english":
            nlp = spacy.load('en_core_web_sm')
        elif language=="spanish":
            nlp = spacy.load('es_core_news_sm')
         
        text1 = nlp(text1)
        text2 = nlp(text2)
        ratio = text1.similarity(text2)
    
        return ratio