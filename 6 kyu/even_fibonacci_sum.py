# Description:
#
# Give the summation of all even numbers in a Fibonacci sequence up to, but not including, the number passed to your function. Or, in other words, sum all the even Fibonacci numbers that are lower than the given number n (n is not the nth element of Fibonnacci sequence) without including n.
#
# The Fibonacci sequence is a series of numbers where the next value is the addition of the previous two values. The series starts with 0 and 1:
#
# 0 1 1 2 3 5 8 13 21...
#
# For example:
#
# eve_fib(0)==0
# eve_fib(33)==10
# eve_fib(25997544)==19544084
# My solution:
def even_fib(m):
    a, b = 0, 1
    even_elements = [0]

    while True:
        a, b  = b, a+b

        if b >= m:
            break

        if b % 2 == 0:
            even_elements.append(b)
    return sum(even_elements)

