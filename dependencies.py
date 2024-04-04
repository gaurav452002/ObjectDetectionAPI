from ultralytics import YOLO
import os

class YOLOSINGLETON:
    _instance: YOLO = None
    '''It is a singleton class to create a single object of the YOLO model and use it accross the liifecycle of the application.'''

    @classmethod
    async def get_instance(cls) -> YOLO:
        '''
        This method insure that if any instance of this class is not created load the YOLO model from disk and create the instance, and if the instance is already created return it.
        '''
        if not cls._instance:
            cls._instance = YOLO(os.getenv('PATH_TO_YOLO_MODEL'))
        return cls._instance
    

# Load YOLO model as a global dependency
async def getYoloModel() -> YOLO:
    '''
    This function returns a singleton class object of the Yolo version 8 object detection model and returns it to use as a global dependency.
    '''
    return await YOLOSINGLETON.get_instance()