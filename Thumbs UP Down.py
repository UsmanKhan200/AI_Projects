import time
import cv2
import mediapipe as mp


#define a video capture object


vid = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,
               max_num_hands=2,
               min_detection_confidence=0.8,
               min_tracking_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

cTime = 0
pTime = 0
tipIds = [8,12,16,20]
tipIds1 = [6,10,14,18]
tipIds2 = [5,9,13,17]
tipIds3 = [4,3,2,1]
tipIdsF = [4,8,12,16,20]
while (True):

    # Capture the video frameq
    # by frame
    ret, frame = vid.read()
    #frame = cv2.flip(frame, 1)
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    #print(results.multi_handedness)
    lmlist = []
    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            for id, lm in enumerate(handlms.landmark):
                #print(id,lm)
                h,w,c = frame.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id,cx,cy)
                lmlist.append([id,cx,cy])

            mpDraw.draw_landmarks(frame, handlms, mpHands.HAND_CONNECTIONS)

    hand_type = ""
    lblist = []
    if results.multi_handedness:
        for hand_index, hand_info in enumerate(results.multi_handedness):
            hand_type = hand_info.classification[0].label
            print(hand_type)

    if hand_type == 'Right':
        if len(lmlist) != 0:
            fingers = []
            for id in range(0, 4):
                if ((lmlist[tipIds[id]][2] > lmlist[4][2] and lmlist[tipIds[id]][1] > lmlist[tipIds2[id]][1]) or \
                        (lmlist[tipIds3[id]][1] < lmlist[tipIds2[id]][1] and lmlist[tipIds[id]][1] < lmlist[tipIds2[id]][1]
                         and lmlist[4][2] < lmlist[5][2]) and (lmlist[18][1]-lmlist[4][1] in range(-90,190))) and (lmlist[0][2]-lmlist[8][2] < 70) and (lmlist[8][2]-lmlist[0][2] < 70) and (lmlist[19][1]-lmlist[4][1] < 38) and (lmlist[4][1]-lmlist[19][1] < 38) and (lmlist[4][2]-lmlist[10][2] < 12):
                    cv2.putText(frame, "THUMBS UP", (20, 20), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)

                elif ((lmlist[tipIds[id]][2] < lmlist[4][2] and lmlist[tipIds[id]][1] > lmlist[tipIds2[id]][1]) or \
                        (lmlist[tipIds3[id]][1] < lmlist[tipIds2[id]][1] and lmlist[tipIds[id]][1] < lmlist[tipIds2[id]][
                        1] and lmlist[4][2] < lmlist[5][2]) and (lmlist[4][1]-lmlist[18][1] in range(-90,190))) and (lmlist[0][2]-lmlist[8][2] < 70) and (lmlist[8][2]-lmlist[0][2] < 70) and (lmlist[19][1]-lmlist[4][1] < 38) and (lmlist[4][1]-lmlist[19][1] < 38) and (lmlist[10][2]-lmlist[4][2] < 12):
                    cv2.putText(frame, "THUMBS DOWN", (20, 20), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)


            # if lmlist[tipIdsF[0]][1] > lmlist[tipIdsF[0] - 1][1] and lmlist[tipIdsF[0]][1] > lmlist[tipIdsF[0] + 2][1]:
            #     fingers.append(1)
        # FINGERS COUNT 1-5
        if lmlist[4][1] < lmlist[17][1]:
            if lmlist[tipIdsF[0]][1] < lmlist[tipIdsF[0] - 1][1] and lmlist[tipIdsF[0]][1] < lmlist[tipIdsF[0] + 2][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            for id in range(1,5):
                if lmlist[tipIdsF[id]][2] < lmlist[tipIdsF[id]-2][2] and lmlist[3][2] > lmlist[tipIdsF[id]-2][2] and lmlist[tipIdsF[id]-3][2] > lmlist[tipIdsF[id]][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            totalfingers = fingers.count(1)
            cv2.putText(frame, str(int(totalfingers)), (30, 100), cv2.FONT_HERSHEY_COMPLEX, 1.0, (255, 0, 0), thickness=2)

        elif lmlist[4][1] > lmlist[18][1]:
            if lmlist[tipIdsF[0]][1] > lmlist[tipIdsF[0] - 1][1] and lmlist[tipIdsF[0]][1] > lmlist[tipIdsF[0] + 2][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            for id in range(1,5):
                if lmlist[tipIdsF[id]][2] < lmlist[tipIdsF[id]-2][2] and lmlist[3][2] > lmlist[tipIdsF[id]-2][2] and lmlist[tipIdsF[id]-3][2] > lmlist[tipIdsF[id]][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            totalfingers = fingers.count(1)
            cv2.putText(frame, str(int(totalfingers)), (30, 100), cv2.FONT_HERSHEY_COMPLEX, 1.0, (255, 0, 0), thickness=2)

#############################################################################################################

    if hand_type == 'Left':
        if len(lmlist) != 0:
            fingers = []
            for id in range(0,4):
                if ((lmlist[tipIds[id]][2] > lmlist[4][2] and lmlist[tipIds[id]][1] < lmlist[tipIds2[id]][1]) or \
                        (lmlist[tipIds3[id]][1] > lmlist[tipIds2[id]][1] and lmlist[tipIds[id]][1] > lmlist[tipIds2[id]][1]
                         and lmlist[4][2] < lmlist[5][2]) and (lmlist[4][1]-lmlist[18][1] in range(-90,190))) and (lmlist[0][2]-lmlist[8][2] < 70) and (lmlist[8][2]-lmlist[0][2] < 70) and (lmlist[19][1]-lmlist[4][1] < 38) and (lmlist[4][1]-lmlist[19][1] < 38) and (lmlist[4][2]-lmlist[10][2] < 12):
                    cv2.putText(frame, "THUMBS UP", (20, 20), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
                elif ((lmlist[tipIds[id]][2] < lmlist[4][2] and lmlist[tipIds[id]][1] < lmlist[tipIds2[id]][1]) or \
                        (lmlist[tipIds3[id]][1] > lmlist[tipIds2[id]][1] and lmlist[tipIds[id]][1] > lmlist[tipIds2[id]][1]
                         and lmlist[4][2] < lmlist[5][2]) and (lmlist[18][1]-lmlist[4][1] in range(-90,190))) and (lmlist[0][2]-lmlist[8][2] < 70) and (lmlist[8][2]-lmlist[0][2] < 70) and (lmlist[19][1]-lmlist[4][1] < 38) and (lmlist[4][1]-lmlist[19][1] < 38) and (lmlist[10][2]-lmlist[4][2] < 12):
                    cv2.putText(frame, "THUMBS DOWN", (20, 20), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)

        # FINGERS COUNT 1-5
        if lmlist[4][1] > lmlist[18][1]:
            if lmlist[tipIdsF[0]][1] > lmlist[tipIdsF[0] - 1][1] and lmlist[tipIdsF[0]][1] > lmlist[tipIdsF[0] + 2][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            for id in range(1,5):
                if lmlist[tipIdsF[id]][2] < lmlist[tipIdsF[id]-2][2] and lmlist[3][2] > lmlist[tipIdsF[id]-2][2] and lmlist[tipIdsF[id]-3][2] > lmlist[tipIdsF[id]][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            totalfingers = fingers.count(1)
            cv2.putText(frame, str(int(totalfingers)), (30, 100), cv2.FONT_HERSHEY_COMPLEX, 1.0, (255, 0, 0), thickness=2)


        elif lmlist[4][1] < lmlist[18][1]:
            if lmlist[tipIdsF[0]][1] < lmlist[tipIdsF[0] - 1][1] and lmlist[tipIdsF[0]][1] < lmlist[tipIdsF[0] + 2][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            for id in range(1,5):
                if lmlist[tipIdsF[id]][2] < lmlist[tipIdsF[id]-2][2] and lmlist[3][2] > lmlist[tipIdsF[id]-2][2] and lmlist[tipIdsF[id]-3][2] > lmlist[tipIdsF[id]][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            totalfingers = fingers.count(1)
            cv2.putText(frame, str(int(totalfingers)), (30, 100), cv2.FONT_HERSHEY_COMPLEX, 1.0, (255, 0, 0), thickness=2)



    cTime= time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(frame,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)


    # Display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
