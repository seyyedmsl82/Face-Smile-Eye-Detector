# Real-Time Face, Eye, and Smile Detection using OpenCV

This Python script utilizes OpenCV to perform real-time detection of faces, eyes, and smiles through a webcam feed. The script draws rectangles around detected faces in blue, eyes in red, and smiles in green.

## Prerequisites

Make sure you have the required Python libraries installed:

```bash
pip install opencv-python
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

2. Download the Haar cascades XML files for face, eye, and smile detection and place them in the project directory. You can find these files in the OpenCV GitHub repository: [haarcascades](https://github.com/opencv/opencv/tree/master/data/haarcascades)

3. Run the script:

```bash
python face_detection.py
```

Press 'q' to exit the application.

Feel free to customize the script and integrate it into your projects!

## Acknowledgments

- Haar cascades XML files for face, eye, and smile detection are part of the OpenCV project.
