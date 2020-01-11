import math
import copy

class Gomoku:
    def __init__(self):
        self.size = int(input('game_size?: '))
        self.win = 5
        self.stack = 8
        self.t = 0
        self.b = [['.' for _ in range(self.size)] for _ in range(self.size)]

    def set(self, nb, nt):
        self.b = copy.deepcopy(nb)
        self.t = copy.deepcopy(nt)
        
    def reset(self):
        self.t = 0
        self.b = [['.' for _ in range(self.size)] for _ in range(self.size)]

    def check_draw(self):
        for i in self.b:
            for ii in i:
                if ii == '.':
                    return False
        return True
    
    def check_win(self):
        if self.check_draw():
            return True, True
        b_succ = []
        w_succ = []
        
        for x in range(len(self.b)):
            for y in range(len(self.b[x])):
                try:
                    s = []
                    for i in range(self.win):
                        s.append(self.b[x+i][y+i])
                    b_succ.append(s==['o' for _ in range(self.win)])
                    w_succ.append(s==['x' for _ in range(self.win)])
                except Exception as e:
                    pass
                
                try:
                    if y-self.win < 0:
                        raise NameError('custom')                    
                    s = []
                    for i in range(self.win):
                        s.append(self.b[x+i][y-i])
                    b_succ.append(s==['o' for _ in range(self.win)])
                    w_succ.append(s==['x' for _ in range(self.win)])

                except Exception as e:
                    pass
                
                try: 
                    s = []
                    for i in range(self.win):
                        s.append(self.b[x][y+i])
                    b_succ.append(s==['o' for _ in range(self.win)])
                    w_succ.append(s==['x' for _ in range(self.win)])
                except Exception as e:
                    pass
                
                try:
                    s = []
                    for i in range(self.win):
                        s.append(self.b[x+i][y])
                    b_succ.append(s==['o' for _ in range(self.win)])
                    w_succ.append(s==['x' for _ in range(self.win)])
                except Exception as e:
                    pass
                if any(b_succ) or any(w_succ):
                    return any(b_succ), any(w_succ)

        return any(b_succ), any(w_succ)

    def render(self):
        for i in self.b:
            print(*i)
        for _ in range(5):
            print('')

    def step(self, x, y):
        if self.b[x][y] != '.':
            return self.check_win()
        
        if self.t == 0:
            self.b[x][y] = 'o'
            self.t = 1
        else:
            self.b[x][y] = 'x'
            self.t = 0
        return self.check_win()


    def ai_step(self, n):
        x = math.floor(n/self.size)
        y = n % self.size
        x1, x2 = self.step(x, y)
        return x1, x2

    def justify(self,ls):
        ls = list(ls)
        for x in range(len(self.b)):
            for y in range(len(self.b[x])):
                if self.b[x][y] != '.':
                    ls[x*len(self.b)+y] = False
        return ls

