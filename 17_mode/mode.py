def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    dict_nums = {}
    count, mode = 0, ''
    for item in nums:
        dict_nums[item] = dict_nums.get(item, 0) + 1
        if dict_nums[item] >= count:
            count, mode = dict_nums[item], item
    return mode