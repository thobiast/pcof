# -*- coding: utf-8 -*-
"""
Python Collection Of Functions.

Package with collection of small useful functions.

Dependencies: requests
"""

import shutil

import requests


def download_file(url, local_file, *, allow_redirects=True, decode=True):
    """
    Download a file.

    Arguments:
        url                    (str): URL to download
        local_file             (str): Local filename to store the downloaded
                                      file

    Keyword arguments (opt):
        allow_redirects (True/False): Allow request to redirect url
                                      default: True
        decode          (True/False): Decode compressed responses like gzip
                                      default: True

    Return:
        Request response headers

    Example:
    >>> download_file("http://google.com/favicon.ico", # doctest: +SKIP
                      "/tmp/google.ico")
    """
    with requests.get(url, stream=True, allow_redirects=allow_redirects) as res:
        if res.status_code != 200:
            raise RuntimeError("Failed downloading url {}".format(url))

        if decode:
            res.raw.decode_content = True

        with open(local_file, "wb") as fd:
            shutil.copyfileobj(res.raw, fd)

    return res.headers


# vim: ts=4
