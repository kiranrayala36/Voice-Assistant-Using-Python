from packages import *

hour = int(datetime.datetime.now().hour)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id )
engine.setProperty('voice',voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-10)
assname="EDITH"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    speak("Hello I am "+ assname +" how may i help you!")


def takecommand():
    # it takes microphone input from the user and return string output
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        speak("say that again please")
        print("say that again please......")
        return "none"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('dragneelking36@gmail.com', 'mydarling36')
    server.sendmail('dragneelking36@gmail.com', to, content)
    server.close()

def age():
    day=23
    month=2
    year=22
    strday=int(datetime.today().strftime('%d'))
    strmonth=int(datetime.today().strftime('%m'))
    stryear=int(datetime.today().strftime('%y'))
    days=[strday-day,((strmonth-month)*30),((stryear-year)*360)]
    age = 0
    for i in range(days):
        age += i
    print(age)
    if age<30:
        print("I'm",age,"days old")
        speak("I'm",age,"days old")
    elif age>30 and age<360:
        age=int(age/30)
        print("I'm",age,"months old")
        speak("I'm",age,"months old")
    elif age>360:
        age=int(age/360)
        print("I'm",age,"years old")
        speak("I'm",age,"years old")

def capture():
    cap = cv2.VideoCapture(1)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
    while True:
        _, frame = cap.read()
        #original_frame = frame.copy()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray, 1.3, 5)
        for x, y, w, h in face:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            face_roi = frame[y:y+h, x:x+w]
            gray_roi = gray[y:y+h, x:x+w]
            smile = smile_cascade.detectMultiScale(gray_roi, 1.3, 25)
            for x1, y1, w1, h1 in smile:
                cv2.rectangle(face_roi, (x1, y1), (x1+w1, y1+h1), (0, 0, 255), 2)
                time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                file_name = f'selfie-{time_stamp}.png'
                cv2.imwrite(file_name, frame)
        cv2.imshow('cam star', frame)
        if cv2.waitKey(10) == ord('q'):
            break