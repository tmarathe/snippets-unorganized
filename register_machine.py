# implementation of a universal register machine

class URM:
    def __init__(self, register, program):
        self.register = register
        self.program = program
        self.program_counter = 1
    
    def successor(self, index):
        self.register[index] += 1
        self.program_counter += 1
    
    def zero(self, index):
        self.register[index] = 0
        self.program_counter += 1
    
    def jump(self, m, n, i):
        if self.register[m] == self.register[n]:
            self.program_counter = i

    

if __name__ == '__main__':
