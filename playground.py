suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')

values = tuple("A,2,3,4,5,6,7,8,9,10,j,Q,K".split(','))
print(values)


deck = []

for value in values:
    for suit in suits:
        deck.append({ 'suit': suit, 'value': value })

print(len(deck))

deck2 = [{'value': value, 'suit': suit} for suit in suits for value in values]
print(deck2)
print(len(deck2))