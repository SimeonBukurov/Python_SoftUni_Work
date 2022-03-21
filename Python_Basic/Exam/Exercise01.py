quantity_paper = int(input())
quantity_fiber = int(input())
litres_glue = float(input())
percent = int(input())
price_paper = quantity_paper * 5.80
price_fiber = quantity_fiber * 7.20
price_glue = litres_glue * 1.20
total_without_discount = price_paper + price_fiber + price_glue
total_with_discount = total_without_discount -(total_without_discount * (percent / 100))
print(f"{total_with_discount:.3f}")