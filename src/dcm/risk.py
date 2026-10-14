# How likely is a format to become unreadable?
# 1 = very safe (open standard), 5 = very risky (old or proprietary)
FORMAT_RISK = {
    "pdf": 1,
    "git": 1,
    "docx": 2,
    "tar": 2,
    "log": 2,
    "database": 3,
    "xls": 3,
    "avi": 4,
    "vsd": 4,
    "mdb": 5,
}

DEFAULT_RISK = 3


def format_risk(file_format):
    if file_format is None:
        return DEFAULT_RISK
    return FORMAT_RISK.get(file_format.lower(), DEFAULT_RISK)




def risk_score(file_format, criticality):
    return format_risk(file_format) * criticality


def risk_level(score):
    if score >= 15:
        return "HIGH"
    if score >= 8:
        return "MEDIUM"
    return "LOW"