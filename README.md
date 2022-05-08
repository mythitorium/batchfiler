batchfiler
=======

Automatically creates batch files by saving clipboard contents.

Instructions given here are for windows (This script isn't worth my time to give a shit about other platforms)

Installing
-------

**Python 3.9 is ideal**

In the very rare chance you care about installing this:

1. Install [pyperclip](https://github.com/asweigart/pyperclip)

```
py -3 -m pip install -U pyperclip
```

2. Download and extract batchfiler's source.

Usage
-------

Running batchfiler

    cd C:\path\to\extracted\code
    py batchfiler.py

The script will automatically save any new ctrl + c's (plaintext only)

Press ctrl + c to kill the script

Configuration
-------

A .ini file containing the following will be created when running the script for the first time, located in the script's directory.

```ini
[config]
prefix:
suffix:
filter:
output_file_name:
output_file_path:
```

Edit the values to customize the script's behavior.

* `prefix` : The prefix string to be attached to each saved clipboard. Default is ""
* `suffix` : The suffix string to be attached to each saved clipboard. Default is ""
* `filter` : Only allow saving the clipboard if it contains this string. Default is ""
* `output_name` : Name of the output file. Default is "output.txt"
* `output_path` : The saved location to the output file. Default puts file in the script's directory

Closing
--------

Ok thanks bye