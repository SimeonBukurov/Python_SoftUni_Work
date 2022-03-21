price_for_one_page = float(input())
price_for_one_cover = float(input())
percent_discount_for_paper = int(input())
price_to_pay_to_designer = float(input())
percent_discount_for_the_sum = int(input())
pages = 899
cover = 2
first_sum = price_for_one_page * pages + price_for_one_cover * cover
first_sum = first_sum - (first_sum * (percent_discount_for_paper / 100))
sum_with_designer = first_sum + price_to_pay_to_designer
discounted_price = sum_with_designer - (sum_with_designer * (percent_discount_for_the_sum / 100))

print(f"Avtonom should pay {discounted_price:.2f} BGN.")
