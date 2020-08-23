"""

1 Ordklasser

Jeg: PO.
spiser: VB.
sushi: NN.
med: PR.
pinner: NN.

"""

#2 Flertydighet

#1. At det finnes flertydighet i språket betyr rett og slett at ord i
#setnigner kan ha forskjellige betydninger (og da helt forskjellige ordklasser
#i noen tilfeller).
#Et eksempel på norsk: Mannen jaget tyven med gevær.
#Et eksempel på engelsk: He fed her cat food.

#2.

import nltk

brown_news = nltk.corpus.brown.tagged_words(categories="news")

#3.

tags = {}

for w, pos in brown_news:
    word = w.lower()
    if word not in tags:
        tags[word] = []
        tags[word].append(pos)
    else:
        if pos not in tags[word]:
            tags[word].append(pos)

listeAvFlertydigeOrd = []

for key, value in tags.items():
    if len(value) > 1:
        listeAvFlertydigeOrd.append(key)

print("Det finnes ", len(listeAvFlertydigeOrd), " flertydige ord i \
Brown-korpuset.", sep = "")

#4.

for key, value in tags.items():
    if len(value) > 6:
        print(key, value)

#5.

def freqs(w):

    for key, value in tags.items():
        if key == w:
            print("Ordet ", key, " forekommer ",
            len([item for item in value if item]), " ganger.", sep = "")

#6.

freqs("to")
freqs("house")

#3 Ordklassetagging med regulære uttrykk

#1.

import re
import nltk

brown_adventure = nltk.corpus.brown.tagged_sents(categories = "adventure")

patterns = [
(r".*ing$", "VBG"),
(r".*ed$", "VBD"),
(r".*es$", "VBZ"),
(r".*ould$", "MD"),
(r".*\'s$", "NNS"),
(r"^-?[0-9] + (.[0-9] + )?$", "CD")
]

regexp_tagger = nltk.RegexpTagger(patterns)

#2.

print(regexp_tagger.evaluate(brown_adventure))

brown_fiction = nltk.corpus.brown.tagged_sents(categories = "fiction")

print(regexp_tagger.evaluate(brown_fiction))
