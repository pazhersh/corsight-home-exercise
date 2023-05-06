# Corsight.ai home assignment
by paz hershberg

## Forward

I would like to start by apoligizing - I am aware that this is meant to be ran on a linux machine (specifically ubuntu), but since I only own windows machines I never tested it on a linux one.
Similarly, I have used Python 3.11, but this should have even less implications than a difference in os's.

That said, I hope that most commands will work on both operating systems, as python should make the overall environment irrelevant for most of its usage.

## Usage

To build and install locally you may run:
```bash
python -m build
pip install ./dist/<the generated file>.whl
```

To run commands simply run
```bash
python -m corsight_home_exercise
```

For example
```bash
python -m corsight_home_exercise disk-size 'C:/'
> {'Total': '243.41114807128906 GiB', 'Used': '76.98932266235352 GiB', 'Free': '166.42182540893555 GiB'}
```

Additially, every command comes with an automatic --help flag, so for example one could use `python -m corsight_home_exercise call-script --help`.