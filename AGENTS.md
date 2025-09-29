# Repository Guidelines

## Project Structure & Module Organization
`mineru-summarizer` is the primary entry point; run it from the repo root. Runtime code lives in `src/`: `core/` hosts the async summary engine, backend wiring, and image uploader; `config/` loads unified YAML settings; `output/` renders Markdown. `mineru/` provides the HTTP client for the upstream MinerU service, while `parse_and_summarize.py` combines PDF parsing with summarization for end-to-end runs. Example inputs (`test_input/`) and expected summaries (`test_data/`) support manual checks; treat `output/` and `.checkpoints/` as temporary artifacts.

## Build, Test, and Development Commands
Create a virtualenv (`python -m venv .venv && source .venv/bin/activate`) and install dependencies with `pip install -r requirements.txt`. Generate or verify configuration via `./mineru-summarizer --init-config` and `./mineru-summarizer --validate --config mineru-config.yaml`. Exercise the CLI locally with `./mineru-summarizer test_input summary.md --compression 50` and explore the PDF workflow using `python parse_and_summarize.py --help`. Run automated checks with `python -m unittest discover -s tests -p 'test_*.py'`; set `DEBUG=1` when investigating failures.

## Coding Style & Naming Conventions
Follow PEP 8 and the existing code style: four-space indentation, `snake_case` for functions, `PascalCase` for classes, and clear docstrings for public entry points. Prefer type hints, dataclasses, and `pathlib.Path` just as in `src/config/unified_config.py` and `src/core/summary_engine.py`. Maintain concise, emoji-prefixed status logs and keep user-facing error messages in Chinese to match existing CLI output.

## Testing Guidelines
Add new tests under `tests/` with filenames `test_<feature>.py` and methods prefixed by `test_`. Use `unittest.IsolatedAsyncioTestCase` or `asyncio.run` to cover async flows such as `SummaryEngine.summarize`, and rely on `unittest.mock` when stubbing `MinerUClient` or S3 uploads. Include fixtures from `test_input/` or lightweight Markdown snippets to cover chunking, checkpoint recovery, and image handling; document any intentionally skipped scenarios.

## Commit & Pull Request Guidelines
Write small, focused commits with short imperative subjects (`add mineru client`, `support parse pdf`) and elaborate in the body when behaviour or schemas change. PR descriptions should state the user impact, configuration updates, test results, and any new CLI flags or prompts, plus before/after snippets for Markdown formatting changes. Update README/USAGE when flags move, and keep generated summaries, checkpoints, and secrets out of the diff.

## Configuration & Secrets
Manage behaviour through `mineru-config.yaml`, but keep real credentials in environment variables or untracked overrides. Never commit API keys, checkpoint bundles, or S3 URLs that expose private data; provide scrubbed samples instead.
