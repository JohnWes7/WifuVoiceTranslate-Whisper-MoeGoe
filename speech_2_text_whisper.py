import whisper
import time

model = whisper.load_model("small")
test_audio = 'record.wav'


# def voice2text_with_timer(path) -> str:
#     global model
#     st = time.time()
#     print("开始转换语音到文字")
#     result = model.transcribe(path)
    
#     end = time.time()
#     print("转换完毕", end - st, result["text"])

#     return result["text"]

# def simple_voice2text(path) -> str:
#     global model

#     result = model.transcribe(path)
#     return result["text"]

def complex_voice2text(path) -> str:
    global model

    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(path)
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # decode the audio
    options = whisper.DecodingOptions(language='Chinese')
    result = whisper.decode(model, mel, options)

    # print the recognized text
    # print(result.text)
    return result.text

if __name__ == "__main__":
    print(complex_voice2text(test_audio))
