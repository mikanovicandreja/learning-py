# Lists & Tuples in Python

users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptylist = []

print ("Dave" in emptylist)

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(users.index('Sara'))

print(users[0:2])

print("")
data_length = len(data)
print(f"Length of the 'data' list: {data_length}")


print("")
users.append('Elsa')
users += ['Jason']      # Don't forget brackets, because it will add every single character
# users.extend(data)
print(users)
users.insert(0, 'Bob')
users[2:2] = ['Eddie', 'Alex']
print(users)

users[1:3] = ['Robert', 'JPJ']
print(users)

users.remove('Bob')
print(users)

print(users.pop())

del users[0]
print(users)

data.clear()
print(data)

users[1:2] = ['dave']
users.sort(key=str.lower)
print(users)

nums = [4,42,78,1,5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)


# Ways of copying lists
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))
print(type(mycopy))

mylist = list([1, "Neil", True])
print(mylist)
print(type(mylist))

# Tuples: content & order cannot be changed

mytuple = (('Dave',42,True))
anothertuple = (1, 4, 2, 8, 2, 2)

print(mytuple)
print(anothertuple)
print(type(mytuple))
print(type(anothertuple))

# Creating a list out of a tuple
newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)


(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))