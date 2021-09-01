import sys
import getopt

from src.settings import DEFAULT_VOLUME

try:
    volume = sys.argv[1]
except IndexError:
    volume = DEFAULT_VOLUME

if 'linux' in sys.platform:
    from src.linux.volume import set_volume
    set_volume(volume)
elif 'win32'  in sys.platform:
    from src.windows.volume import set_volume
    set_volume(volume)
elif 'darwin'  in sys.platform:
    print('Platform currently not supported')