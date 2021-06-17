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

# ip = "23+45*+"
ip = "235+*6-"
print(f"\npostfix expression :\n{ip}")
print(f"\nresult = {postfix_eval(ip)}")