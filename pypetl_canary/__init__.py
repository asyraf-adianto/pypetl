"""
    pypetl Initialization

    Description:
        This function developed so that the other pypetl function can be imported directly
        Example:
            - from pypetl.core.anyone into pyetl.anyone
            - from pypetl.io.anytwo into pypetl.anytwo
"""

# Import future function
from __future__ import absolute_import

# Import other package to be mapped later
from pypetl_canary import core
from pypetl_canary.io.db import *
from pypetl_canary.transform.convert import *
from pypetl_canary import engine, config
