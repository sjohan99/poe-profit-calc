# Scripts

To run the scripts, you need to install the dependencies with:

```
poetry install --with bin
```

## `poe-wiki-gems.py`

This script pulls all gems from https://poegems.com/ and scrapes the [Path of Exile Wiki](https://www.poewiki.net/) for the experience required to level each gem to max and write the results to `output/gem_xp.json`.

### Usage

```
poetry run python bin/poe-wiki-gems.py
```
