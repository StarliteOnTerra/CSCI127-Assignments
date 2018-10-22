def divide_cake(A, B, u):
    if u > 0:
        x = u * (B // A) 
    return x
print(divide_cake(5, 10, 1))
print(divide_cake(3, 6, 2))
print(divide_cake(2, 5, 3))
print(divide_cake(8, 10, 5))
