def strips(l,n):
    x=""
    y=""
    l=sorted(l)
    for i in l:
        x+=i[1]
        y+=i[2]
    print(x,y)

l=["1Au","4uF","5qx","7Uv","9sY","8lT","2Sk","6NN","3f3"]
strips(l,len(l))