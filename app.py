import speech_recognition as sr
import moviepy.editor as mp
from pydub import AudioSegment
from pydub.utils import make_chunks
import os


# Video to Audio
clip = mp.VideoFileClip(r"test.mp4")
clip.audio.write_audiofile(r"testMp3.wav")


# Audio to text
def process_audio(filename):
    txtf = open("output.txt", "w+")
    myaudio = AudioSegment.from_wav(filename)
    chunks_length_ms = 8000
    chunks = make_chunks(myaudio, chunks_length_ms)
    for i, chunk in enumerate(chunks):
        chunkName = './chunked/'+filename+"_{0}.wav".format(i)
        print("I am exporting", chunkName)
        chunk.export(chunkName, format="wav")
        file = chunkName
        r = sr.Recognizer()
        with sr.AudioFile(file) as source:
            audio_listened = r.listen(source)
        try:
            rec = r.recognize_google(audio_listened)
            txtf.write(rec+".")
        except sr.UnknownValueError:
            print("I don't recognize your audio")
        except sr.RequestError as e:
            print("could not get the result, check your internet")


try:
    os.makedirs("chunked")
except:
    pass
    process_audio("testMp3.wav")
