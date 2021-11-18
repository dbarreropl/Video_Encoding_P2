# from rgb_yuv import rgb_to_yuv
import os

# f5 to run
if __name__ == '__main__':

    option=0
while not option==5:

    print("1. Cut video")
    print("2. Extract YUV histogram")
    print("3. Resize Video")
    print("4. Audio into Mono and change Codec")
    print("5. Exit")
    option = int(input("Option: "))

    if option == 1:
        print("#Cut video")
        start = int(input("Start: "))
        end = int(input("End: "))
        os.system('ffmpeg -i video.mp4 -ss 00:00:'+str(start)+'.0 -t 00:00:' +
                str(end-start)+'.0 video_cut.mp4')

    if option == 2:
        print("#Extract YUV histogram")
        os.system('ffmpeg -y -report -i video_cut.mp4 -vf "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay" video_cut_histo.mp4')

    if option == 3:
        print("#Resize Video")
        resolution = int(input("1-720p, 2-480p, 3-360x240p, 4-160x120p: "))
        if resolution==1:
            os.system('ffmpeg -i video_cut.mp4 -vf scale=-1:720 -preset slow -crf 18 video_720.mp4')
        elif resolution==2:
            os.system('ffmpeg -i video_cut.mp4 -vf scale=480:-1 -preset slow -crf 18 video_480.mp4')
        elif resolution==3:
            os.system('ffmpeg -i video_cut.mp4 -vf scale=360:240 -preset slow -crf 18 video_360x240.mp4')
        elif resolution==4:
            os.system('ffmpeg -i video_cut.mp4 -vf scale=160:120 -preset slow -crf 18 video_160x120.mp4')

    if option == 4:
        print("#Audio into Mono and change Codec")
        os.system('ffmpeg -i video_cut.mp4')
        codec = raw_input("Audio codec: ")
        os.system('ffmpeg -i video_cut.mp4 -ac 1 -vcodec copy -acodec ' +codec +' video_mono_'+codec+'.mp4')
        os.system('ffmpeg -i video_mono_'+codec+'.mp4')
        #ffmpeg -codecs
