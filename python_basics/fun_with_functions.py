# Odd/Even
numberList = [1,2,3,4,5,6,]
def odd_even(val):
    for val in numberList:
        if val % 2 == 0:
            print "Number is " + val  + ". This is an even number"
        else:
            print "Number is " + val + ". This is an odd number"


# Multiply
def multiply(list, multiplyBy):
    b = []
    for num in list:
        b.append(num * multiplyBy)
    return b
# multiply([2,4,10,16], 5)

# Hacker Challenge
def layered_multiples(arr):
  newArr = []
  for num in arr:
    newArr.append(['1'] * num)
  return newArr
x = layered_multiples(multiply([2,4,5],3))
print x
# output
# [[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
