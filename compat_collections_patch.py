# compat_collections_patch.py

import collections
import collections.abc

# Monkey-patch for Python 3.10+ compatibility with namedlist
if not hasattr(collections, 'Mapping'):
    collections.Mapping = collections.abc.Mapping
