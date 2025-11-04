from fastapi import FastAPI
from app.api.v1.router import api_router
from app.api.v1.endpoints import auth
from app.core.config import settings  # ← FIX: Thêm 'app.'
import uvicorn

app = FastAPI()

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}


if __name__ == "__main__":
    print(f"Server is running at: http://{settings.HOST}:{settings.PORT} !!!!")
    uvicorn.run(
        "app.main:app",  # ← FIX: Thêm 'app.' prefix
        host=settings.HOST, 
        port=settings.PORT, 
        reload=settings.DEBUG, 
        proxy_headers=True, 
        forwarded_allow_ips="*"
    )