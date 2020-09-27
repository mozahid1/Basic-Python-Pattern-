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
    k = 2*n - 2
    for i in range(0,n-1):     #1
        for j in range(0,k):   #2
            print(end=" ")     #3
        k = k - 2              #4
        for j in range(0,i+1): #5
            print("* ",end="")
        print("\r")
    k = -1                         #6
    for i in range(n-1,-1,-1):     #7
        for j in range(k,-1,-1):   #8
            print(end=" ")
        k = k + 2                  #9
        for j in range(0,i+1):     #10
            print("* ",end="")
        print("\r")
pattern(5)

"""
1. (0,5-1) - helps to print 4 line & value of i is 0,1,2,3
   looks like 4 line: 
   ----------
   ----------
   ----------
   ----------
2. (0,8) - helps to print in this five line & value of j is 0,1,2,3,4,5,6,7
3. Because of printing end with space here that's why first time it's print 8 space then 
4. k = k - 2 means first print 8 space then next line print 6 then 4,2,0
5. We knew form '1' values of i = 0,1,2,3
   in for loop i+1 = 0+1 = 1 first time
               i+1 = 1+1 = 2 second time
               3 time it's run and 
               print "* " & end says it takse star and go to new line
               after '3's 8th value space it print * 
               then 6th value space it print * *
               then 4th value space it print * * *
               then 2nd value space it print * * * *
               
6. negetive indexing k = -1
7. (n-1,-1,-1) says (5-1,-1,-1) = (4,-1,-1)
        x^ y^
        x = n -1 to before -1 that means 0
        y = -1 say distance of before two are -1
        4 - 1 = 3
        3 - 1 = 2
        2 - 1 = 1
        1 - 1 = 0 then stop. so we got 4,3,2,1,0 <-- five line
8. (k,-1,-1) is as like as before.at first because of k = -1 so that 
   (-1,-1,-1) means not usable & next line says end that
9. k = k + 2 get at first k = -1 + 2 = 1 means 0,1 go to for loop and print two space
                    again,k = 1 + 2 = 3 means 0,1,2,3 go to for loop and print four space
                    again,k = 3 + 2 = 5 means 0,1,2,3,4,5 go to for loop and print six space
                    again,k = 5 + 2 = 7 means 0,1,2,3,4,5,6,7 go to for loop and print eight space 
                    then finist cause we know befor for loop say it happen 5 line.
                       
10. We knew n = 5 -1 = 4 first time in '1' but now here n + 1 = 5+1 so that values of i = 0,1,2,3,4
   in for loop i+1 = 0+1 = 1 first time
               i+1 = 1+1 = 2 second time
               3,4,5 time it's run and 
               print "* " after the space line          
   and then we got result.                      
"""