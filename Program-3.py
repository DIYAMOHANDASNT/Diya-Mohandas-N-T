def conditional_odd_series(a):
  if a % 2 == 0:
    a = a - 1
  result = []
  for i in range(a):
      result.append(2*i + 1)
  return result

print("Output: ",conditional_odd_series(6))
