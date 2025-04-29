def is_boomerang(points):
  """
  Determines if three points form a boomerang.

  Args:
    points: A list of three points, where each point is a list [x, y].

  Returns:
    True if the points form a boomerang, False otherwise.
  """
  if len(points) != 3:
    return False

  if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
    return False

  x1, y1 = points[0]
  x2, y2 = points[1]
  x3, y3 = points[2]

  # Check if the points are collinear using the determinant method
  area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
  return area != 0


def test_is_boomerang():
  """
  Tests the is_boomerang function with several test cases.
  """
  test_cases = [
    ([[1, 1], [2, 3], [3, 2]], True),
    ([[1, 1], [2, 2], [3, 3]], False),
    ([[0, 0], [1, 0], [2, 0]], False),
    ([[0, 0], [1, 1], [0, 1]], True),
    ([[1, 0], [0, 0], [2, 0]], False),
    ([[1, 1], [2, 2], [1, 1]], False)  # Duplicate point
  ]

  correct_count = 0
  total_count = len(test_cases)

  for i, (points, expected) in enumerate(test_cases):
    result = is_boomerang(points)
    if result == expected:
      print(f"Test {i+1}: True")
      correct_count += 1
    else:
      print(f"Test {i+1}: False")
      print(f"  Input: {points}")
      print(f"  Expected: {expected}")
      print(f"  Got: {result}")

  print(f"{correct_count}/{total_count}")


if __name__ == "__main__":
  test_is_boomerang()