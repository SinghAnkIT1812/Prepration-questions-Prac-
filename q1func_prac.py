#func takes more no. of list to return their average
def heylist(*args):
    average=[]
    for pair in zip(*args):
        average.append(sum(pair)/len(pair))
    return average
print(heylist([1,2,3],[4,5,6],[7,8,9]))
#using lambda function
hey_list1 = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]

print(hey_list1([1,2,3],[4,5,6],[7,8,9]))