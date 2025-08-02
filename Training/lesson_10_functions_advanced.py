# 🔁 Bonus Lesson: Functions II - Advanced Ops

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "error: Divede by zero"
    return x / y

# ⚙️ Function Composition
def calculate_total_price(price, quantity, tax_rate=0.08):
    subtotal = multiply(price, quantity)
    tax = multiply(subtotal, tax_rate)
    total = add(subtotal, tax)
    return total
# 🧪 Reusable Testing Function
def test_functions():
    print("Add: ", add(10, 5))
    print("Subtract: ", subtract(10, 5))
    print("Multiply: ", multiply(10, 5))
    print("Divide: ", divide(10, 5))
    print("Total Price: ", calculate_total_price(20, 3))

# 🚀 Execute Tests
if __name__ == "__main__":
    test_functions()