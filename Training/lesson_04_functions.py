def welcome_commander (name):
    print(f"🛸 Welcome aboard, Commander {name}!")

def calculate_power(base, multiplier):
    power = base * multiplier 
    return power

def main():
    name = "Bryan"
    base_power = 3000
    multiplier = 3.2

    welcome_commander(name)
    final_power = calculate_power(base_power, multiplier)

    print(f"💥 Final Power Level: {final_power}")

    if final_power > 9000:
        print ("f🔥 It's over 9000!!! True coder unlocked.")

    else:
        print ("🧩 Training in Progress...")

main ()