class Entry:
    def __init__(self):
        self.true_list = []
        self.false_list = []
        self.next_list = []
        self.type = None
        self.value = None
        self.quad = 0
        self.place = ""
        self.lenght = 1
        self.detect = 0
        self.IDdetect = False
        # self.case_dict = []

    @staticmethod
    def backpatch(indexes, quad_list, target):
        for index in indexes:
            quad_list[index].result += ' ' + str(target)