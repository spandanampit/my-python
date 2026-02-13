import cv2
import numpy as np
from mss import mss

with mss() as sct:
    monitor = sct.monitors[1]
    screen_width = monitor["width"]
    screen_height = monitor["height"]

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter("Recording.mp4", fourcc, 20.0, (screen_width, screen_height))

    print("Recording... Press Ctrl+C in terminal to stop.")

    try:
        while True:
            screenshot = sct.grab(monitor)
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
            out.write(frame)

    except KeyboardInterrupt:
        print("Recording stopped.")

    out.release()

print("Saved successfully.")
