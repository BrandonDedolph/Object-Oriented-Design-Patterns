class Computer:
    def __init__(self):
        self.cpu = None
        self.memory = None
        self.storage = None
        self.gpu = None


    def __str__(self):
        return f"Computer [CPU: {self.cpu}, Memory: {self.memory}, Storage: {self.storage}, GPU: {self.gpu}]"
