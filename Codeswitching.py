from random import choice
from typing import List, Tuple
from random import shuffle
from math import log10



def read_data(content : str) -> List[List[Tuple[str, str]]]:

    corpus = []
    for tweet in content.split("\n\n")[1:]:
        if not tweet:
            continue
        corpus.append([(line.split("\t")[0].lower(), line.split("\t")[1]) for line in tweet.split("\n")])
    
    return corpus

corpus = read_data(open("TWT_HI_EN_FN.txt", "r", encoding="utf-8").read())

filtered_corpus = []
for tweet in corpus:
    x=1
    for mot,tag in tweet:
        if tag =="ne":
            x = -1
    if x==1:
        filtered_corpus.append(tweet)
        

shuffle(filtered_corpus)
train_set = filtered_corpus[:int(.8 * len(filtered_corpus))]
test_set = filtered_corpus[int(.8 * len(filtered_corpus)):]




en_corpus=[]
all_en_char = []
for tweet in train_set:
    for mot,tag in tweet:
        if tag =="en":
            en_corpus.append(mot)
for mot in en_corpus:
    for c in mot:
        all_en_char.append(c)
all_en_char =Counter(all_en_char)
print(all_en_char)


hi_corpus=[]
all_hi_char = []
for tweet in train_set:
    for mot,tag in tweet:
        if tag =="hi":
            hi_corpus.append(mot)
for mot in hi_corpus:
    for c in mot:
        all_hi_char.append(c)
all_hi_char =Counter(all_hi_char)
print(all_hi_char)



all_en_char = {k: log10(v / sum(all_en_char.values())) for k, v in all_en_char.items()}
all_hi_char = {k: log10(v / sum(all_hi_char.values()))for k, v in all_hi_char.items()}
all_univ_char = {k:log10(v / sum(all_univ_char.values())) for k, v in all_univ_char.items()}



