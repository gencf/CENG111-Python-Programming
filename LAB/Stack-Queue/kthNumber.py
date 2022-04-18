from Stack import Stack

def kthNumber(l, n):
    st = Stack()
    for i in l:
        if st.is_empty():
            st.push(i)

        elif st.top() <= i:
            st.push(i)

        else:
            st2 = Stack()
            while not st.is_empty() and st.top() > i:
                st2.push(st.pop())

            st.push(i)

            while not st2.is_empty():
                st.push(st2.pop())

    sorted = st.Stack
    return sorted[n - 1]

print(kthNumber([14, 5, 3, 7, -9, 0, 1, 3, 4, -3, -11, 6, 9, -1, -3, -12], 7))
print(kthNumber([14, 5, 3, 7, -9, 0, 1, 3, 4, -3, -11, 6, 9, -1, -3, -12], 12))
