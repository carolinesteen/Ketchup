class Parser:
    def __init__(self):
        pass

    # Format TBD
    def parse(self, inp: str):
        inp = inp.split()
        if len(inp) == 0:
            return "", ""
        elif len(inp) == 1:
            return inp[0], ""
        else:
            command = inp[0]
            argument = ' '.join(inp[1:])
            return command, argument
