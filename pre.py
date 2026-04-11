n = int(input('enter n'))

result = 0
fact = 1

for i in range(1,n+1):
  fact = fact * i
  result = result + i/fact

print(result)


curr_pop = 10000

for i in range(10,0,-1):
  print(i,curr_pop)
  curr_pop = curr_pop/1.1


rows = int(input('enter number of rows'))

for i in range(1,rows+1):
  for j in range(1,i+1):
    print('*',end='')
  print()



# Q1.   Find the length of a given string without using the len() function
# s = input("Enter a string: ")

# count = 0
# for i in s:
#   count += 1
# print('Given string length is', count)



#Q.2 # Extract username from a given email. 
# Eg if the email is nitish24singh@gmail.com 
# then the username should be nitish24singh

# s = input("Enter a Email: ")
# pos = (s.index('@'))
# print(s[0:pos])



# Q.3  Count the frequency of a particular character in a provided string. 
# Eg 'hello how are you' is the string, the frequency of h in this string is 2.

# s = input("Enter a line: ")
# pos = input("What would youu like to search: ")

# counter = 0
# for i in s:
#     if i == pos:
#         counter += 1
# print('frequency of char is: ', counter)



#Q. 4 
# Write a program which can remove a particular character from a string.

# s = input('enter the string ')
# term = input('what would like to remove ')

# result = ''

# for i in s:
#     if i != term:
#         result = result + i

# print(result)



# Q.5 
# Write a program that can check whether a given string is palindrome or not.
# abba
# malayalam

# s = input("Enter a word: ")
# flag = True

# for i in range(0, len(s)//2):
#     if s[i] != s[len(s) -i -1]:
#         flag = False
#         print("Not a palindrome")
#         break

# if flag:
#     print('palindrome')



# Q. 6'
# Write a program to count the number of words in a string without split()

# s = input('enter the string')
# L = []
# temp = ''
# for i in s:

#   if i != ' ':
#      temp = temp + i
#   else:
#      L.append(temp)
#      temp = ''

# L.append(temp)
# print(L)



# Q.7 
# Write a python program to convert a string to title case without using the title()
# s = input('enter the string')

# L = []
# for i in s.split():
#     L.append(i[0].upper() + i[1:].lower())

# print("".join(L))



# Q.8 
# Write a program that can convert an integer to string.

number = int(input("Enter a Number: "))

digits = '0123456789'
result = ''
while number != 0:
    result = digits[number % 10] + result
    number = number // 10

print(result)
print(type(result))



# Create 2 lists from a given list where 
# 1st list will contain all the odd numbers from the original list and
# the 2nd one will contain all the even numbers 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_numbers = []
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)



# How to take list as input from user
numbers = list(map(int, input("Enter numbers: ").split()))
print(numbers)


# Write a program to merge 2 list without using the + operator
L1 = [1,2,3,4]
L2 = [5,6,7,8]

L1.extend(L2)

print(L1)


# Write a program to replace an item with a different item if found in the list 
L = [1,2,3,4,5,3]
# replace 3 with 300


L = [1,2,3,4,5,3]

for i in range(len(L)):
    if L[i] == 3:
        L[i] = 300

print(L)



# Write a program that can convert a 2D list to 1D list
L = [[1, 2, 3], [4, 5, 6], [7, 8]]

result = []

for sublist in L:
    for item in sublist:
        result.append(item)

print(result)



# Write a program to remove duplicate items from a list

L = [1,2,1,2,3,4,5,3,4]

unique = []
for x in L:
    if x not in unique:
        unique.append(x)

print(unique)



# Write a program to check if a list is in ascending order or not
L = [1, 2, 3, 4, 5]

is_sorted = True

for i in range(len(L) - 1):
    if L[i] > L[i + 1]:
        is_sorted = False
        break

print("Ascending" if is_sorted else "Not Ascending")
