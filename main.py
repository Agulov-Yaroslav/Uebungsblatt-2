"""Übungsblatt 02"""

# Aufgabe 1

A = 1
B = 17835
print(A + 2 * B)

C = 10
print((3 ** (C - 1)) + 1)

D = 37
print(True and not D - 37)

# Aufgabe 2

QUOTE = "Python ist eine universelle, üblicherweise interpretierte höhere Programmiersprache."

F = 0
G = 11
H = 2
I = -17
J = 24
K = -1
print(QUOTE[F:G] + QUOTE[H] + QUOTE[I] + 2 * QUOTE[J] + QUOTE[K])

L = -73
M = 52
N = 5
print(QUOTE[:L] + "su" + QUOTE[48:M:2] + QUOTE[-6::N])

# Aufgabe 3

CORPUS_TEXT = (
    "Good evening. Over 400000 million pounds were wiped off the "
    "value of shares this afternoon, when someone in the Stock "
    "Exchange coughed. Sport: capital punishment is to be "
    "re-introduced in the first and second division. Any player found "
    "tackling from behind or controlling the ball with the lower part "
    "of the arm will be hanged. But the electric chair remains the "
    "standard punishment for threatening the goalie. Finally, "
    "politics: the latest opinion poll published today shows Labour "
    "ahead with 40 %, the AA second with 38 % and not surprisingly "
    "Kentucky Fried Chicken running the Liberals a very close third. "
    "And now back to me. Hello. And now it's time to go over to Hugh "
    "Delaney in Paignton."
)

SENTENCES = CORPUS_TEXT.split('. ')
SENTENCES_COUNT = len(SENTENCES)
# print(SENTENCES)
# print(SENTENCES_COUNT)

# Aufgabe 4

CORPUS_CLEANED = CORPUS_TEXT
symbols = '.,:'
for symbol in symbols:
    CORPUS_CLEANED = CORPUS_CLEANED.replace(symbol, '')

TOKENS = CORPUS_CLEANED.split(' ')
TOKENS_COUNT = len(TOKENS)
# print(TOKENS)
# print(TOKENS_COUNT)

# TYPES = list(set(CORPUS_TEXT.lower().split(' ')))
TYPES = list(set(TOKENS))
TYPES_COUNT = len(TYPES)
# print(TYPES)
# print(TYPES_COUNT)

# Aufgabe 5

KEYWORDS = ["Stock", "the", "40"]
FEATURES = {}
for KEYWORD in KEYWORDS:
    FEATURES.update({KEYWORD: [len(KEYWORD),
                               KEYWORD.isdigit(),
                               KEYWORD.istitle(),
                               CORPUS_TEXT.count(KEYWORD)]})
# print(FEATURES)

# Zusatzaufgabe 6

# Antwort:
# Indexierung in Python beginnt mit 0 und nicht mit 1,
# deswegen der ‚fünfte‘ Symbol in dem Wort ‚Hallo‘ ist eigentlich der vierte.

# Zusatzaufgabe 7

# Antwort:
# A tuple is a collection which is ordered and unchangeable.
