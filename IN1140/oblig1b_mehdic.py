# -*- coding: utf-8 -*-

"""

1 Regulære uttryk

Epost-adressen som ikke kan gjenkjennes med gitt regulære uttrykk er nummer 3.

2 Regulære uttryk for verb

Her er ett regulært uttrykk som gjenkjenner gitt former av verbene spise,
kjøpe, tenke og løpe:
/spis(er|te|e|)|kjøp(er|te|e|)|tenk(er|te|e|)|løp(er|te|e|)/

"""

# 3 Tokenisering med regulære uttrykk

# Her er et regulært uttryk som definerer et gyldig norsk ord, uten å
# inkludere tegnsetting:
# /[a-zA-ZæÆøØåÅ]/
# Her matcher jeg alt fra a til z, A til Z og de norske alphabetene på både
# stor og liten bokstav.
