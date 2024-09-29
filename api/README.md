## Install

This project uses [poetry](https://python-poetry.org/). To install the dependencies, run:

```
poetry install
```

### Scripts

The [bin](bin) directory contains scripts for automating tasks. These have separate dependencies which can be installed with:

```
poetry install --with bin
```

### Environment Variables

- Make a copy of the file [`.env.example`](.env.example) as `.env.local` and populate the variables if necessary.

## Serve

### Local development

```
make run-local
```

### Prod

```
make run-prod
```

## Test

```
poetry run pytest
```
