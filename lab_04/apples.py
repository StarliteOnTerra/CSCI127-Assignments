def countApplesAndOranges(s,t,a,b,apples,oranges):
    num_apples = 0
    num_oranges = 0
    for d in apples:
        d = a + d
        if s <= d and t >= d:
            num_apples += 1
    for d in oranges:
        d = b + d
        if t >= d and s <= d:
            num_oranges
            num_apples += 1
    print(num_apples)
    print(num_apples)

countApplesAndOranges(4,12,1,15,[5,3,-2],[2,6,-7])
countApplesAndOranges(-2,7,-5,8,[7,10,-2],[4,-5,-9])
        
            
        
        
        
        
    
 

    