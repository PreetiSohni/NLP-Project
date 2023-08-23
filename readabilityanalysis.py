import nltk
from nltk.corpus import cmudict
from collections import defaultdict
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize, sent_tokenize
from tqdm import tqdm


nltk.download('punkt')
nltk.download('cmudict')
nltk.download('averaged_perceptron_tagger')

import string

# Initialize a dictionary to cache syllable counts

syllable_cache = defaultdict(int)


def avg_sen_length(len_word,len_sen):
    return len(len_word)/len(len_sen)

def avg_num_word_sen(len_word,len_sen):
    return len(len_word)/len(len_sen)


def remove_punctuation(text):
    translator = str.maketrans("", "", string.punctuation)
    clean_text = text.translate(translator)
    return clean_text

def syllable_count(word):
    if word.lower() in syllable_cache:
        return syllable_cache[word.lower()]

    d = cmudict.dict()
    if word.lower() in d:
        syllables = max([len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]])
        syllable_cache[word.lower()] = syllables
        return syllables
    else:
        return 1  # Default syllable count

def analyze_readability(text):
    words = word_tokenize(text)
    sentences = sent_tokenize(text)
    total_words = len(words)
    total_sentences = len(sentences)

    total_syllables = sum([syllable_count(word) for word in words])
    syllables_per_word = total_syllables / total_words

    tagged_words = pos_tag(words)
    personal_pronoun_count = sum([1 for word, tag in tagged_words if tag == 'PRP'])

    total_characters = sum([len(word) for word in words])
    average_word_length = total_characters / total_words

    return syllables_per_word, personal_pronoun_count, average_word_length

# Example text
# text = "This is an example sentence with some complex words and long sentences. It demonstrates the analysis of readability."

# # Analyze readability variables
# syllables_per_word, personal_pronoun_count, average_word_length = analyze_readability(text)
# print("Syllables per Word:", syllables_per_word)
# print("Personal Pronoun Count:", personal_pronoun_count)
# print("Average Word Length:", average_word_length)





def gunning_fog_index(text):
    words = nltk.word_tokenize(text)
    sentences = nltk.sent_tokenize(text)
    total_words = len(words)
    total_sentences = len(sentences)

    
    total_words = len(words)
    total_sentences = len(sentences)
    
    complex_words = [word for word in tqdm(words, desc="Calculating Syllable Counts") if syllable_count(word) >= 3]
    complex_word_count = len(complex_words)
    
    average_words_per_sentence = total_words / total_sentences
    percentage_complex_words = (complex_word_count / total_words) * 100
    
    fog_index = 0.4 * (average_words_per_sentence + percentage_complex_words)
    return fog_index,percentage_complex_words,complex_word_count

def syllable_count(word):
    if word.lower() in syllable_cache:
        return syllable_cache[word.lower()]
    
    d = cmudict.dict()
    if word.lower() in d:
        syllables = max([len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]])
        syllable_cache[word.lower()] = syllables
        return syllables
    else:
        return 1  # Default syllable count

# # Example text
# text = article_text

# # Calculate Gunning Fog Index
# index,per_complex_words,number_of_words,number_of_sentences,complex_word_count = gunning_fog_index(text)
# print("Gunning Fog Index:", index)
# print("percentage_complex_words:",per_complex_words)
# print("Number of words:",number_of_words)
# print("Number of sentences:",number_of_sentences)
# print("Number of complex words:",complex_word_count)







