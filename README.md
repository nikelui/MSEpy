# MSEpy
A rework of Magic Set Editor in Python and Qt5.  
The aim is to be as much cross-compatible as possible, without depending too much on external libraries.

## Sources
The original project can be found [here](http://magicseteditor.sourceforge.net/). The development has been still for quite a long time and they have moved the forum [here](http://magicseteditor.boards.net/).  
The original code was on subversion and I can't seem to find it, so I am using the resources and the source code as a reference from a github fork [(here)](https://github.com/Lymia/MagicSetEditor2).

## Instructions
Just launch the `MSE.py` script in Python3 (might provide tools like bash script or .com launcher in the future).  
You can modify the .ui layout files (using Qt designer or similar), but you need to re-compile them using pyuic5:
```
  pyuic5 layout.ui -o layout.py
```
And also the resources file used in the project, with pyrcc5:
```
  pyrcc5 resources.qrc -o resources_rc.py
```

**Prerequisites** (_still in progress_)

+ A working Python3 distribution
+ PyQt5


## Changelog
_version 0.1_

+ Layout of loading screen. The "Open set" button opens a file dialog to select a .mse-set file
+ Instead of using a custom format to save the data, switched to more global standards. Added scripts to convert the set file in .json (TODO: parse the symbol file and convert to SVG).
