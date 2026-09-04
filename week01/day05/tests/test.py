"""Tests for the energy_insights.stats module."""

import pytest

from energy_insights.stats import compute_daily_averages, find_spikes


def sample_data():
    """Sample data for testing."""
    return [
        {"timestamp": "2025-10-01T00:00:00Z", "price": "46.0"},
        {"timestamp": "2025-10-01T01:00:00Z", "price": "47.2"},
        {"timestamp": "2025-10-01T02:00:00Z", "price": "48.5"},
        {"timestamp": "2025-10-01T03:00:00Z", "price": "49.0"},
        {"timestamp": "2025-10-01T04:00:00Z", "price": "50.1"},
        {"timestamp": "2025-10-01T05:00:00Z", "price": "51.3"},
        {"timestamp": "2025-10-01T06:00:00Z", "price": "52.0"},
        {"timestamp": "2025-10-01T07:00:00Z", "price": "53.4"},
        {"timestamp": "2025-11-01T08:00:00Z", "price": "51.4"},
        {"timestamp": "2025-12-01T09:00:00Z", "price": "52.4"},
        {"timestamp": "2025-09-01T00:00:00Z", "price": "54.4"},
    ]


# Daily Compute Tests
def test_compute_daily_averages_single_row():
    """Single row input should return the same price as the average."""
    rows = [{"timestamp": "2025-10-01T00:00:00Z", "price": "46.0"}]
    result = compute_daily_averages(rows, "timestamp", "price")
    assert result == {"2025-10-01": 46.0}


def test_compute_daily_averages_multiple_rows():
    """Multiple rows for the same day should return the average price."""
    rows = sample_data()
    result = compute_daily_averages(rows, "timestamp", "price")
    assert result["2025-10-01"] == pytest.approx(49.6875)


def test_compute_daily_averages_empty_rows():
    """Empty rows list should return an empty dictionary."""
    rows = []
    result = compute_daily_averages(rows, "timestamp", "price")
    assert result == {}


def test_compute_daily_averages_missing_columns():
    """Missing price column key raises KeyError."""
    rows = [{"timestamp": "2025-10-01T00:00:00Z"}]
    with pytest.raises(KeyError):
        compute_daily_averages(rows, "timestamp", "price")


def test_compute_daily_averages_invalid_price():
    """Non-numeric price string raises ValueError."""
    rows = [{"timestamp": "2025-10-01T00:00:00Z", "price": "abc"}]
    with pytest.raises(ValueError):
        compute_daily_averages(rows, "timestamp", "price")


# Find Spikes Tests
def test_find_spikes_single_item():
    """top=1 returns only the highest single spike."""
    rows = sample_data()
    spikes = find_spikes(rows, "price", top=1)
    assert len(spikes) == 1
    assert spikes[0]["timestamp"] == "2025-09-01T00:00:00Z"


def test_find_spikes_top_larger_than_data():
    """top is larger than total available rows."""
    rows = sample_data()
    spikes = find_spikes(rows, "price", top=20)
    assert len(spikes) == 11


def test_find_spikes_empty_rows():
    """Empty rows list returns an empty list."""
    assert find_spikes([], "price", top=5) == []


def test_find_spikes_less_than_1_top():
    """top<1 returns an empty list."""
    rows = sample_data()
    assert find_spikes(rows, "price", top=0) == []


def test_find_spikes_missing_column():
    """Missing price column key raises KeyError."""
    rows = [{"timestamp": "2025-10-01T00:00:00Z"}]
    with pytest.raises(KeyError):
        find_spikes(rows, "price", top=2)


def test_find_spikes_invalid_price():
    """Non-numeric price string raises ValueError."""
    rows = [{"timestamp": "2025-10-01T00:00:00Z", "price": "invalid"}]
    with pytest.raises(ValueError):
        find_spikes(rows, "price", top=1)
