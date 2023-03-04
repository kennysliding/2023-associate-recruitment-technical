# read input
n = int(input())
sizes = input().split() 
# xxs = -1, xs = 0, s = 1, m = 2, l = 3, xl = 4, xxl = 5, and so on
m = int(input())
requests = input().split()

# define the size order, transform the sizes to int
def size_to_int(size):
    if size == 'S':
        return 1
    elif size == 'M':
        return 2
    elif size == 'L':
        return 3
    # count the number of x in this string
    x_count = size.count('X')
    if "S" in size:
        return 1 - x_count
    if "L" in size:
        return 3 + x_count

sizes = [size_to_int(size) for size in sizes].sort()
requests = [size_to_int(request) for request in requests].sort()

# check if all requests can be fulfilled
fulfilled = True
for request in requests:
    if sizes[0] >= request:
        sizes.pop(0)
    else:
        fulfilled = False
        break
    
if fulfilled:
    print('Yes')
else:
    print('No')