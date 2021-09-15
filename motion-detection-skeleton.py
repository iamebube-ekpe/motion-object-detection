import cv2

cap = cv2.VideoCapture(0)

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while True:
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY) # convert to gray scale, it is easier to find contours
    blur = cv2.GaussianBlur(gray, (5, 5), 0) # blur the image to reduce noise
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) # threshold the image to get only the motion
    dilated = cv2.dilate(thresh, None, iterations=3) # dilate the image to fill in the gaps
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # find the contours in the image

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour) # get the bounding rectangle of the contour

        if cv2.contourArea(contour) < 10000: # if the contour is too small, ignore it
            continue

        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2) # draw the rectangle around the contour

        cv2.putText(frame1, f"Status: {'Movement'}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3) # put text on the image




    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2) # draw the contours on the image

    cv2.imshow("feed", frame1)

    frame1 = frame2
    ret, frame2 = cap.read() # read the next frame

    key = cv2.waitKey(1)
    if key == ord('q'):
        break # exit if escape key is pressed


cv2.destroyAllWindows()
cap.release()