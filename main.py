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
