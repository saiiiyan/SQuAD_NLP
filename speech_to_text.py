import speech_recognition as sr  
 
# get audio from the microphone
def recog():
	r = sr.Recognizer()
	with sr.Microphone() as source:                                                                       
		print("Speak:")                                                                                   
   		audio = r.listen(source)    
	try:
		text = r.recognize_google(audio)
	except sr.UnknownValueError:
		print("Could not understand audio")
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
	return text
