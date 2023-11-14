def shuffle( nums, n):
    result = []
    array_x = nums[:n]
    array_y = nums[n:]

    for i in range(len(array_x)):
        result.append(array_x[i])
        result.append(array_y[i])
    return result
    


print(shuffle([1,1,2,2],2))