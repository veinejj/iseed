from datetime import datetime
from gtts import gTTS
import playsound

news = "[안녕하세요. 저는 장지아입니다.]"
tts = gTTS(text=news, lang='ko')
tts.save("name_jang.mp3")
playsound.playsound("name_jang.mp3",True)
