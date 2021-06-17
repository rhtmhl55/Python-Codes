def infix_to_postfix(ip):
	d = {'+' : 1, '-' : 1, '/' : 2, '*' : 2, '^' : 3}
	st = []
	post = ""
	for ch in ip:
		if ch.isdigit():
		# if ch.isalpha():
			post += ch
		else: 
			if len(st)==0 or ch=="(" or st[len(st)-1]=="(":
				st.append(ch)
			elif ch==")":
				while(len(st)!=0 and st[len(st)-1] != "("):
					post += st.pop()
				st.pop()
			elif d[ch] > d[st[len(st)-1]]:
				st.append(ch)
			else:
				while(len(st)!=0 and st[len(st)-1]!='(' and d[st[len(st)-1]] >= d[ch]):
					post += st.pop()
				st.append(ch)
	while(len(st) != 0):
		post += st.pop()
	return post

def postfix_eval(ip):
	st = []
	for ch in ip:
		if ch.isdigit():
			st.append(int(ch))
		else:
			op2 = st.pop()
			op1 = st.pop()
			if ch == "+":
				st.append(op1+op2)
			if ch == "-":
				st.append(op1-op2)
			if ch == "*":
				st.append(op1*op2)
			if ch == "/":
				st.append(op1/op2)
			if ch == "^":
				st.append(pow(op1,op2))
	return st.pop()

infix = "2*(3+5)-6"
# infix = "a+b*(c^d-e)^(f+g*h)-i"
print(f"\ninfix expression : \n{infix}")

postfix = infix_to_postfix(infix)
print(f"\npostfix expression : \n{postfix}")

res = postfix_eval(postfix)
print(f"\nresult = {res}")