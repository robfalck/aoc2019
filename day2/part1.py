with open('input.txt') as wdf:
    line = wdf.readline()

tokens = [int(s) for s in line.split(',')]

tokens[1] = 12
tokens[2] = 2

# tokens = [1,9,10,3,2,3,11,0,99,30,40,50]


def add(pos, tokens):
    address_1 = tokens[pos + 1]
    address_2 = tokens[pos + 2]
    address_3 = tokens[pos + 3]
    tokens[address_3] = tokens[address_1] + tokens[address_2]
    return pos + 4, tokens

def mul(pos, tokens):
    address_1 = tokens[pos + 1]
    address_2 = tokens[pos + 2]
    address_3 = tokens[pos + 3]
    tokens[address_3] = tokens[address_1] * tokens[address_2]
    return pos + 4, tokens



def process_instruction(pos, tokens):
    halt = False
    if tokens[pos] == 1:
        pos, tokens = add(pos, tokens)
    elif tokens[pos] == 2:
        pos, tokens = mul(pos, tokens)
    elif tokens[pos] == 99:
        halt = True
    else:
        raise ValueError('unrecognized code', tokens[pos])
    return pos, tokens, halt

if __name__ == '__main__':
    pos = 0
    print(pos, tokens)
    while True:
        pos, tokens, halt = process_instruction(pos, tokens)
        # print
        print(pos, tokens)
        if halt:
            break

# 10694