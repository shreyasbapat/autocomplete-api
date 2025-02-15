import csv
from fast_autocomplete.misc import read_csv_gen


def get_words(path):

    csv_gen = read_csv_gen(path, csv_func=csv.DictReader)

    words = []

    for line in csv_gen:
        train_line = line['train_line']
        train_line.strip('"')
        print(train_line)
        words.append(train_line)
    return words