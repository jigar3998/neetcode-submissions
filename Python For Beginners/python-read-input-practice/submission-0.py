def add_two_numbers() -> int:
    nums = input().split(",")
    int_nums = []
    for num in nums:
        int_nums.append(int(num))
    return sum(int_nums)



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
