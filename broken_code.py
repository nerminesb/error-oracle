def calculate_travel_cost(distance, price):
    # This will crash if price is 0
    return distance / price

print("Starting Paris Trip...")
# CRASH: Division by zero!
print(calculate_travel_cost(100, 0))