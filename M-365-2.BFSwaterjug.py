"""
Three Jugs and one target-> Collect(A, B, C, k)
return: calculate the minimum steps. If not possible, return -1

capacity = [A,B,C]
Visited = []
processQ = []
[A,0,0]
[0,B,0]
[0,0,C]

def MovingSteps
[a,b,c]
# a move to b
# a move to c
# b move to a
# b move to c
# c move to a
# c move to b
# fill c
# fill a
# fill b

while processQ:
    item = processQ.pop()
    if item satisfy k:
        return steps
    if item in visited:
        continue
    else:
        arr = MovingSteps(item)
        for i

"""
from collections import deque

CAPACITY = [6, 10, 15]


def moveto(item):
    # item -> [A,0,0]
    possible_move = []
    for times in range(3):
        for ind in range(3):
            if ind != times:
                # ie. times = A; ind = B
                if item[ind] < CAPACITY[ind] and item[times] != 0:
                    # jug B hasn't been filled up yet. A can fill it up
                    quota = (CAPACITY[ind]-item[ind])  # how mush it can fill
                    temp = item.copy()
                    if quota >= item[times]:  # pour all of A to other jug
                        temp[ind] += item[times]
                        temp[times] = 0
                    else:
                        temp[times] = item[times] - quota
                        temp[ind] = CAPACITY[ind]
                    possible_move.append(temp)
            else:
                # times = B; ind = B -> fill itself
                if item[ind] == 0:
                    temp = item.copy()
                    temp[ind] = CAPACITY[ind]
                    possible_move.append(temp)

    return possible_move


def collect(A, B, C, K):
    processQ = []
    visited = []
    processQ = deque()
    # init the first move
    processQ.append([0, [0, 0, 0]])
    visited = set()

    while processQ:
        item = processQ.popleft()
        # check K
        if K in item[1]:
            return item[0]

        for move in moveto(item[1]):
            next_move = tuple(move)
            if next_move not in visited:
                visited.add(next_move)
                processQ.append([item[0]+1, move])

    print('Not possible')
    return -1


if __name__ == "__main__":
    print(f'For k = 12, it needs {collect(6,10,15,12)}')
    assert collect(6, 10, 15, 14) == 5


"""
Test
for i in range(16):
    print(collect(6, 10, 15, i))
"""
"""
Test case
1
Number of steps required: 4
2
Number of steps required: 4
3
Number of steps required: 4
4
Number of steps required: 2
5
Number of steps required: 2
6
Number of steps required: 1
7
Number of steps required: 6
8
Number of steps required: 6
9
Number of steps required: 2
10
Number of steps required: 1
11
Number of steps required: 4
12
Number of steps required: 4
13
Number of steps required: 6
14
Number of steps required: 5
"""
