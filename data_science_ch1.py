sentence = "Peter Piper picked a peck of pickled peppers A peck of pickled \
peppers Peter Piper picked If Peter Piper picked a peck of pickled \
peppers Wheres the peck of pickled peppers Peter Piper picked"

word_dict = {}

for word in sentence.split():
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1

print word_dict

#Setting default key
for word in sentence.split():
    word_dict.setdefault(word, 0)
    word_dict[word] += 1

print word_dict

#Setting default key
from collections import defaultdict

word_dict = defaultdict(int)

for word in sentence.split():
    word_dict[word] += 1

print word_dict

#Using counter
from collections import Counter

words = sentence.split()

word_count = Counter(words)

print word_count['Peter'] #Number of occurrences for Peter
print word_count