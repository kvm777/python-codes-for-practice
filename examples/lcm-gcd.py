a,b = map(int, input().split())



c= max(a, b)

while True:
    if c%a==0 and c%b==0:
        break
    c+=1

print(f"lcm of {a} and {b} is {c}")



d = min(a,b)

while True:
    if a%d==0 and b%d==0:
        break
    d-=1

print(f"gcd of {a} and {b} is {d}")

