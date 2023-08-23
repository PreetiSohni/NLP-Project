import pandas as pd
from openpyxl import load_workbook
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import cmudict
nltk.download('cmudict')

import webscrape as wb
import analysisentiment as ans
import readabilityanalysis as rda

excel_file = "F:\\arpit_nlp_project\\Output Data Structure.xlsx"
existing_data = pd.read_excel(excel_file)

url= "https://insights.blackcoffer.com/rise-of-telemedicine-and-its-impact-on-livelihood-by-2040-3-2/"

stop_word_file_path="F:\\arpit_nlp_project\\StopWords-20230807T050056Z-001\\StopWords\\StopWords_GenericLong.txt"
pos_file_path="F:\\arpit_nlp_project\\MasterDictionary-20230807T050056Z-001\\MasterDictionary\\positive-words.txt"
neg_file_path="F:\\arpit_nlp_project\\MasterDictionary-20230807T050056Z-001\\MasterDictionary\\negative-words.txt"

stop_words=ans.read_text_file_return_list(stop_word_file_path)
pos_words=ans.read_text_file_return_list(pos_file_path)
neg_words=ans.read_text_file_return_list(neg_file_path)

title,article_text=wb.extract_article_content(url)
clean_text=rda.remove_punctuation(article_text)
article_list_words=clean_text.split(" ")
article_list_sentence=clean_text.split('.')
word_count=len(article_list_words)

    
#### Sentimental Analysis ( Extracting derived variables - positive score, negative score, polarity score, subjectivity score )

total_words_after_cleaning,pos_scr,neg_scr,pol_scr,subj_scr=ans.text_sentiment_variables(article_list_words,stop_words,pos_words,neg_words)

### Analysis of readability ( Average sentence length, Gunning fog index, complex word count
 ### percentage_complex_words,total cleaned word  )

avg_sen_length=rda.avg_sen_length(article_list_words,article_list_sentence)

fog_index,percentage_complex_words,complex_word_count = rda.gunning_fog_index(article_text)

total_cleaned_words=total_words_after_cleaning

syllables_per_word, personal_pronoun_count, average_word_length=rda.analyze_readability(clean_text)

new_data={"POSITIVE SCORE":pos_scr,"NEGATIVE SCORE":neg_scr,"POLARITY SCORE":pol_scr,
          "SUBJECTIVITY SCORE":subj_scr,"AVG SENTENCE LENGTH":avg_sen_length,"PERCENTAGE OF COMPLEX WORDS":percentage_complex_words,
          "FOG INDEX":fog_index,"AVG NUMBER OF WORDS PER SENTENCE":average_word_length,
          "COMPLEX WORD COUNT":complex_word_count,"WORD COUNT":word_count,
          "SYLLABLE PER WORD":syllables_per_word,"PERSONAL PRONOUNS":personal_pronoun_count,"AVG WORD LENGTH":average_word_length}

condition = (existing_data['URL'] == url)

existing_data.loc[condition,["POSITIVE SCORE","NEGATIVE SCORE","POLARITY SCORE","SUBJECTIVITY SCORE",
                             "AVG SENTENCE LENGTH","PERCENTAGE OF COMPLEX WORDS","FOG INDEX","AVG NUMBER OF WORDS PER SENTENCE",
                             "COMPLEX WORD COUNT","WORD COUNT","SYLLABLE PER WORD","PERSONAL PRONOUNS",
                            "AVG WORD LENGTH" ]]=[new_data[column] for column in ["POSITIVE SCORE","NEGATIVE SCORE","POLARITY SCORE","SUBJECTIVITY SCORE",
                             "AVG SENTENCE LENGTH","PERCENTAGE OF COMPLEX WORDS","FOG INDEX","AVG NUMBER OF WORDS PER SENTENCE",
                             "COMPLEX WORD COUNT","WORD COUNT","SYLLABLE PER WORD","PERSONAL PRONOUNS",
                            "AVG WORD LENGTH" ]]

with pd.ExcelWriter(excel_file) as writer:
    existing_data.to_excel(writer)  





