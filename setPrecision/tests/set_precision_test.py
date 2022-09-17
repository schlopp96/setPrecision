from ..set_precision import set_precision, set_sigfigs


def test_sp_generic() -> None:
    assert set_precision(3.1415926, 3) == 3.142


def test_sp_zero_precision() -> None:
    assert set_precision(10.5, 0) == 10


def test_sp_large_number() -> None:
    assert set_precision(5280.40836894, 2) == 5280.41


def test_sp_non_float() -> None:
    assert set_precision(150, 5) == 150.00000


def test_sp_default_precision() -> None:
    assert set_precision(1485809.4861172) == 1485809.49


def test_ssf_generic() -> None:
    assert set_sigfigs(3.1459, 3) == 3.15


def test_ssf_zero_precision():
    assert set_sigfigs(10.5, 0) == 0


def test_ssf_large_number() -> None:
    assert set_sigfigs(5280.40836894, 2) == 5300


def test_ssf_non_float() -> None:
    assert set_sigfigs(1555313, 5) == 1555300


def test_ssf_default_precision() -> None:
    assert set_sigfigs(1485809.4861172) == 1000000
