import os
from rich.traceback import install
import subprocess

# Activting the Rich Traceback Error Format
install()

def is_font_installed(font_name):
    try:
        if os.name == 'nt':
            output = subprocess.check_output(['powershell', '-Command', f'(New-Object -ComObject Shell.Application).Namespace(0x14).Items() | Where-Object {{$_.Name -eq "{font_name}"}}'])
        elif os.name == 'posix':
            output = subprocess.check_output(['fc-list', ':family'])
        elif os.name == 'darwin':
            output = subprocess.check_output(['system_profiler', 'SPFontsDataType'])
        else:
            return False
        return font_name in output.decode('utf-8')
    except subprocess.CalledProcessError:
        return False

# Run chcp 65001 when the lib package is accessed
if os.system == 'nt':
    os.system('chcp 65001')
elif os.system == 'posix':
    os.system('export PYTHONIOENCODING=utf-8')
elif os.system == 'darwin':
    os.system('export PYTHONIOENCODING=utf-8')
else:
    pass

if not is_font_installed('MesloLGSDZ Nerd Font'):
    #l.debug('MesloLGSDZ Nerd Font is not installed. Please install to have a better experience.')
    sym: dict[str, str | None] = {
        "DEBUG": None,
        "INFO": None,
        "WARN": None,
        "ERROR": None,
        "CRITICAL": None
    }

else:
    #l.debug('MesloLGSDZ Nerd Font is installed.')
    sym: dict[str, str | None] = {
        "DEBUG": "",
        "INFO": "",
        "WARN": "",
        "ERROR": "",
        "CRITICAL": ""
    }
