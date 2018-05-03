import random
import string
import csv

CHARACTERS = string.punctuation.translate({ord(c): None for c in ".!?\"\'"}) + \
             string.ascii_letters * 2 + string.ascii_lowercase * 4
CHARACTERS_LEN = len(CHARACTERS)


def generate_random_corpus(sentences_count, corpus_path):
    for i in range(sentences_count):
        words_in_sentence = random.randint(1, 30)
        text = "{}.".format(__generate_random_sentence(words_in_sentence))
        with open(corpus_path, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter='\t')
            csv_writer.writerow([text, "RN"])
        print("{}/{} Sentence saved".format(i + 1, sentences_count))


def __generate_random_word(word_length):
    word = ""
    for i in range(word_length):
        random_index = random.randint(0, CHARACTERS_LEN - 1)
        random_letter = CHARACTERS[random_index]
        word = "{}{}".format(word, random_letter)
    return word


def __generate_random_sentence(sentence_length):
    sentence = ""
    for i in range(sentence_length):
        word_length = random.randint(1, 16)
        word = __generate_random_word(word_length)
        if i > 0:
            sentence = "{} {}".format(sentence, word)
        else:
            sentence = "{}{}".format(sentence, word)
    return sentence


def __generate_random_text(sentences_count):
    text = ""
    while sentences_count > 0:
        words_in_sentence = random.randint(1, 30)
        sentence = __generate_random_sentence(words_in_sentence)
        text = "{}{}.".format(text, sentence)
        sentences_count -= 1
    return text
