import pyaudio
import numpy as np
 
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
 
def get_sound_data():
    p = pyaudio.PyAudio()
    print(p.get_default_output_device_info())
    print(p.get_device_count())
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
 
    audio_data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
    stream.stop_stream()
    stream.close()
    p.terminate()
    return audio_data

def test():
    import pyaudio
    pa = pyaudio.PyAudio()
    pa.get_default_output_device_info()    

print(get_sound_data())
# test()