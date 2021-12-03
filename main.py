import speech_recognition
import pyttsx3
from datetime import date,datetime
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
 
def weather(city, robot_brain):
    city = city.replace(" ", "+")
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    weather = soup.select('#wob_tm')[0].getText().strip()
    robot_brain = weather
    return robot_brain

robot_mouth = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()
robot_brain = ""
today = date.today()
now = datetime.now()

while True:
	with speech_recognition.Microphone() as mic:
		print("Robot: I'm listening")
		audio = robot_ear.listen(mic)
	print("Robot: ...")
	try:
		you = robot_ear.recognize_google(audio)
	except:
		you = ""
	print("You: " + you)
	if you == "":
		robot_brain	= " I can't hear you, try again"
	elif "name" in you:
		robot_brain = "my name is Advices"
	elif "how are you" in you:
		robot_brain = "I'm fine thanks"
	elif "old" in you:
		robot_brain = "I'm 2 months"
	elif "hello" in you:
		robot_brain = "hello my boss"
	elif "weather" in you:
		city = "Vaasa"+" weather"
		robot_brain = weather(city, robot_brain)
	elif "today" in you:
		robot_brain	= today.strftime("%B %d, %Y")
	elif "time" in you:
		robot_brain = now.strftime("%H:%M:%S")
	elif "president of Finland" in you:
		robot_brain = "Sauli Niinistö"
	elif "prime minister of Finland" in you:
		robot_brain = "Sanna Marin"
	elif "bye" in you:
		robot_brain = "Goodbye"
		print("Robot: " + robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	elif "cool boy" in you:
		robot_brain = "of course that's my boss, Khuyen Vu"
	elif "thank" in you:
		robot_brain = "You're welcome"
		print("Robot: " + robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	else:
		robot_brain	= "I can not hear you, can you ask again ?"
	print("Robot: " + robot_brain)
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()


