import uvicorn
from fastapi import FastAPI
from prometheus_client import start_http_server

from settings import settings


from passion_sync.route.user import user_router, couple_router
from passion_sync.route.activity import activity_router

app = FastAPI()
prom = start_http_server(port=9101)

app.include_router(user_router)
app.include_router(couple_router)
app.include_router(activity_router)


def main():
    uvicorn.run(app)


if __name__ == "__main__":
    main()
