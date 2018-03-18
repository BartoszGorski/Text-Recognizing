import argparse

from base_gen.BaseGen import BaseGen


def runner(args):
    base_gen = BaseGen()
    base_gen.generate_base(args.corpus_file, args.base_file, args.language)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate data with language features.')
    parser.add_argument('-c', '--corpus_file', default="corpus.txt",
                        help='Path to txt file where save article texts. default=\"corpus.txt\"')
    parser.add_argument('-b', '--base_file', default="base.csv",
                        help='Path to csv file where save data. default=\"base.csv\"')
    parser.add_argument('-l', '--language', default='en',
                        help='Article language (type abbreviation, for example \'en\', \'pl\', default=\'en\')')

    args = parser.parse_args()
    runner(args)
