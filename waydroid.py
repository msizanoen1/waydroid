#!/usr/bin/env python3
# Copyright 2021 Oliver Smith
# SPDX-License-Identifier: GPL-3.0-or-later
# PYTHON_ARGCOMPLETE_OK
import sys
import tools
import os

lp_key = 'LD_LIBRARY_PATH'  # for GNU/Linux and *BSD.
lp_orig = os.environ.get(lp_key + '_ORIG')
if lp_orig is not None:
    os.environ[lp_key] = lp_orig  # restore the original, unmodified value
else:
    # This happens when LD_LIBRARY_PATH was not set.
    # Remove the env var as a last resort:
    os.environ.pop(lp_key, None)

if __name__ == "__main__":
    sys.exit(tools.main())
