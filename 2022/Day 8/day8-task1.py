with open("2022/Day 8/input.txt", "r", encoding="utf8") as inputfile:
    grid = []
    visabletrees = int()
    for line in inputfile.readlines():
        grid.append([int(tree) for tree in line.rstrip()])
    col = 1
    for column in grid:
        # Ignore the top and bottom
        if column == grid[0] or column == grid[-1]:
            visabletrees += len(column)
            continue
        # Add the first and last trees
        visabletrees += 2
        # Ignore the first and last
        row = 1
        for tree in column[1:-1]:
            # print(f"Col:{col}, Row:{row}, Tree:{tree}")
            visable = False
            if col != 1:
                for above in grid[: col - 1]:
                    if tree <= above[row]:
                        visable = False
                        break
                    visable = True
                    break
                for below in grid[col + 1 :]:
                    if tree <= below[row]:
                        visable = False
                        break
                    visable = True
                    break
            elif col == 1 and tree > grid[col - 1][row]:
                visable = True
            elif tree > grid[col + 1][row]:
                visable = True
            if row != 1:
                for left in grid[col][: row - 1]:
                    if tree <= left:
                        visable = False
                        break
                    visable = True
                    break
                for right in grid[col][row + 1 :]:
                    if tree <= right:
                        visable = False
                        break
                    visable = True
                    break
            elif row == 1 and tree > grid[col][row - 1]:
                visable = True
            elif tree > grid[col][row - 1]:
                visable = True
            if visable:
                visabletrees += 1
                # print(f"VISABLE: Col:{col}, Row:{row}, Tree:{tree}")
            row += 1
        col += 1
print(visabletrees)
