#!/usr/bin/env python
# coding: utf-8

# In[21]:


k = 1
  

def printSolution(seat,M,N):  
  
    global k 
    print(k, "-\n") 
    k = k + 1
    for i in range(M):  
        for j in range(N): 
            print(seat[i][j], end = " ") 
        print("\n") 
    print("\n")  

def Check(seat, row, col) : 
    print (row,col)
      
    # Check this row on right side  
    i=row
    j=col+1
    if (seat[i][j]):
        return False
    # check on row on left side
    i=row
    j=col-1
    if i>-1 and j>-1:
        if(seat[i][j]):
            return False
    #check dia left up   
    i=row-1
    j=col-1
    if i>-1 and j>-1:
        if (seat [i][j]):
            return False
    # Check upper diagonal on right side  
    i = row-1
    j = col+1
    if i>-1 and j>-1:
        if(seat[i][j]):
            return False
    # Check upper side  
    i = row-1
    j = col
    if i>-1 and j>-1:
        if(seat [i][j]):
            return False   
  
    # Check lower diagonal on left side  
    i = row +1
    j = col -1
    if i>-1 and j>-1:
        if(seat[i][j]):
            return False
    #check lower right side
    i = row-1
    j = col-1
    if i>-1 and j>-1:
        if(seat[i][j]):
            return False   
    #check lower side 
    i=row+1
    j=col
    if i>-1 and j>-1:
        if(seat[i][j]):
            return False
  
    return True
  

def ChangeRow(seat,i,j,M,N,P,a) : 
      

    if (a == P):  
        printSolution(seat,M,N)  
        return True
  

    res = False
    for i in range(M):
      

        if (Check(seat, i, j)):  
          
            # Place this queen in board[i][col]  
            seat[i][j] = 1;  
  
            # Make result true if any placement  
            # is possible  
            res = ChangeRow(seat,i,j+1,M,N,P,a+ 1) or res; 
            

            seat[i][j] = 0 # BACKTRACK  
            

    return res 
  

def solve() : 
  
    seat = [[0 for j in range(10)]  
                for i in range(10)] 
    M=int(input())
    N=int(input())
    P=int(input())
  
    printSolution(seat,M,N)
    if (ChangeRow(seat, 0,0,M,N,P,0) == False):  
      
        print("Solution does not exist")  
        return
    return
  
# Driver Code  
solve()  


# In[ ]:





# In[ ]:




