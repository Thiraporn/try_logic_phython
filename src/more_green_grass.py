# more_green_grass
class MoreGreenGrass:
    @staticmethod
    def more_green_grass(gardens):
        arrSize = len(gardens)
        max_left = [0] * arrSize
        max_righ = [0] * arrSize
        result = [0] * arrSize
        # compare(oneway) when move from left
        max_left[0] = gardens[0]
        for i in range(1, arrSize):
            max_left[i] = max(max_left[i-1], gardens[i])
        print(f'max_left >> {max_left}')

        # compare(oneway) when move from right
        max_righ[arrSize - 1] = gardens[arrSize - 1]
        for i in range(arrSize-2, -1, -1):
            max_righ[i] = max(max_righ[i+1], gardens[i])
        print(f'max_righ >> {max_righ}')

        # compare(2-ways)
        # main concept : left|self<index>|right    ---> self = index ===>  left neighborhood  -1 and right neighborhood +1
        for i in range(0, arrSize):
            if i == 0:  # start first neighborhood---> no garden/neighborhood on left---> defualt
                result[i] = max_righ[i+1]
            elif i == arrSize-1:  # end of town ---> no garden/neighborhood on right---> defualt
                result[i] = max_left[i-1]
            else:
                result[i] = max(max_left[i-1], max_righ[i+1])
        return result


mgg = MoreGreenGrass()
array = [2, 5, 1, 6, 7, 4, 5]
print(f'MoreGreenGrass >> {mgg.more_green_grass(array)}')
