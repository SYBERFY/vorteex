import sys
import subprocess


def open_browser(link):
    if sys.platform == 'win32':
        subprocess.Popen(['start', link], shell=True)

    elif sys.platform == 'darwin':
        subprocess.Popen(['open', link])

    else:
        try:
            subprocess.Popen(['xdg-open', link])
        except OSError:
            print(f'Go to: {link}')
