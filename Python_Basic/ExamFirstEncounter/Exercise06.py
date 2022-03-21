first_num = input()
counter = 0
flag = False
for k in range(int(first_num), 9):
    if k % 2 == 0:
        second_num = input()
        for l in range(10, int(second_num)):
            if l % 2 != 0:
                third_num = input()
                for m in range(int(third_num), 9):
                    if m % 2 == 0:
                        forth_num = input()
                        for n in range(10, int(forth_num)):
                            if n % 2 != 0:
                                first_couple = k * 10 + l
                                second_couple = m * 10 + n
                                if first_couple == second_couple:
                                    flag = True
                                    print("Cannot change the same player.")
                                else:
                                    print(f"{k}{l} - {m}{n}")
                                    counter += 1
                                if counter < 6:
                                    flag = True
                                    break
                                break
