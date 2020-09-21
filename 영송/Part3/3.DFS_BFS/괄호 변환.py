container = input()

ans = ''
stack = []
for i in range(len(container)):
    if container[i] == '(':
        stack.append(container[i])
    elif container[i] ==')':
        stack.pop()

