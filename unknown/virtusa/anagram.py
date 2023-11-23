    

def anagram(input1,input2):
        #read only region 
        s1=input1
        s2=input2
        if sorted(s1)==sorted(s2):
            return 'yes'
        else:
            return 'no'


s1 = input()
s2 = input()
print(anagram(s1,s2))

        