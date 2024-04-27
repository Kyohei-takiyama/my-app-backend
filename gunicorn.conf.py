import json as _json
import os as _os


bind = "0.0.0.0:8080"
loglevel = "info"
accesslog = "-"
errorlog = "-"
graceful_timeout = 120
timeout = 120
keepalive = 5
worker_tmp_dir = "/dev/shm"


if _os.getenv("DEBUG") == "True":
    reload = True
    loglevel = "debug"

_cores = _os.cpu_count() or 1
if _max_workers := _os.getenv("MAX_WORKERS"):
    workers = min(_cores, int(_max_workers))
else:
    workers = _cores

# For debug
print(_json.dumps({k: v for k, v in locals().items() if not k.startswith("_")}))
