import math

def sqroot(num):
	st, end = 0, num
	ans = 0
	while(st <= end):
		mid = (st+end)//2
		# print("mid =",mid)
		if mid*mid == num:
			return mid
		if mid*mid > num:
			end = mid-1
		else:
			ans = st
			st = mid+1
	incr = 0.1
	for i in range(5):
		while ans*ans <= num:
			ans += incr
		ans -= incr
		incr /= 10
	return ans


print("enter number to find its square root : ",end="")
num = float(input())
# print(f"sqroot({num}) = {sqroot(num)}")
print("\nsqroot(%d) = %.5f" % (num, sqroot(num)))