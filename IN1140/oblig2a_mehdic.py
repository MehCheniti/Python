"""

1 Språkmodeller

En språkmodell er en statistisk sannsynlighetsmodell som bruker
korpusfrekvenser for å beregne sannsynligheten for sekvenser av ord. Noen
anvendelser av slike modeller: talegjenkjenning, maskinoversettelse,
håndskriftgjenkjenning prediksjon og ordklassetagging.

2 Språkmodeller

1. Bigrammene som forekommer i korpuset er <Per, synger>, <synger, ikke>,
<Kari, synger>, <Ola, synger> og <synger, ikke>.

2. Vi bruker denne formelen: Count(wi - 1, wi)/ Count(wi), hvor
Count(wi - 1|wi) er antall forekomster av "w1 - 1 wi" og Count(wi) antall
forekomster av "wi" i tekstkorpusen.

3. Sannsynlighetene vi trenger for setningen "<s> Kari synger ikke </s>" er:
(P(Kari|<s>)) * (P(synger|Kari)) * (P(ikke|synger)) * (P(</s>|ikke)) =
(Count(<s>, Kari)/ Count(<s>)) * (Count(Kari, synger)/ Count(Kari)) *
(Count(synger, ikke)/ Count(synger)) * (Count(ikke, </s>)/ Count(ikke)) =
((1/3) / (3/3)) * ((1/3) / (1/3)) * ((2/3) / (3/3)) * ((2/3) / (2/3)) = (1/3)
* 1 * (2/3) * 1 = 2/9.

"""

#3 Språkmodeller med Python

#1.

import nltk
from collections import Counter, defaultdict
from nltk import bigrams, trigrams
import numpy as np

moby = nltk.corpus.gutenberg.words("melville-moby_dick.txt")
print("Total antall tokens i teksten: ", len(moby), ".", sep = "")
print(" ")

#2.

distinct_words = []
for w in moby:
    distinct_words.append(w.lower())
print("Totall antall ord-typer i teksten: ", len(set(distinct_words)), ".",
sep = "")
print(" ")

#3.

frequenceWords = Counter(moby)
print("De 20 mest frekvente ordene er: ", frequenceWords.most_common(20), ".",
sep = "")
print(" ")

#4.

print("Frekvensen av ordet 'peace' er: ", frequenceWords["peace"], ".",
sep = "")
print("Frekvensen av ordet 'whale' er: ", frequenceWords["whale"], ".",
sep = "")
print("Frekvensen av ordet 'boy' er: ", frequenceWords["boy"], ".", sep = "")
print(" ")

#5.

moby_sents = nltk.corpus.gutenberg.sents("melville-moby_dick.txt")
fourth_sentence = moby_sents[3]
print("Bigrammene til den fjerde setningen er: ",
list(bigrams(fourth_sentence)), ".", sep = "")
print(" ")

#6.

fifth_sentence = moby_sents[4]
print("Trigrammene til den femte setningen er: ",
list(trigrams(fifth_sentence)), ".", sep = "")
print(" ")

#7.

bigram_counts = defaultdict(lambda: defaultdict(lambda: 0))
bigram_model = defaultdict(lambda: defaultdict(lambda: 0.0))
for sentence in moby_sents:
    for w1, w2 in bigrams(sentence, pad_right=True, pad_left=True):
        bigram_counts[w1][w2] += 1

text = [None, None]

sentence_is_finished = False

while not sentence_is_finished:
    key = tuple(text[-2:])
    words = list(bigram_model[key].keys())
    probs = list(bigram_model[key].values())
    text.append(np.random.choice(words, p = probs))

if text[-2:] == [None, None]:
    sentence_is_finished = True

print("".join([t for t in text if t]))

#8.

probabilities = {}
for word, count in bigram_model.items():
    probabilities[word] = count / total_words

text = np.random.choice(list(probabilities.keys()), 20,
p = list(probabilities.values()))

word_probabilities = []
for w in text:
    word_probabilities.append(probabilities[w])
print("Sannsynligheten for den genererte teksten er: ",
np.prod(word_probabilities), ".", sep = "")
