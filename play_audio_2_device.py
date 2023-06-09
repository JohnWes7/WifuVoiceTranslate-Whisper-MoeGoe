import wave
import pyaudio
import sounddevice as sd
import soundfile as sf


def play_voice(device_id, path):
    data, fs = sf.read(path, dtype='int16')

    sd.play(data, fs, device=device_id)
    sd.wait()



# def play_audio(path):

#     CHUNK = 1024
#     wf = wave.open(path, 'rb')
#     p = pyaudio.PyAudio()

#     stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                     channels=wf.getnchannels(),
#                     rate=wf.getframerate(),
#                     output=True)

#     data = wf.readframes(CHUNK)

#     while data != b"":
#         stream.write(data)
#         data = wf.readframes(CHUNK)

#     stream.stop_stream()
#     stream.close()
#     p.terminate()

if __name__ == '__main__':
    path1 = 'wifu.wav'
    path2 = 'record.wav'
    device = 12
    
    # play_audio(path1)

    play_voice(device, path1)