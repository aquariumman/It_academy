from random import randint

def tasknum(tasknumber:str, task='Task'):
    string = f"{task}  {tasknumber}"
    print(string.center(77, '='))


tasknum(1)
# a = None
# b = None
# while not a or not b:
#     a = input("Please enter the 'a' variable here: ")
#     b = input("Please enter the 'b' variable here: ")
#
#
# print()
# print(f'Variable a = {a}. And it has id:' + str(id(a)))
# print(f'Variable b = {b}. And it has id:' + str(id(b)))
#
# a, b = b, a
#
# print()
# print("After swapping".center(33, ' '))
# print(f'Variable a = {a}. And it has id:' + str(id(a)))
# print(f'Variable b = {b}. And it has id:' + str(id(b)))
#
# a = int(b) + int(a)
# b = int(a) - int(b)
# a = int(a) - int(b)
#
# print()
# print("After swapping".center(33, ' '))
# print(f'Variable a = {a}. And it has id:' + str(id(a)))
# print(f'Variable b = {b}. And it has id:' + str(id(b)))

tasknum(2)
# def createsequence(numofnums=10):
#
#     sequence = list()
#     for i in range(numofnums):
#         sequence.append(randint(-5, 5))
#     return sequence
#
# def finder(seq):
#     pairs = 0
#     i = 1
#     while i < len(seq):
#         if (seq[i]>0 and seq[i-1]<0) or(seq[i]<0 and seq[i-1]>0):
#             pairs +=1
#         i += 1
#     return pairs
#
# figuresinlist = int(input("How long the sequence should be: "))
# if figuresinlist <= 2:
#     figuresinlist = 10
# seq = createsequence(figuresinlist)
# print(seq)
# print(f"We've got {finder(seq)} pairs with different signs in our sequence.")

tasknum(3)
# def drawtable_2(m, n, l, k):
#     a = [[' ', '1', '2', '3', '4', '5', '6', '7', '8'],
#          ['1', '*', '*', '*', '*', '*', '*', '*', '*'],
#          ['2', '*', '*', '*', '*', '*', '*', '*', '*'],
#          ['3', '*', '*', '*', '*', '*', '*', '*', '*'],
#          ['4', '*', '*', '*', '*', '*', '*', '*', '*'],
#          ['5', '*', '*', '*', '*', '*', '*', '*', '*'],
#          ['6', '*', '*', '*', '*', '*', '*', '*', '*'],
#          ['7', '*', '*', '*', '*', '*', '*', '*', '*'],
#          ['8', '*', '*', '*', '*', '*', '*', '*', '*']]
#
#     for i in reversed(range(9)):
#         for j in range(9):
#             if i == m and j == n:
#                 print("Q".center(3, ' '), end='')
#             elif i == l and j == k:
#                 print("F".center(3, ' '), end='')
#             else:
#                 print(a[i][j].center(3, ' '), end='')
#         print()
#
# # def drawtable(m, n, l, k):
# #
# #     for i in reversed(range(0, 9)):
# #         if i == 0:
# #             print(' '.center(3, ' '), end='')
# #         else:
# #            print(str(i).center(3, ' '), end='')
# #         for q in reversed(range(1, 9)):
# #             if i == m and q == n:
# #                 print("Q".center(3, ' '), end='')
# #             elif i == l and q == k:
# #                 print("F".center(3, ' '), end='')
# #             elif i == 0:
# #                 for h in range(1, 9):
# #                     print(str(h).center(3, ' '), end="")
# #                 break
# #             else:
# #                 print("*".center(3, ' '), end="")
# #         print()
# #
# # drawtable(m, n, l, k)
# #
#
# #drawtable_2(m, n, l, k)
#
# def diagonals(m, n):
#     coordunderattack = list()
#     y = m
#     x = n
#     while (y != 1 and y != 8) and (x != 1 and x != 8):
#         y += 1
#         x += 1
#         coordunderattack.append([y, x])
#     y = m
#     x = n
#     while (y != 1 and y != 8) and (x != 1 and x != 8):
#         y += 1
#         x -= 1
#         coordunderattack.append([y, x])
#     y = m
#     x = n
#     while (y != 1 and y != 8) and (x != 1 and x != 8):
#         y -= 1
#         x += 1
#         coordunderattack.append([y, x])
#     y = m
#     x = n
#     while (y != 1 and y != 8) and (x != 1 and x != 8):
#         y -= 1
#         x -= 1
#         coordunderattack.append([y, x])
#
#     return coordunderattack
#
# def isunderattack(m, n, l, k):
#     death = False
#     if m == l or n == k:
#         death = True
#     elif [k, l] in diagonals(m, n):
#         death = True
#
#     return death
#
# def mainfunc():
#     m, n, l, k = 0, 0, 0, 0
#     while (not 9 > m > 0) or (not 9 > n > 0):
#         print("\nRange 1 - 8 including".center(40, "_"), end='\n\n')
#         m = int(input('Enter "Y" for Queen:'))
#         n = int(input('Enter "X" for Queen:'))
#
#     while (not 9 > l > 0) or (not 9 > k > 0):
#         print("\nRange 1 - 8 including".center(40, "_"), end='\n\n')
#         l = int(input('Enter "Y" for Victim:'))
#         k = int(input('Enter "X" for Victim:'))
#
#     drawtable_2(m, n, l, k)
#     if isunderattack(m, n, l, k):
#         print("The figure is going to be hit")
#     else:
#         print("The figure is in safety so far.")
#
# mainfunc()

tasknum(4)
# num = int(input("Enter the num here: "))
# snum = str(num)
# lnum = [int(x) for x in snum]
# summ = sum(lnum)
# print(f'You entered {num}.\nThe sum of all figures = {summ}')

tasknum(5)
# keys = tuple(range(10))
# values = [x for x in "qwer"]
# print("Keys\n", keys)
# print("Values\n", values,"\n\n")
#
# dictionary = {}
#
# for x in range(len(keys)):
#     if x >= len(values):
#         dictionary[keys[x]] = None
#     else:
#         dictionary[keys[x]] = values[x]
#
# print(dictionary)

tasknum(6)

# dictionary = {'driver': 'mongodb',
#               'host': '102.168.1.10',
#               'port': 27017,
#               'username': 'someuser',
#               'password': 'passwdpasswd',
#               'dbname': 'testdatabase'}
#
# string_1 = str(dictionary['driver'])+'://'+str(dictionary['username'])+':'+str(dictionary['password'])+'@'+\
#          str(dictionary['host'])+':'+str(dictionary['port'])+'/'+str(dictionary['dbname'])
#
# string_2 = f"{dictionary['driver']}://{dictionary['username']}:{dictionary['password']}@{dictionary['host']}:{dictionary['port']}/{dictionary['dbname']}"
#
#
# print(string_1)
# print(string_2)

tasknum(8)

data = [
{'fname': 'Adam', 'lname': 'Bouen'},
{'fname': 'Katrin', 'lname': 'McOwel'},
{'fname': 'Kraig', 'lname': 'Tomson'},
{'fname': 'Adam', 'lname': 'Bouen'},
{'fname': 'Katrin', 'lname': 'McOwel'},
{'fname': 'Kraig', 'lname': 'Tomson'},
{'fname': 'Adam', 'lname': 'Bouen'}
]

lifromd = set()
for i in range(len(data)):
    lifromd.add(tuple(data[i].items()))

lifromd = list(lifromd)

clearlist = []
for i in range(len(lifromd)):
    clearlist.append(dict(lifromd[i]))

print("List with duplicates: ")
print(data)
print("Clear list: ")
print(clearlist)
