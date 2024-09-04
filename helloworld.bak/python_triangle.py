print('  *')
print(' ***')
print('*****')

print('')


print('   *')
print('  ***')
print(' *****')
print('*******')

print('')

print('***')
print('***')
print('***')
print('******************************************************************************************')
print('**************************************************************************************************************************************************************')


print('')

for i in range(5):
  print(i)


print('')

for i in range(6):
  print(i)

print('')

for i in range(0,6):
  print(i)


print('')

for i in range(2,6):
  print(i)

print('')

n=6
for i in range(2,n):
  print(i)

print('')


n=6
for i in range(n):
  print(i)

print('')


n=4
for i in range(n):
  print(i)

print('')


n=4
for i in range(0,n): # 0,1,2,3
  print(i)
# 0
# 1
# 2
# 3

print('')

n=4
for i in range(0,n): # 0,1,2,3
  print(i,end='')
# 0123
print('')

n=4
for j in range(0,n): # 0,1,2,3
    print('*',end='')
# **** 
print('')
print('')

n=4
for j in range(0,n): # 0,1,2,3
    print('*')
# *
# *
# *
# *
print('')

print('aaa')
print('bbb')
print('')

print('aaa',end='')
print('bbb')

print('')
# 例子1
# ****
# ****
# ****
# ****

for i in range(0,4): # range(0,4) <==> 0,1,2,3
    for j in range(1,5):# range(1,5) <==> 1,2,3,4
        print('*',end='')  # ****
    print('')


print('')


for i in range(0,2): # range(0,4) <==> 0,1
    for j in range(1,5):# range(1,5) <==> 1,2,3,4
        print('*',end='')  # ****
    print('')


print('')


for i in range(1,5): # range(1,5) <==> 1,2,3,4
    for j in range(0,2):# range(0,2) <==> 0,1
        print('*',end='')
    print('')

print('')

# 例子1
n=4
for i in range(0,n):
    for j in range(0,n):
        print('*',end='')
    print('')

print('')

# 例子2
n=4
for i in range(0,n):
    for j in range(0,i+1):
        print('*',end='')
    print('')

# 空一行
print('')

# 例子3
n=4
for i in range(n):
    for j in range(0,n-i):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    print('')

print('')
# 例子3
n=20
for i in range(n):
    for j in range(0,n-i):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    print('')
