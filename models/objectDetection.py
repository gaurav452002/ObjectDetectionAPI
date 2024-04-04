from pydantic import BaseModel

class CellPhoneDetectionResult(BaseModel):
    '''
    Response Data Type for Cell Phone detection request.

    Params:
        fileName (str): filename of the uploaded image(Type = UploadFile from fastapi).
        detected (bool): resuult that the cell phone detected or not.
        confidence (float): confidence score for cell phone detection in given image.
    '''
    fileName: str
    detected: bool
    confidence: float = 0
