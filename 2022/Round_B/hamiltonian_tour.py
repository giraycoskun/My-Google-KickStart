# Hamiltonian Tour
# KickStart 2022 Round B Problem 4
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74/0000000000acf318#problem


test_count = int(input())
for k in range(test_count):
    R, C = map(int, input().split())
    grid = []
    for _ in range(R):
        test = list(input())
        grid.append(test)

    cycle = {}
    stack = [(0, 0)]
    control = {(0, 0)}
    while len(stack) != 0:
        i, j = stack.pop()
        if (2 * i, 2 * j) not in cycle:
            cycle[(2 * i, 2 * j)] = (2 * i, 2 * j + 1)
        if (2 * i, 2 * j + 1) not in cycle:
            cycle[(2 * i, 2 * j + 1)] = (2 * i + 1, 2 * j + 1)
        if (2 * i + 1, 2 * j + 1) not in cycle:
            cycle[(2 * i + 1, 2 * j + 1)] = (2 * i + 1, 2 * j)
        if (2 * i + 1, 2 * j) not in cycle:
            cycle[(2 * i + 1, 2 * j)] = (2 * i, 2 * j)

        if i + 1 < R:
            if grid[i + 1][j] == '*' and (i + 1, j) not in control:
                control.add((i + 1, j))
                stack.append((i + 1, j))
                cycle[(2 * i + 1, 2 * j + 1)] = (2 * i + 1 + 1, 2 * j + 1)
                cycle[(2 * i + 1 + 1, 2 * j)] = (2 * i + 1, 2 * j)
        if i - 1 >= 0:
            if grid[i - 1][j] == '*' and (i - 1, j) not in control:
                control.add((i - 1, j))
                stack.append((i - 1, j))
                cycle[(2 * i, 2 * j)] = (2 * i - 1, 2 * j)
                cycle[(2 * i - 1, 2 * j + 1)] = (2 * i, 2 * j + 1)
        if j + 1 < C:
            if grid[i][j + 1] == '*' and (i, j + 1) not in control:
                control.add((i, j + 1))
                stack.append((i, j + 1))
                cycle[(2 * i, 2 * j + 1)] = (2 * i, 2 * j + 1 + 1)
                cycle[(2 * i + 1, 2 * j + 1 + 1)] = (2 * i + 1, 2 * j + 1)
        if j - 1 >= 0:
            if grid[i][j - 1] == '*' and (i, j - 1) not in control:
                control.add((i, j - 1))
                stack.append((i, j - 1))
                cycle[(2 * i), 2 * j - 1] = (2 * i, 2 * j)
                cycle[(2 * i + 1, 2 * j)] = (2 * i + 1, 2 * j - 1)

    continue_check = False
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '*':
                if (i, j) not in control:
                    path = "IMPOSSIBLE"
                    print("Case #{case_no}: {answer}".format(case_no=k + 1, answer=path))
                    continue_check = True
                    break
        if continue_check:
            break

    if continue_check:
        continue

    path = ""
    root = (0, 0)
    next_node = cycle[root]
    first = True
    # grid_map = [['*' for _ in range(2*C)] for _ in range(2*R)]
    while root != (0, 0) or first:
        first = False
        if next_node[0] == root[0] - 1:
            path += 'N'
            # grid_map[root[0]][root[1]] = '↑'
        elif next_node[0] - 1 == root[0]:
            path += 'S'
            # grid_map[root[0]][root[1]] = '↓'
        elif next_node[1] - 1 == root[1]:
            path += 'E'
            # grid_map[root[0]][root[1]] = '→'
        elif next_node[1] == root[1] - 1:
            path += 'W'
            # grid_map[root[0]][root[1]] = '←'
        root = next_node
        next_node = cycle[root]

    # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in grid_map]))

    print("Case #{case_no}: {answer}".format(case_no=k + 1, answer=path))
