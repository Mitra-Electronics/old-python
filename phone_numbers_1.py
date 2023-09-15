from phonenumbers import geocoder, parse, carrier, timezone
# geocoder: to know the specific
# location to that phone number



phone_number = parse("+91 62909 88546")
# Indian phone number example: +91**********
# Nepali phone number example: +977**********


# this will print the country name
print(geocoder.description_for_number(phone_number, 'en'))
print(carrier.name_for_number(phone_number, 'en'))
print(timezone.time_zones_for_number(phone_number))
