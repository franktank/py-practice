def lbs(nums):
    if len(nums) == 0:
        return 0

    dplr = [1 for _ in range(len(nums))]
    dprl = [1 for _ in range(len(nums))]

    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                dplr[i] = max(dplr[i], dplr[j] + 1)


    for i in range(len(nums) - 2, -1, -1):
        for j in range(len(nums) - 1, i, -1):
            if nums[i] > nums[j]:
                dprl[i] = max(dplr[i], dplr[j] + 1)

    max_len = -1
    for i in range(len(nums)):
        max_len = max(max_len, dplr[i] + dprl[i] - 1)

    return max_len
