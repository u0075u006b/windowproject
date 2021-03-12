
class QSSadd:
    def __init__(self):
        pass

    @staticmethod
    def readqss(style):
        with open(style, 'r') as f:
            return f.read()
