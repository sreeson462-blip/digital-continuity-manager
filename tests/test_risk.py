from dcm.risk import format_risk, risk_score, risk_level


def test_format_risk_known_formats():
    assert format_risk("pdf") == 1
    assert format_risk("mdb") == 5


def test_format_risk_ignores_case():
    assert format_risk("MDB") == 5


def test_format_risk_unknown_or_missing_uses_default():
    assert format_risk("xyz") == 3
    assert format_risk(None) == 3


def test_risk_score_is_format_times_criticality():
    assert risk_score("mdb", 5) == 25
    assert risk_score("pdf", 1) == 1


def test_risk_level_boundaries():
    assert risk_level(15) == "HIGH"
    assert risk_level(14) == "MEDIUM"
    assert risk_level(8) == "MEDIUM"
    assert risk_level(7) == "LOW"