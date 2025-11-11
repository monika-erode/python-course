# Example: apply discount and list cart items

cart_items = ["notebook", "pen", "water bottle"]
total_price = 12000  

# If/elif/else to decide discount
if total_price >= 2000:
    discount = 0.50  # 50%
elif total_price >= 1000:
    discount = 0.10  # 10%
else:
    discount = 0.0   # 0%

final_price = total_price * (1 - discount)
print(f"Final price: ₹{final_price:.2f}")

# For loop to print items with index
for index, item in enumerate(cart_items, start=1):
    print(f"{index}. {item}")

# While loop example: countdown timer (simple)
count = 10
while count > 0:
    print("Processing in", count)
    count -= 1
print("Done.")
