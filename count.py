class counter:
    def __init__(self,fn):
        self.count=0
        self.fn=fn
        
    def __call__(self,*args):
        self.count=self.count+1
        return self.fn(*args)
        
    def counter(self):
        return self.count
