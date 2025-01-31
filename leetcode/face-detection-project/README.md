# face-detection-project/face-detection-project/README.md

# Face Detection Project

This project implements real-time face detection using OpenCV and a webcam. It captures video frames and detects faces, highlighting them in the video feed.

## Project Structure

```
face-detection-project
├── src
│   ├── main.py          # Entry point of the application
│   └── utils
│       └── __init__.py  # Utility functions for face detection
├── requirements.txt     # List of dependencies
└── README.md            # Project documentation
```

## Requirements

To run this project, you need to install the following dependencies:

- OpenCV

You can install the required packages using pip. Create a virtual environment and run:

```
pip install -r requirements.txt
```

## Usage

1. Ensure your webcam is connected and working.
2. Run the main application:

```
python src/main.py
```

3. The application will open a window displaying the webcam feed with detected faces highlighted.

## License

This project is open-source and available under the MIT License.