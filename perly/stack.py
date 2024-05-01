class Stack:
    def __init__(self):
        """A representation of a computational stack
        Parameters
        ----------
        stack: list
            the computational stack
            
        Methods
        -------
        append(num:float)
            adds a number to the stack
        pop()
            pops the last number from the stack
        get_significant_digits()
            returns the current number of sig figs the stack is set to
        set_significant_digits(digits:int)
            sets the stack's number of sig figs
        clear()
            clears the stack
        """
        
        
        self.stack = []
        self.sig_figs = 3

    def pop(self) -> float:
        try:
            return self.stack.pop()
        except IndexError:
            raise Exception("Popped from empty stack")
    
    def get_significant_digits(self) -> int:
        return self.sig_figs

    def set_significant_digits(self, digits:int) -> None:
        try:
            int(digits)
            self.sig_figs = digits
        except ValueError:
            raise Exception(f"Invalid value for significant digits: {digits}")

    def clear(self) -> None:
        self.stack = []

    def append(self, *value:float) -> None:
        """
        Takes a token or list of tokens and adds them to the stack or executes a computation as appropriate
        """
        for i in value:
            try:
                float(i)
                self.stack.append(float(i))
            except ValueError:
                raise Exception(f"Invalid number passed to stack {i}")
    
    def __repr__(self) -> str:
        if self.stack != []:
            rep_string = ''
            for entry in self.stack[:-1]:
                rep_string += f'%.{self.get_significant_digits()}g' % entry + '\n'
            rep_string += f'%.{self.get_significant_digits()}g' % self.stack[-1]
        else: rep_string = ''
        return rep_string
