# -*- coding: utf-8 -*-
"""Test bandwidth_converter function."""

import pytest
from pcof import bytesconv


@pytest.mark.parametrize(
    "number, f_unit, t_unit, f_time, t_time, result",
    [
        (1, "bps", "Kbps", "seconds", "seconds", 0.001),
        (1000000, "bps", "Gbps", "seconds", "seconds", 0.001),
        (1000, "Kbps", "Mbps", "seconds", "seconds", 1),
        (1000, "Kbps", "Gbps", "seconds", "seconds", 0.001),
        (1, "Mbps", "Kbps", "seconds", "seconds", 1000),
        (100, "Mbps", "Gbps", "seconds", "seconds", 0.1),
        (1, "Gbps", "Mbps", "seconds", "seconds", 1000),
        (1, "Gbps", "Gbps", "seconds", "minutes", 60),
        (1, "Gbps", "Gbps", "seconds", "hours", 3600),
        (1, "Tbps", "Mbps", "seconds", "seconds", 1000000),
    ],
)
def test_bandwidth_converter_bits_to_bits(
    number, f_unit, t_unit, f_time, t_time, result
):
    """Convert from bits to bits."""
    assert bytesconv.bandwidth_converter(
        number, from_unit=f_unit, to_unit=t_unit, from_time=f_time, to_time=t_time
    ) == (result, "{}/{}".format(t_unit, t_time))


@pytest.mark.parametrize(
    "number, f_unit, t_unit, f_time, t_time, result",
    [
        (1, "bps", "Bytes", "seconds", "seconds", 0.125),
        (100, "Kbps", "KB", "seconds", "seconds", 12.5),
        (1000, "Kbps", "MB", "seconds", "seconds", 0.125),
        (1000, "Kbps", "GB", "seconds", "seconds", 0.000125),
        (100, "Mbps", "MB", "seconds", "seconds", 12.5),
        (100, "Mbps", "GB", "seconds", "seconds", 0.0125),
        (1, "Gbps", "Mbps", "seconds", "seconds", 1000),
        (1, "Tbps", "GB", "seconds", "seconds", 125),
        (100, "Mbps", "MB", "seconds", "minutes", 750),
        (100, "Mbps", "GB", "seconds", "hours", 45),
        (100, "Mbps", "TB", "seconds", "days", 1.08),
        (1, "Gbps", "MB", "seconds", "seconds", 125),
        (1, "Gbps", "GB", "seconds", "minutes", 7.5),
        (1, "Gbps", "TB", "seconds", "days", 10.8),
        (1, "Gbps", "TB", "seconds", "months", 324),
        (10, "Gbps", "GB", "seconds", "seconds", 1.25),
        (10, "Gbps", "GB", "seconds", "minutes", 75),
        (10, "Gbps", "TB", "seconds", "hours", 4.5),
        (10, "Gbps", "TB", "seconds", "days", 108),
        (25, "Gbps", "GB", "seconds", "minutes", 187.5),
        (1, "Tbps", "GB", "seconds", "seconds", 125),
        (1, "Tbps", "TB", "seconds", "hours", 450),
    ],
)
def test_bandwidth_converter_bits_to_bytes_decimal(
    number, f_unit, t_unit, f_time, t_time, result
):
    """Convert from bits to bytes (Decimal)."""
    assert bytesconv.bandwidth_converter(
        number, from_unit=f_unit, to_unit=t_unit, from_time=f_time, to_time=t_time
    ) == (result, "{}/{}".format(t_unit, t_time))


@pytest.mark.parametrize(
    "number, f_unit, t_unit, f_time, t_time, result",
    [
        (100, "Kbps", "Bytes", "seconds", "seconds", 12500),
        (100, "Kbps", "KiB", "seconds", "seconds", 12.2),
        (1000, "Kbps", "KiB", "seconds", "seconds", 122.1),
        (1000, "Kbps", "MiB", "seconds", "minutes", 7.2),
        (100, "Mbps", "MiB", "seconds", "seconds", 11.9),
        (100, "Mbps", "GiB", "seconds", "hours", 41.9),
        (1, "Gbps", "MiB", "seconds", "seconds", 119.2),
        (10, "Gbps", "GiB", "seconds", "seconds", 1.2),
        (10, "Gbps", "TiB", "seconds", "hours", 4.1),
        (10, "Gbps", "TiB", "seconds", "days", 98.2),
        (25, "Gbps", "GiB", "seconds", "seconds", 2.9),
        (25, "Gbps", "GiB", "seconds", "minutes", 174.6),
        (1, "Tbps", "GiB", "seconds", "seconds", 116.4),
        (1, "Tbps", "TiB", "seconds", "minutes", 6.8),
        (1, "Tbps", "PiB", "seconds", "days", 9.6),
    ],
)
def test_bandwidth_converter_bits_to_bytes_binary(
    number, f_unit, t_unit, f_time, t_time, result
):
    """Convert from bits to bytes (binary)."""
    x = bytesconv.bandwidth_converter(
        number, from_unit=f_unit, to_unit=t_unit, from_time=f_time, to_time=t_time
    )
    assert (round(x[0], 1), x[1]) == (result, "{}/{}".format(t_unit, t_time))


@pytest.mark.parametrize(
    "number, f_unit, t_unit, f_time, t_time, result",
    [
        (100, "Bytes", "bps", "seconds", "seconds", 800),
        (10, "KB", "bps", "seconds", "seconds", 80000),
        (1000, "KB", "Mbps", "seconds", "seconds", 8),
        (12, "MB", "Mbps", "seconds", "seconds", 96),
        (10, "GB", "Gbps", "seconds", "seconds", 80),
        (40, "GB", "Gbps", "seconds", "seconds", 320),
        (750, "KB", "Kbps", "minutes", "seconds", 100),
        (60, "MB", "Mbps", "minutes", "seconds", 8),
        (3600, "MB", "Mbps", "hours", "seconds", 8),
        (450, "GB", "Gbps", "hours", "seconds", 1),
        (10.8, "TB", "Gbps", "days", "seconds", 1),
    ],
)
def test_bandwidth_converter_bytes_decimal_to_bits(
    number, f_unit, t_unit, f_time, t_time, result
):
    """Convert from bytes (decimal) to bits."""
    assert bytesconv.bandwidth_converter(
        number, from_unit=f_unit, to_unit=t_unit, from_time=f_time, to_time=t_time
    ) == (result, "{}/{}".format(t_unit, t_time))


@pytest.mark.parametrize(
    "number, f_unit, t_unit, f_time, t_time, result",
    [
        (100, "Bytes", "bps", "seconds", "seconds", 800),
        (10, "KiB", "Kbps", "seconds", "seconds", 81.9),
        (1000, "KiB", "Mbps", "seconds", "seconds", 8.2),
        (12, "MiB", "Mbps", "seconds", "seconds", 100.7),
        (10, "GiB", "Gbps", "seconds", "seconds", 85.9),
        (40, "GiB", "Gbps", "seconds", "seconds", 343.6),
        (60, "MiB", "Mbps", "minutes", "seconds", 8.4),
        (7, "GiB", "Mbps", "hours", "seconds", 16.7),
        (45, "GiB", "Mbps", "hours", "seconds", 107.4),
        (60, "GiB", "Mbps", "hours", "seconds", 143.2),
        (500, "GiB", "Gbps", "hours", "seconds", 1.2),
    ],
)
def test_bandwidth_converter_bytes_binary_to_bits(
    number, f_unit, t_unit, f_time, t_time, result
):
    """Convert from bytes (binary) to bits."""
    x = bytesconv.bandwidth_converter(
        number, from_unit=f_unit, to_unit=t_unit, from_time=f_time, to_time=t_time
    )
    assert (round(x[0], 1), x[1]) == (result, "{}/{}".format(t_unit, t_time))


@pytest.mark.parametrize(
    "number, f_unit, t_unit, f_time, t_time, result",
    [
        (1024, "Bytes", "KB", "seconds", "seconds", 1.02),
        (1024, "KB", "MB", "seconds", "seconds", 1.02),
        (1024, "KB", "GB", "seconds", "hours", 3.69),
        (10, "MB", "MB", "seconds", "minutes", 600),
        (10, "MB", "GB", "seconds", "hours", 36),
        (20, "MB", "GB", "seconds", "minutes", 1.20),
        (10, "GB", "GB", "seconds", "minutes", 600),
        (500, "GB", "TB", "hours", "days", 12),
        (2, "TB", "GB", "minutes", "seconds", 33.33),
        (2, "TB", "TB", "minutes", "hours", 120),
    ],
)
def test_bandwidth_converter_bytes_dec_to_bytes_dec(
    number, f_unit, t_unit, f_time, t_time, result
):
    """Convert bytes decimal to bytes decimal."""
    x = bytesconv.bandwidth_converter(
        number, from_unit=f_unit, to_unit=t_unit, from_time=f_time, to_time=t_time
    )
    assert (round(x[0], 2), x[1]) == (result, "{}/{}".format(t_unit, t_time))


@pytest.mark.parametrize(
    "number, f_unit, t_unit, f_time, t_time, result",
    [
        (1024, "Bytes", "KiB", "seconds", "seconds", 1),
        (1024, "KB", "MiB", "seconds", "seconds", 0.98),
        (1024, "KB", "GiB", "seconds", "hours", 3.43),
        (10, "MB", "MiB", "seconds", "minutes", 572.2),
        (10, "MB", "GiB", "seconds", "hours", 33.53),
        (20, "MB", "GiB", "seconds", "minutes", 1.12),
        (10, "GB", "GiB", "seconds", "minutes", 558.79),
        (25, "GB", "TiB", "seconds", "hours", 81.85),
        (2, "TB", "TiB", "minutes", "hours", 109.1),
        (100, "KB", "MiB", "minutes", "hours", 5.72),
        (9000, "MB", "GiB", "days", "days", 8.38),
        (9000, "MB", "GiB", "days", "hours", 357.6),
        (9000, "MB", "KiB", "days", "seconds", 101.7),
    ],
)
def test_bandwidth_converter_bytes_dec_to_bytes_binary(
    number, f_unit, t_unit, f_time, t_time, result
):
    """Convert bytes (decimal) to bytes (binary)."""
    x = bytesconv.bandwidth_converter(
        number, from_unit=f_unit, to_unit=t_unit, from_time=f_time, to_time=t_time
    )
    assert (round(x[0], 2), x[1]) == (result, "{}/{}".format(t_unit, t_time))


@pytest.mark.parametrize(
    "number, f_unit, t_unit, f_time, t_time, result",
    [
        (1024, "Bytes", "KB", "seconds", "seconds", 1.02),
        (1024, "KiB", "MB", "seconds", "seconds", 1.05),
        (1024, "KiB", "GB", "seconds", "hours", 3.77),
        (10, "MiB", "MB", "seconds", "minutes", 629.15),
        (10, "MiB", "GB", "seconds", "hours", 37.75),
        (30, "MiB", "GB", "seconds", "minutes", 1.89),
        (10, "GiB", "GB", "seconds", "minutes", 644.25),
        (500, "GiB", "MB", "days", "minutes", 372.83),
        (300, "MiB", "MB", "minutes", "seconds", 5.24),
        (300, "MiB", "GB", "minutes", "hours", 18.87),
    ],
)
def test_bandwidth_converter_bytes_dec_to_bytes_binary(
    number, f_unit, t_unit, f_time, t_time, result
):
    """Convert bytes (binary) to bytes (decimal)."""
    x = bytesconv.bandwidth_converter(
        number, from_unit=f_unit, to_unit=t_unit, from_time=f_time, to_time=t_time
    )
    assert (round(x[0], 2), x[1]) == (result, "{}/{}".format(t_unit, t_time))


def test_bandwidth_converter_raise_unit():
    with pytest.raises(ValueError, match=r"invalid unit. It must be.*"):
        bytesconv.bandwidth_converter(10, from_unit="KB", to_unit="XX")

    with pytest.raises(ValueError, match=r"invalid unit. It must be.*"):
        bytesconv.bandwidth_converter(10, from_unit="XX", to_unit="KB")


def test_bandwidth_converter_raise_time():
    with pytest.raises(ValueError, match=r"invalid time. It must be.*"):
        bytesconv.bandwidth_converter(
            10, from_unit="bps", to_unit="KB", from_time="XXX"
        )

    with pytest.raises(ValueError, match=r"invalid time. It must be.*"):
        bytesconv.bandwidth_converter(10, from_unit="bps", to_unit="KB", to_time="XXX")


# vim: ts=4
