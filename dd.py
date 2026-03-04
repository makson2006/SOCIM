import datetime


def validate_score(prompt):
    """Ensures input is an integer between 1 and 5"""
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 5:
                return value
            print("Invalid input. Please enter a score between 1 and 5.")
        except ValueError:
            print("Error: Input must be a whole number.")


def calculate_severity(impact, urgency):
    """Algorithmic calculation of incident priority (LO1)."""
    score = impact + urgency
    if score >= 9: return "CRITICAL"
    if score >= 7: return "HIGH"
    if score >= 5: return "MEDIUM"
    return "LOW"


def log_incident(incident_list):
    """Implementation of Incident Logging with Metadata."""
    print("\n--- LOG NEW SECURITY INCIDENT ---")
    title = input("Incident Title: ")
    client = input("Client Name: ")
    category = input("Category (e.g., Malware, Phishing): ")
    desc = input("Full Description: ")

    impact = validate_score("Impact Score (1-5): ")
    urgency = validate_score("Urgency Score (1-5): ")

    severity = calculate_severity(impact, urgency)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_incident = {
        "id": len(incident_list) + 1,
        "title": title,
        "client": client,
        "category": category,
        "severity": severity,
        "status": "OPEN",
        "timestamp": timestamp,
        "remediation": "None recorded",
        "description": desc
    }
    incident_list.append(new_incident)
    print(f"\n[SUCCESS] Incident ID {new_incident['id']} logged as {severity}.")


def update_incident(incident_list):
    """Allows analysts to update status and add evidence/remediation."""
    search_id = int(input("\nEnter Incident ID to update: "))
    for inc in incident_list:
        if inc['id'] == search_id:
            print(f"Current Status: {inc['status']}")
            new_status = input("Enter New Status (OPEN/INVESTIGATING/CLOSED): ").upper()
            inc['status'] = new_status
            inc['remediation'] = input("Add Remediation Action/Evidence: ")
            print("Record updated successfully.")
            return
    print("Incident ID not found.")


def generate_report(incident_list):
    """Compliance reporting for Northbridge clients."""
    client = input("\nEnter Client Name for report: ").lower()
    print(f"\n--- COMPLIANCE REPORT: {client.upper()} ---")
    matches = [i for i in incident_list if i['client'].lower() == client]

    if not matches:
        print("No records found for this client.")
        return

    for m in matches:
        print(f"ID: {m['id']} | {m['timestamp']} | {m['severity']} | Status: {m['status']}")
        print(f"   Action: {m['remediation']}")
    print("-" * 30)


def main_menu():
    """Event-driven program loop."""
    incidents = []
    while True:
        print("\n" + "=" * 50)
        print(" NORTHBRIDGE CYBER SERVICES - SOC INCIDENT TRACKER")
        print("=" * 50)
        print("1. Log New Incident")
        print("2. Update Incident (Status/Remediation)")
        print("3. Search/Filter by Client")
        print("4. View All Incidents")
        print("5. Exit System")

        choice = input("\nSelect Task (1-5): ")

        if choice == '1':
            log_incident(incidents)
        elif choice == '2':
            update_incident(incidents)
        elif choice == '3':
            generate_report(incidents)
        elif choice == '4':
            for inc in incidents: print(inc)
        elif choice == '5':
            print("Terminating secure session...");
            break
        else:
            print("Invalid selection.")


if __name__ == "__main__":
    main_menu()