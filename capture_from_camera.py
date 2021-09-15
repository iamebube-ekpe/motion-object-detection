import cv2

cap = cv2.VideoCapture(0)

# To save the frames captured from the camera
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        output.write(frame)
        # Display it in grayscale
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Print width and height of the frame
        # print(f'Frame width: {cap.get(cv2.CAP_PROP_FRAME_WIDTH)}')
        # print(f'Frame height: {cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}')

        cv2.imshow('frame', frame) #Swap gray variable name with frame variable to see the difference

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
output.release()
cv2.destroyAllWindows()