# CellPhone-Predictor-API

CellPhone-Predictor-API is a Python FastAPI project designed to detect whether an image contains a cellphone or not, utilizing the YoloV8 medium model.

## Installation

### Prerequisites
- **`Python (version 3.12.2)`**

### Steps

1. **Clone the repository:**
    ```bash
    git clone https://github.com/munna0912/CellPhone-Predictor-API
    ```

2. **Navigate to the project directory:**
    ```bash
    cd <Project root directory>
    ```

3. **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment:**
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

5. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

6. **Download the Yolo Object Detection Model:**
    - Download the Yolo Model from [`https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8m.pt`](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8m.pt).

7. **Put the Downloaded 'yolov8m.pt' file into the services directory and rename it as 'yolov8m_local.pt'.**

8. **Create a .env file at root directory and write it there:**
    ```bash
    PATH_TO_YOLO_MODEL=<path to your model>
    ```

    if step 7 followed `<path to your model> = .\services\yolov8m_local.pt`

9. **Run the server:**
    Execute the "main.py" file from the root directory.

10. **Access the application:**
    Access the FastAPI interface for testing at [`http://localhost:5000/docs`](http://localhost:5000/docs) in your web browser.
  
Feel free to explore the API and test the cellphone detection functionality using the provided FastAPI interface.
