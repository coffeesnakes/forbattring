transform = [5, 4, 3, 2, 1]
def toDictSq(arr):
  d = dict()
  for i in arr:
    d[i] = i*i
  print(d)

toDictSq(transform)