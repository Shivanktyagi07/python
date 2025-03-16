# creating list:

list = [1, 2, 3, 4, 5]

print(list[0])
print(list[2])
print(list[4])


#append in list:-> it add only one element at last:
list.append(6)
print(list)

print(list[5])

#extend in lis:-> its add multiple elements at the end of the list:
list.extend([7, 8, 9, 10])
print(list)

#insert at any specific position:
list.insert(2, 0);
print(list)


#REMOVING ELEMENTS FROM LIST:
nums = [1, 2, 3, 4, 5]

# Remove by value:
nums.remove(3)
print(nums)  

# Remove by index:
nums.pop(1)
print(nums)  

# Remove using del:
del nums[0]
print(nums)  


#finding index:
lists = [1, 2, 3, 4, 5]
index = lists.index(3)
print(index)

#sort and reverse a list:
num = [ 2, 5, 1 ,8, 9, 4];
num.sort()
print(num)

num.reverse();
print(num)

#copying a list:
copied = num.copy()
print(copied)
