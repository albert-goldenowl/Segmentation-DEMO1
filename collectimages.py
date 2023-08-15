import cv2
import os
save_dir = 'images'
if os.path.exists(save_dir) == False:
    os.mkdir(save_dir)
images = sorted(os.listdir(save_dir), key=lambda x: int(x.split('.')[0]))
if len(images) == 0:
    i = 0
else:
    i = int(images[-1].split('.')[0]) + 1

frame_shape = (640, 480)
target_shape = imshape[:2]
half_width = target_shape[0] // 2
half_height = target_shape[1] // 2
x0 = frame_shape[0] // 2 - half_width
y0 = frame_shape[1] // 2 - half_height
x1 = frame_shape[0] // 2 + half_width
y1 = frame_shape[1] // 2 + half_height
cam = cv2.VideoCapture(0)
while True:
    fps = cam.get(cv2.CAP_PROP_FPS)
    
    ret, frame = cam.read()
    ori_frame = frame.copy()
    frame = cv2.resize(frame, frame_shape)
    cv2.putText(frame, str(int(fps)), (5, 30), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 1)
    cv2.rectangle(frame, (x0, y0), (x1, y1), (0, 255, 0), 2)
    cv2.imshow('cam', frame)
    k = cv2.waitKey(1)
    filename = '{}/{}.jpg'.format(save_dir, i)
    if k == ord('s'):
        photo = ori_frame[y0:y0+target_shape[1], x0:x0+target_shape[0]]
        cv2.imwrite(filename, photo)
        i += 1
        print(f'Photo shot, named: {filename}')
    if k == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()