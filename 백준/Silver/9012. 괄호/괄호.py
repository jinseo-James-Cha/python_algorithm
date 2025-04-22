T = int(input())
for _ in range(T):
    ip = input()
    st = []
    flag = True
    for parenthesis in ip:
        if parenthesis == '(':
            st.append('(')
        else:
            if st:
                st.pop()
            else:
                flag = False
                break
    if st:
        flag = False
    print('YES' if flag else 'NO')