import uvicorn
from fastapi import FastAPI
from prometheus_client import start_http_server
from loguru import logger

from passion_sync.settings import settings
from passion_sync.route.user import user_router, couple_router
from passion_sync.route.activity import activity_router
logger.info(f"Initializing Passion Sync.")
logger.info(f"Server Port: {settings.server_port}. Metrics Port: {settings.metrics_port}.")

app = FastAPI()
prom = start_http_server(port=settings.metrics_port)

app.include_router(user_router)
app.include_router(couple_router)
app.include_router(activity_router)


def main():
    uvicorn.run(app, host="0.0.0.0", port=settings.server_port)


if __name__ == "__main__":
    main()
