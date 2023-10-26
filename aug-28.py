def validate(str):
    c = 6
    if(len(str)>=6 and len(str)<=22):
        c-=1

    for i in str:
        if i.isupper():
            c-=1
            break
    for i in str:
        if i.islower():
            c-=1
            break
    for i in str:
        if i.isnumeric():
            c-=1
            break

    spl = ["@", "!", "&", "^", "%", "*", "#"]
    for i in str:
        if i in spl:
            c-=1
            break

    for i in range(len(str)-1):
        if str[i] == str[i+1]:
            break
    else:
        c-=1
    
    return c



s = input()
print(validate(s))