phone_numbers = ['919999999999','919999999999','+919999999999','+919999999999']

cleaned_numbers = [number.replace('+', '') for number in phone_numbers]

print(cleaned_numbers)
