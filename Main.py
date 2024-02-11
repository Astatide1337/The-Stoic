from TTS import generateAudio
import os
import random
import ffmpeg
import subprocess

music = os.listdir('./Music')[random.randint(0, len(os.listdir('./Music'))-1)]
backgroundVideo = os.listdir('./Background')[random.randint(0, len(os.listdir('./Background'))-1)]

generateAudio()
# audio = os.listdir("./GeneratedTTS")
# audio = max(audio, key=lambda x: os.path.getctime(os.path.join("./GeneratedTTS", x)))

# audioDuration = float(ffmpeg.probe(f'./GeneratedTTS/{audio}')['streams'][0]['duration'])
# videoDuration = float(ffmpeg.probe(f'./Background/{backgroundVideo}')['streams'][0]['duration'])

# concatBackgroundVideo = []
# while audioDuration > videoDuration:
#     backgroundVideo = os.listdir('./Background')[random.randint(0, len(os.listdir('./Background'))-1)]
#     print("Selected background: ", backgroundVideo)
#     for video in concatBackgroundVideo:
#         videoDuration += float(ffmpeg.probe(video)['streams'][0]['duration'])
#     concatBackgroundVideo.append(f'./Background/{backgroundVideo}')

# if concatBackgroundVideo == []:
#     concatBackgroundVideo.append(f'./Background/{backgroundVideo}')

    

# #resize the videos in the list so that they are the same dimensions
# # for video in concatBackgroundVideo:
# #     ffmpeg.input(video).output('../Temp/'+video.split('/')[-1], s='1080x1920').run()



# inputs = []
# filter_complex = "concat=n={}:v=1:a=0[out]".format(len(concatBackgroundVideo))
# for i, video in enumerate(concatBackgroundVideo):
#     inputs.extend(["-i", video])
#     filter_complex = "[{}:v]".format(i) + filter_complex
# concatenateCMD = [
#     "ffmpeg",
#     "-y",
#     *inputs,
#     "-filter_complex",
#     filter_complex,
#     "-map",
#     "[out]",
#     "./Temp/concatenatedVideo.mp4",
# ]
# subprocess.run(concatenateCMD)


# combineMusicAndAudio = (
#     f"ffmpeg -y -i ./GeneratedTTS/{audio} -i ./Music/{music} "
#     "-filter_complex [0:a]volume=1.5[a1];[1:a]volume=0.5[a2];[a1][a2]amix=inputs=2:duration=first "
#     "./Temp/finalAudio.mp3"
# )
# subprocess.run(combineMusicAndAudio, shell=True)


# #check if srt file exists
# if not os.path.exists('./Temp/finalAudio.srt'):
#     try:
#         subprocess.run(
#                 ["auto_subtitle_llama", "./Temp/finalAudio.mp3", "-o", "./Temp/"]
#             )
#     except:
#         print("Error generating subtitles on video")
# else:
#     os.remove('./Temp/finalAudio.srt')
#     try:
#         subprocess.run(
#                 ["auto_subtitle_llama", "./Temp/finalAudio.mp3", "-o", "./Temp/"]
#             )
#     except:
#         print("Error generating subtitles on video")


# createVideoCMD = (
#     "ffmpeg -y -i ./Temp/concatenatedVideo.mp4 -i ./Temp/finalAudio.mp3 "
#     "-vf \"subtitles=./Temp/finalAudio.srt:force_style='Alignment=10,Fontsize=20,Fontname=Gabriola,Shadow=1,PrimaryColour=&Hffffff&',"
#     "eq=brightness=-0.01\" "
#     f"-map 0:v -map 1:a -shortest -b:v 2000k -preset slow -crf 18 ./Videos/{audio}.mp4"
# )
# subprocess.run(createVideoCMD, shell=True)

# #remove temp files
# try:
#     os.remove('./Temp/concatenatedVideo.mp4')
#     os.remove('./Temp/finalAudio.mp3')
#     os.remove('./Temp/finalAudio.srt')
#     os.remove(f'./GeneratedTTS/{audio}')
# except:
#     print("Error removing temp files")