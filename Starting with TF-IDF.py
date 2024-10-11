import pandas as pd
import numpy as np


corpus = ["data science is one of the most important fields of science","this is one of the best data science training","data scientist analyze data"]

word_set = set()
for doc in corpus:
    words = doc.split(" ")
    word_set = word_set.union(set(words))
    
print('Number of words in the corpus:', len(word_set))
print('The words in the corpus: \n', word_set)
