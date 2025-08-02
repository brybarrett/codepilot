# training/lesson_05_lists.py

print("🧠 CodePilot Dev Tools Tracker")
print("------------------------------")

# Create a list of your dev tools
dev_tools = ["Python", "Visual Studio Code", "Git", "Github", "ChatGPT"]

# Print each tool with its index
print("🔎 Current Loadout:")
for index, tool in enumerate(dev_tools):
    print(f"{index + 1}. {tool}")

# Add a new tool to the list
dev_tools.append("Flask")
print("\n⚡ Flask acquired! Updated Loadout:")

for index, tool in enumerate(dev_tools):
    print(f"{index + 1}. {tool}")

# Show total number of tools
print(f"\n🧰 Total Tools in Loadout: {len(dev_tools)}")