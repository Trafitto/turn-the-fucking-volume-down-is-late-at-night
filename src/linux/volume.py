import alsaaudio

def set_volume(new_volume):
    
    mixer = alsaaudio.Mixer()
    current_volume = int(mixer.getvolume()[0])

    if new_volume < current_volume:
        mixer.setvolume(new_volume)
        print(f'Set new volume to {new_volume}%')
    

