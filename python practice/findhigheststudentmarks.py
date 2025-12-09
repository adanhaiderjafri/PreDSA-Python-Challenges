data = {"Ali": 88, "Ayesha": 91, "Omar": 95, "Shahid": 95}

max_value = max(data.values())  # 95
names = [k for k, v in data.items() if v == max_value]

print(f"Students who get maximum marks: {names}")

