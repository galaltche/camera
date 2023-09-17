# import cv2
# import streamlit as st
# import numpy as np
# import tempfile
#
# cap = cv2.VideoCapture(1)
# st.title("Bond Video Chat")
# frame_placeholder = st.empty()
# stop_button_pressed = st.button("Stop")
#
# while cap.isOpened() and not stop_button_pressed:
#     ret, frame = cap.read()
#     if not ret:
#         st.write("The video capture has ended")
#         break
#     frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     frame_placeholder.image(frame, channels="RGB")
#     if cv2.waitKey(1) & 0XFF == ord("q") or stop_button_pressed:
#         break
# cap.release()
# cv2.destroyAllWindows()
#
#



import cv2
import streamlit as st

def realTimeFeed():
    stframe = st.empty()
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        stframe.image(frame, channels="BGR")
        cv2.imshow("feed", frame)
        if cv2.waitKey(3) & 0XFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()

st.title("Bond Video Chat")
realTimeFeed()

