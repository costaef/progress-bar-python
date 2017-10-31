# progress-bar-python
A simple terminal progress bar for Python applications.

## Usage

Copy the ``progressbar.py`` module into the target project directory.

### Example

You can run the example code from the project folder to see the progress bar default behavior:

```bash
$ git clone https://github.com/costaef/progress-bar-python.git
$ cd progress-bar-python
$ python example.py
```

The terminal will show the progress bar animated.

Or do it yourself like the examples below.

```python
from time import sleep
from progressbar import ProgressBar

steps = 50
progress_bar = ProgressBar(steps)
progress_bar.prefix_text = '-----> Progress:'

for i in range(1, steps + 1):
    sleep(0.2)
    progress_bar.show(i)

progress_bar.complete()
```

The result will be:

#### Intermediary State

```bash
-----> Progress: |█████████████████████████████░░░░░░░░░░░░░░░░░░░░░| 58.0%
```

#### Completed

```bash
-----> Progress: |██████████████████████████████████████████████████| 100.0% 
-----> Completed!
```

## Customization

The progress bar can be customized through some attributes:

#### Prefix text
```python
progress_bar.prefix_text = '-----> Progress:'
```
#### Suffix text
```python
progress_bar.suffix_text = 'completed'
```
#### Progress character
```python
progress_bar.progress_char = '#'
```
#### Fill character
```python
progress_bar.fill_char = '.'
```

These customizations would result in the progress bar below:

```bash
-----> Progress: |#############################.....................| 58.0% completed
```
