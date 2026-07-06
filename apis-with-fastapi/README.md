# Building DevOps APIs with FastAPI

Teams often trigger automation, health checks, and reporting through APIs. This
module turns your Python logic into a real HTTP service with
[FastAPI](https://fastapi.tiangolo.com/).

You'll start with a one-file "hello" API, then study a full Internal DevOps
Utilities API that exposes system metrics, log analysis, and AWS info — with
routers, services, auto-generated docs, and a Dockerfile.

---

## Learning objectives

- Build an API with FastAPI and run it with `uvicorn`
- Understand the request/response flow and JSON responses
- Organize a real app into `routers/` (HTTP) and `services/` (logic)
- Reuse the log-analyzer and metrics logic from earlier modules behind endpoints
- Explore the auto-generated Swagger docs at `/docs`

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn psutil boto3
```

## What's inside

```
apis-with-fastapi/
├── examples/
│   └── hello_api.py                 # smallest possible FastAPI app
├── practice/
│   └── README.md
└── solution/
    └── devops-utilities-api/        # the full multi-file app
        ├── main.py                  # uvicorn entrypoint
        ├── app/api.py               # FastAPI app + / and /health
        ├── routers/                 # metrics, logs, aws endpoints
        ├── services/                # the actual logic
        ├── app.log                  # sample log for /logs
        ├── requirements.txt
        └── Dockerfile
```

## Quick start (single-file example)

```bash
uvicorn examples.hello_api:app --reload
# open http://127.0.0.1:8000/docs
```

## The full app

```bash
cd solution/devops-utilities-api
pip install -r requirements.txt
python main.py                 # runs uvicorn on http://0.0.0.0:8000
```

Then try the endpoints:

```bash
curl http://127.0.0.1:8000/                     # hello
curl http://127.0.0.1:8000/health               # {"status":"ok"}
curl http://127.0.0.1:8000/metrics              # CPU/mem/disk
curl http://127.0.0.1:8000/logs                 # analyze bundled app.log
curl http://127.0.0.1:8000/aws/s3               # needs AWS creds
```

Interactive docs: http://127.0.0.1:8000/docs

## Practice

See [`practice/README.md`](practice/README.md).
