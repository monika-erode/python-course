# Example: format invoice line and parse CSV line

# Given variables
product = "Notebook"
qty = 3
price_per_unit = 49.99

# Formatting an invoice line (f-strings)
total = qty * price_per_unit
invoice_line = f"{product:<15} x {qty:>2} @ ₹{price_per_unit:,.2f} = ₹{total:,.2f}"
print(invoice_line)

# Parsing a CSV line (split and strip)
csv_line = "Asha, 99999 11111, asha@example.com\n"
name, phone, email = [part.strip() for part in csv_line.split(",")]
print("Name:", name, "Phone:", phone, "Email:", email)

# Common string operations
s = " Hello, World! "
print("strip:", s.strip())
print("lower:", s.lower())
print("replace:", s.replace("World", "Asha"))
print("contains 'Hello':", "Hello" in s)
