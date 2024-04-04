import json
from ultralytics import YOLO
from PIL.Image import Image

class ImageService:
    '''This class defines multiple services that enable users to perform various operations on an input image'''

    @staticmethod
    def detect_cellphone_from_stream(image: Image, model: YOLO) -> float:
        '''
        If there is a cell phone present in the input image, the YOLO model will detect and return its confidence score. If no cell phone is detected, the output will be 0.
        
        Args:
            image (PIL.IMAGE.IMAGE): This is the image file to be processed.
	        model (YOLO): This is the input YOLO model object.

        '''

        # Detect objects in the image
        result: list = json.loads(model(image)[0].tojson())

        # Get confidence of cellphone detection
        cellPhone_confidence: float = 0

        # Return the confidence of the cell phone object with the highest confidence score ifthere are multiple cell phones in image.
        for obj in result:
            if obj['name'] == 'cell phone' and obj['confidence'] > cellPhone_confidence:
                cellPhone_confidence = obj['confidence']
        return cellPhone_confidence
