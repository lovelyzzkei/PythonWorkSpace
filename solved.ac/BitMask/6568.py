import sys; read = sys.stdin.readline

lines = []
for i in range(32):
    lines.append(read())

ret = []
for tc in range(len(lines)//32):
    memory = [0] * 32
    adder = 0; pc = 0
    
    for i in range(tc*32, (tc+1)*32):
        line = lines[pc]
        # 명령어 해석
        order = int('0b'+line[:3],2); address = int('0b'+line[3:],2)
        pc += 1     # pc 1 증가

        if order == 0:
            memory[address] = adder
        if order == 1:
            adder = memory[address]
        if order == 2:
            if adder == 0:
                pc = address
        if order == 3:
            continue
        if order == 4:
            adder -= 1
        if order == 5:
            adder += 1
        if order == 6:
            pc = address
        if order == 7:
            adder = 0; pc = 0

    # 32개의 테스트 케이스로 나눔
    ret.append(bin(adder))
    print(ret)