# Hand Gesture-Based Brightness Control

This project demonstrates a computer vision application that controls the screen brightness using hand gestures. The implementation leverages the OpenCV library for video processing, MediaPipe for hand tracking, and the Screen Brightness Control (SBC) library to adjust the screen brightness. The user can control the brightness by changing the distance between their thumb and index finger.

## Features
- **Real-time hand tracking**: Detects and tracks hands using MediaPipe.
- **Brightness control**: Adjusts screen brightness based on the distance between the thumb and index finger.
- **Visual feedback**: Displays visual elements such as circles and lines between fingers and a brightness bar.

## Technologies Used
- **Python**: Programming language.
- **OpenCV**: For video capture and image processing.
- **MediaPipe**: For hand detection and tracking.
- **Screen Brightness Control**: For changing the screen brightness.
- **NumPy**: For numerical operations.
- **Math**: For calculating the distance between points.




## Code Overview

### `handDetector` Class
- **`__init__`**: Initializes the MediaPipe hands object with parameters like `mode`, `maxHands`, `detectionCon`, and `trackCon`.
- **`findHands`**: Detects hands in the input frame and optionally draws landmarks.
- **`findPosition`**: Returns the list of landmarks for the detected hand.

### Main Script
- Captures video frames using OpenCV.
- Detects hand landmarks using the `handDetector` class.
- Computes the distance between the thumb and index finger to adjust the brightness.
- Displays the brightness bar and FPS on the screen.

## Requirements
- Python 3.x
- OpenCV
- MediaPipe
- NumPy
- Screen Brightness Control



## Acknowledgments
- [MediaPipe](https://mediapipe.dev) for providing the hand tracking solution.
- [Screen Brightness Control](https://github.com/CarterPlank/screen-brightness-control) for controlling screen brightness.

## Contact
For any inquiries, please contact Rishi jain at rishi.jain0920@gmail.com
