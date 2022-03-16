class Cell:

    def __init__(self, row, column, ordinalnumber, number):
        self.row = row
        self.column = column
        self.ordinalnumber = ordinalnumber
        self.number = number
        self.puzzleNumber = 0
        self.block = 0
        self.chosen = False
        self.potential = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.eliminate = []
        self.adjust = True
        self.entered = 0
        self.wrong = 0
        self.related_wrong = 0
        self.related_number = 0
        self.pencil = True
        self.pencil_number = []
        self.related_pencil = False
        
        self.x = 0
        self.y = 0
        self.centerx = 0
        self.centery = 0
        self.center = 0
        self.left = 0
        self.right = 0
        self.top = 0
        self.bottom = 0
        
        self.level = ""
        self.time = 0