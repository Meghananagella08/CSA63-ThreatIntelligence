required_elements = {
    "Scope": ["scope", "applies to", "covers"],
    "Roles and Responsibilities": [
        "roles and responsibilities",
        "responsibilities"
    ],
    "Enforcement": ["enforcement", "disciplinary action"],
    "Review Cycle": [
        "review cycle", "reviewed annually",
        "review every year", "annual review"
    ],
    "Approval Authority": [
        "approved by", "approval authority",
        "authorized by"
    ]
}

print("Enter the security policy text.")
print("Type END on a new line when finished.")

lines = []

while True:
    line = input()
    if line.strip().upper() == "END":
        break
    lines.append(line)

policy = " ".join(lines).lower()

missing = []

for element, keywords in required_elements.items():
    if not any(keyword in policy for keyword in keywords):
        missing.append(element)

print("\n--- Security Policy Assessment ---")

if not missing:
    print("All required governance elements appear to be present.")
else:
    print("Missing governance elements:")
    for element in missing:
        print("-", element)