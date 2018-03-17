import argparse

from base_gen.BaseGen import BaseGen
from base_gen.CsvManager import write_to_csv_file


def runner(args):
    base_gen = BaseGen()
    for i in range(args.iterations):
        data = base_gen.collect_articles_date(args.language, args.shortest_article)
        write_to_csv_file(args.file_name, data)
        print("{} - {}".format(args.language, i))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate data with language features.')
    parser.add_argument('-l', '--language', default='en',
                        help='Article language (type abbreviation, for example \'en\', \'pl\', default=\'en\')')
    parser.add_argument('-i', '--iterations', type=int, default=100,
                        help='Script iterations (default=100)')
    parser.add_argument('-f', '--file_name', default="base.csv",
                        help='Path to csv file where save data. default=\"base.csv\"')
    parser.add_argument('-s', '--shortest_article', type=int, default=500,
                        help='Shortest article length (characters), default=500')

    args = parser.parse_args()
    runner(args)
