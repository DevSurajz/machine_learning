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
