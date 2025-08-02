# Lesson_09_functions.py

print("\n🔧 Initializing Function Training...\n")

# Initialize XP and skills
total_xp = 0
skills_trained = []

# Define a reusable function
def train_skill(skill,xp):
    global total_xp
    print(f"🚀 Training Skill: {skill}...(+{xp} XP)")
    total_xp += xp
    skills_trained.append(skill)

# Train on multiple skills
train_skill("Python", 500)
train_skill("Git", 300)
train_skill("Flask", 400)

# Display final stats
print("\n🧠 Total XP Gained:",total_xp)
print("🧰 Skills trained:", ",".join(skills_trained))