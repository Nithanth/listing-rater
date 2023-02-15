import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

def flesch_kincaid_readability(text):
    # Tokenize the input text into sentences and words
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    # Count the number of words, sentences, and syllables
    num_words = len(words)
    num_sentences = len(sentences)
    num_syllables = 0

    # Count the number of syllables in each word using the CMU Pronouncing Dictionary
    cmu_dict = nltk.corpus.cmudict.dict()
    for word in words:
        if word.lower() in cmu_dict:
            num_syllables += max([len(list(y for y in x if y[-1].isdigit())) for x in cmu_dict[word.lower()]])

    # Calculate the Flesch-Kincaid readability score
    score = 0.39 * (num_words / num_sentences) + 11.8 * (num_syllables / num_words) - 15.59

    # Round the score to two decimal places
    score = round(score, 2)

    return score

def ease(score):
    score *= 100
    if score >= 90 and score <= 100:
        return 'very_easy'
    elif score >= 80 and score < 90:
        return 'easy'
    elif score >= 70 and score < 80:
        return 'fairly_easy'
    elif score >= 60 and score < 70:
        return 'standard'
    elif score >= 50 and score < 60:
        return 'fairly_difficult'
    elif score >= 30 and score < 50:
        return 'difficult'
    else:
        return 'very_confusing'


def test():
    text = "The quick brown fox jumps over the lazy dog. She sells seashells by the seashore."
    score = flesch_kincaid_readability(text)
    print(score)
    print(ease(score))

test()