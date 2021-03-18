import pyttsx3
import speech_recognition as sr 
import webbrowser as wb
import datetime
import os

engine = pyttsx3.init()

indo_voice_id = 'indonesian+f3'
rusi_voice_id = 'russian'
itali_voice_id = 'italian'
en_fe_voice_id = 'english+f4'


engine.setProperty('rate', 217) 
engine.setProperty('volume', 0.5)
engine.setProperty('voice', indo_voice_id)

def rec(audio):
	engine.say(audio)
	engine.runAndWait()
	
def runprog():
    	time = int(datetime.datetime.now().hour)
    	if time>=0 and time<12:
        	rec("Selamat Pagi Master!")

    	elif time>=12 and time<18:
        	rec("Selamat Siang Master!")   

    	else:
        	rec("Selamat Malam Master!")  

    	rec("Memulai Program Membutuhkan Beberapa Waktu Hingga Program Berhasil Berjalan Sepenuhnya")   
	
def takeCommand():
    #It takes microphone input from the user and returns string output

	r = sr.Recognizer()
	with sr.Microphone() as source:      
		print("Zero Mendengarkan...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:   
		query = r.recognize_google(audio, language ='id-IDN').lower()
		print(f"Kata Master: {query}\n")

	except Exception as e:
	# print(e)    
		print("Zero Tidak Dapat Mendengarkan Apa Yang Master Katakan Tolong Ulangi Perintah...")  
		return "None"
	return query
if __name__ == "__main__":
	runprog()
	while True:
        	query = takeCommand()
        	# Logic for executing tasks based on query
        	if 'zero' in query :
        		rec('iya master ada yang bisa saya bantu?')
        	elif 'zero matikan komputer' in query or 'matikan komputer' in query :
        		shutdown = 'shutdown -h now' 
        		rec('baik master , proses mematikan komputer dalam 5, 4, 3, 2, 1')
        		os.system(shutdown)
        	elif 'wikipedia' in query :
        		rec('Searching Wikipedia...')
        		query = query.replace("wikipedia", "")
        		results = wikipedia.summary(query, sentences=2)
        		rec("According to Wikipedia")
        		print(results)
        		rec(results)
        	elif 'jam berapa sekarang' in query :
        		strTime = datetime.datetime.now().strftime("%H:%M:%S")
        		rec(f"Master, sekarang jam {strTime}")
        	elif 'open youtube' in query:
        		rec('baik master , membuka youtube')
        		webbrowser.open("youtube.com")
        	elif 'open google' in query:
        		rec('baik master , membuka google')
        		webbrowser.open("google.com")
        	elif 'open stackoverflow' in query:
        		rec('baik master , membuka stackoverflow')
        		webbrowser.open("stackoverflow.com")
        	elif 'zero matikan program' in query or 'matikan program' in query :
        		rec('baik master senang dapat membantu anda, mematikan program dalam 5, 4, 3, 2, 1')
        		break
            	

        	

