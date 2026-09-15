import pytest

from catalog import classify_model_size


def test_one_feature_is_tiny():
    assert classify_model_size(1) == "tiny"


@pytest.fixture
def documented_boundaries():
    """Límites que la pareja irá cubriendo durante la sesión."""
    return (5, 6, 15, 16, 30, 31)
