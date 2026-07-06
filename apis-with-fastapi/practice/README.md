# Practice: Extend the DevOps Utilities API

Work in `solution/devops-utilities-api/` (copy it if you'd like a clean start).

## Your tasks

1. Add a `/version` endpoint that returns `{"version": "1.2.0"}`.
2. Add a `/logs/errors` endpoint that returns only the ERROR count from the
   log analyzer service (reuse `services/logs_service.py`).
3. Add a query param to `/metrics` so a caller can pass a custom `cpu_threshold`
   (e.g. `/metrics?cpu_threshold=50`).
4. Bonus: write a `Dockerfile`-based run: build the image and hit `/health`.

## Verify

```bash
cd solution/devops-utilities-api
python main.py
curl http://127.0.0.1:8000/version
curl http://127.0.0.1:8000/logs/errors
curl "http://127.0.0.1:8000/metrics?cpu_threshold=50"
```

Explore everything interactively at http://127.0.0.1:8000/docs
