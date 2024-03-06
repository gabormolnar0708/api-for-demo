from typing import Union

from fastapi import FastAPI, HTTPException
import random
import time

app = FastAPI()

@app.get("/")
def read_root():
    sleep_time = random.randint(100, 150)
    time.sleep(sleep_time/1000)
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    sleep_time = random.randint(150, 200)
    if item_id == 50:
        time.sleep(10)
        raise HTTPException(status_code=404, detail="Item not found")
    time.sleep(sleep_time/1000)
    return {"item_id": item_id, "q": q}


@app.get("/purchase/{item_id}")
def purchase_item(item_id: int):
    sleep_time = random.randint(170, 250)
    price = random.randint(1000, 20000)
    if item_id == 75:
        time.sleep(10)
        raise HTTPException(status_code=404, detail="Item not found")
    time.sleep(sleep_time/1000)
    return {"status": "OK",
            "price": price}
