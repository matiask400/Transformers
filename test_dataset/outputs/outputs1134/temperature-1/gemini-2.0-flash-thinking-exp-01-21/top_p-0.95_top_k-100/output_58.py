def is_valid_start_value(startValue, nums):
  current_sum = startValue
  for num in nums:
    current_sum += num
    if current_sum < 1:
      return False
  return True

def min_start_value(nums):
  startValue = 1
  while True:
    if is_valid_start_value(startValue, nums):
      return startValue
    startValue += 1

def test_min_start_value():
  test_cases = [
    ([-3, 2, -3, 4, 2], 5),
    ([1, 2], 1),
    ([1, -2, -3], 5)
  ]
  correct_count = 0
  for nums, expected_output in test_cases:
    output = min_start_value(nums)
    if output == expected_output:
      print('True')
      correct_count += 1
    else:
      print('False')
  print(f'{correct_count}/{len(test_cases)}')

if __name__ == '__main__':
  test_min_start_value()