

class IntCodeComputer(object):

    def __init__(self):
        pass

    def _add(self, pos, tokens, modes=None):

        _modes = [0, 0, 0] if modes is None else modes

        if _modes[0] == 0:
            a = tokens[tokens[pos + 1]]
        else:
            a = tokens[pos + 1]

        if _modes[1] == 0:
            b = tokens[tokens[pos + 2]]
        else:
            b = tokens[pos + 2]

        if _modes[2] == 0:
            output_address = tokens[pos + 3]
        else:
            raise ValueError('Output address in parameter mode!')

        tokens[output_address] = a + b
        return pos + 4, tokens

    def _mul(self, pos, tokens, modes=None):
        _modes = [0, 0, 0] if modes is None else modes

        if _modes[0] == 0:
            a = tokens[tokens[pos + 1]]
        else:
            a = tokens[pos + 1]

        if _modes[1] == 0:
            b = tokens[tokens[pos + 2]]
        else:
            b = tokens[pos + 2]

        if _modes[2] == 0:
            output_address = tokens[pos + 3]
        else:
            raise ValueError('Output address in parameter mode!')

        tokens[output_address] = a * b
        return pos + 4, tokens

    def _store(self, pos, tokens, modes=None):
        tokens[tokens[pos + 1]] = int(input('enter input'))
        return pos + 2, tokens

    def _output(self, pos, tokens, modes=None):
        if modes[0] == 0:
            print(tokens[tokens[pos + 1]])
        elif modes[0] == 1:
            print(tokens[pos + 1])
        else:
            raise ValueError('unknown mode in output', modes[0])
        return pos + 2, tokens

    def _process_instruction(self, pos, tokens):
        halt = False

        # Decode instruction/parameter modes
        instruction = tokens[pos]
        opcode = int(str(instruction)[-2:])
        modes = str(instruction)[:-2][::-1]
        modes = [int(modes[k]) if len(modes) > k else 0 for k in range(4)]

        # print(instruction, opcode, modes)

        if opcode == 1:
            pos, tokens = self._add(pos, tokens, modes=modes)
        elif opcode == 2:
            pos, tokens = self._mul(pos, tokens, modes=modes)
        elif opcode == 3:
            pos, tokens = self._store(pos, tokens, modes=modes)
        elif opcode == 4:
            pos, tokens = self._output(pos, tokens, modes=modes)
        elif opcode == 99:
            halt = True
        else:
            raise ValueError('unrecognized code', tokens[pos])
        return pos, tokens, halt

    def run_program(self, inp, mem=100):
        tokens = [int(s) for s in inp.split(',')]
        tokens = [tokens[i] if i < len(tokens) else 0 for i in range(mem)]
        pos = 0
        while True:
            pos, tokens, halt = self._process_instruction(pos, tokens)
            if halt:
                break
        return tokens



if __name__ == '__main__':
    sample = '1002,4,3,4,33'
    comp = IntCodeComputer()
    output = comp.run_program(sample)
    print(output)

    sample = '1101,100,-1,4,0'
    output = comp.run_program(sample)
    print(output)