# python-skeleton

[![PyPI - Version](https://img.shields.io/pypi/v/python-skeleton.svg)](https://pypi.org/project/python-skeleton)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python-skeleton.svg)](https://pypi.org/project/python-skeleton)

-----

**Table of Contents**

- [Setup](#setup)
- [Installation](#installation)
- [License](#license)


## Setup
Install pipx (https://github.com/pypa/pipx)
```console
pip install pipx
```

Ensure pipx is added to the PATH
```console
pipx ensurepath
```

Install Hatch (https://hatch.pypa.io/latest/install/)
```console
pipx install hatch
```

Set Hatch virtual env path to be project relative
```console
hatch config set dirs.env.virtual ".hatch"
```

Create default env
```console
hatch env create
```

Install pre-commit
```console
pip install pre-commit
```

Install the git hook scripts
```console
pre-commit install
```

## Installation

```console
pip install python-skeleton
```

## License

`python-skeleton` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
