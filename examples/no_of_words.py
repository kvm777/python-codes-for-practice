
#frequency of word 
'''
input : a b f a d e b d 
output: {'a': 2, 'b': 2, 'f': 1, 'd': 2, 'e': 1}
'''

n=list(map(str,input().split()))

res={key:n.count(key) for key in n}

print(res)