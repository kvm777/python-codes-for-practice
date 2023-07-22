def fun(s):
    if s.count('{')==s.count("}"):
        return 'correct'

    else:
        return 'error'
s='{{{{}}}'
print(fun(s))