def binary_search(nums, target):
  l = 0
  r = len(nums) - 1

  while l <= r:
    mid = l + ((r - l) // 2)

    if nums[mid] == target:
      return mid

    if target < nums[mid]:
      r = mid - 1
    else:
      l = mid + 1
  return -1


arr1 = [1, 2, 18, 24, 28, 29]  # 2
arr2 = [1, 2, 5, 18, 24, 28, 29]  # 3
arr3 = [1, 2, 5, 13, 15, 16, 24, 28, 29]  # -1
arr4 = [18, 24, 28, 29]  # 0
arr5 = [1, 2, 5, 13, 15, 16, 18]  # 6
target = 18

print(binary_search(arr1, target))
print(binary_search(arr2, target))
print(binary_search(arr3, target))
print(binary_search(arr4, target))
print(binary_search(arr5, target))

# NOTES:
