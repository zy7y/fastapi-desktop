import os.path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

static_file_abspath = os.path.join(os.path.dirname(__file__), "static")

app.mount("/static", StaticFiles(directory=static_file_abspath), name="static")


@app.get("/")
def index():
    return FileResponse(f"{static_file_abspath}/index.html")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)