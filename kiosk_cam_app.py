import cv2
#from text_rec import recog
import pyautogui
from time import sleep
import cv2
import pytesseract
from PIL import Image
from playsound import playsound
import pygetwindow as gw

cam = cv2.VideoCapture(1)

cv2.namedWindow("Software")

img_counter = 0

driverWindow = gw.getWindowsWithTitle(r'C:\WINDOWS\py.exe')[0]
driverWindow.minimize()
sfWindow = gw.getWindowsWithTitle('Software')[0]
sfWindow.move(10, 10)

dirWin = gw.getWindowsWithTitle(r'C:\Users\USERNAME\Desktop\CamApp')[0]
dirWin.minimize()

def recog(imgPath):
    pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    img = cv2.imread(imgPath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    conf = r'--oem 3 --psm 6 outputbase digits'

    boxes = pytesseract.image_to_data(img, config=conf)
    temp_list=[]
    adh_list=[]
    for x,b in enumerate(boxes.splitlines()):
        if(x!=0):
            b = b.split()
            if(len(b)>=12):
                if((b[11].startswith('8') or b[11].startswith('9')) and len(b[11])==11):
                    #xx,yy,w,h = int(b[6]), int(b[7]),int(b[8]), int(b[9])
                    #cv2.putText(img, b[11],(xx,yy),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,225),2)
                    print(b[11])
                    temp_list.append(b[11])
                if(len(b[11])==12):
                    #xx,yy,w,h = int(b[6]), int(b[7]),int(b[8]), int(b[9])
                    #cv2.putText(img, b[11],(xx,yy),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,225),2)
                    print(b[11])
                    adh_list.append(b[11])
    print(temp_list,adh_list)
    return temp_list,adh_list

def mouseAction(cif_num):
    all_win=gw.getAllTitles()
    for i in all_win:
        if(i.startswith('KIOSK_URL')):
            tempLink = i
            break
    #print(tempLink)
    ieWindow = gw.getWindowsWithTitle(tempLink)[0]
    ieWindow.restore()
    ieWindow.activate()
    sleep(0.25)
    screenWidth, screenHeight = pyautogui.size()
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.scroll(10000)
    sleep(.25)
    pyautogui.click(300, 265)
    #pyautogui.click(1050, 47)
    pyautogui.write(cif_num)
    sleep(0.25)
    pyautogui.click(641,263)
    sleep(.2)
    pyautogui.press('enter')

def mouseActionAEPS(cif_num):
    all_win=gw.getAllTitles()
    for i in all_win:
        if(i.startswith('KIOSK_URL')):
            tempLink = i
            break
    print(tempLink)
    ieWindow = gw.getWindowsWithTitle(tempLink)[0]
    ieWindow.restore()
    ieWindow.activate()
    sleep(0.25)
    screenWidth, screenHeight = pyautogui.size()
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.scroll(10000)
    sleep(.25)
    pyautogui.click(273, 314)
    sleep(.5)
    #pyautogui.click(1050, 47)
    pyautogui.write(cif_num)
    sleep(0.25)

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("Software", frame)
    #cv2.putText(frame, a[0],(200,200),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,225),2)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "img/opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        a,b=recog(img_name)
        #print('Auto GUI Start')
        if(len(a)>=1):
            #print('In the loop')
            playsound('data/beep.mp3')
            mouseAction(a[0])
        elif(len(b)>=1):
            #print('In the loop')
            playsound('data/beep.mp3')
            mouseActionAEPS(b[0])
        #print(a)
        img_counter += 1

cam.release()
cv2.destroyAllWindows()
        
