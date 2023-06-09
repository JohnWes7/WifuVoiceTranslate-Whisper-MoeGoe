import subprocess
import os

model_path = "E:/FOO/vits/model/G_latest.pth"
config_path = "E:/FOO/vits/model/config.json"

tts_or_vc = "t"
test_text = "[JA]おやすみなさいです[JA]"
speaker_id = '1'
save_path = "E:/FOO/wifu.wav"
continue_cmd = "n"

command_open_vits = "vits\\MoeGoe\\MoeGoe.exe"
test_command = 'python testcmd.py'


def main():
    # print("执行 vits\\MoeGoe\\MoeGoe.exe")
    with os.popen(command_open_vits, 'w') as popen:
        popen.write(model_path + "\n")
        popen.write(config_path + "\n")
        popen.write(tts_or_vc + "\n")
        popen.write(test_text + "\n")
        popen.write(speaker_id + "\n")
        popen.write(save_path + "\n")
        popen.write(continue_cmd + "\n")


def testmain():
    popen = subprocess.Popen(
        [test_command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


if __name__ == "__main__":
    main()
