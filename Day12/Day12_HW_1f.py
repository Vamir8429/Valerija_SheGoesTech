from collections import Counter

def get_word_usage(srcpath, destpath):
    with open(srcpath, encoding="utf-8") as fin, open(destpath, mode="w", encoding="utf-8") as f:
        text = fin.read()
    word_list = text.split()
    word_count = Counter(word_list)
    result = word_count.most_common(3)
    f.write(result)
    print(result)

srcpath='Day12/sherlock_holmes_adventures.txt'
destpath='Day12/count_sherlock.txt'
get_word_usage(srcpath, destpath)

#Output result = [('the', 5412), ('and', 2794), ('of', 2724)]

#ERROR: 

#/Day12/lol.py", line 9, in get_word_usage
#    f.write(result)
#TypeError: write() argument must be str, not list


