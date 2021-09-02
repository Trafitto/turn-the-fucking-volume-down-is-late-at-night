# Turn the fucking volume down is late at night

While gaming at night I keep the volume of my headset high but I don't notice the volume of my voice.

The plan is to schedule this script several times and turn the volume down little by little

### Prerequisites

For Windows is required [PyCaw](https://github.com/AndreMiras/pycaw)

`pip install pycaw`


For Linux is required [alsaaudio](https://pypi.org/project/pyalsaaudio/)

`pip install pyalsaaudio`


## Usage

Virtualenv:

`pipenv shell`

Default volume: 80%

`python turn_volume_down.py`

## Schedule the script for Windows

You can import the `Turn the fucking volume down is late at night.xml` into the Windows Task Scheduler
but make sure to do this changes this in the file with the your full path of the file

```
<Actions Context="Author">
    <Exec>
      <Command>"C:\your\full\path\turn_volume_down.bat"</Command>
      <Arguments>70</Arguments>
    </Exec>
  </Actions>
```

You will also need to change the python path and the script path in the .bat

Note: You need to specify the full path like this `"C:\Users\Trafitto\AppData\Local\Programs\Python\Python36-32\python.exe"`