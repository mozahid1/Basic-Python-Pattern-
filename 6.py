"""
  *
 * *
*   *
 * *
  *
"""

def pattern(n):
    for i in range(n): # i = 0,1,2,3,4 <-- five line of code
        for j in range(n): # j = 0,1,2,3,4
            if i+j == 2 or i-j == 2 or i+j == 6 or j-i == 2:
                print("*",end="")
            else:
                print(end=" ")
        print()
pattern(5)

