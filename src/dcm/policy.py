# Illustrative retention periods in years.
# Real periods depend on law and client contracts.
RETENTION_YEARS = {
    "contracts": 10,
    "source code": 10,
    "customer data": 7,
    "hr records": 7,
    "support records": 5,
    "design documents": 5,
    "documentation": 5,
    "logs": 3,
    "media": 3,
    "backups": 1,
}

DEFAULT_RETENTION = 5


def retention_years(category):
    return RETENTION_YEARS.get(category.lower(), DEFAULT_RETENTION)



def retention_status(years, format_risk):
    if years >= 5 and format_risk >= 4:
        return "ACTION"
    if years >= 3 and format_risk >= 3:
        return "REVIEW"
    return "OK"