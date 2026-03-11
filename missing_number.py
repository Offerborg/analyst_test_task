def missing_number(nums: list) -> int:
    n = len(nums) + 1
    # Сумма от 1 до n
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Пример
nums = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11]
print(missing_number(nums))  # 7