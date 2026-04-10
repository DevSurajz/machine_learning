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
