<h1 align="center"> Template Python App </h1>
<h3 align="center"> Subtitle </h3>


## How To Use

> [!IMPORTANT]
>
> Prequisites: [uv](https://docs.astral.sh/uv/getting-started/installation/)
>
> To install: `pip install uv`

### Initial setup

Run `uv sync` to create a .venv and install dependencies as specified in `pyproject.toml`. Then use `uv run` to run scripts, and pip commands.

Examples:

- `uv run main.py <kwargs/args>`
- `uv run streamlit run app.py`
- `uv run ruff check`

### Initialize directories and files

`uv run main.py init-dirs`
