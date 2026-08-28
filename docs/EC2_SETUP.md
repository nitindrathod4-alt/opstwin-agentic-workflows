# EC2 Setup

On a fresh Ubuntu instance, install the missing Python tooling first:

```bash
sudo apt-get update
sudo apt-get install -y python3-venv python3-pip
```

Then from the repository:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
python -m evaluation.run_benchmark
python -m opstwin.demo
```

Run as a normal Ubuntu user when possible. Avoid running the project as root unless necessary.

## Troubleshooting

If `python3 -m venv .venv` reports that `ensurepip` is unavailable, install the version-matched `python3.X-venv` package shown by the error message, recreate `.venv`, and activate it again.
