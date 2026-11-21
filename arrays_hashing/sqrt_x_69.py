def mySqrt(x: int) -> int:
        #mysqrt = 0
        for i in range(x+1):
            if i*i > x:
                return mysqrt
            mysqrt = i
        return mysqrt
    
x = 2
print(mySqrt(x))