import pytest

from catalog import classify_model_size


def test_five_features_is_tiny():
    assert classify_model_size(5) == "tiny"


def test_six_features_is_small():
    assert classify_model_size(6) == "small"
 
 
def test_zero_features_is_invalid():
    with pytest.raises(ValueError):
        classify_model_size(0)