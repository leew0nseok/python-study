def MoM(A, k):
  if (|A| == 1): return A[0]
  S, L, M, medians = [], [], [], []
  i = 0
  while(i + 4 < |A|):
    medians.append(find_median_five(L[i : i+5]))
    i += 5
  if(i < |A| and i + 4 >= |A|):
    medians.append(find_median_five(L[i+5: ]))
  mom = MoM(medians, len(medians)//2)
  for v in A:
    if(v < mom): S.append(v)
    elif(v > mom): L.append(v)
    else: M.append(v)
  if(len(S) > k): return MoM(S, k)
  elif(len(S) + len(M) < k): return MoM(B, k - len(S) - len(M))
  else: return mom