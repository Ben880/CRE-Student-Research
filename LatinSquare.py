
def LatinSquareGenerator(size, index):
    mod = index % size  # gets column and remainder
    row = (index - mod)/size  # gets row
    rowmod = row % size  # gets row within repeating pattern
    num = mod-rowmod  # index of our number
    if num < 0:  # if index is negative loop around from top
        num += size
    return int(num)

