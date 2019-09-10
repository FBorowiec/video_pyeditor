import numpy as np
import cv2
import os
import pyscreenshot as pys


def screen_record(video_name):
  forcc = cv2.VideoWriter_fourcc(*'MP4V')
  out = cv2.VideoWriter(os.getcwd() + '/videos/' + video_name + '.mp4', forcc, 5.0, (1920,1080))

  while True:
    img= pys.grab()
    img_np=np.array(img)
    frame= cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow('Screen', frame)
    out.write(frame)
    if cv2.waitKey(20) & 0xFF==ord('q'):
      break

  out.release()
  cv2.destroyAllWindows()

  return None