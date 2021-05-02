import sys
def partition3(num):
  s = sum(num)

  # check if s is divisible by 3.
  if s % 3 != 0:
    return 0

  # we are trying to find a subset of given numbers that has a total sum of 's/3'.
  s = int(s / 3)

  n = len(num)
  dp = [[False for x in range(s+1)] for y in range(n)]

  # populate the sum=0 column, as we can always have '0' sum without including
  # any element
  for i in range(0, n):
    dp[i][0] = True

  # with only one number, we can form a subset only when the required sum is
  # equal to its value
  for j in range(1, s+1):
    dp[0][j] = num[0] == j

  # process all subsets for all sums
  for i in range(1, n):
    for j in range(1, s+1):
      # if we can get the sum 'j' without the number at index 'i'
      if dp[i - 1][j]:
        dp[i][j] = dp[i - 1][j]
      elif j >= num[i]:  # else if we can find a subset to get the remaining sum
        dp[i][j] = dp[i - 1][j - num[i]]
  # the bottom-right corner will have our answer.
  if dp[n - 1][s]: return 1
  else: return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))