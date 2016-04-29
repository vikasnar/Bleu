import sys
import codecs
import os
import re
ref_counts = []
cand_dict = {}
debug = codecs.open('debug.txt', 'w', 'utf-8')


def count_ngram(cand, ref, n):
    candidate_file = codecs.open(cand, 'r', 'utf-8')
    for root, dirs, files in os.walk(ref):
        for f in files:
            reference_file = codecs.open(os.path.join(root, f), 'r', 'utf-8')
            for line in reference_file.readlines():
                count_dict = {}
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
                        ngram = words[i].lower()
                    if ngram in count_dict.keys():
                        count_dict[ngram] += 1
                    else:
                        count_dict[ngram] = 1
            for key, value in count_dict.iteritems():
                debug.write(u"{} - {}\n".format(key, value))
            debug.write("---------------\n")
            ref_counts.append(count_dict)
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
                for j in range(i, i + n):
                    ngram = "{} {}".format(ngram, words[j])
                ngram = ngram.strip().lower()
            else:
                ngram = words[i].lower()
            if ngram in cand_dict:
                cand_dict[ngram] += 1
            else:
                cand_dict[ngram] = 1
    for key, value in cand_dict.iteritems():
        debug.write(u"{} - {}\n".format(key, value))
    debug.write("---------------\n")


def precision():
    count_clip = 0
    count = sum(cand_dict.values())
    for m in cand_dict.keys():
        m_w = cand_dict[m]
        m_max = 0
        for ref in ref_counts:
            if m in ref:
                m_max = max(m_max, ref[m])
        m_w = min(m_w, m_max)
        count_clip += m_w
    print '{}/{}'.format(count_clip, count)
    return float(count_clip)/count


def main():
    count_ngram(sys.argv[1], sys.argv[2], 1)
    print precision()

main()
