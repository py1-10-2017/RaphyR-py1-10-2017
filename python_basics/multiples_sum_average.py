# Multiples Part I - print odd numbers
for num in range(0, 1000):
    if num % 2 == 1:
        print num

# Multiples Part I - print multiples of 5
for num in range(0, 1000000):
    if num % 5 == 0:
        print num

# Sum list
a = [1, 2, 5, 10, 255, 3]
sum = 0
for num in a:
    sum += num
print sum
avg = sum / len(a)
print avg
