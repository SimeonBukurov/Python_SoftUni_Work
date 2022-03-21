days_staying = int(input())
type_of_app = input()
rating = input()
price = 0
total = 0
if days_staying < 10:
    if type_of_app == "room for one person":
        price = 18
        total = (days_staying - 1) * price
    elif type_of_app == "apartment":
        price = 25
        room_price = (days_staying - 1) * price
        total = room_price - (room_price * 0.30)
    elif type_of_app == "president apartment":
        price = 35
        room_price = (days_staying - 1) * price
        total = room_price - (room_price * 0.10)
elif 10 <= days_staying <= 15:
    if type_of_app == "room for one person":
        price = 18
        total = (days_staying - 1) * price
    elif type_of_app == "apartment":
        price = 25
        room_price = (days_staying - 1) * price
        total = room_price - (room_price * 0.35)
    elif type_of_app == "president apartment":
        price = 35
        room_price = (days_staying - 1) * price
        total = room_price - (room_price * 0.15)
elif days_staying > 15:
    if type_of_app == "room for one person":
        price = 18
        total = (days_staying - 1) * price
    elif type_of_app == "apartment":
        price = 25
        room_price = (days_staying - 1) * price
        total = room_price - (room_price * 0.5)
    elif type_of_app == "president apartment":
        price = 35
        room_price = (days_staying - 1) * price
        total = room_price - (room_price * 0.20)

if rating == "positive":
    total = total + (total * 0.25)
elif rating == "negative":
    total = total - (total * 0.10)

print(f"{total:.2f}")