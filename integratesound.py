
import os
import wave


def Integrate(output_dir=None, outname=None):
    print("All pieces generated.")
    print("integrate all pieces into one file")
    # integrate all pieces into one file
    # 读取bark_samples文件夹下的所有wav文件
    wav_files = []
    # 先对那里面的所有文件进行按时间先后排序
    for root, dirs, files in os.walk(output_dir):
        for file in files:
            if file.endswith('.wav'):
                # 先
                wav_files.append(os.path.join(root, file))
    wav_files.sort(key=lambda x: os.path.getmtime(x))

    # 读取每个wav文件的音频数据
    audio_data = []
    for wav_file in wav_files:
        audio_data.append(wave.open(wav_file, 'rb'))
    # 创建一个新的音频文件
    new_wav = wave.open(outname, 'wb')
    # 配置声道数、量化位数和采样频率
    new_wav.setnchannels(1)
    new_wav.setsampwidth(audio_data[0].getsampwidth())
    new_wav.setframerate(audio_data[0].getframerate())
    # 遍历每个音频文件，读取音频数据并写入新文件
    for i in range(len(audio_data)):
        new_wav.writeframes(audio_data[i].readframes(audio_data[i].getnframes()))
    # 关闭文件
    new_wav.close()
    for i in range(len(audio_data)):
        audio_data[i].close()
    print("integrate all pieces into one file done")

    print("All pieces integrated into one file.")
    print("All done.")


if __name__ == "__main__":
    Integrate(output_dir="./bark_samples/The expression", outname="dilemma2.wav")
