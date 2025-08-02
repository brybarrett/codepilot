
# 🌀 Lesson 08 - Loops: XP Generator Engine

print ("🔁 Initializing XP Generator...\n")

xp_log = []
xp_total = 0

# Loop through 5 coding sessions
for session in range (1, 6):
    print(f"📚 Session {session}: Coding...")
    gained = session * 300
    xp_total += gained
    xp_log.append(f"✅ Session {session} complete: +{gained} XP")

print('\n🔁 Reviewing XP Log:')
for log in xp_log:
    print(log)

print(f"\n💾 Total XP Gained: {xp_total}")

# Optional while loop
print("⏳ Training continues...")
xp_total += 200
print(f"➕ XP Boost: +200 → Total XP: {xp_total}")

print(f"\n🏆 Level Up Achieved! New XP: {xp_total}")