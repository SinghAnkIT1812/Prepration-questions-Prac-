#function will tell how many list in the given list

def funcinlist(l):
    count=0
    for i in l:
        if type(i)==list:

    
        
            count+=1
    return count

mixed=[[1,2,3],[1,2],[4,4],[41,66]]
print(funcinlist(mixed))