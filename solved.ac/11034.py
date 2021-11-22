import sys; read = sys.stdin.readline

ret = []
while True:
    try: 
        a, b, c = map(int, read().split())
    except:
        print("\n".join(str(x) for x in ret))
        break
    
    ret.append(c-b-1 if c-b >= b-a else b-a-1)