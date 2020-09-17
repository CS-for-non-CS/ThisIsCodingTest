def separate(word):
    left = right = i = 0

    while left == 0 or right == 0 or left != right:
        if word[i] == '(':
            left += 1
        else:
            right += 1
        i += 1

    return [word[:i], word[i:]]


def is_valid(word):
    left = right = i = 0

    while i < len(word):
        if word[i] == '(':
            left += 1
        else:
            right += 1

        if left < right:
            return False

        i += 1

    return True


def make_right(word):
    if not len(word):
        return ''

    u, v = separate(word)

    if is_valid(u):
        return u + make_right(v)

    result = '('
    result += make_right(v)
    result += ')'

    u = list(u[1:len(u) - 1])

    for i in range(len(u)):
        if u[i] == '(':
            u[i] = ')'
        else:
            u[i] = '('

    return result + ''.join(u)


def solution(p):
    if not len(p):
        return ''

    result = make_right(p)
    return result


print(solution("(()())()"))
