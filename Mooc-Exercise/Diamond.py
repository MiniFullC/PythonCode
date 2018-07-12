import math
def fourth(n):
    n+=1
    cc=math.ceil((n*2-19)/2)
    ff=math.floor((n*2-19)/2)
    print(cc,ff)
    for col in range(n*2-1):
        if(col==0 or col==n*2-2):
            print('+',end='')
        else:
            print('-',end='')
    print()
    for a in reversed(range(n-1)):
        print('|',end='')
        for b in range(a):
            print(' ',end='')
        for c in range(n-a-1):
            if(c==n-a-2 or a==0):
                print('*',end='')
            else:
                print('-',end='')
        for d in range(n-a-2):
            if(a==0):
                print('*',end='')
            else:
                print('+',end='')
        for e in range(a):
            print(' ',end='')
        print('|')
        
            
    for i in range(n-2):
        print('|',end='')
        for j in range(i+1):
            print(' ',end='')
        for k in reversed(range(n-i-2)):
            if(k==0):
                print('*',end='')
            else:
                print('+',end='')
        for l in reversed(range(n-i-3)):
            print('-',end='')
        for m in range(i+1):
            print(' ',end='')
        print('|')
    for col in range(n*2-1):
        if(col==0 or col==n*2-2):
            print('+',end='')
        else:
            print('-',end='')
    print()
    print('|',end='')
    
    for i in range(cc):
        print(' ',end='')
    print("This is a graph.",end='')
    for i in range(ff):
        print(' ',end='')
    print('|')
    for col in range(n*2-1):
        if(col==0 or col==n*2-2):
            print('+',end='')
        else:
            print('-',end='')
        
 
fourth(20)
 

