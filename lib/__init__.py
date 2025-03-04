import os
from rich.traceback import install

# Activting the Rich Traceback Error Format
install()


# Run chcp 65001 when the lib package is accessed
if os.system == 'nt':
    os.system('chcp 65001')
elif os.system == 'posix':
    os.system('export PYTHONIOENCODING=utf-8')
elif os.system == 'darwin':
    os.system('export PYTHONIOENCODING=utf-8')
else:
    pass