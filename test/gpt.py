import numpy as np
import wave

# Open the float WAV file
with wave.open('test/wifu_float.wav', 'rb') as wave_file:
    # Get the number of frames and the sample rate
    num_frames = wave_file.getnframes()
    sample_rate = wave_file.getframerate()

    # Read the data from the WAV file as a float array
    wav_data = np.frombuffer(wave_file.readframes(num_frames), dtype=np.float32)

# Convert the float array to int16 format by scaling it to the range [-32767, 32767]
int_data = (wav_data * 32767).astype(np.int16)

# Save the int16 data to a new WAV file
with wave.open('int16_file.wav', 'wb') as wave_file:
    wave_file.setnchannels(1)  # Set the number of channels to 1 (mono)
    wave_file.setsampwidth(2)  # Set the sample width to 2 bytes (16-bit)
    wave_file.setframerate(sample_rate)  # Set the sample rate
    wave_file.writeframes(int_data.tobytes())  # Write the int16 data to the WAV file
