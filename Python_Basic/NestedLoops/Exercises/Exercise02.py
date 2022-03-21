start_number = int(input())
end_number = int(input())

for n in range(start_number, end_number + 1):
    num_to_str = str(n)
    even_sum = 0
    odd_sum = 0
    for index, digit in enumerate(num_to_str):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if even_sum == odd_sum:
        print(n, end=' ')
