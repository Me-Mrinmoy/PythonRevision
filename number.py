import phonenumbers
from phonenumbers import geocoder, carrier

# Replace this with the mobile number in international format
phone_number = phonenumbers.parse("+916290149780")  # +91 for India

# Get the location (registered region) of the mobile number
location = geocoder.description_for_number(phone_number, "en")
print(f"Registered Location: {location}")

# Get the carrier (telecom operator) of the mobile number
carrier_name = carrier.name_for_number(phone_number, "en")
print(f"Carrier: {carrier_name}")
