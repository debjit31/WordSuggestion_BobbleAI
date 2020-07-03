import sys
def longestCSub(a,b):
	m,n = len(a), len(b)
	dp = [[None for j in range(n+1)]for i in range(m+1)]
	for i in range(m+1):
		for j in range(n+1):
			if i == 0 or j == 0:
				dp[i][j]=0
			elif a[i-1] == b[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]
			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
	return dp[m][n]

with open(sys.argv[1], 'r') as f:
	contents = f.read()
data = contents.split('\n')

word = sys.argv[-1].capitalize()
d = {}
for i in data:
	k,v = i.split(', ')
	d[k] = int(v)
all_suggestions = []
for i in list(d.keys()):
	lc = longestCSub(i, word)
	if lc >= 1:
		all_suggestions.append(i)
print(*all_suggestions)

