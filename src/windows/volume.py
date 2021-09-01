from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

from src.settings import WINDOWS_VOLUME_MAP, DEFAULT_VOLUME


def set_volume(new_volume):
    # Get default audio device using PyCAW
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Get current volume
    current_volume = volume.GetMasterVolumeLevel()
    try:
        new_volume = WINDOWS_VOLUME_MAP[new_volume]
    except KeyError:
        print(f'Volume: {volume} is not supported')
        new_volume = WINDOWS_VOLUME_MAP[DEFAULT_VOLUME]

    if new_volume < current_volume:
        volume.SetMasterVolumeLevel(new_volume, None)
        print(f'Set new volume to {new_volume} db')
