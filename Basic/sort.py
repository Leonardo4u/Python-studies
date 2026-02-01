def simple_sort(cards):
  cards = list(cards)
  if not cards:
    return []
  lowest = min(cards)
  removed = False
  rest = []
  for c in cards:
    if not removed and c == lowest:
      removed = True
      continue
    rest.append(c)
  return [lowest] + simple_sort(rest)


if __name__ == "__main__":
  # exemplo de uso: original não deve ser mutado
  original = [3, 1, 4, 1, 5, 9, 2]
  sorted_list = simple_sort(original)
  print("sorted:", sorted_list)
  print("original:", original)