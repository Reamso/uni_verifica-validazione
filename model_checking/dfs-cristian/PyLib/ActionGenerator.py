class ActionGenerator:

    def __init__(self, *args):
        self.args = args
        self.cardinality = reduce(lambda x, y : x * y, [len(i) for i in args])
        self.index = 0


    def next():
        temp = self.index
        self.index = self.index + 1
        if(temp < self.cardinality):
            out = [] * len(args)
            for i in range(len(args)):
                out[i] = args[i][temp % len(args[i])]
                temp = temp / len(args[i])
            return out
        else
            return None
