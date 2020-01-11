from Gomoku_v4 import Gomoku
import numpy as np
import cv2
import time
search_n = 6
block_penalty = 1 #problematic
null_reward = 0
value_activation = 1
stone_reward = 1
ini_reward = 1
env = Gomoku()
ai_turn = int(input('black or white? (0 for white and 1 for black)'))
SELF_PLAY = False

def click(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:   
        x = int(x/(500/env.size))
        y = int(y/(500/env.size))
        env.step(y,x)
        
def draw_img(board):
    cv2.namedWindow('game')
    cv2.setMouseCallback('game',click)
    gap = 15
    real_img = np.zeros((500,500,3))
    for x in range(int(len(real_img))):
        for y in range(int(len(real_img))):
            real_img[x][y] = (0, 255, 0)
                       
    for x1 in range(len(board)):
        for y1 in range(len(real_img)):
            real_img[int(len(real_img)/len(board)*x1)+gap][y1] = (0,0,0)
            real_img[y1][int(len(real_img)/len(board)*x1)+gap] = (0,0,0)

    for x2 in range(len(board)):
        for y2 in range(len(board)):
            if board[x2][y2] == 'o':
                cv2.circle(real_img, (int(((len(real_img)/len(board))*y2)+gap),int(((len(real_img)/len(board))*x2)+gap)), 11, (0,0,0),-1)
            if board[x2][y2] == 'x':
                cv2.circle(real_img, (int(((len(real_img)/len(board))*y2)+gap),int(((len(real_img)/len(board))*x2)+gap)), 11, (255, 255, 255),-1)
    cv2.imshow('game',real_img)
    cv2.waitKey(1)
    
def b1(x,y,b,t):
    if t == 0:
        counter = ini_reward
        for i in range(1, search_n):
            if x-i<0 or y-i<0 or b[x-i][y-i]=='x':
                counter -= block_penalty
                break
            if b[x-i][y-i] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward

    else:
        counter = ini_reward
        for i in range(1, search_n):
            if x-i<0 or y-i<0 or b[x-i][y-i]=='o':
                counter -= block_penalty
                break
            if b[x-i][y-i] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward

    return counter

def b2(x,y,b,t):
    if t == 0:
        counter = ini_reward
        for i in range(1, search_n):
            if x-i<0 or b[x-i][y]=='x':
                counter -= block_penalty
                break
            if b[x-i][y] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward

    else:
        counter = ini_reward
        for i in range(1, search_n):
            if x-i<0 or b[x-i][y]=='o':
                counter -= block_penalty
                break
            if b[x-i][y] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward

    return counter

def b3(x,y,b,t):
    if t == 0:
        counter = ini_reward
        for i in range(1, search_n):
            if y-i<0 or b[x][y-i]=='x':
                counter -= block_penalty
                break
            
            if b[x][y-i] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward
    else:
        counter = ini_reward
        for i in range(1, search_n):
            if y-i<0 or b[x][y-i]=='o':
                counter -= block_penalty
                break
            if b[x][y-i] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward

    return counter

def b4(x,y,b,t):
    if t == 0:
        counter = ini_reward
        for i in range(1, search_n):
            if x+i>=len(b) or y-i<0 or b[x+i][y-i]=='x':
                counter -= block_penalty
                break
            if b[x+i][y-i] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward
    else:
        counter = ini_reward
        for i in range(1, search_n):
            if x+i>=len(b) or y-i<0 or b[x+i][y-i]=='o':
                counter -= block_penalty
                break
            if b[x+i][y-i] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward
    return counter

def f1(x,y,b,t):
    if t == 0:
        counter = ini_reward
        for i in range(1, search_n):
            if x+i>=len(b) or y+i>=len(b) or b[x+i][y+i]=='x':
                counter -= block_penalty
                break
            if b[x+i][y+i] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward

    else:
        counter = ini_reward
        for i in range(1, search_n):
            if x+i>=len(b) or y+i>=len(b) or b[x+i][y+i]=='o':
                counter -= block_penalty
                break
            if b[x+i][y+i] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward

    return counter

def f2(x,y,b,t):
    if t == 0:
        counter = ini_reward
        for i in range(1, search_n):
            if x+i>=len(b) or b[x+i][y]=='x':
                counter -= block_penalty
                break
            if b[x+i][y] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward
    else:
        counter = ini_reward
        for i in range(1, search_n):
            if x+i>=len(b) or b[x+i][y]=='o':
                counter -= block_penalty
                break
            if b[x+i][y] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward

    return counter

def f3(x,y,b,t):
    if t == 0:
        counter = ini_reward
        for i in range(1, search_n):
            if y+i>=len(b) or b[x][y+i]=='x':
                counter -= block_penalty
                break
            if b[x][y+i] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward

    else:
        counter = ini_reward
        for i in range(1, search_n):
            if y+i>=len(b) or b[x][y+i]=='o':
                counter -= block_penalty
                break
            if b[x][y+i] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward
    return counter

def f4(x,y,b,t):
    if t == 0:
        counter = ini_reward
        for i in range(1, search_n):
            if x-i<0 or y+i>=len(b) or b[x-i][y+i]=='x':
                counter -= block_penalty
                break

            if b[x-i][y+i] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward
    else:
        counter = ini_reward
        for i in range(1, search_n):
            if x-i<0 or y+i>=len(b) or b[x-i][y+i]=='o':
                counter -= block_penalty
                break

            if b[x-i][y+i] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward
    return counter
    
def evaluate(b, t):
    values = [0 for _ in range(len(b)**2)]
    threats = [0 for _ in range(len(b)**2)]
    if t == 0:
        ot = 1
    else:
        ot = 0
    for x in range(len(b)):
        for y in range(len(b)):
            if b[x][y] != '.':
                values[x*len(b)+y] = False
                threats[x*len(b)+y] = False
            else:
                value = ([b1(x,y,b,t)+f1(x,y,b,t), b2(x,y,b,t)+f2(x,y,b,t), b3(x,y,b,t)+f3(x,y,b,t), b4(x,y,b,t)+f4(x,y,b,t)])
                threat = ([b1(x,y,b,ot)+f1(x,y,b,ot), b2(x,y,b,ot)+f2(x,y,b,ot), b3(x,y,b,ot)+f3(x,y,b,ot), b4(x,y,b,ot)+f4(x,y,b,ot)])
                value = max(value)
                threat = max(threat)                     
                values[x*len(b)+y] = int(value)
                threats[x*len(b)+y] = int(threat)
    if max(values)-value_activation >= max(threats):
        return values
    return threats

def main():

    env.reset()
    env.render()
    bw = False
    ww = False
    if ai_turn == 0 or SELF_PLAY:
        value_list = evaluate(env.b, env.t)
        env.step(int(env.size/2), int(env.size/2))
    while not (bw or ww):
        if env.t == ai_turn or SELF_PLAY:
            value_list = evaluate(env.b, env.t)
            action = np.argmax(value_list)
            bw, ww = env.ai_step(action)
            env.render()
        else:
            draw_img(env.b)
    
        draw = bw and ww
        draw_img(env.b)
        if not draw:
            if bw:
                print('black won!')
                time.sleep(60)
            if ww:
                print('white_won!')
                time.sleep(60)
        else:
            print('draw!')
            time.sleep(60)
if __name__ == '__main__':
    main()
    
