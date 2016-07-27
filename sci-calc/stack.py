class stack:
    def __init__(self):
        self.itm=[]
    def push(self,d):
        self.itm.append(d)
    def pop(self):
        return self.itm.pop()
    def isempty(self):
        return self.itm==[]
    def peek(self):
        return self.itm[len(self.itm)-1]
    def size(self):
        return len(self.itm)
    def printstk(self):
        return (print(self.itm))
    
