import math
import osascript

def set_volume(new_volume):

    _, current_volume, err=osascript.run("output volume of (get volume settings)")

    if err:
        raise Exception(err)
    
    if new_volume < current_volume:
        osascript.run(f"set volume output volume {new_volume}")
        _, updated_volume, err=osascript.run("output volume of (get volume settings)")
        print(f'New volume set to {updated_volume}%')
    else:
        print('Volume is lower')

