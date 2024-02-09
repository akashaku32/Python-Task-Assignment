n=int(input("enter the row:"))
m=int(input("enter the column:"))
for i in range(1,n+1):
    
        for j in range(1, m+1):
            if j%2!=0:
                print("  ---",end="")
            else:
                print("       ",end="")
        print()
        for j in range(1,m+1):
            if j%2!=0:
                print("/     \\",end="")
            else:
                print("_ _ _",end="")
        print()
        for j in range(1,m+1):
            if j%2!=0:
                print("\\     /",end="")
            else:
                 print("     ",end="")
        print()
        for j in range(1,m+1):
            if i==n:
                if j%2!=0:
                    print("  ---",end="")
                else:
                    print("       ",end="")
        
        
        
        
            
             
             


        
        
        
        
        
