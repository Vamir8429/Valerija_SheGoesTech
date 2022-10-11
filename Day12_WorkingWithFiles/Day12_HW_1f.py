from collections import Counter
from pathlib import Path

def get_word_usage(srcpath, destpath, encoding="utf-8"):
    with open(srcpath, encoding=encoding) as fin, open(destpath, mode="w", encoding=encoding) as fon:
        text = fin.read()
        word_list = text.split()
        word_count = Counter(word_list)
        result = word_count.most_common(3)
        for x in result:
            fon.write(str(x))

srcpath='Day12/sherlock_holmes_adventures.txt'
destpath='Day12/count_sherlock.txt'
get_word_usage(srcpath, destpath)

#Output result = [('the', 5412), ('and', 2794), ('of', 2724)]

#ERROR: 

#/Day12/lol.py", line 9, in get_word_usage
#    f.write(result)
#TypeError: write() argument must be str, not list


