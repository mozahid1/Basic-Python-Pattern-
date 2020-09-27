"""
   * * * * * *
    * * * * *
     * * * *
      * * *
       * *
        *
        *
       * *
      * * *
     * * * *
    * * * * *
   * * * * * *
"""
def pattern(n):
    k = n - 2
    for i in range(n, -1, -1):  # i = 3,2,1,0
       for j in range(k, 0, -1):  # j = 3,2,1
          print(end=" ")  # space
       k = k + 1
       for j in range(0, i + 1):  # as usual
           print("* ", end="")
       print("\r")
    k = 2*n - 2
    for i in range(0,n+1):       # i = 0,1,2,3,4 <-- five line
        for j in range(0,k):   # j = 0,1,2,3,4,5,6,7
            print(end=" ")     # space
        k = k - 1
        for j in range(0,i+1): # as usual
            print("* ",end="")
        print("\r")
pattern(5)