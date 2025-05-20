def count_mult(numbers):
  result = {}
  for i in range(1,10):
    count = 0
    for num in numbers:
      if num % i == 0:
        count = count + 1
    result[i] = count
  return result

numbers = [1,2,3,4,5,6,7,8,9,10]
print(count_mult(numbers))
