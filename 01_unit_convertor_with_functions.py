pounds_to_kilograms = 0.453592

def calculate_conversion(user_weight_in_pounds):
    user_in_kilos = user_weight_in_pounds * pounds_to_kilograms
    return user_in_kilos

def print_results():
    print("Your weight in kilograms is", calculate_conversion(165))

print_results()