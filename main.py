from typing import Optional
from fastapi import FastAPI


app = FastAPI()


# オペレーションという
@app.get("/")
async def index():
    return {"message": "hello world"}


# パスパラメータ
@app.get("/countries/{country_name}")
# 型ヒントを入れるとバリテーションできる
async def index(country_name: str):
    return {"message": country_name}


# クエリパラメータ
@app.get("/countries/")
# Optionalをつけると必須でなくても良いことになる。
async def country(country_name: Optional[str] = None, country_no: Optional[int] = None):
    return {
        "country_name": country_name,
        "country_no": country_no,
    }

