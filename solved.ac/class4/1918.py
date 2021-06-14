import sys; read = sys.stdin.readline

def postfix(exp):
    s = []
    ret = ''

    for i in range(len(exp)):
        if exp[i] == ')':
            while s[-1] != '(':
                ret += s.pop()
            s.pop()

        elif exp[i] == '+' or exp[i] == '-':
            while s and s[-1] != '(':
                ret += s.pop()
            s.append(exp[i])
        elif exp[i] == '*' or exp[i] == '/':
            while s and s[-1] != '(':
                if s[-1] == '+' or s[-1] == '-':
                    break
                ret += s.pop()

            s.append(exp[i])
        else:
            s.append(exp[i])
    
    for c in s:
        ret += c
    
    return ret

exp = read().strip()
print(postfix(exp))