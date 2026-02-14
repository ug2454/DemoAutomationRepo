# REST API Automation Tests

## Run

Start the dev app first (see its README), then:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

Optionally override the target URL:

```bash
DEV_APP_URL=http://127.0.0.1:8000 pytest -q
```
