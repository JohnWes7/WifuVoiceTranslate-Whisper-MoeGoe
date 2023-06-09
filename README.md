# WifuVoiceTranslate-Whisper-MoeGoe

中文语言说话转老婆说话并输出到虚拟麦克风折磨队友

具体实现:

1 使用whisper 进行中文语音转中字

2 使用微软翻译api中字到日字

3 使用moegoe日字到日音再输出到虚拟麦

moegoe模型放在vits/model下面
更名为G_lastest.pth和config.json
确保有vites/model/G_lastest.pth和vites/model/config.json