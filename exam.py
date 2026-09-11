# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Programming in Python
# ## Exam: September 8, 2026
#
#
# You can solve the exercises below by using standard Python 3.13 libraries, NumPy, Matplotlib, Pandas, PyMC.
# You can browse the documentation: [Python](https://docs.python.org/3.13/), [NumPy](https://numpy.org/doc/2.3/index.html), [Matplotlib](https://matplotlib.org/3.10.8/users/index.html), [Pandas](https://pandas.pydata.org/pandas-docs/version/2.3/index.html), [PyMC](https://www.pymc.io/projects/docs/en/stable/api.html).
# You can also look at the [slides](https://homes.di.unimi.it/monga/lucidi2425/pyqb00.pdf) or your code on [GitHub](https://github.com).
#
#
# **The exam is "open book", but it is strictly forbidden to communicate with others or "ask questions" online (i.e., stackoverflow is ok if the answer is already there, but you cannot ask a new question or use ChatGPT and similar products). Suspicious canned answers or plagiarism among student solutions will cause the invalidation of the exam for all the people involved.**
#
# To test examples in docstrings use
#
# ```python
# import doctest
# doctest.testmod()
# ```
#
# **SOLVE EACH EXERCISE IN ONE OR MORE NOTEBOOK CELLS AFTER THE QUESTION (delete the `pass` instruction).**
#
#
# The data used in this exam are from:
#
# Salerno, C., Buck, J., & Kamel, S. (2023). Predation cues amplify the effects of
# parasites on the personality of a keystone grazer [Dataset]. Zenodo.
# https://doi.org/10.5061/dryad.18931zd24
#
# The dataset is in the file [parasites.csv](./parasites.csv). Each row is one behavioral trial.
#
# Columns:
#  - `State`: US state where all the snails were collected (`NC` = North Carolina)
#  - `Location`: site where all the snails were collected (`AB` = Atlantic Beach)
#  - `Shell Length`: total shell length of the individual (millimeters)
#  - `Shell Width`: total shell width of the individual (millimeters)
#  - `Aperture Length`: total length of the individual's inner aperture (millimeters)
#  - `Weight`: total weight of the individual (grams)
#  - `Condition`: whether the trial was conducted without predator cues (`none`) or with predator cues (`pw`)
#  - `Infection status`: infection status of the individual (`0` = uninfected, `1` = infected)
#  - `Combo`: how the individual was paired: `0` = uninfected snail with uninfected snail, `1` = uninfected snail with infected snail, `2` = infected snail with uninfected snail
#  - `Individual`: identifier of the specific snail (each individual has 3 rows per condition, i.e., repeated measures)
#  - `Trial`: trial number (each snail was tested three times per condition)
#  - `Baseline`: behavioral response of the snail in the open arena (values below 1 mean the snail was essentially inactive)
#  - `Water`: behavioral response of the snail when predator cues were presented (values below 1 mean essentially no response)
#  - `Refuge`: behavioral response of the snail with a refuge available (values below 1 mean the snail did not use the refuge)
#


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pymc as pm
import arviz as az # feel free to ignore the warning about the major refactoring ongoing

# ### Exercise 1 (max 2 points)
#
# Read the file [parasites.csv](./parasites.csv) into a pandas DataFrame called `df`. Be sure to interpret correctly numerical data and the first column name (it begins with a byte-order mark and ends with a trailing space).
#
# Hint: the file is encoded in UTF-8 with a byte-order mark (use the `encoding` parameter of `pd.read_csv`, e.g. `encoding='utf-8-sig'`) and rename the first column to `State`.

pass

# ### Exercise 2 (max 2 points)
#
# Compute the mean `Shell Length` and the mean `Weight` for each `Infection status` and for each `Combo`.
#
# To get full marks, do not use explicit loops.

pass

# ### Exercise 3 (max 6 points)
#
# Define a function `longest_streak` that takes two pandas Series of the same length, `active` (boolean values) and `trials` (integer trial numbers), and returns a tuple `(length, start)`: `length` is the length of the longest streak of consecutive trial numbers for which `active` is `True`, and `start` is the trial number at which that streak begins. A streak is broken whenever `active` is `False` or when two consecutive positions do not have adjacent trial numbers (e.g., trials 1 and 3 are not consecutive).
#
# If there is no streak, return `(0, 0)`.
#
# The function must use a `while` loop to count the streak. To get full marks you should declare correctly the type hints (the signature of the function) and add a doctest string.

pass

# ### Exercise 4 (max 4 points)
#
# Use the function defined in Exercise 3 to check how many (Individual, Condition) pairs have a streak of at least 2 consecutive active trials (i.e., `Baseline >= 1`). Note that each individual was tested exactly 3 times per condition; order the trials with `sort_values`.

pass

# ### Exercise 5 (max 4 points)
#
# Add a column `active` to `df` that is `True` when `Baseline >= 1` and `False` otherwise (values below 1 mean the snail was essentially inactive). Then compute the total number of active observations for each `Condition` and for each `Combo`.
#
# To get full marks, do not use explicit loops.

pass

# ### Exercise 6 (max 5 points)
#
# For each `Combo`, compute the total number of observations and the number of observations where the snail was active (`active == True`). Make a scatter plot with `Combo` on the x-axis, the count on the y-axis, and different colors for total vs active observations. Put proper labels and a legend.

pass

# ### Exercise 7 (max 5 points)
#
# Make a picture with a plot for each `Infection status` value (1 row, 2 columns). Each plot should be a density histogram of `Baseline`. Overlay the two `Condition` values (`none` and `pw`) in different colours with `alpha=0.5`. Put proper titles and axis labels.

pass

# ### Exercise 8 (max 5 points)
#
# Consider the following statistical model for the probability that a snail is infected:
# - the parameter $\alpha$ is normally distributed with mean 0, and stdev 1
# - the parameter $\beta_{\text{shell}}$ is normally distributed with mean 0, and stdev 1
# - the parameter $\beta_{\text{weight}}$ is normally distributed with mean 0, and stdev 1
# - the probability of infection is given by $\text{invlogit}(\alpha + \beta_{\text{shell}} \cdot \text{Shell Length} + \beta_{\text{weight}} \cdot \text{Weight})$
# - the observed binary outcome `infected` (1 if `Infection status == 1`, 0 otherwise) follows a Bernoulli distribution with that probability
#
# Use PyMC to sample the posterior distributions. Plot the posterior with `az.plot_posterior`.

pass
