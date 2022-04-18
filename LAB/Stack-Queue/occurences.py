from Queue import Queue

def substr_position(a, b):
    positions = []
    q = Queue()
    a = list(a)
    b = list(b)

    for i in range(len(a)):
        if a[i] == b[0]:
            flag = 1
            for j in range(i, i + len(b)):
                if j == len(a):
                    break
                Queue.Enqueue(q, a[j])

            for k in range(len(b)):
                if Queue.is_empty(q):
                    flag = 0
                    break

                elif Queue.Dequeue(q) != b[k]:
                    flag = 0
                    break

            if flag:
                positions.append(i)   

    return positions        
        
print(substr_position("bacbacbacbbab","abc"))
print(substr_position("abababc", "aba"))
print(substr_position("bacbacbacbbab","bac"))