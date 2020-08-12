# -*- coding: utf-8 -*-
"""
Python Collection Of Functions.

A collection of small useful functions.

Usage help:
    Importing package does not give access to modules' functions.
    It is required to import each module to check its function help
    and to use its functions.

    Example:
        import pcof.decorators
        help(pcof.decorators)

        from pcof import bytesconv
        help(bytesconv)
        bytesconv.bytes2human(2048)
            ('2.00', 'KB')
"""

__name__ = "pcof"
__description__ = "Python Collection Of Functions."
__url__ = "https://github.com/thobiast/pcof"
__license__ = "MIT"
__author__ = "Thobias Salazar Trevisan"


from pcof.__version__ import __version__  # noqa

# vim: ts=4
