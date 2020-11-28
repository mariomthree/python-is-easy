
def containList(firstList, secondList):
    counter = 0
    for itemOfFirstList in firstList:
        for itemOfSecondList in secondList:
            if itemOfFirstList == itemOfSecondList:
                counter += 1
    return True if counter == len(secondList) else False

# firstList = [
#     [2, 3, 1],
#     [4,5],
#     [6,8]
# ]
# secondList = [
#     [4, 5],
#     [6,8]
# ]

firstList = [
    ['a', 'b'],
    ['e'],
    ['c', 'd']
]
secondList = [
    ['g']
]

print(f"Output: {containList(firstList, secondList)}")
