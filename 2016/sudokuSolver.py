import collections


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = 0 if n == 0 else len(board[0])
        if m != 9 or n != 9: return
        candidates = set('123456789')

        filled = 0

        # rowX, colX, regionX
        allC = {}
        regionC = collections.defaultdict(set)  # {(0-2, 0-2): x, y candidates}
        colC = collections.defaultdict(set)  # {0-8: x, y candidates}
        regionX = collections.defaultdict(set)
        colX = collections.defaultdict(set)
        rowC = collections.defaultdict(set)  # cur candidates
        rowX = collections.defaultdict(set)

        def do_clear(X, C, dq, allC):
            for mark in X:
                for x, y in C:
                    if mark in allC[(x, y)]:
                        allC[(x, y)].discard(mark)
                        if len(allC[(x, y)]) == 1:
                            dq.append((x, y))

        dq = collections.deque()
        for i in range(9):  # for col
            for j in range(9):
                if board[i][j] == '.':
                    cur_c = candidates.copy()
                    allC[(i, j)] = cur_c
                    colC[j].add((i, j))
                    rowC[i].add((i, j))
                    regionC[(i // 3, j // 3)].add((i, j))
                else:
                    filled += 1
                    c = board[i][j]
                    rowX[i].add(c)
                    colX[j].add(c)
                    regionX[(i // 3, j // 3)].add(c)
                if i == 8:
                    do_clear(colX[j], colC[j], dq, allC)
                if (i + 1) % 3 == (j + 1) % 3 == 0:
                    do_clear(regionX[(i // 3, j // 3)], regionC[(i // 3, j // 3)], dq, allC)
            do_clear(rowX[i], rowC[i], dq, allC)

        while dq:
            x, y = dq.popleft()
            filled += 1
            c = str(allC[(x, y)].pop())
            board[x][y] = c
            rowX[x].add(c)
            colX[y].add(c)
            regionX[(x // 3, y // 3)].add(c)
            do_clear([c], rowC[x], dq, allC)
            do_clear([c], colC[y], dq, allC)
            do_clear([c], regionC[(x // 3, y // 3)], dq, allC)
            rowC[x].discard((x, y))
            colC[y].discard((x, y))
            regionC[(x // 3, y // 3)].discard((x, y))
            del allC[(x, y)]

        if filled < 81:
            keys = list(allC.keys())
            keys.sort()

            def check(board, x, y, n):
                for i in range(9):
                    if board[x][i] == n and i != y or board[i][y] == n and x != i:
                        return False
                sx, sy = x // 3 * 3, y // 3 * 3
                for i in range(sx, sx + 3):
                    for j in range(sy, sy + 3):
                        if board[i][j] == n and i != x and j != y:
                            return False
                return True

            def search(allC, board, filled, keys, ki):
                x, y = keys[ki]
                print('Entering:', x, y, allC[(x, y)])
                for nextN in allC[(x, y)]:
                    print('Checking: ', x, y, nextN, ki, )
                    if check(board, x, y, nextN):
                        print('OKay:', x, y, nextN, ki)
                        new_filled = filled + 1
                        board[x][y] = nextN
                        if new_filled == 81:
                            print('True : reached 81')
                            return True
                        if search(allC, board, new_filled, keys, ki + 1):
                            return True
                        board[x][y] = '.'
                print('False: Exhausted:', x, y, ki)
                for i in board: print(i)
                return False
            res = search(allC, board, filled, keys, 0)
            print(res)



s = Solution()
board = [
     "..9748...",
     "7........",
     ".2.1.9...",
     "..7...24.",
     ".64.1.59.",
     ".98...3..",
     "...8.3.2.",
     "........6",
     "...2759.."
     ]
newb = []
for i in board:
    newb.append([c for c in i])

for i in newb:
    print(i)
print('=' * 100)
s.solveSudoku(newb)
for i in newb: print(i)
