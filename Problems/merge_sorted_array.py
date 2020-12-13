def merge_sorted_arr1(nums1, nums2):
  # check if there are 2 lists with items inside
  # p1 for nums1, p2 for nums2
  p1 = 0
  p2 = 0
  result = []
  # if 1 input list is empty
  if len(nums1) == 0:
    return nums2
  elif len(nums2) == 0:
    return nums1

  # when we haven't reached the end of a list
  while p1 < len(nums1) or p2 < len(nums2):
    # when we have reached the end of nums2 or we haven't reached the end of nums1 and ele in nums1 is less then ele in nums2
    if p2 == len(nums2) or (p1 < len(nums1) and nums1[p1] < nums2[p2]):
      result.append(nums1[p1])
      p1 += 1
    else:
      result.append(nums2[p2])
      p2 += 1

  return result


def merge_sorted_arr2(nums1, nums2):
  # check if there are 2 lists with items inside
  # p1 for nums1, p2 for nums2
  p1 = 0
  p2 = 0
  result = []
  # if 1 input list is empty
  if len(nums1) == 0:
    return nums2
  elif len(nums2) == 0:
    return nums1

  # when we haven't reached the end of a list
  while p1 < len(nums1) and p2 < len(nums2):
    if nums1[p1] < nums2[p2]:
      result.append(nums1[p1])
      p1 += 1
    else:
      result.append(nums2[p2])
      p2 += 1

  # add the remaining elements to result list
  return result + nums1[p1:] + nums2[p2:]


print(merge_sorted_arr2([0, 3, 4, 31], [4, 6, 30]))
print(merge_sorted_arr2([0, 3, 4, 31], [4]))
print(merge_sorted_arr2([0], [4]))
print(merge_sorted_arr2([0], []))
print(merge_sorted_arr2([], [4]))
print(merge_sorted_arr2([], []))

# Time: o(n + m) because we have to go through both input lists
# Space: o(n) because we are creating a list
# The 2nd solution is simplier