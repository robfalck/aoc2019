import sys


class IntCodeComputer(object):
    """
    The IntCode Computer for AoC2019.

    Parameters
    ----------
    stdio : bool
        If True, interact with this computer through stdin/stdout. Otherwise, programmatically
        interact with this computer through set_input and get_output
    """

    def __init__(self, name='a', stdio=True, input_queue=None, output_queues=None, relative_base=0):
        self._name = name
        self._input_count = 0
        self._phase_setting = None
        self._input_signal = None
        self._output_value = None
        self._use_stdio = stdio
        self._output_queues = [] if output_queues is None else output_queues
        self._input_queue = input_queue
        self._relative_base = relative_base

    def _get_parameter_address(self, idx, pos, tokens, modes=None):
        _modes = [0, 0, 0] if modes is None else modes
        if _modes[idx] == 0:
            address = tokens[pos + 1 + idx]
        elif _modes[idx] == 1:
            address = pos + 1 + idx
        else:
            address = self._relative_base + pos + 1 + idx
        return address

    def _add(self, pos, tokens, modes=None):
        a = self._get_parameter_address(0, pos, tokens, modes)
        b = self._get_parameter_address(1, pos, tokens, modes)
        output_address = self._get_parameter_address(2, pos, tokens, modes)

        tokens[output_address] = tokens[a] + tokens[b]

        new_pos = pos + 4 if output_address != pos else pos

        return new_pos, tokens

    def _mul(self, pos, tokens, modes=None):
        a = self._get_parameter_address(0, pos, tokens, modes)
        b = self._get_parameter_address(1, pos, tokens, modes)
        output_address = self._get_parameter_address(2, pos, tokens, modes)

        tokens[output_address] = tokens[a] * tokens[b]

        new_pos = pos + 4 if output_address != pos else pos

        return new_pos, tokens

    def _store(self, pos, tokens, modes=None):
        output_address = self._get_parameter_address(0, pos, tokens, modes)

        if self._use_stdio:
            tokens[output_address] = int(input('enter input'))
        else:
            tokens[output_address] = int(self._input_queue.get())

        new_pos = pos + 2 if output_address != pos else pos

        return new_pos, tokens

    def _output(self, pos, tokens, modes=None):
        address = self._get_parameter_address(0, pos, tokens, modes)

        if self._use_stdio:
            print(tokens[address])

        for q in self._output_queues:
            q.put(tokens[address])

        return pos + 2, tokens

    def _jump_if_true(self, pos, tokens, modes=None):
        a = self._get_parameter_address(0, pos, tokens, modes)
        b = self._get_parameter_address(1, pos, tokens, modes)

        if tokens[a] != 0:
            new_pos = tokens[b]
        else:
            new_pos = pos + 3

        return new_pos, tokens

    def _jump_if_false(self, pos, tokens, modes=None):
        a = self._get_parameter_address(0, pos, tokens, modes)
        b = self._get_parameter_address(1, pos, tokens, modes)

        if tokens[a] == 0:
            new_pos = tokens[b]
        else:
            new_pos = pos + 3

        return new_pos, tokens

    def _less_than(self, pos, tokens, modes=None):
        a = self._get_parameter_address(0, pos, tokens, modes)
        b = self._get_parameter_address(1, pos, tokens, modes)
        output_address = self._get_parameter_address(2, pos, tokens, modes)

        tokens[output_address] = 1 if tokens[a] < tokens[b] else 0

        new_pos = pos + 4 if output_address != pos else pos

        return new_pos, tokens

    def _equals(self, pos, tokens, modes=None):
        a = self._get_parameter_address(0, pos, tokens, modes)
        b = self._get_parameter_address(1, pos, tokens, modes)
        output_address = self._get_parameter_address(2, pos, tokens, modes)

        tokens[output_address] = 1 if tokens[a] == tokens[b] else 0

        new_pos = pos + 4 if output_address != pos else pos

        return new_pos, tokens

    def _adjust_relative_base(self, pos, tokens, modes=None):
        a = self._get_parameter_address(0, pos, tokens, modes)

        self._relative_base = tokens[a]

        return pos + 2, tokens

    def _process_instruction(self, pos, tokens):
        halt = False

        # Decode instruction/parameter modes
        instruction = tokens[pos]
        opcode = int(str(instruction)[-2:])
        modes = str(instruction)[:-2][::-1]
        modes = [int(modes[k]) if len(modes) > k else 0 for k in range(4)]

        if opcode == 1:
            pos, tokens = self._add(pos, tokens, modes=modes)
        elif opcode == 2:
            pos, tokens = self._mul(pos, tokens, modes=modes)
        elif opcode == 3:
            pos, tokens = self._store(pos, tokens, modes=modes)
        elif opcode == 4:
            pos, tokens = self._output(pos, tokens, modes=modes)
        elif opcode == 5:
            pos, tokens = self._jump_if_true(pos, tokens, modes=modes)
        elif opcode == 6:
            pos, tokens = self._jump_if_false(pos, tokens, modes=modes)
        elif opcode == 7:
            pos, tokens = self._less_than(pos, tokens, modes=modes)
        elif opcode == 8:
            pos, tokens = self._equals(pos, tokens, modes=modes)
        elif opcode == 9:
            pos, tokens = self._adjust_relative_base(pos, tokens, modes=modes)
        elif opcode == 99:
            halt = True
        else:
            raise ValueError('unrecognized code', tokens[pos], tokens, pos)
        return pos, tokens, halt

    def set_input(self, inp):
        self._input_queue.put(inp)

    def get_output(self):
        self._output_queue.get()

    def run_program(self, inp, mem=1000, input_queue=None, output_queues=None):
        self._input_queue = input_queue
        self._output_queues = [] if output_queues is None else output_queues
        self._input_count = 0
        self._output_value = None
        tokens = [int(s) for s in inp.split(',')]
        tokens = [tokens[i] if i < len(tokens) else 0 for i in range(mem)]
        pos = 0
        while True:
            pos, tokens, halt = self._process_instruction(pos, tokens)
            if halt:
                break
        return tokens


if __name__ == '__main__':
    comp = IntCodeComputer()
    comp.run_program(sys.argv[1])
