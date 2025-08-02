# tools/xp_tracker.py

import json
import os

XP_FILE = "xp_data.json"
XP_PER_FEATURE = {
    "regex": 5,
    "api": 5,
    "bug": 5
}

def load_xp():
    if not os.path.exists(XP_FILE):
        return 0
    try:
        with open(XP_FILE, 'r') as f:
            return json.load(f).get("xp", 0)
    except:
        return 0

def add_xp(feature):
    xp = load_xp()
    xp += XP_PER_FEATURE.get(feature, 1)
    with open(XP_FILE, 'w') as f:
        json.dump({"xp": xp}, f)
    return xp

def get_xp_percentage():
    current_xp = load_xp()
    return min(int((current_xp / 100) * 100), 100)  # Cap at 100%
