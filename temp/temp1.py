def create_staircase(nums):  # Wrong option
    while len(nums) != 0:
        step = 1
        subsets = []
        if len(nums) >= step:
            subsets.append(nums[0:step])
            nums = nums[step:]
            step += 1
        else:
            return False

    return


def create_staircase1(nums):
    step = 1
    subsets = []
    while len(nums) != 0:
        if len(nums) >= step:
            subsets.append(nums[0:step])
            nums = nums[step:]
            step += 1
        else:
            return False

    return subsets


def main():
    nums = [1, 2, 3, 4, 5, 6]
    print(create_staircase1(nums))


if __name__ == "__main__":
    main()