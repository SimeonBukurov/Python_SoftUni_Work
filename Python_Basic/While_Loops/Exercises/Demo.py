import geocoder
import phonenumbers
from phonenumbers import timezone, carrier

geocoder, timezone, carrier
number = '+359892759826'
ch_number = phonenumbers.parse(number)
time_zone = timezone.time_zones_for_number(ch_number)
print(time_zone)

ch_number = phonenumbers.parse(number)
print(geocoder.description_for_number(ch_number, 'en'))

ch_number = phonenumbers.parse(number, 'RO')
print(carrier.mame_for_number(ch_number, 'en'))
