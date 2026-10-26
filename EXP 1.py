def identify_application(scenario):
    scenario = scenario.lower()

    if any(word in scenario for word in
           ["bank", "payment", "transaction", "fraud"]):
        return "Banking Fraud Prevention"

    elif any(word in scenario for word in
             ["hospital", "patient", "medical", "healthcare"]):
        return "Healthcare Data Protection"

    elif any(word in scenario for word in
             ["online store", "e-commerce", "retail", "shopping"]):
        return "E-commerce Fraud Prevention"

    elif any(word in scenario for word in
             ["cloud", "server", "network", "intrusion"]):
        return "Network and Cloud Security"

    else:
        return "General Cyber Threat Intelligence"


scenario = input("Enter a business scenario: ")
result = identify_application(scenario)

print("Threat Intelligence Application:", result)