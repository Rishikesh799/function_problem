"""-------------------------------MAP FUNCTION--------------------------------------------------------------------------
#1.Create list of multiple of 3 of given range of element using map function.

print(list(map(lambda x:x*3,range(1,11))))
OUTPUT==[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

-----------------------------------------------------------------------------------------------------------------------
#2.Add multiple list using map function.
x=[1,2,3]
y=[4,5,6]
z=[7,8,9]

print(list(map(lambda i,j,k:i+j+k,x,y,z)))
OUTPUT==[12, 15, 18]
-----------------------------------------------------------------------------------------------------------------------
#3.Write a Python program to listify the list of given strings individually using Python map.
X=["RED","BLUE","ORANGE"]

print(list(map(list,X)))
OUTPUT==[['R', 'E', 'D'], ['B', 'L', 'U', 'E'], ['O', 'R', 'A', 'N', 'G', 'E']]
------------------------------------------------------------------------------------------------------------------------
#4.Python program to  create a list of tuples from given having number and its cube in same tuple.

print(list(map(lambda x:(x,x**3),range(1,11))))
OUTPUT==[(1, 1), (2, 8), (3, 27), (4, 64), (5, 125), (6, 216), (7, 343), (8, 512), (9, 729), (10, 1000)]
------------------------------------------------------------------------------------------------------------------------
#5.Write a Python program to listify the list of given strings individually using Python map.

x=["PRANAY","RISHIKESH","PRATIK"]
print(list(map(lambda i:list(i),x)))
[['P', 'R', 'A', 'N', 'A', 'Y'], ['R', 'I', 'S', 'H', 'I', 'K', 'E', 'S', 'H'], ['P', 'R', 'A', 'T', 'I', 'K']]
-----------------------------------------------------------------------------------------------------------------------
#6.. Write a Python program to convert all the characters in uppercase and lowercase and eliminate duplicate letters from a given sequence. Use map() function.
x=["rishikesh","pranay"]

print(list(map(lambda i :(set(i.upper()),set(i.lower())),x)))
-----------------------------------------------------------------------------------------------------------------------
#7.Convert string into integer and form new list using map.

x=("1","3","4","5")
print(list(map(lambda i:int(i),x)))
OUTPUT==[1, 3, 4, 5]
-----------------------------------------------------------------------------------------------------------------------
#8.Write a Python program to count the same pair in two given lists using  map() function.
x=[1,2,3,4,5,6,8]
y=[2,1,5,4,6,6,9]

z=list(map(lambda i,j: i==j , x,y))
print(" the no of same pair of list is :==",z.count(True))
OUTPUT==the no of same pair of list is :== 2
"""
