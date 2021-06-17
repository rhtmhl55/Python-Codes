import sys

def l_child(ind):
	return ind*2+1

def r_child(ind):
	return ind*2+2

def parent(ind):
	return (ind-1)//2

def max_heapify(ind, n, lst):
	l_ind = l_child(ind)
	r_ind = r_child(ind)
	lrgst_ind = ind
	if l_ind<n and lst[l_ind]>lst[lrgst_ind]:
		lrgst_ind = l_ind
	if r_ind<n and lst[r_ind]>lst[lrgst_ind]:
		lrgst_ind = r_ind
	if lrgst_ind != ind:
		lst[ind], lst[lrgst_ind] = lst[lrgst_ind], lst[ind]
		max_heapify(lrgst_ind, n, lst)

def build_max_heap(n, lst):
	for i in reversed(range(n//2)):
		max_heapify(i, n, lst)

def extract_max(n, lst):
	lst[0], lst[n-1] = lst[n-1], lst[0]
	max_heapify(0, n-1, lst)
	return lst[n-1]

# def heap_sort(n, lst):
# 	build_max_heap(n, lst)
# 	for i in reversed(range(1, n)):
# 		lst[0], lst[i] = lst[i], lst[0]
# 		max_heapify(0, i, lst)

def heap_sort(n, lst):
	build_max_heap(n, lst)
	for i in reversed(range(2, n+1)):
		extract_max(i, lst)

def increase_key(ind, key, n, lst):
	lst[ind] = key
	while ind != 0 and lst[parent(ind)] < key:
		lst[ind], lst[parent(ind)] = lst[parent(ind)], lst[ind] 
		ind = parent(ind)

def delete_key(ind, n, lst):
	if n==1:
		return []
	max_int = sys.maxsize
	increase_key(ind, max_int, n, lst)
	extract_max(n, lst)
	return lst[:-1]


ip_str = "4251739"
lst = [int(i) for i in ip_str]
n = len(lst)
print(f"original list :\n{lst}")

# heap_sort(n, lst)
# print(f"list after heapsort :\n{lst}")

build_max_heap(n, lst)
print(f"list after build_max_heap :\n{lst}")

# increase_key(n-1, 10, n, lst)
# print(f"list after increase_key(n-1, 10, n, lst) :")
# print(lst)

lst = delete_key(2, n, lst)
print(f"list after delete_key(2, n, lst) :")
print(lst)