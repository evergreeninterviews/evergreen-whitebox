#!/usr/bin/env python
from django.core.management import execute_manager
try:
    import egiproject.settings.local
except ImportError:
    import sys
    sys.stderr.write('Could not import egiproject.settings.local\n')
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(egiproject.settings.local)
