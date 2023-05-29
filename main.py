import sys, os, re
import kenlm
from spelling_correcter import get_candidates
import time

arpa_path = 'data/lm_binary.arpa'
lm_model = kenlm.LanguageModel(arpa_path)

def correct_one(line):
    if ' ' in line.strip():
        utt, hpy = line.strip().split(' ', 1)
    else:
        utt = line.strip()
        hpy = ''
        return line.strip()
    hpy = re.sub(' +', ' ', hpy)
    words = hpy.strip().split(' ')
    for i in range(len(words)):
        word = words[i]
        candidates = list(get_candidates(word))
        if len(candidates) == 1:
            words[i] = candidates[0]
        else:
            max_lm_score = float('-inf')
            for candidate in candidates:
                if i == 0:
                    if len(words) == 1:
                        tmp_hpy = candidate
                    else:
                        tmp_hpy = ' '.join([candidate, words[i+1]])
                elif i + 1 < len(words):
                    tmp_hpy = ' '.join([words[i-1], candidate, words[i+1]])
                else:
                    tmp_hpy = ' '.join([words[i-1], candidate]) 

                lm_score = lm_model.score(tmp_hpy.upper())
                if lm_score > max_lm_score:
                    max_lm_score = lm_score
                    candidate_dict = {}
                    candidate_dict[str(candidate)] = lm_score
                    #print(tmp_hpy, lm_score)
            words[i] = list(candidate_dict.keys())[0]
    result = utt + ' ' + (' '.join(words)).upper()
    return result

if __name__ == '__main__':
    hpy_txt, hpy_fix_txt = sys.argv[1:3]

    start_time = time.time()
    count = ''
    with open(hpy_txt, 'r') as f:
        for line in f:
            hpy_fix = correct_one(line)
            count += hpy_fix + '\n'

    with open(hpy_fix_txt, 'w') as f:
        f.write(count)

    end_time = time.time()
    print('total_time:', (end_time - start_time))
