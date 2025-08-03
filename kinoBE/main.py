from typing import Union, Dict
from fastapi import FastAPI, APIRouter

from kinoBE.tools import tag_router, item_router, association_router, user_router
from kinoBE.core import env_loader

app = FastAPI()


# Load all routers into the app
routers: Dict[str, APIRouter] = {
        "/tag": tag_router,
        "/item": item_router,
        "/association": association_router,
        "/user": user_router,
    },

for prefix, router in routers.items():
    app.include_router(
        router,
        prefix=f"/{env_loader.ROOT_PATH}" + prefix,
    )