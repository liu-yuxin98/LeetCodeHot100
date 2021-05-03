class MinStack(object):


    def __init__(self):
        self.stack = []


    def push(self, x):
        self.stack.insert(0,x)
        return None


    def pop(self):
        self.stack.pop(0)
        return None


    def top(self):
        return self.stack[0]


    def getMin(self):
        return min(self.stack)



