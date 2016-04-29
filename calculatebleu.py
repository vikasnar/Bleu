import sys
import codecs
import re
c_dict = {}
r_dict = {}


def count_ngram(ref, n):
    reference_file = codecs.open(ref, 'r', 'utf-8')
    for line in reference_file.readlines():
        line = re.sub("[^\w']", ' ', line)
        words = line.strip().split()
        if n > 1:
            limits = len(words) - n + 1
        else:
            limits = len(words)
        for i in range(0, limits):
            ngram = ""
            if n > 1:
                for j in range(i, i+n):
                    ngram = "{} {}".format(ngram, words[j])
                ngram = ngram.strip().lower()
            else:
                ngram = words[i]
            if ngram in c_dict.keys():
                c_dict[ngram] += 1
            else:
                c_dict[ngram] = 1


def precison(cand, n):
    candidate_file = codecs.open(cand, 'r', 'utf-8')
    count = 0
    for line in candidate_file.readlines():
        line = re.sub("[^\w']", ' ', line)
        words = line.strip().split()
        if n > 1:
            limits = len(words) - n + 1
        else:
            limits = len(words)
        for i in range(0, limits):
            ngram = ""
            if n > 1:
                for j in range(i, i+n):
                    ngram = "{} {}".format(ngram, words[j])
                ngram = ngram.strip().lower()
            else:
                ngram = words[i]
            if ngram in c_dict.keys() and c_dict[ngram] > 0:
                c_dict[ngram] -= 1
                count += 1
    print "{}/{}".format(count, limits)
    return float(count)/limits


def main():
    count_ngram(sys.argv[2], 2)
    print precison(sys.argv[1], 2)

main()
