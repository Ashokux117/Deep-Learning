import cv2
import numpy as np
import streamlit as st

st.title("🎨 Real-time Color Detection")

start = st.button("Start Camera")

if start:
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to access camera")
            break

        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # RED mask
        low_red = np.array([0, 50, 50])
        high_red = np.array([10, 255, 255])
        red_mask = cv2.inRange(hsv_frame, low_red, high_red)
        red = cv2.bitwise_and(frame, frame, mask=red_mask)

        # BLUE mask
        low_blue = np.array([94, 80, 2])
        high_blue = np.array([126, 255, 255])
        blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
        blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

        # GREEN mask
        low_green = np.array([45, 100, 100])
        high_green = np.array([75, 255, 255])
        green_mask = cv2.inRange(hsv_frame, low_green, high_green)
        green = cv2.bitwise_and(frame, frame, mask=green_mask)

        # Convert BGR → RGB for display
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        red_rgb = cv2.cvtColor(red, cv2.COLOR_BGR2RGB)
        blue_rgb = cv2.cvtColor(blue, cv2.COLOR_BGR2RGB)
        green_rgb = cv2.cvtColor(green, cv2.COLOR_BGR2RGB)

        # Show in browser
        st.image(frame_rgb, caption="Original", channels="RGB")
        st.image(red_rgb, caption="Red", channels="RGB")
        st.image(blue_rgb, caption="Blue", channels="RGB")
        st.image(green_rgb, caption="Green", channels="RGB")

    cap.release()
