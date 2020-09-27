"""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

def pattern(n):
    for i in range(0,n):         # i = 0,1,2,3,4 <-- five line of code
        for j in range(0,i+1):   # as usual print star
            print("* ",end="")
        print("\r")
    for i in range(n,-1,-1):     # i = 4,3,2,1,0 <-- five line of code
        for j in range(0,i+1):   # as usual print star
            print("* ",end="")
        print("\r")
pattern(5)