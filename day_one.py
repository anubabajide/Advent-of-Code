from common import get_input

def find_increasing_count(nums):
    count = 0
    for i in range(1, len(nums)):
        if int(nums[i]) > int(nums[i-1]):
            count += 1
    return count

def get_sliding_window(nums):
    rolling_sum = [0]
    for val in nums:
        rolling_sum.append(val+rolling_sum[-1])
    sum_array = []
    for i in range(3, len(rolling_sum)):
        sum_array.append(rolling_sum[i]-rolling_sum[i-3])
    return find_increasing_count(sum_array)

if __name__ == "__main__":
    numbers = get_input("day_one.txt")
    print(f"First Answer: {find_increasing_count(numbers)}")
    print(f"Second Answer: {get_sliding_window(numbers)}")