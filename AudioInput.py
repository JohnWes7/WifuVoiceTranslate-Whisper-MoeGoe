import time
# import numpy as np
import pyaudio
import wave
import input_thread
import speech_2_text_whisper
import text_translate_microsoft
import vits_with_py
import play_audio_2_device
import audioop


VAIO_INPUT_ID = 12
VAIO_OUT_PUT = 3
CHUNK = 1024  # 每个缓冲区的帧数
FORMAT = pyaudio.paInt16  # 采样位数


def main2():
    
    wave_output_file = 'record.wav'
    py_audio = pyaudio.PyAudio()
    mic_info = py_audio.get_device_info_by_index(VAIO_OUT_PUT)
    MIC_CHANNELS = mic_info['maxInputChannels']
    MIC_SAMPLING_RATE = int(mic_info['defaultSampleRate'])

    stream = py_audio.open(format=FORMAT,
                        channels=MIC_CHANNELS,
                        rate=MIC_SAMPLING_RATE,
                        input=True,
                        frames_per_buffer=CHUNK,
                        input_device_index=VAIO_OUT_PUT)



    frames = []  # 音频帧
    keylist = ["", "q"]  # 按键检测
    inp_thr = input_thread.input_thread("inputA", keylist)  # 按键检测线程
    inp_thr.start()  # 开启线程

    wifu_save_path = 'wifu.wav'

    while True:
        is_recording = False
        st_time = time.time()  # 记录开始时间
        while inp_thr.get(keylist[0]) and not inp_thr.get(keylist[1]):
            if is_recording == False:
                is_recording = True
                print("开始录制")

            now_time = time.time()
            print("\r录制中: ", now_time - st_time, "s", end="")
            data = stream.read(CHUNK)
            frames.append(data)

        if is_recording and inp_thr.get(keylist[0]) == False:
            print("\r               ")
            print("录制结束", wave_output_file)
            print("开始储存", wave_output_file)

            wf = wave.open(wave_output_file, 'wb')  # 打开这个文件，以二进制写入的方式
            wf.setnchannels(MIC_CHANNELS)  # 设置单声道
            wf.setsampwidth(py_audio.get_sample_size(FORMAT))  # 设置采样位宽
            wf.setframerate(MIC_SAMPLING_RATE)  # 设置采样率
            wf.writeframes(b''.join(frames))  # 把所有的帧连成一段语音
            wf.close()  # 关闭写入
            frames = []  # 清空给录音
            print("储存完毕: ", wave_output_file)
            print()

            st_time = time.time()
            print("开始转文字:")
            text_zh = speech_2_text_whisper.complex_voice2text(wave_output_file)
            print("语音转文字完成:", text_zh, f'{time.time() - st_time : .2f}')
            print()

            st_time = time.time()
            print("开始翻译为日语")
            text_ja = text_translate_microsoft.zh_translate_2_ja(text_zh)
            print("翻译完毕:", text_ja, f'{time.time() - st_time : .2f}')
            print()

            st_time = time.time()
            print("开始转为老婆语音")
            vits_with_py.MoeGoe_custom_main(text_ja, out_path=wifu_save_path)
            print("转换完毕:", text_ja, f'{time.time() - st_time : .2f}')
            print()

            print("播放")
            play_audio_2_device.play_voice(VAIO_INPUT_ID, wifu_save_path)
            print("播放完毕")

        if inp_thr.get(keylist[1]):
            break

        time.sleep(0.1)

    stream.stop_stream()
    stream.close()
    py_audio.terminate()
    inp_thr.stop()
    print("done")


if __name__ == "__main__":
    main2()
