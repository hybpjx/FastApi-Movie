from uvicorn import run
from backend.api import app





if __name__ == '__main__':
    run("run:app",debug=True,reload=True)



