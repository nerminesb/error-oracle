def calculate_travel_cost(distance, price):

    return distance / price

print("Starting Paris Trip...")
# CRASH: Division by zero!
print(calculate_travel_cost(100, 0))