import cv2
import numpy as np
import pyautogui
screen_size = pyautogui.size()
video = cv2.VideoWriter('recording.avi' , cv2.VideoWriter_fourcc(*'MJPG') , 50 , screen_size)
while True:
    screen_shot = pyautogui.screenshot()
    frame = np.array(screen_shot)
    color = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    video.write(color)
    cv2.imshow("recording" , color)
    if cv2.waitKey(1) == ord('exit'):break
video.release()
cv2.destroyAllWindows()
