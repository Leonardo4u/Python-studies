def simple_sort(cards):
  sorted_cards = []
  while cards:
    lowest_card = min(cards)  
    sorted_cards.append(lowest_card)
    cards.remove(lowest_card)
  return sorted_cards