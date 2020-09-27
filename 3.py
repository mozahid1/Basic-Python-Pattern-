
"""
        *
       * *
      * * *
     * * * *
    * * * * *
"""

def pattern(n):
    k = 2*n - 2                    # k = 8
    for i in range(n,-1,-1):       # i = 5,4,3,2,1,0 --> six line of code
        for j in range(k,0,-1):    # j = 8,7,6,5,4,3,2,1 --> eight space then print
            print(end=" ")
        k = k + 1                  # k = 9,10,11,12,13
        for j in range(0,i+1):     # it gets space & print star after that
            print("*",end=" ")
        print("\r")
pattern(5)



