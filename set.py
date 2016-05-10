set1 = "dogs chase cats"
set2 = "dogs hate cats"

set1_words = set(set1.split())
set2_words = set(set2.split())

print set1_words
print set2_words

common_words = set1_words.intersection(set2_words)
no_common_words = len(set1_words.intersection(set2_words))
print common_words

unique_words = set1_words.union(set2_words)
no_unique_words = len(set1_words.union(set2_words))
print unique_words

#Jaccard similarity function manually
simmilarity = no_common_words / (1.0 * no_unique_words)
print simmilarity

#Jaccard similarity function from sklearn
from sklearn.metrics import jaccard_similarity_score

one = [1 if w in set1_words else 0 for w in unique_words]
two = [1 if w in set2_words else 0 for w in unique_words]

print one
print two

jaccard_simmilarity = jaccard_similarity_score(one,two)
print jaccard_simmilarity