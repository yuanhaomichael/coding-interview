# POJ 1852

# the key is that when 2 ants meet and turn in the reverse direction
# it's equivalent to them pass through one another. So essentially each ant
# can be seen as on its own just going either to the left or the right
# until falling off.


def solution(length, ants: list[int]):
  least = 0
  most = 0

  for i in range(len(ants)):
    least = min(least, min(ants[i], length - ants[i]))
    most = max(most, max(ants[i], length - ants[i]))

  return [least, most]