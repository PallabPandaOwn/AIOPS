
from fastapi import FastAPI
import uvicorn

def main():
    #print("Hello from chai-code!")
    uvicorn.run(app, host="0.0.0", port=8000)


app = FastAPI() # Create an instance of FastAPI
# Define a simple route

@app.get("/")
def read_root():
    return {"Hello from chai-code!"}

if __name__ == "__main__":
    main()
