#!C:\Users\611903295\Downloads\Pytest_selenium_end_to_end_test\env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'confirm==0.1.3','console_scripts','confirm'
__requires__ = 'confirm==0.1.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('confirm==0.1.3', 'console_scripts', 'confirm')()
    )
