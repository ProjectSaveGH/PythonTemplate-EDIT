import os
import subprocess

from lib.logger.logger import Logger
import tkinter as tk
from tkinter import filedialog

l: Logger = Logger(printLog=True)

def clearup(path: str, SHOW: bool = False, msg: bool = True) -> None:
    HAS_ERR: bool = False
    DIST: str = os.path.join(path, 'dist')
    BUILD: str = os.path.join(path, 'build')

    tmp = path.split("/")[-1]
    print(tmp)
    EGG_INFO: str = os.path.join(path, f'{tmp}.egg-info')
    del tmp

    SHOW = ( not SHOW )
    
    if not os.name == 'nt':
        if os.path.exists(DIST):
            try:
                l.info(f'Cleaning up: {DIST} ( CMD: \'rm -rf {DIST}\' )')
                subprocess.run(['rm', '-rfv', DIST], capture_output=SHOW)
                l.info('Cleaned up successfully')
            except Exception as e:
                l.error(f'Error: {e}')
                l.error(f'Failed to clean up: {DIST}')
                l.error('Please clean up manually')
                HAS_ERR = True

        if os.path.exists(BUILD):
            try:
                l.info(f'Cleaning up: {BUILD} ( CMD: \'rm -rf {BUILD}\' )')
                subprocess.run(['rm', '-rfv', BUILD], capture_output=SHOW)
                l.info('Cleaned up successfully')
            except Exception as e:
                l.error(f'Error: {e}')
                l.error(f'Failed to clean up: {BUILD}')
                l.error('Please clean up manually')
                HAS_ERR = True
                
        if os.path.exists(EGG_INFO) or True:
            try:
                l.info(f'Cleaning up: {EGG_INFO} ( CMD: \'rm -rf {EGG_INFO}\' )')
                subprocess.run(['rm', '-rfv', EGG_INFO], capture_output=SHOW)
                l.info('Cleaned up successfully')
            except Exception as e:
                l.error(f'Error: {e}')
                l.error(f'Failed to clean up: {EGG_INFO}')
                l.error('Please clean up manually')
                HAS_ERR = True
    else:
        if os.path.exists(DIST):
            try:
                l.info(f'Cleaning up: {DIST} ( CMD: \'del -rf {DIST}\' )')
                subprocess.run(['rmdir', '-rfv', DIST], capture_output=SHOW)
                l.info('Cleaned up successfully')
            except Exception as e:
                l.error(f'Error: {e}')
                l.error(f'Failed to clean up: {DIST}')
                l.error('Please clean up manually')
                HAS_ERR = True

        if os.path.exists(BUILD):
            try:
                l.info(f'Cleaning up: {BUILD} ( CMD: \'del -rf {BUILD}\' )')
                subprocess.run(['rmdir', '-rfv', BUILD], capture_output=SHOW)
                l.info('Cleaned up successfully')
            except Exception as e:
                l.error(f'Error: {e}')
                l.error(f'Failed to clean up: {BUILD}')
                l.error('Please clean up manually')
                HAS_ERR = True
                
        if os.path.exists(EGG_INFO) or True:
            try:
                l.info(f'Cleaning up: {EGG_INFO} ( CMD: \'del -rf {EGG_INFO}\' )')
                subprocess.run(['rmdir', '-rfv', EGG_INFO], capture_output=SHOW)
                l.info('Cleaned up successfully')
            except Exception as e:
                l.error(f'Error: {e}')
                l.error(f'Failed to clean up: {EGG_INFO}')
                l.error('Please clean up manually')
                HAS_ERR = True
    
    if HAS_ERR:
        l.error('')
        l.error('-' * 20)
        if msg:
            l.critical('Failed to clean up', exit=True, exit_code=1)
        else:
            l.error('Failed to clean up')
    else:
        if msg:
            l.info('')
            l.info('-' * 20)
            l.info('Cleaned up successfully')
            l.info('')
            l.info('You can now build the package')
            l.info('')
            l.info('-' * 20)

def copy(path_old: str, path_new: str, SHOW: bool = False) -> None:
    HAS_ERR: bool = False
    SHOW = ( not SHOW )

    try:
        if os.path.exists(path_new):
            try:
                l.info(f'Deleting existing path: {path_new} ( CMD: \'del -rf {path_new}\' )')
                for root, dirs, files in os.walk(path_new, topdown=False):
                    for name in files:
                        os.remove(os.path.join(root, name))
                    for name in dirs:
                        os.rmdir(os.path.join(root, name))
                os.rmdir(path_new)
                l.info('Deleted existing path successfully')
                    
            except Exception as e:
                l.error(f'Error: {e}')
                l.error(f'Failed to delete existing path: {path_new}')
                l.error('Please delete manually')
                l.error('')
                l.error('-' * 20)
                l.critical('Failed to delete old package', exit=True, exit_code=1)
        
        for root, dirs, _ in os.walk(path_old):
            for name in dirs:
                if not os.path.exists(os.path.join(path_new, name)):
                    os.makedirs(os.path.join(path_new, name))
                    
        path_old = path_old.replace('\\', '/')
        path_new = path_new.replace('\\', '/')

        l.info(f'Copying package: {path_old} to {path_new} ( CMD: \'cp -r {path_old} {path_new}\' )')
        subprocess.run(['cp', '-rfv', path_old, path_new], capture_output=SHOW)
        l.info('Copied package successfully')
    except Exception as e:
        l.error(f'Error: {e}')
        l.error(f'Failed to copy package: {path_old} to {path_new}')
        l.error('Please copy manually')
        HAS_ERR = True
    
    if HAS_ERR:
        l.error('')
        l.error('-' * 20)
        l.critical('Failed to copy package', exit=True, exit_code=1)
    else:
        l.info('')
        l.info('-' * 20)
        l.info('Copied package successfully')
        l.info('')
        l.info('You can now build the package')
        l.info('')
        l.info('-' * 20)


def build(path: str, SHOW: bool = False) -> None:
    HAS_ERR: bool = False
    SHOW = ( not SHOW )

    try:
        l.info(f'Building package: {path} ( CMD: \'python3 setup.py sdist bdist_wheel\' )')
        os.chdir(path.replace('\\\\', '/').replace('\\', '/'))
        subprocess.run(['python3', 'setup.py', 'sdist', 'bdist_wheel'], capture_output=SHOW)
        l.info('Built package successfully')
    except Exception as e:
        l.error(f'Error: {e}')
        l.error(f'Failed to build package: {path}')
        l.error('Please build manually')
        HAS_ERR = True
    
    if HAS_ERR:
        l.error('')
        l.error('-' * 20)
        l.critical('Failed to build package', exit=True, exit_code=1)
    else:
        l.info('')
        l.info('-' * 20)
        l.info('Built package successfully')
        l.info('')
        l.info('You can now upload the package to PyPI')
        l.info('')
        l.info('-' * 20)

def upload(path: str, SHOW: bool = False) -> None:
    HAS_ERR: bool = False
    SHOW = ( not SHOW )

    try:
        l.info(f'Uploading package: {path} ( CMD: \'twine upload dist/*\' )')
        os.chdir(path.replace('\\\\', '/').replace('\\', '/'))
        subprocess.run(['twine', 'upload', 'dist/*'], capture_output=SHOW)



    except Exception as e:
        l.error(f'Error: {e}')
        l.error(f'Failed to upload package: {path}')
        l.error('Please upload manually')
        HAS_ERR = True
    
    if HAS_ERR:
        l.error('')
        l.error('-' * 20)
        l.critical('Failed to upload package', exit=True, exit_code=1)
    else:
        l.info('')
        l.info('-' * 20)
        l.info('Uploaded package successfully')
        l.info('')
        l.info('You can now install the package')
        l.info('')
        l.info('-' * 20)


def p():
    input("")

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    dict = filedialog.askdirectory(title='Select New Libary Directory').replace('/', '\\')
    dict_old = filedialog.askdirectory(title='Select Current Libary Directory').replace('/', '\\')
    show: bool = input('Show output? (y/n): ').lower() == 'y'
    os.system('cls' if os.name == 'nt' else 'clear')
    if dict:
        clearup(dict, show, False)
        input('\n\nPress Enter to continue...\n\n')
        copy(dict_old, dict, show)
        input('\n\nPress Enter to continue...\n\n')
        build(f'{dict}/lib', show)
        input('\n\nPress Enter to continue...\n\n')
        upload(f"{dict}/lib", show)
        input('\n\nPress Enter to exit...')
        clearup(dict, show, False)
    else:
        l.error('No directory selected')