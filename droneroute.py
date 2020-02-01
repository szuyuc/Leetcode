count = 0


def routing(lanes):
    global count
    # print(lanes)
    # print(count)

    if len(lanes) == 0:
        return
    if len(lanes) == 1:
        if lanes[0] != 0:
            count += 1
            print
        return
    # check if zeros in array. If yes, split the array by zero
    if 0 in lanes:
        start = 0
        zero_ind = [ind for ind, val in enumerate(lanes) if val == 0]
        for val in zero_ind:
            if val != 0:
                routing(lanes[start:val])
            start = val+1
        if start < len(lanes):
            routing(lanes[start:])
    else:
        # if length of plants is bigger than len(lanes)
        min_lane = min(lanes)
        len_lane = len(lanes)

        """
        # optimize for non-duplicate numbers
        minimum = float('inf')
        dic = {}  # we want to know if there are duplicates
        flag = False
        for val in lanes:
            if val < minimum:
                minimum = val
            if val in dic.keys():
                flag = True
            else:
                dic[val] = 1

        if not flag:
            count += len_lane
            return
        # end of optimization
        """
        if min_lane >= len_lane:
            count += len_lane
            return
        else:
            count += min_lane
            for ind, val in enumerate(lanes):
                lanes[ind] -= min_lane
            routing(lanes)


def tranform_numbers(string):
    arr = string.split(' ')

    print(arr)
    return [int(num) for num in arr]


# test
#routing([1, 5, 4, 1, 2])
#routing([2, 2, 2, 3])
#routing([0, 4, 3, 0, 1])
#routing([1, 2, 3, 4, 5, 1, 3, 3, 3, 2, 2, 2, 3, 2, 2, 1, 3])
#routing(tranform_numbers("2 2 1 2"))
#routing(tranform_numbers("1 2 3 4 5"))
#routing(tranform_numbers("1 2 3 4 5 6 7 8 9 10"))
#routing(tranform_numbers("1 2 1 2"))
#routing(tranform_numbers("1 3 3 3"))
#routing(tranform_numbers("3 3 3 1000000000 3"))
#routing(tranform_numbers("3 3 3 2 3 3 3 2 3 3 3 2"))

print(count)
