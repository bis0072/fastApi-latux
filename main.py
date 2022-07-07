from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    return [{"message": "Hello World"}]



@app.get("/data")
async def data():
    return [{"message": "Hello data"}]
    

