def find_legal_position(arr, n_row, n_queens, trace_back=False):
    start = 0
    if trace_back:
        start = arr[n_row] + 1
    for col in range(start, n_queens):
        ok = True
        for row in range(n_row):  # [0, n_row)
            if arr[row] == col:  # two queens share the same column
                ok = False
                break
            if n_row - row == abs(col - arr[row]): # two queens share the same diagonal
                ok = False
                break
        if ok:
            return col
    return None  # no position we can place a queen on the n_row
    
def solve_queen_puzzle(n_queens):
    result = [0] * n_queens
    n_row = 0  # 从0行开始，一行一行安置皇后
    while n_row < n_queens:
        pos = find_legal_position(result, n_row, n_queens)
        if pos is not None: # 往前走
            result[n_row] = pos
            if n_row == n_queens - 1:
                yield result[:] # 找到一个结果，返回
        if pos is None or n_row == n_queens - 1:
            while 1:
                n_row -= 1
                if n_row < 0:
                    return # 所有路已经穷尽
                pos = find_legal_position(result, n_row, n_queens, back_tracing=True)
                if pos:  # 换条路试一下
                    result[n_row] = pos
                    break
        n_row += 1