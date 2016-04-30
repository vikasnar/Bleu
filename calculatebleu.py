import sys
import codecs
import os
import re

debug = codecs.open('debug.txt', 'w', 'utf-8')


def fetch_data(cand, ref):
    references = []
    for root, dirs, files in os.walk(ref):
        for f in files:
            reference_file = codecs.open(os.path.join(root, f), 'r', 'utf-8')
            references.append(reference_file.readlines())
    candidate_file = codecs.open(cand, 'r', 'utf-8')
    candidate = candidate_file.readlines()
    return candidate, references


def count_ngram(candidate, references, n):
    clipped_count = 0
    count = 0
    for si in range(len(candidate)):
        ref_counts = []
        for reference in references:
            ref_sentence = reference[si]
            ngram_d = {}
            ref_sentence = re.sub("[^\w']", ' ', ref_sentence)
            words = ref_sentence.strip().split()
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
                if ngram in ngram_d.keys():
                    ngram_d[ngram] += 1
                else:
                    ngram_d[ngram] = 1
            for key, value in ngram_d.iteritems():
                debug.write(u"{} - {}\n".format(key, value))
            debug.write("---------------\n")
            ref_counts.append(ngram_d)
        # candidate
        cand_sentence = candidate[si]
        cand_dict = {}
        cand_sentence = re.sub("[^\w']", ' ', cand_sentence)
        words = cand_sentence.strip().split()
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
        clipped_count += clip_count(cand_dict, ref_counts) * n
        count += limits * n
    return float(clipped_count) / count


def clip_count(cand_d, ref_ds):
    count = 0
    for m in cand_d.keys():
        m_w = cand_d[m]
        m_max = 0
        for ref in ref_ds:
            if m in ref:
                m_max = max(m_max, ref[m])
        m_w = min(m_w, m_max)
        count += m_w
    print "{}/{}".format(count, sum(cand_d.values()))
    return count


def main():
    candidate, references= fetch_data(sys.argv[1], sys.argv[2])
    pr = count_ngram(candidate, references, 3)
    print pr

main()
