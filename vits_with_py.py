import sys
sys.path.append("MoeGoe")
import MoeGoe.MoeGoe

# TODO: 改相对路径
model_path = "./vits/model/G_latest.pth"
config_path = "./vits/model/config.json"

tts_or_vc = "t"
test_text = "おやすみなさいです"
speaker_id = '1'
save_path = "E:/FOO/wifu.wav"
continue_cmd = "n"
MoeGoe.MoeGoe.start(model_path=model_path, config_path=config_path)


def MoeGoe_custom_main(text, speaker_id=0, out_path=save_path):
    text = '[JA]'+text+'[JA]'
    MoeGoe.MoeGoe.custom_main(
        text=text, speaker_id=speaker_id, out_path=out_path)


if __name__ == "__main__":
    MoeGoe_custom_main(test_text)
    pass
