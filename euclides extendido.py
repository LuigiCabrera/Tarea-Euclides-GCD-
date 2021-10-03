def ext_euclid(a,b):
    if a % b == 0:
        return b,0,1
    r, x_, y_ = ext_euclid(b, a%b)
    x, y = y_, x_ - int(a/b)*y_
    return r,x,y

print("\n\n\t*** Euclides Algorithm Extended ***\n\n")

while True:
    print("Write 0 to exit")
    a = int(input("Write A: "))
    if a == 0: break
    b = int(input("Write B: "))
    if b == 0: break
    r, x, y = ext_euclid(a, b)
    print(f"\nGCD({a}, {b}) = {r}\nx = {x}\ty = {y}\n\n")
