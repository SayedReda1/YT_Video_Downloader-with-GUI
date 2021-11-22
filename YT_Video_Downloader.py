from pytube import YouTube
import os
import time

# the input data
type = input("Video or Audio: ").strip().lower()
url = input("Enter Video URL: ")
resolution = input("Enter the resolution: ")
path = input("Enter file path to download: ")
abs_path = os.path.abspath(path)        # transfer the input path to abs path

# calling the module
vid = YouTube(url)
try:
    # execute the itag for the selected resolution
    itag = []
    if type == "video":
        for str in vid.streams.filter(res=resolution, subtype="mp4"):
            itag.append(str.itag)

    elif type == "audio":
        for str in vid.streams.filter(type="audio"):
            itag.append(str.itag)

    else:
        print("Unknown type")
    
    # downloading the vid
    stream = vid.streams.get_by_itag(itag[0])
    stream.download(output_path=abs_path)
    # print a message notifies that the download is complete
    def finish():
        print("Download Complete")
    vid.register_on_complete_callback(finish())

except:
    print("Wrong input, please try again")
finally:
    print("Window will close after....")
    time.sleep(1)
    for s in range(1,4):
        print(s)
        time.sleep(1)



