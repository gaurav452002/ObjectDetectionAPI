import logging
import sys
from fastapi import Depends, FastAPI
import uvicorn
from dotenv import load_dotenv
from dependencies import getYoloModel
from routers import detectCellPhone
from contextlib import asynccontextmanager

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"), 
        logging.StreamHandler(sys.stdout)
    ]
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # Load the ML model
        await getYoloModel()
        logging.info("Loaded the ML model successfully.")
    # Error Handling
    except IOError as err:
        logging.critical("Failed to load the ML model. Reason: %s", err)
        raise IOError("Failed to load the ML model. Reason: {}".format(err))
    except Exception as e:
        logging.critical("Failed to load the ML model, Unexpected file. Reason: %s",e)
        raise Exception("Failed to load the ML model, Unexpected file. Reason: {}".format(e))
    yield
    # Close connections, and release resources here at the end of application lifecycle.
    
app = FastAPI(dependencies=[Depends(getYoloModel)], lifespan=lifespan)

app.include_router(router=detectCellPhone.router)

@app.get("/")
async def root():
    logging.info("Root endpoint accessed.")
    return {'message': 'Welcome to the Cell Phone detector!!!'}

# include uvicorn server
if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")