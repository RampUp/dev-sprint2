# Practice - Chapter 7

# def countdown(n):
#     if n <= 0:
#         print 'Blastoff!'
#     else:
#         print n
#         countdown(n-1)

# def countdown(n):
#     while n > 0:
# 		print n
#         n = n-1
#     print 'Blastoff!'

# def print_n(s, n):
#     if n <= 0:
#         return
# 	print s
# 	print_n(s, n-1)

def print_n(s,n):
	while n > 0:
		print s
		n = n-1

print_n('Sidd is awesome!',3)