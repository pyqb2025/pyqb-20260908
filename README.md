
# Jellyfish

Data source:


Salerno, C., Buck, J., & Kamel, S. (2023). Predation cues amplify the effects of
parasites on the personality of a keystone grazer [Dataset]. Zenodo.
https://doi.org/10.5061/dryad.18931zd24

## Setup

The `exam.py` is intended to be modified as a
[jupyter](https://jupyter.org/) notebook. The notebook format `.ipynb`, however,
is not very convenient for configuration management, testing, and giving
feedback via the usual "pull-request" mechanism provided by Github. Thus, this
repository uses
[jupytext](https://jupytext.readthedocs.io/en/latest/install.html) to **pair** a
pure Python file with a notebook with the same name. The notebook is
automatically created when you open the Python file with jupyter, and the two
files are kept in sync. 

To start, you need the following actions:

```sh
python3.13 -m venv VIRTUAL_ENVIRONMENT
# remember to activate the virtual environment according to your operating system rules:
source VIRTUAL_ENVIRONMENT/bin/activate # adapt to your system
pip install -r requirements.txt
jupyter notebook
```

Then you can open the `exam.py` as a notebook in the browser.


## Test

To test examples in docstrings use:

```python
import doctest
doctest.testmod()
```


You can execute tests locally on the python file:


```sh
mypy exam.py
python -m doctest exam.py
```
