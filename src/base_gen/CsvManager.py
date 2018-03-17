import csv
import os.path
import sys

BASE_FORMAT = ['language', 'page_id', 'average_world_len', 'vowel_ratio',
               'average_words_in_sentence', 'non_ascii_ratio', 'double_letter_ratio',
               'double_vowel_ratio',
               'a_ratio',
               'b_ratio',
               'c_ratio',
               'd_ratio',
               'e_ratio',
               'f_ratio',
               'g_ratio',
               'h_ratio',
               'i_ratio',
               'j_ratio',
               'k_ratio',
               'l_ratio',
               'm_ratio',
               'n_ratio',
               'o_ratio',
               'p_ratio',
               'q_ratio',
               'r_ratio',
               's_ratio',
               't_ratio',
               'u_ratio',
               'v_ratio',
               'w_ratio',
               'x_ratio',
               'y_ratio',
               'z_ratio']


def create_csv_file(path):
    try:
        with open(path) as f:
            pass
    except FileNotFoundError as fnfe:
        with open(path, 'w') as f:
            f.write(','.join(BASE_FORMAT))
            f.write('\n')


def write_to_csv_file(path, analysed):
    create_header = False if os.path.isfile(path) else True
    with open(path, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        if create_header:
            csv_writer.writerow(BASE_FORMAT)
        csv_writer.writerow(unwrap_analyse(analysed))


def unwrap_analyse(analysed):
    return [analysed['language'],
            analysed['page_id'],
            analysed['word_length'],
            analysed['vowel_ratio'],
            analysed['words_in_sentences'],
            analysed['non_ascii_ratio'],
            analysed['doubles_ratio']['doubles_letters'],
            analysed['doubles_ratio']['doubles_vowels'],
            ] + analysed['letter_ratio']
