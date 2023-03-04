# read input
n = int(input())
records = []
for i in range(n):
    records.append(input().split())

all_valid = True
error_codes = []

for record in records:
    if record[1] == 'false':
        all_valid = False
        error_codes.append(record[2])

if all_valid:
    print('Yes')
else:
    print('No')
    print(' '.join(error_codes))