from gtts import gTTS
import playsound
import os

tts = gTTS(text='ষুভো রাত্রি! আমি আপ্নাদের কি ভাবে সাহাজ্জ কোর্তে পারি?', lang='bn')
tts.save("night.mp3")
os.system("mpg321 night.mp3")
playsound.playsound('night.mp3', True)