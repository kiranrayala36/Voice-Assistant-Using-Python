from packages import *
from functions import *

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        # Logic for executing tasks
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia"," ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia") 
            print(results)
            speak(results)

        if 'bye' in query:
            speak("bye sir!")
            print("bye sir!")
            if hour>=0 and hour<20:
                speak("Have a good day")
            else:
                speak("Good night sweet dreams")
            
            break

        if "search" in query:
            speak("What do you want me to search for?")
            keyword = takecommand().lower()
            # if "keyword" is not empty
            if keyword != '':
                url = "https://google.com/search?q=" + keyword
                # webbrowser module to work with the webbrowser
                speak("Here are the search results for " + keyword)
                webbrowser.open(url)
                sleep(3)

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
 
        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")
 
        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")  
 
        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            # music_dir = "G:\\Song"
            music_dir = ""
            songs = os.listdir(music_dir)
            print(songs)   
            random = os.startfile(os.path.join(music_dir, songs[1]))
 
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")   
            speak(f"Sir, the time is {strTime}")
 
        elif 'open brave' in query:
            speak("Opening brave browser")
            codePath = r"C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(codePath)
 
        elif 'email to friend' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "dragneelking36@gmail.com"   
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
 
        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                speak("whome should i send")
                to = "dragneelking36@gmail.com"  
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
 
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "what's your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)
 
        elif "change assistant name " in query:
            speak("What would you like to call me, Sir ")
            assname = takecommand()
            speak("Thanks for naming me")
 
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
 
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Kiran.")
             
        elif 'joke' in query:
            speak(pyjokes.get_joke())
             
        elif "calculate" in query:
             
            app_id = "R2GQAL-QP7A9YJUXJ"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text

            print("The answer is " + answer)
            speak("The answer is " + answer)
 
        elif "who i am" in query:
            speak("If you talk then definitely your human.")
 
        elif "why you came to world" in query:
            speak("To keep you in a company!")
 
        elif 'powerpoint presentation' in query:
            speak("opening Power Point presentation")
            #power = r"C:\\Users\\GAURAV\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
            #os.startfile(power)
            webbrowser.open("https://www.slideshare.net/AnushkaGhosh5/power-point-presentation-on-artificial-intelligence"  )
 
        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
 
        elif "who are you" in query:
            speak("I am your virtual assistant created by Kiran")
 
        elif 'reason for you' in query:
            speak("My reason is to provide assistant for you")
 
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed successfully")
 
        elif 'open bluestack' in query:
            appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
            os.startfile(appli)
 
        elif 'news' in query:
             
            try:
                jsonObj = urlopen('''https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=4aeed1b59c7140ad87ae6d8689acc85d''')
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e))
 
         
        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
 
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                 
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
 
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop edith from listening commands")
            a = int(takecommand())
            time.sleep(a)
            print(a)
 
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/search/" + location + "")
 
        #elif "camera" in query or "take a photo" in query:
           # ec.capture(0, "Edith Camera ", "img.jpg")
 
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
             
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
 
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
 
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takecommand()
            file = open('edith.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takecommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "show note" in query:
            speak("Showing Notes")
            file = open("edith.txt", "r")
            print(file.read())
            speak(file.read(6))
 
        elif "update assistant" in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream = True)
             
            with open("Voice.py", "wb") as Pypdf:
                 
                total_length = int(r.headers.get('content-length'))
                 
                for ch in progress.bar(r.iter_content(chunk_size = 2391975),
                                       expected_size =(total_length / 1024) + 1):
                    if ch:
                      Pypdf.write(ch)
                     
        # NPPR9-FWDCX-D2C8J-H872K-2YT43
        elif "edith" in query or "edit" in query:
            wishme()
 
        elif "weather" in query:
            api_key = "ab75362cd3f13b45fc686b613f91105e"  # Enter the API key you got from the OpenWeatherMap website
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak("city name please")
            city_name = takecommand().lower()

            complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name  # This is to complete the base_url, you can also do this manually to checkout other weather data available
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]

                current_temperature =int( y["temp"]-273.15)
                z = x["weather"]

                weather_description = z[0]["description"]

                speak(" Temperature is " +
                                str(current_temperature) +" degree celcius" +
                    " and sky is " +
                                str(weather_description))
                print(" Temperature is " +
                                str(current_temperature) +" degree celcius" +
                    " and sky is " +
                                str(weather_description))

            else:
                speak(" City Not Found ")
             
        elif "send message " in query:
                # You need to create an account on Twilio to use this service
                account_sid = 'Account Sid key'
                auth_token = 'Auth token'
                client = Client(account_sid, auth_token)
 
                message = client.messages \
                                .create(
                                    body = takecommand(),
                                    from_='Sender No',
                                    to ='Receiver No'
                                )
 
                print(message.sid)
 
        elif "Good Morning" in query:
            speak("A warm" +query)
            speak("How are you Mister")
            speak(assname)
 
        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:  
            speak("I'm not sure about, may be you should give me some time")

        elif "hai" in query or "hello" in query or "hi" in query or "hey" in query:
            speak("Hello sir!")
 
        elif "how are you" in query:
            speak("I'm fine, glad you me that")
 
        elif "i love you" in query:
            speak("It's hard to understand")
 
        elif "what is" in query or "who is" in query:
             
            # Use the same API key
            # that we have generated earlier
            client = wolframalpha.Client("R2GQAL-QP7A9YJUXJ")
            res = client.query(query)
             
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")
        
        elif 'capture' in query:
            speak("Say cheese!")
            capture()

        elif "your age" in query or "how old are you":
            pass

