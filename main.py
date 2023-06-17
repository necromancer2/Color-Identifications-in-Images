import cv2
import cv2 as cv
import pandas as pd
from tkinter import filedialog
import tkinter as tk
from tkinter.filedialog import askopenfilename


def color_name(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]

    return cname


# function to get x,y coordinates of mouse double click
def draw_shapes(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, x_pos, y_pos, clicked
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = media[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


# declaring global variables (are used later on)
clicked = False
r = g = b = x_pos = y_pos = 0

# Reading csv file with pandas and giving names to each column
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)


# Dialogue box for selecting files
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

# read videos if to get colour from a video.
# capture = cv2.VideoCapture(file_path)
#
# while True:
#     isTrue, frame = capture.read()
#     cv2.imshow("video",frame)
#     if cv2.waitKey(40) & 0xFF==ord('d'):
#         break
#
# capture.release()
# cv2.destroyAllWindows()


media = cv2.imread(file_path)


cv2.namedWindow('media')
cv2.setMouseCallback('media', draw_shapes)

while True:

    cv2.imshow("media", media)
    if clicked:

        # cv2.rectangle(media, start point, endpoint, color, thickness)-1 fills entire rectangle
        cv2.rectangle(media, (40, 20), (700, 60), (b, g, r), -1)

        # Creating text string to display( Color name and RGB values )
        text = color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

        # cv2.putText(media,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(media, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        # For very light colours we will display text in black colour
        if r + g + b >= 600:
            cv2.putText(media, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False

    # Break the loop when user hits 'esc' key
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()