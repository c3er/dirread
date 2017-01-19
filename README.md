# Introduction

This script reads the files inside the given directory and shows all text files in a single HTML page. The generated HTML will be opened with the standard web browser automatically.

# Usage

## Basic call

```
python dirread.py <Path to directory of interest>
```

## Example

This shows its own source code:

```
python dirread.py .
```

# Requirements

It was tested only with this configuration:

* Windows 10 64 Bit (Version 1607)
* Python 3.5.2 32 Bit
  * The standard installer from [python.org](https://www.python.org/)
  * Not compatible with Python versions prior to 3.5
* Firefox 50 32 Bit

It may run with other configurations.

## Additional libraries to install

### Python

See [requirements.txt](requirements.txt) for the libraries that are needed. It should be enough to type

```
pip install -r requirements.txt
```


# Known bugs

* .gitignore support: Negated patterns (starting with "!") are ignored currently. Because of this, files are not shown that would not be ignored otherwise.
* Certain web projects with much JavaScript code cause prism.js to be stucked at rendering.
