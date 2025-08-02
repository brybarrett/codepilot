# Lesson_03_loops.py

name = "Bryan"
daily_xp = [120,150,180,200,250]
total_xp = 0

print("Welcome back, Commander", name + ".")

print("\n📅 Weekly XP Log:")
for day, xp in enumerate(daily_xp, start=1):
    print(f"Day {day}: +{xp} XP")
    total_xp += xp

print("\n🔭🔁 Calculating total XP...")
print("🏆 Total XP Earned:", total_xp)

# Bonus milestone
if total_xp >1000:
    print("🎉Rank Up Unlocked!")
else:
    print("Keep Grinding...")