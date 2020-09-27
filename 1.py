"""
        *
      * *
    * * *
  * * * *
* * * * *
"""

def pattern(n):
    k = 2*n - 2
    for i in range(0,n):       #1
        for j in range(0,k):   #2
            print(end=" ")     #3
        k = k - 2              #4
        for j in range(0,i+1): #5
            print("* ",end="")
        print("\r")
pattern(5)

"""
1. (0,5) - helps to print 5 line & value of i is 0,1,2,3,4
   looks like 5 line: 
   ----------
   ----------
   ----------
   ----------
   ----------
2. (0,8) - helps to print in this five line & value of j is 0,1,2,3,4,5,6,7
3. Because of printing end with space here that's why first time it's print 8 space then 
4. k = k - 2 means first print 8 space then next line print 6 then 4,2,0
5. We knew form '1' values of i = 0,1,2,3,4
   in for loop i+1 = 0+1 = 1 first time
               i+1 = 1+1 = 2 second time
               3,4,5 time it's run and 
               print "* " & end says it takse star and go to new line
               after '3's 8th value space it print * 
               then 6th value space it print * *
               then 4th value space it print * * *
               then 2nd value space it print * * * *
               then 0th value space it don't print.
   and then we got result.                      
"""
