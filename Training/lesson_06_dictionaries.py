# 📙CodePilot - Lesson 06: Dictionaries
print("📘 Initializing Developer Profile...\n")

# Define your profile using a dictionary
dev_profile = {
    "name": "Bryan",
    "level": 6,
    "skills": ["Python", "Git", "HTML", "CSS"],
    "active": True,
    "xp": 1250
    }

# Display key info
print(f"🧔🏻 Name: {dev_profile['name']}")
print(f"🏆 Level: {dev_profile['level']}")
print(f"🔨 Skills: {', '.join(dev_profile['skills'])}")
print(f"✅ Active: {dev_profile['active']}")
print(f"✨ XP: {dev_profile['xp']}")

# Simulate Leveling up
print("\n⚙️ Leveling up...\n")
dev_profile["level"] += 1
dev_profile["xp"] += 300
dev_profile["skills"].append ("Flask")

# Reprint updated profile
print(f"🔁 Updated Level: {dev_profile['level']}")
print(f"⚡ XP Gained: {dev_profile['xp']}")
print(f"🧩 New Skills: {', '.join(dev_profile['skills'])}")
