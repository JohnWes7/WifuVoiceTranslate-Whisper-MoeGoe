import speech_recognition as sr
import json

if __name__ == '__main__':
    mic_dict = {}
    for mic_id, mic_name in enumerate(sr.Microphone.list_microphone_names()):
        mic_dict[mic_id] = mic_name
        print(f'{mic_id}: {mic_name}')

    
    with open('mic_devices.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(mic_dict, ensure_ascii=False))
        
    