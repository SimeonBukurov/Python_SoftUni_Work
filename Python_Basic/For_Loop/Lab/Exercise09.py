n = int(input())
left_sum = 0
right_sum = 0
for first_numbers in range(1, n + 1):
    value = int(input())
    left_sum += value
for second_numbers in range(1, n + 1):
    value = int(input())
    right_sum += value


diff = abs(left_sum - right_sum)
sum = left_sum or right_sum
if left_sum == right_sum:
    print(f"Yes, sum = {sum}")
else:
    print(f"No, diff = {diff}")