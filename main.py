import time
import cv2

pt1 = (0, 0)
pt2 = (0, 0)
mouseDown = False

window_name = 'Opencv'

ret_set = []


def draw(event, x, y, flags, args):
    global pt1, pt2, mouseDown, ret_set

    if event == cv2.EVENT_LBUTTONDOWN:

        if not mouseDown:
            pt1 = (x, y)
            pt2 = (x, y)
            mouseDown = True
        elif mouseDown:
            pt2 = (x, y)
            ret_set.append([pt1, pt2])
            mouseDown = False
    elif event == cv2.EVENT_RBUTTONDOWN:
        mouseDown = False

    if event == cv2.EVENT_MOUSEMOVE and mouseDown:
        pt2 = (x, y)


cap = cv2.VideoCapture('./data/road.mp4')

fps = int(cap.get(cv2.CAP_PROP_FPS))

if cap.isOpened():

    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, draw)

    while True:

        ret, frame = cap.read()

        if ret:
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            if mouseDown:
                cv2.rectangle(frame, pt1, pt2, (0, 0, 255), 2)

            if ret_set:
                for rectangle in ret_set:
                    (x1, y1), (x2, y2) = rectangle
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

            cv2.imshow(window_name, frame)

        else:
            break

        time.sleep(1 / fps)

    cap.release()
    cv2.destroyAllWindows()

else:
    print("Can't Read VideoCapture!")
