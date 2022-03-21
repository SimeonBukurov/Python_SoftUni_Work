amount_of_sweater = 0
amount_of_toys = 0
number_of_adults = 0
number_of_kids = 0
price_for_toy = 0
price_for_sweater = 0
while True:
    age = input()
    if age == "Christmas":
        print(f"Number of adults: {number_of_adults}")
        print(f"Number of kids: {number_of_kids}")
        print(f"Money for toys: {price_for_toy}")
        print(f"Money for sweaters: {price_for_sweater}")
        break
    age_of_family_member = int(age)

    if age_of_family_member > 16:
        number_of_adults += 1
        price_for_sweater += 15
        amount_of_sweater += 1
    elif age_of_family_member <= 16:
        number_of_kids += 1
        price_for_toy += 5
        amount_of_toys += 1




