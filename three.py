def max_val(nums):
    ans = 0

    # 遍历一个数字作为中位数的情况
    for i in range(len(nums)):
        mid_num = nums[i]

        # 尝试找到最远边界距离
        dist = min(i, len(nums) - i - 1)
        print(f"i: {i}, dist: {dist}")
        # 尝试遍历边界从 0 到 最远的情况
        for j in range(dist + 1):
            if j == 0:
                continue
            average_num = (sum(nums[(i - j): i + 1]) + sum(nums[(len(nums) - j):len(nums)])) / (2 * j + 1)
            print(f"i: {i}, j: {j}")
            print(f"sum1: {sum(nums[(i - j): i + 1])}, sum2: {sum(nums[(len(nums) - j):len(nums)])}")
            print(f"dict one: {i - j} {len(nums) - j}, average: {average_num}, mid num: {mid_num}")
            ans = max(ans, average_num - mid_num)
            print(f"ans: {ans}")

    print("two----------------------------------------------")
    # 遍历两个数字作为中位数的情况
    for i in range(len(nums) - 1):
        mid_num = (nums[i] + nums[i + 1]) / 2

        # 尝试找到最远边界距离
        dist = min(i, len(nums) - (i + 1) - 1)
        print(f"i: {i}, dist: {dist}")
        # 尝试遍历边界从 0 到 最远的情况
        for j in range(dist + 1):
            if j == 0:
                continue
            average_num = (sum(nums[(i - j): i + 2]) + sum(nums[(len(nums) - j):len(nums)])) / (2 * j + 2)
            print(f"i: {i}, j: {j}")
            print(f"sum1: {sum(nums[(i - j): i + 2])}, sum2: {sum(nums[(len(nums) - j):len(nums)])}")
            ans = max(ans, average_num - mid_num)
            print(f"dict one: {i - j} {len(nums) - j}, average: {average_num}, mid num: {mid_num}")
            print(f"ans: {ans}")

    return ans


print(max_val([1, 3, 5, 7, 9]))
