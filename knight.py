from timeit import default_timer as timer
]
# 1 2 3
# 4 5 6
# 7 8 9
#   0
ADJACENCY = {
  0: (4, 6),
  1: (6, 8),
  2: (7, 9),
  3: (4, 8),
  4: (3, 9, 0),
  6: (1, 7, 0),
  7: (2, 6),
  8: (1, 3),
  9: (2, 4),
}

# initialize a blank 10x100 2d array.
memo = [None] * 10
for i in range(10):
    memo[i] = [0] * 100

def count_numbers_unchecked(starting_num, lenLimit):
  if lenLimit == 1:
    return 1

  # Check if (starting_num, lenLimit) has already been computed.
  # if it has, return it without computing again.
  if (memo[starting_num][lenLimit] > 0):
    return memo[starting_num][lenLimit]

  # If I have not, compute it.
  num_hops = 0
  for next_hop in ADJACENCY[starting_num]:
    num_hops += count_numbers_unchecked(next_hop, lenLimit - 1)

  # Save it after computing it so I don't have to do so again next time.
  memo[starting_num][lenLimit] = num_hops;
  return num_hops

def count_numbers(starting_num, lenLimit):
  if not 0 <= starting_num <= 9:
    raise ValueError('invalid starting_num')
  if lenLimit <= 0:
    raise ValueError('invalid length')

  return count_numbers_unchecked(starting_num, lenLimit)

starting_num = 1 # Where do I start?
lenLimit = 99 # What's my sequence limit?
print "Limit: {}. Count: {}.".format(lenLimit, count_numbers(starting_num, lenLimit))
