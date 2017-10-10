# Find and replace
words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")
print words.replace("day", "month")

# Min and max
x = [2,54,-2,7,12,98]
print min(x)
print max(x)

# First and last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[-1]

# New list
# 1) sort list
# 2) split list in half
# 3) push list created from the first position 0 of
#   the list created from the second
# 4) output: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
half_point = len(x)/2
first_half = x[:half_point]
second_half = x[half_point:]
second_half.insert(0,first_half)
print second_half
