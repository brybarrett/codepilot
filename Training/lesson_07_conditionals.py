
# 🧠 CodePilot Training - Lesson 07: Conditional Logic

print("🛡️ Initiating Security Check...\n")

security_clearance = "Level 2"
authorized = True
failed_attempts = 0

# Run security logic
if security_clearance == "level 3" and authorized:
    print("✅ Access Granted: Full System Override")
elif security_clearance == "level 2" and authorized:
    print("🟠 Access Granted: Limited Developer Mode")
elif failed_attempts > 3:
    print("🚨 Access Denied: Too Many Failed Attempts")
else:
    print("❌ Access Denied: Unauthorized")

# XP Logic Based on Access
xp = 0

if security_clearance == "Level 3":
    xp += 2000
elif security_clearance == "Level 2":
    xp += 1600
else:
    xp += 100

    # Bonus Logic
if authorized and failed_attempts == 0:
    xp += 300

print(f"\n📈 XP Gained: {xp}")
print("🔒 Security logic complete.")