import numpy as np
from collections import deque


def pull_left_top(d:np.array):
    while np.count_nonzero(d[:, :1]) == 0:
        d = np.roll(d, shift=-1)
    while np.count_nonzero(d[:1, :]) == 0:
        d = np.roll(d, shift=-1, axis=0)
    return d


def block_split(block, x, y):
    q = deque()
    q.append((x, y, 0))
    visit = np.zeros_like(block)
    visit[x][y] = 1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    l = len(block)

    while q:
        x, y, d = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= l or ny >= l:
                continue
            if block[nx][ny] == 1 and visit[nx][ny] == 0: # 이어진 2\1
                q.append((nx, ny, d+1))
                visit[nx][ny] = 1
                block[nx][ny] = 0

    return pull_left_top(visit)


def match(hole, block):
    for _ in range(4):
        block = pull_left_top(np.rot90(block))
        tmp = hole - block
        if np.count_nonzero(tmp) == 0:
            return True
    return False


def solution(game_board, block):
    # blocks
    block = np.array(block, int)
    blocks = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}
    for i in range(len(block)):
        for j in range(len(block)):
            if block[i][j] == 1:
                b = block_split(block, i, j)
                blocks[np.count_nonzero(b)].append(b)

    # holes
    hole = 1 - np.array(game_board, int)
    holes = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}
    for i in range(len(block)):
        for j in range(len(block)):
            if hole[i][j] == 1:
                h = block_split(hole, i, j)
                holes[np.count_nonzero(h)].append(h)
    result = 0

    for i in range(1, 7):
        for h in holes[i]:
            for j, b in enumerate(blocks[i]):
                if match(h, b):
                    result += i
                    blocks[i].pop(j)
                    break

    return result