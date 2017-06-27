def symmetric(S):
    n = len(S)
    if n == 0:
        return True
    try:
      for row in S:
          if len(row) != n:
              return False
          for i in range(n):
              for j in range(n):
                  if S[i][j] != S[j][i]:
                      return False
          return True
    except TypeError:
      return False

print(symmetric([]))
#>>> True
print(symmetric([1]))
#>>> False
print(symmetric([1, 2, 3]))
#>>> False
print(symmetric([[1, 2, 3], [2, 3, 4], [3, 4, 1]]))
#>>> True
print(symmetric([["cat", "dog", "fish"], ["dog", "dog", "fish"], ["fish", "fish", "cat"]]))
#>>> True
print(symmetric([["cat", "dog", "fish"], ["dog", "dog", "dog"], ["fish","fish","cat"]]))
#>>> False
print(symmetric([[1, 2], [2, 1]]))
#>>> True
print(symmetric([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]))
#>>> False
print(symmetric([[1,2,3], [2,3,1]]))
#>>> False
