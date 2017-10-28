def hindex(citations):
  bucket = [0 for i in range(len(citations)+1)]
  for i in range(len(citations)):
    if citations[i] < len(citations)+1:
      bucket[citations[i]] += 1
    else:
      bucket[len(citations)] += 1

  count = 0
  for i in range(len(citations),-1,-1):
    count += bucket[i]
    if count >= i:
      return i
  return 0
