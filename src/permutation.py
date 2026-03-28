# permutation
def findPermutation(array, beginInx):
    if beginInx == len(array)-1:
        print(f'ARRAY : {array}')
    else:
        for i in range(beginInx, len(array)):
            # fixed select character
            swap(array, beginInx, i)
            # select other childs
            findPermutation(array, beginInx+1)
            swap(array, beginInx, i)


# fixed selection
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


characters = ['A', 'B', 'C']
findPermutation(characters, 0)
