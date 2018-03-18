import argparse

from base_gen.ArticleGetter import ArticleGetter


def save_text(text, corpus_file):
    with open(corpus_file, "a") as file:
        file.write(" {}".format(text))


def runner(args):
    article_getter = ArticleGetter()
    for i in range(args.iterations):
        text = article_getter.get_article(args.language, args.shortest_article)
        save_text(text, args.corpus_file)
        print("{} - get {} article out of {}".format(args.language, i+1, args.iterations))
    print("Articles saved to {}".format(args.corpus_file))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Save cleared articles from wikipedia in one file.')
    parser.add_argument('-l', '--language', default='en',
                        help='Article language (type abbreviation, for example \'en\', \'pl\', default=\'en\')')
    parser.add_argument('-i', '--iterations', type=int, default=100,
                        help='Script iterations (default=100)')
    parser.add_argument('-c', '--corpus_file', default="corpus.txt",
                        help='Path to txt file where save article texts. default=\"corpus.txt\"')
    parser.add_argument('-s', '--shortest_article', type=int, default=500,
                        help='Shortest article length (characters), default=500')

    args = parser.parse_args()
    runner(args)
