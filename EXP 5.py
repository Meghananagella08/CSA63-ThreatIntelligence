def classify_report(description, audience):
    text = (description + " " + audience).lower()

    strategic_keywords = [
        "business risk", "executives", "board",
        "long-term trends", "financial impact",
        "senior management", "investment"
    ]

    tactical_keywords = [
        "attack techniques", "tactics",
        "techniques and procedures", "ttps",
        "detection rules", "defensive controls",
        "security engineers"
    ]

    operational_keywords = [
        "active campaign", "current attack",
        "threat actor", "planned operation",
        "incident response", "attack targets",
        "soc analysts"
    ]

    scores = {
        "Strategic": sum(k in text for k in strategic_keywords),
        "Tactical": sum(k in text for k in tactical_keywords),
        "Operational": sum(k in text for k in operational_keywords)
    }

    if max(scores.values()) == 0:
        return "Unclassified - More information required"

    return max(scores, key=scores.get)


description = input("Enter threat report description: ")
audience = input("Enter intended audience: ")

result = classify_report(description, audience)

print("Threat Intelligence Classification:", result)