# METU Department of Computer Engineering
# CENG111 Fall 2010 Lab Week 8 Questions

# Section 1
# Write a function named "expand" which takes a list as its argument and returns a list similar to the argument, except that if a number appears in the list, then the return value contains that many copies of the following object. Check the examples below. 
# Note: You *must* use recursion. Usage of iterative statements is forbidden! 
# Hint: ['a'] * 3 -> ['a', 'a', 'a']
# 
# Examples:
# >>> expand(['ceng', 3, '1', 2, 'ret'])
# ['ceng', '1', '1', '1', 'ret', 'ret']
# >>> expand(['a', 3, 'cv', 'rt', 1, 'fd'])
# ['a', 'cv', 'cv', 'cv', 'rt', 'fd']
# >>> expand(['a', 3, 'cv', 'rt', 0, 'gg', 1, 'fd'])
# ['a', 'cv', 'cv', 'cv', 'rt', 'fd']
def expand(lst):
	if not lst:
		return []
	if type(lst[0]) == int:
		return ([lst[1]] * lst[0]) + expand(lst[2:])
	else:
		return [lst[0]] + expand(lst[1:])


# Section 2
# Write a function chkParantheses(s) which will take a string as argument,
# and return number of parantheses which remain unclosed. The function should
# return a positive number if the extra parantheses are of type '(' and
# a negative number if the extra parantheses are of type ')'. Returned value
# must be zero if there are equal number of '(' and ')' in the string.
#
# examples:
# >>> chkParantheses('( this paranthesis remains open')
# 1
#
# >>> chkParantheses('def function(arg1, arg2)):')
# -1
#
# >>> chkParantheses('()())())')
# -2
#
# >>> chkParantheses('one (1) is the first natural number.')
# 0
def chkParantheses(s):
    if len(s) == 0:
        return 0
    else:
        if s[0] == '(':
            return 1 + chkBalance(s[1:])
        elif s[0] == ')':
            return -1 + chkBalance(s[1:])
        else:
            return chkBalance(s[1:])

# Section 3
# Write a function partition(t, n) which will take a tuple (t) and
# a number (n) as arguments. This function should return a tuple with two
# elements which are lists. The first list must contain numbers from tuple
# which are smaller than n, and the second list must contain numbers from
# tuple greater than or equal to n.
#
# examples:
# >>> partition( (1,2,3,4,5) , 3)
# ([1, 2], [3, 4, 5])
#
# >>> partition( (4,12,7,2.5,4), 5)
# ([4, 2.5, 4], [12, 7])
def partition(t, n):
    if len(t) == 1:
        if t[0] < n:
            return ( [t[0]], [] )
        else:
            return ( [], [t[0]] )
    else:
        temp = partition( t[:-1], n )
        if t[-1] < n:
            temp[0].append(t[-1])
            return temp
        else:
            temp[1].append(t[-1])
            return temp
			
# Section 4
# Write a function merge(t1,t2) which will merge two sorted lists.
# Lists will only contain numbers in increasing order.
# Returned list must be sorted. t1 and t2 are *not* necessarily of the same length.
#
# examples:
# >>> merge([1,3,4,7,9,47],[2,6,8,12])
# [1, 2, 3, 5, 6, 7, 8, 9, 12, 47]
def merge(t1,t2):
    if len(t1) == 0:
        return t2
    elif len(t2) == 0:
        return t1
    else:
        if t1[0] < t2[0]:
            return [t1[0]] + merge(t1[1:], t2)
        else:
            return [t2[0]] + merge(t1, t2[1:])

# Section 5
# Write a function listCalculator(t1,t2,op) which takes 3 lists as arguments.
# First two arguments will contain numbers and the third argument will contain
# basic mathematical operators: '+', '-', '*', '/'. All of these lists will
# have the same length. The function should return a list which contains
# results of the mathematical operations applied on corresponding elements of
# t1 and t2. For example, if op[0] is '-', first element of the list returned
# by the function should be equal to t1[0] - t2[0].
#
# examples:
# >>> listCalculator([1.0,2.0,3.0,4.0], [10.0,4.0,7.0,20.0], ['+','*','-','/'])
# [11.0, 8.0, -4.0, 0.20000000000000001]
def listCalculator(t1,t2,op):
    if len(op) == 0:
        return []
    elif op[0] == '+':
        return [t1[0]+t2[0]] + listCalculator(t1[1:], t2[1:], op[1:])
    elif op[0] == '-':
        return [t1[0]-t2[0]] + listCalculator(t1[1:], t2[1:], op[1:])
    elif op[0] == '*':
        return [t1[0]*t2[0]] + listCalculator(t1[1:], t2[1:], op[1:])
    elif op[0] == '/':
        return [t1[0]/t2[0]] + listCalculator(t1[1:], t2[1:], op[1:])

# Section 6
# Write a function sumall which computes the sum of all numbers in a list. Note
# that the list may contain objects other than numbers. 
# >>> sumall([1,3,4,5,'gse',[12,43,5],'14'])
# 13
def sumall(lst):
	if len(lst) == 0:
		return 0
	elif type(lst[0]) in (int, long, float): # or x == int or x == long or x == float
		return lst[0] + sumall(lst[1:])
	else:
		return sumall(lst[1:])

# Section 7
# Write a function compare(t1, t2) which takes two tuples with same
# size as arguments. This function should return a list whose n'th element
# is 'same' if n'th element of t1 are t2 are equal and 'different', otherwise.
#
# examples:
# >>> compare( (1,2,5,4), (1,2,4,4))
# ['same', 'same', 'different', 'same']
def compare(t1, t2):
    if len(t1) == 0:
        return []
    else:
        if t1[0] == t2[0]:
            return ['same'] + compare(t1[1:], t2[1:])
        else:
            return ['different'] + compare(t1[1:], t2[1:])
