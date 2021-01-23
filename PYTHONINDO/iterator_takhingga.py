class InfIter:
    """infinite iterator"""

    def __iter__(self):
        self.num = 1
        return self
    def __next__(self):
        num = self.num
        return num