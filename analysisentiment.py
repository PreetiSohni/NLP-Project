


def read_text_file_return_list(file_path):
    with open(file_path,'r') as file:
        words=file.readlines()
        
    list_of_words=[word.strip() for word in words ]
    list_of_words=[word.lower() for word in list_of_words]
    
    return list_of_words





def text_sentiment_variables(article_list_words,stop_words,pos_words,neg_words):
    """
    Args - list of words of article test, list of stop words, list of positive words,list of negative words
    
    return - total_words_after_cleaning,positive score, negative score, polarity score, subjectivity score
    
    """

    filtered_article_words=[word for word in article_list_words if word.lower() not in stop_words]
    total_words_after_cleaning=len(filtered_article_words)
    positive_score=sum([1 for word in filtered_article_words if word in pos_words])
    negative_score=sum([-1 for word in filtered_article_words if word in neg_words])*(-1)
    polarity_score=(positive_score-negative_score)/((positive_score+negative_score)+0.000001)
    subjectivity_score=(positive_score+negative_score)/((total_words_after_cleaning)+0.000001)

    return total_words_after_cleaning,positive_score,negative_score,polarity_score,subjectivity_score