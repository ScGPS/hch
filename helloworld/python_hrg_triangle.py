# -*- coding: UTF-8 -*-

# 例子1
# ***
# ***
# ***
n=4
for i in range(0,n):
    for j in range(0,n):
        print('*',end='')
    print('')

# 空一行
print('')

# 例子2
# *
# **
# ***
# ****
n=4
for i in range(0,n):
    for j in range(0,i+1):
        print('*',end='')
    print('')

# 空一行
print('')

# 例子3
#      *
#     **
#    ***
#   ****
#  *****
n=4
for i in range(n):
    for j in range(0,n-i):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    print('')



