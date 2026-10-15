from dcm.policy import retention_years, retention_status


def test_retention_years_known_categories():
    assert retention_years("contracts") == 10
    assert retention_years("backups") == 1


def test_retention_years_unknown_uses_default():
    assert retention_years("something else") == 5


def test_status_action_for_long_retention_and_risky_format():
    assert retention_status(10, 5) == "ACTION"
    assert retention_status(5, 4) == "ACTION"


def test_status_review_for_medium_retention_and_medium_risk():
    assert retention_status(3, 3) == "REVIEW"
    assert retention_status(5, 3) == "REVIEW"


def test_status_ok_for_short_retention_or_safe_format():
    assert retention_status(1, 5) == "OK"
    assert retention_status(10, 1) == "OK"