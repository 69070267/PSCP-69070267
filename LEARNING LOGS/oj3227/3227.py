"""aaaaa"""
card = input().strip().upper()
symbol_part = card[:-1]
setset_part = card[-1]
symbol = {
    'A': 'ace',
    'J': 'jack',
    'Q': 'queen',
    'K': 'king'
}
setset = {
    'D': 'diamonds',
    'H': 'hearts',
    'S': 'spades',
    'C': 'clubs'
}
symbol_name = symbol.get(symbol_part, symbol_part)
setset_name = setset[setset_part]
print(f"{symbol_name} of {setset_name}")
