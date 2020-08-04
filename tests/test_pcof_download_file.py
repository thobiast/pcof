# -*- coding: utf-8 -*-
"""Test download_file function."""

from unittest.mock import patch
import pytest
from pcof import pcof


@patch("pcof.pcof.requests.get", autospect=True)
def test_download_file_raise(mock_get):
    mock_get.return_value.__enter__.return_value.status_code = 300
    with pytest.raises(RuntimeError, match=r"Failed downloading url.*"):
        pcof.download_file("nourl", "nofile")
    mock_get.assert_called()


@patch("builtins.open", autospec=True)
@patch("pcof.pcof.shutil.copyfileobj", autospec=True)
@patch("pcof.pcof.requests.get", autospect=True)
def test_download_file(mock_get, mock_copyfileobj, mock_open):
    url = "http://url"
    local_file = "/tmp/some_localfile"
    header = {"Content-Encoding": "gzip", "Content-Length": "1494"}

    mock_get.return_value.__enter__.return_value.status_code = 200
    mock_get.return_value.__enter__.return_value.headers = header

    ret = pcof.download_file(url, local_file)

    assert ret == header

    mock_get.assert_called_once_with(url, stream=True, allow_redirects=True)
    mock_open.assert_called_once_with(local_file, "wb")

    # get mock context manager open file descriptor
    file_handle = mock_open.return_value.__enter__.return_value
    raw = mock_get.return_value.__enter__.return_value.raw
    mock_copyfileobj.assert_called_with(raw, file_handle)


# vim: ts=4
