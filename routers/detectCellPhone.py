import io
import logging
from PIL import Image
from typing import Annotated
from fastapi import APIRouter, File, UploadFile, HTTPException, Depends
from ultralytics import YOLO
from dependencies import getYoloModel
from models.objectDetection import CellPhoneDetectionResult
from services.imageService import ImageService

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/detectCellPhone",
    tags=["detectCellPhone"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def detect_cellphone(inputImage: Annotated[UploadFile, File(description="Upload image file only")], model: YOLO = Depends(getYoloModel)) -> CellPhoneDetectionResult:
    '''
    process the uploaded image by post request and return the cell phone detection result and confidence score as response.

    Args:
        image (UploadFile): uploaded image file
        model (YOLO): use YOLO object detection model from global dependencies
    '''

    logger.info("Received request to detect cell phone.")
    
    # Check if the uploaded file is an image
    if not inputImage.content_type.startswith("image/"):
        logger.error("Uploaded file is not an image. Filename: {}, content-type: {}".format(inputImage.filename, inputImage.content_type))
        raise HTTPException(status_code=415, detail="Uploaded file is not an image.")

    try:
        # Read image from the buffer
        image_stream : bytes = await inputImage.read()
        image : Image.Image = Image.open(io.BytesIO(image_stream))

        # Detect cellphone in image
        confidence : float = ImageService.detect_cellphone_from_stream(image, model)

        result : CellPhoneDetectionResult = CellPhoneDetectionResult(fileName= inputImage.filename, detected=confidence > 0, confidence=confidence)
        await inputImage.close()
        logger.info("200: Response delivered for cell phone detection request.")
        return result
    
    # Error Handling
    except IOError as e:
        logger.error("Unable to read uploaded image. Filename: {}, content-type: {}, Reason: {}".format(inputImage.filename, inputImage.content_type, e))
        raise HTTPException(status_code=422, detail="Unable to read uploaded image. Filename: {}; content-type: {}; Reason: {}".format(inputImage.filename, inputImage.content_type, e))
    except RuntimeError as e:
        logger.error("Error while detecting objects using the yolo detection model. Reason: %s", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    except Exception as e:
        logger.error("Error: %s", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
