def find(*a):
    print(a)
    x=list(a)
    x=sorted(x)
    for i in range(1,5):
        print(x.pop(),end=' ')
        
find(7,8,4,5,2,3,90,214,68,89)#function call        
