
def isPalRec(st, s, e) : 	
	if (s == e): 
		return True

	if (st[s] != st[e]) : 
		return False

	
	if (s < e + 1) : 
		return isPalRec(st, s + 1, e - 1); 

	return True

def isPalindrome(st) : 
	n = len(st) 
	
	if (n == 0) : 
		return True
	
	return isPalRec(st, 0, n - 1); 


def dynamic_recuurence2(liste,st,start,count):
	
	if(count>len(st)):
		return liste
	if(start+count<=len(st)):
		print(st[start:start+count])
		if(isPalindrome(st[start:start+count])):
			liste.append(st[start:start+count])
	else:
		start=-1
		count=count+1
	dynamic_recuurence2(liste,st,start+1,count)	
			


st="dcacd"
liste = []
dynamic_recuurence2(liste,st,0,2)
print(str(liste) + " are palindrome")
print(str(liste[-1]) + " is max polindrome")