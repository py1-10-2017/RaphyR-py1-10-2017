# firstRow = '*'
# secondRow = []
# while len(firstRow) < 56:
#     # first line
#     if len(firstRow) == 7:
#         firstRow = firstRow + '\n' + '-'
#     if len(firstRow) == 16:
#         firstRow = firstRow + '\n' + '*'
#     elif len(firstRow) % 8 == 0 and firstRow[-1] == '*':
#         firstRow = firstRow + '\n'
#
#
#     # elif len(firstRow) % 16 == 0 and firstRow[-1] == ' ':
#     #     firstRow = firstRow + '\n' + ' '
#
#     if firstRow[-1] == '*':
#         firstRow += '-'
#     else:
#         firstRow += '*'
#
# print firstRow

def checkerboard():
    for i in range(0, 8):
        if i%2 == 0:
            print "* " * 4
        else:
            print " *" * 4

checkerboard()
