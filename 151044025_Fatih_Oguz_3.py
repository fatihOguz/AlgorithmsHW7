def knapSack(W, wt, val, n,flag): 

	if n == 0 or W == 0: 
		return 0

	
	if (wt[n-1] > W): 
		return knapSack(W, wt, val, n-1,flag)  
	else: 	
		print("wt  " + str(wt[n-1] )+ " flag " + str(flag))
		if(wt[n-1]-flag>4):
			flag=wt[n-1]
			return max( 
				val[n-1] + knapSack( 
					W-wt[n-1], wt, val, n-1,flag), 
				knapSack(W, wt, val, n-1,flag)) 
		else:
			return knapSack(W, wt, val, n-1,flag) 






val = [2,5,100,12,120,62] 
wt = [32, 11, 10,6,5,1] 
W = 99999999999
n = len(val) 
flag=0
print (knapSack(W, wt, val, n,flag) )
