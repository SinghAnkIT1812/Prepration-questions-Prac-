#is_even=lambda a:a%2==0
#print(is_even(2))

#last_char=lambda a:a[::-1]

#print(last_char('ankit'))

#lambda with if else

#length_s=lambda a: True if len(a)>5 else False
#print(length_s('chu'))

def find_pos(l,s):
    for pos, name in enumerate(l):
        if name==s:
            return pos
    return -1
names=['harshita','harshit','ankit']
print(find_pos(names,'harshit'))

