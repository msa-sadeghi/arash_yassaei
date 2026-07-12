import json

tasks = [
    {"text": "خرید پیاز", "done": False, "priority": "معمولی"},
    {"text": "مطالعه جاوااسکریپت", "done": True, "priority": "بالا"},
]
try:
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)
    with open("tasks.json", "r", encoding="utf-8") as f:
        tasks = json.load(f)
        print(tasks[0]["text"])
except:
    print("error")
