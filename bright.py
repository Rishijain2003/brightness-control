import cv2
import time
import numpy as np
import handtracking as htm
import math
import screen_brightness_control as sbc  # For brightness control

################################
wCam, hCam = 640, 480
################################
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7)

minBright = 0     # Minimum brightness level
maxBright = 100   # Maximum brightness level

brightness = 0    # Variable to store current brightness
brightnessBar = 400
brightnessPer = 0

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        # Find coordinates of the thumb (ID 4) and index finger (ID 8)
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)  # Distance between thumb and index finger
        #print(length)

        # Map the distance to the brightness range (Hand range: 50 - 300)
        brightness = np.interp(length, [50, 300], [minBright, maxBright])
        brightnessBar = np.interp(length, [50, 300], [400, 150])
        brightnessPer = np.interp(length, [50, 300], [0, 100])

        # Set the brightness
        sbc.set_brightness(int(brightness))

        # Change color if hand is closed (for feedback)
        if length < 50:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

    # Draw a brightness bar on the screen
    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(brightnessBar)), (85, 400), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f'{int(brightnessPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
    

    # FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    cv2.imshow("Img", img)
    cv2.waitKey(1)