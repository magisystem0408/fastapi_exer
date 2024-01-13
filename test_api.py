import requests
import json

def main():
    url = "http://127.0.0.1:8000/item/"
    body = {
        "name": "T-shirt",
        "description": "string",
        "price": 1000,
        "tax": 1.1
    }
    # 辞書型をjson形式で変えてあげる
    res = requests.post(url, json.dumps(body), timeout=60)
    print(res.json())


if __name__ == '__main__':
    main()
