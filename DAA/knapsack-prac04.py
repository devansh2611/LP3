def knapsack(W,n,wt,val):
    dp=[0 for i in range(W+1)]

    print(dp)

    for i in range(1,n+1):
        for j in range(W,0,-1):
            if wt[i-1]<=j:
                dp[j]=max(dp[j],dp[j-wt[i-1]]+val[i-1])
            
    return dp[W]

wt=[3, 4, 6, 5]
val=[2, 3, 1, 4]
W = 8
n = len(val)
print(knapsack(W,n, wt, val))