from dcm import db

SAMPLE_ASSETS = [
    ("Client Contracts", "Contracts", "Legal", "SharePoint", "PDF", 5),
    ("Source Code Repositories", "Source code", "Engineering", "GitHub Enterprise", "Git", 5),
    ("Customer Support Tickets", "Support records", "Support", "Jira Service Desk", "Database", 4),
    ("Payroll Records", "HR records", "HR", "Legacy Payroll Server", "XLS", 5),
    ("Architecture Diagrams", "Design documents", "Architecture", "Network Drive", "VSD", 3),
    ("Project Documentation", "Documentation", "Project Management", "Confluence", "DOCX", 3),
    ("Daily Backups", "Backups", "Infrastructure", "Cloud Storage", "TAR", 5),
    ("Audit Logs", "Logs", "Security", "Log Server", "LOG", 4),
    ("Marketing Videos", "Media", "Marketing", "Local NAS", "AVI", 2),
    ("Old CRM Export", "Customer data", "Sales", "Legacy Laptop", "MDB", 4),
]


def seed():
    existing = {row["name"] for row in db.list_assets()}
    added = 0
    for asset in SAMPLE_ASSETS:
        if asset[0] not in existing:
            db.add_asset(*asset)
            added += 1
    print(f"Added {added} assets")


if __name__ == "__main__":
    seed()


