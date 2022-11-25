from random import choice
from typing import List, Tuple
from random import shuffle



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
