import os
import subprocess

for file in os.listdir("./audio"):
    if file.endswith(".webm") or file.endswith(".opus"):
        webmFile = "./audio/" + file
        mp3File = "./audio/" + file.split(".")[0] + ".mp3"
        command = f'ffmpeg -i "{webmFile}" -vn -ab 128k -ar 44100 -y "{mp3File}"'
        subprocess.call(command, shell=True)
        
        if os.path.exists("./audio/" + file.split(".")[0] + ".mp3"):
            os.remove("./audio/" + file)
            print("Removed: " + file)