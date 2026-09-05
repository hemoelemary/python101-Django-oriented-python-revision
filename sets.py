#sets
#mutable
# lst = [var1,var2,var3]
dictionary = {
    'key':'value'
}
s = {'s1','s2','s3'}
print(s)
s = {'s1','s2','s4','s4'}
print(s) #just merging s4 together in no order and no repeat
s.add('s5')
print(s)
s.remove('s1')
print(s)
