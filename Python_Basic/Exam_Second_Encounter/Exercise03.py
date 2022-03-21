team = input()
type_of_souvenir = input()
amount_of_bought_souvenirs = int(input())
price_of_the_souvenir = 0
sum_for_souvenir = 0
if team == "Argentina":
    if type_of_souvenir == "flags":
        price_of_the_souvenir = 3.25
        sum_for_souvenir = price_of_the_souvenir * amount_of_bought_souvenirs
        print(f"Pepi bought {amount_of_bought_souvenirs} {type_of_souvenir} of {team} for {sum_for_souvenir:.2f} lv.")

    elif type_of_souvenir == "caps":
        price_of_the_souvenir = 7.20
        sum_for_souvenir = price_of_the_souvenir * amount_of_bought_souvenirs
        print(f"Pepi bought {amount_of_bought_souvenirs} {type_of_souvenir} of {team} for {sum_for_souvenir:.2f} lv.")

    elif type_of_souvenir == "posters":
        price_of_the_souvenir = 5.10
        sum_for_souvenir = price_of_the_souvenir * amount_of_bought_souvenirs
        print(f"Pepi bought {amount_of_bought_souvenirs} {type_of_souvenir} of {team} for {sum_for_souvenir:.2f} lv.")

    elif type_of_souvenir == "stickers":
        price_of_the_souvenir = 1.25
        sum_for_souvenir = price_of_the_souvenir * amount_of_bought_souvenirs
        print(f"Pepi bought {amount_of_bought_souvenirs} {type_of_souvenir} of {team} for {sum_for_souvenir:.2f} lv.")
    else:
        print("Invalid stock!")



elif team == "Brazil":
    if type_of_souvenir == "flags":
        price_of_the_souvenir = 4.20
        sum_for_souvenir = price_of_the_souvenir * amount_of_bought_souvenirs
        print(f"Pepi bought {amount_of_bought_souvenirs} {type_of_souvenir} of {team} for {sum_for_souvenir:.2f} lv.")

    elif type_of_souvenir == "caps":
        price_of_the_souvenir = 8.50
        sum_for_souvenir = price_of_the_souvenir * amount_of_bought_souvenirs
        print(f"Pepi bought {amount_of_bought_souvenirs} {type_of_souvenir} of {team} for {sum_for_souvenir:.2f} lv.")

    elif type_of_souvenir == "posters":
        price_of_the_souvenir = 5.35
        sum_for_souvenir = price_of_the_souvenir * amount_of_bought_souvenirs
        print(f"Pepi bought {amount_of_bought_souvenirs} {type_of_souvenir} of {team} for {sum_for_souvenir:.2f} lv.")

    elif type_of_souvenir == "stickers":
        price_of_the_souvenir = 1.20
        sum_for_souvenir = price_of_the_souvenir * amount_of_bought_souvenirs
        print(f"Pepi bought {amount_of_bought_souvenirs} {type_of_souvenir} of {team} for {sum_for_souvenir:.2f} lv.")
    else:
        print("Invalid stock!")


elif team == "Croatia":
    if type_of_souvenir == "flags":
        price_of_the_souvenir = 2.75
        sum_for_souvenir = price_of_the_souvenir * amount_of_bought_souvenirs
        print(f"Pepi bought {amount_of_bought_souvenirs} {type_of_souvenir} of {team} for {sum_for_souvenir:.2f} lv.")

    elif type_of_souvenir == "caps":
        price_of_the_souvenir = 6.90
        sum_for_souvenir = price_of_the_souvenir * amount_of_bought_souvenirs
        print(f"Pepi bought {amount_of_bought_souvenirs} {type_of_souvenir} of {team} for {sum_for_souvenir:.2f} lv.")

    elif type_of_souvenir == "posters":
        price_of_the_souvenir = 4.95
        sum_for_souvenir = price_of_the_souvenir * amount_of_bought_souvenirs
        print(f"Pepi bought {amount_of_bought_souvenirs} {type_of_souvenir} of {team} for {sum_for_souvenir:.2f} lv.")

    elif type_of_souvenir == "stickers":
        price_of_the_souvenir = 1.10
        sum_for_souvenir = price_of_the_souvenir * amount_of_bought_souvenirs
        print(f"Pepi bought {amount_of_bought_souvenirs} {type_of_souvenir} of {team} for {sum_for_souvenir:.2f} lv.")
    else:
        print("Invalid stock!")



elif team == "Denmark":
    if type_of_souvenir == "flags":
        price_of_the_souvenir = 3.10
        sum_for_souvenir = price_of_the_souvenir * amount_of_bought_souvenirs
        print(f"Pepi bought {amount_of_bought_souvenirs} {type_of_souvenir} of {team} for {sum_for_souvenir:.2f} lv.")

    elif type_of_souvenir == "caps":
        price_of_the_souvenir = 6.50
        sum_for_souvenir = price_of_the_souvenir * amount_of_bought_souvenirs
        print(f"Pepi bought {amount_of_bought_souvenirs} {type_of_souvenir} of {team} for {sum_for_souvenir:.2f} lv.")

    elif type_of_souvenir == "posters":
        price_of_the_souvenir = 4.80
        sum_for_souvenir = price_of_the_souvenir * amount_of_bought_souvenirs
        print(f"Pepi bought {amount_of_bought_souvenirs} {type_of_souvenir} of {team} for {sum_for_souvenir:.2f} lv.")

    elif type_of_souvenir == "stickers":
        price_of_the_souvenir = 0.90
        sum_for_souvenir = price_of_the_souvenir * amount_of_bought_souvenirs
        print(f"Pepi bought {amount_of_bought_souvenirs} {type_of_souvenir} of {team} for {sum_for_souvenir:.2f} lv.")
    else:
        print("Invalid stock!")
else:
    print("Invalid country!")




