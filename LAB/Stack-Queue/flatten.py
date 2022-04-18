from Queue import Queue 

def flatten(l):
    q = Queue()
    flag = 0
    for i in l:
        if type(i) == list:
            flag = 1
            for j in i:
                q.Enqueue(j)

        else:
            q.Enqueue(i)

    if flag:
        return flatten(q.Queue) 
                
    else:
        return q.Queue

print(flatten([1,2,3,4]))
print(flatten([1,[2],3,4]))
print(flatten([1,[[2],3],4]))
print(flatten([1,[[2],3],[[[4]]]]))