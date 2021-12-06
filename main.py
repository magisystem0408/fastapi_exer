from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel, Field

# # オペレーションという
# @app.get("/")
# async def index():
#     return {"message": "hello world"}
#
#
# # パスパラメータ
# @app.get("/countries/{country_name}")
# # 型ヒントを入れるとバリテーションできる
# async def index(country_name: str):
#     return {"message": country_name}
#
#
# # クエリパラメータ
# @app.get("/countries/")
# # Optionalをつけると必須でなくても良いことになる。
# async def country(country_name: Optional[str] = None, country_no: Optional[int] = None):
#     return {
#         "country_name": country_name,
#         "country_no": country_no,
#     }
#


class ShopInfo(object):
    name: str
    location: str


# モデル作成
class Item(BaseModel):
    # バリテーション
    name: str = Field(min_length=4, max_length=12)
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None

class Data(BaseModel):
    ShopInfo: Optional[ShopInfo]
    items: List[Item]

app = FastAPI()

@app.post("/item/")
#     型をセットしてあげる
async def create_item(data: Data):
    return {"message": {"data": data}}
