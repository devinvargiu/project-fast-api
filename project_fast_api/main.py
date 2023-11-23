import uvicorn
from fastapi import FastAPI
app = FastAPI()


@app.get("/")
async def main_route():
  return {"message": "Hey, It is me Goku"}


def start():
    print("Starting server uvicorn, please wait...")
    uvicorn.run("project_fast_api.main:app", host="0.0.0.0", port=5000, reload=True)

if __name__ == "__main__":
    start()
