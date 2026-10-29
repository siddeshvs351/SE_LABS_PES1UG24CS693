import pytest
from thermostat_control import target_temperature, hvac_action, energy_alert


# 1. TARGET TEMPERATURE TESTS

def test_away_mode():
    assert target_temperature("away", True, 12) == 16


def test_sleep_mode_before_6():
    assert target_temperature("sleep", True, 5) == 18


def test_sleep_mode_after_22():
    assert target_temperature("sleep", True, 22) == 18


def test_sleep_mode_daytime():
    assert target_temperature("sleep", True, 12) == 20


def test_unoccupied():
    assert target_temperature("home", False, 12) == 18


def test_morning_temperature():
    assert target_temperature("home", True, 7) == 22


def test_morning_boundary_at_6():
    assert target_temperature("home", True, 6) == 22


def test_morning_boundary_at_9():
    assert target_temperature("home", True, 9) == 20


def test_evening_temperature():
    assert target_temperature("home", True, 18) == 21


def test_evening_boundary_at_17():
    assert target_temperature("home", True, 17) == 21


def test_evening_boundary_at_22():
    assert target_temperature("home", True, 22) == 20


def test_default_temperature():
    assert target_temperature("home", True, 12) == 20


# 2. HVAC ACTION TESTS

def test_hvac_idle():
    assert hvac_action(20, 20.5, 10) == "idle"


def test_hvac_heat_boost():
    assert hvac_action(18, 22, 2) == "heat_boost"


def test_hvac_heat():
    assert hvac_action(18, 22, 10) == "heat"


def test_hvac_cool_boost():
    assert hvac_action(25, 20, 35) == "cool_boost"


def test_hvac_cool():
    assert hvac_action(25, 20, 20) == "cool"


def test_hvac_exact_difference_one():
    assert hvac_action(20, 21, 10) == "heat"


# 3. ENERGY ALERT TESTS

def test_no_readings():
    assert energy_alert([], 10) == "ok"


def test_all_readings_within_limit():
    assert energy_alert([5, 8, 10], 10) == "ok"


def test_one_reading_over_limit():
    assert energy_alert([15, 5, 6], 10) == "warning"


def test_half_readings_over_limit():
    assert energy_alert([15, 5], 10) == "warning"


def test_majority_readings_over_limit():
    assert energy_alert([15, 16, 5], 10) == "critical"


def test_all_readings_over_limit():
    assert energy_alert([15, 16, 20], 10) == "critical"