"""

1 Konktekstfrie grammatikker

1. Setningen kan enten bety at Per slår både Ola og boka, eller at Per bruker
boka for å slå Ola.

2. Vi må utvide grammatikken med en "VP -> V PP".

3. Den er rekusriv, fordi grammatikken kan generere et uendelig antall
strukturer.

"""

#2 Chunking

import nltk
from nltk.corpus import conll2000 as con

grammar = """
NP:
{<DT>?<JJ>*<NN>}
{<DT>?<NN>}
{<NNP>?<NNS>}
{<NNP>+}
{<DT>*<JJ>}
{<DT>?<NNP>*<NN>}
"""
cp = nltk.RegexpParser(grammar)

test_chunks = con.chunked_sents("test.txt", chunk_types=["NP"])

print(cp.evaluate(test_chunks))

#3 Betydningsdisambiguering (WSD) med en Naive Bayesklassifiserer

f = open("wsd_tren.txt")

senses = {}
instances = 0

features = {}
for l in f:
    fields = l.split()
    cl = fields[0]

senses[cl] = senses.get(cl,0) + 1
instances += 1

for feat in fields[1:]:
    if feat in features:
        features[feat][cl] = features[feat].get(cl,0) + 1
    else:
        features[feat] = {cl:1}

f.close()

#Ved å bruke count(b, w)/ count(w) kan vi beregne sannsynligheten for
#betydningen Removing, som blir til 2/ 16 = 0.125.

tekstfil = open("wsd_tren.txt", "r")
les = tekstfil.read()

liste = []
listeAvRemoving = []

splitter = les.split()
for ord in splitter:
    liste.append(ord)

for i in liste:
    if i == "Removing":
        listeAvRemoving.append(i)

print(len(listeAvRemoving) / len(liste))
