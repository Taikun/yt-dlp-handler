import yt_dlp
import os
import survey
import subprocess


# Remove local characters from string
def remove_local_characters(string):
    # List of local characters
    local_characters = ["á", "é", "í", "ó", "ö", "ő", "ú", "ü", "ű"]

    # List of characters to replace local characters with
    replace_characters = ["a", "e", "i", "o", "o", "o", "u", "u", "u"]

    # Replace local characters with characters from replace_characters list
    for i in range(len(local_characters)):
        string = string.replace(local_characters[i], replace_characters[i])

    return string


# Dowload video in flac format
def download(link, format):
    # get current working directory
    cwd = os.getcwd()
    print("Exporting as: " + format)
    # Check if audio folder exists
    if not os.path.exists(cwd + "/audio"):
        # Create audio folder
        os.makedirs("audio")

    # Download video
    # Check if video already exists in audio folder with any extension
    if os.path.exists(
        cwd + "/audio/" + remove_local_characters(get_title(link)) + ".*"
    ):
        print("File already exists")
        return
    # Check with yt-dlp -F command if format is available
    stream = os.popen("yt-dlp -F " + link)
    output = stream.read()
    # Check if format is available
    if format not in output:
        print("Format not available")
        format = "bestaudio"

    stream = os.popen(
        "yt-dlp "
        + " -x -f "
        + format
        + " "
        + link
        + " -o "
        + "audio/"
        + remove_local_characters("%(title)s")
        + ".%(ext)s"
    )
    output = stream.read()
    print(output)


# Get title of video from youtube link
def get_title(link):
    with yt_dlp.YoutubeDL() as ydl:
        info = ydl.extract_info(link, download=False, process=False)
        title = info["title"]
        # Print a text and the title of the video
        print("Downloading: " + title)

        remove_local_characters(title)

        return title


def get_playlist(link):
    with yt_dlp.YoutubeDL() as ydl:
        info = ydl.extract_info(link, download=False, process=False)
        title = info["title"]
        # Print a text and the title of the video
        print("Downloading: " + title)
        link = info["webpage_url"]
        # download(link)
        # download(ydl.extract_info(link, download=False, process=False)["webpage_url"])

        return title


if __name__ == "__main__":
    # link = input("Enter youtube link: ")
    # link = "https://youtu.be/U1NuDWfynbY"
    # print(get_title(link))
    # download(link)
    # # print(
    # get_playlist(
    #     "https://www.youtube.com/watch?v=U1NuDWfynbY&list=RDMMU1NuDWfynbY&start_radio=1"
    # )

    inputType = ("list", "individual")
    inputTypeIndex = survey.routines.select("List or individual?: ", options=inputType)
    print(f"Answered {inputTypeIndex}.")

    link = survey.routines.input("link? ")
    print(f"Answered {link}.")

    formatIndex = 0
    format = ("bestaudio", "flac", "mp3", "aac", "m4a", "opus", "vorbis", "wav")
    formatIndex = survey.routines.select("List or individual?: ", options=format)
    print(f"Answered {formatIndex}.")

    if inputTypeIndex == 0:
        # Get all videos from playlist
        playlist = yt_dlp.YoutubeDL().extract_info(
            link,
            download=False,
        )
        if playlist is not None:
            for video in playlist.get("entries", []):
                print(video["title"])
                download(video["webpage_url"], format[formatIndex])
        else:
            print("Invalid playlist link")
    else:
        import yt_dlp
        import os
        import survey


        # Remove local characters from string
        def remove_local_characters(string):
            # List of local characters
            pass


        # Dowload video in flac format
        def download(link, format):
            # get current working directory
            pass


        # Get title of video from youtube link
        def get_title(link):
            pass


        def get_playlist(link):
            with yt_dlp.YoutubeDL() as ydl:
                info = ydl.extract_info(link, download=False, process=False)
                title = info["title"]
                # Print a text and the title of the video
                print("Downloading: " + title)
                link = info["webpage_url"]
                # download(link)
                # download(ydl.extract_info(link, download=False, process=False)["webpage_url"])

                return title


        if __name__ == "__main__":
            # link = input("Enter youtube link: ")
            # link = "https://youtu.be/U1NuDWfynbY"
            # print(get_title(link))
            # download(link)
            # # print(
            # get_playlist(
            #     "https://www.youtube.com/watch?v=U1NuDWfynbY&list=RDMMU1NuDWfynbY&start_radio=1"
            # )

            inputType = ("list", "individual")
            inputTypeIndex = survey.routines.select("List or individual?: ", options=inputType)
            print(f"Answered {inputTypeIndex}.")

            link = survey.routines.input("link? ")
            print(f"Answered {link}.")

            format = ("bestaudio", "flac", "mp3", "aac", "m4a", "opus", "vorbis", "wav", default="bestaudio")
            formatIndex = survey.routines.select("List or individual?: ", options=format)
            print(f"Answered {formatIndex}.")

            if inputTypeIndex == 0:
                # Get all videos from playlist
                playlist = yt_dlp.YoutubeDL().extract_info(
                    link,
                    download=False,
                )
                if playlist is not None:
                    for video in playlist.get("entries", []):
                        print(video["title"])
                        download(video["webpage_url"], format[formatIndex])
                else:
                    print("Invalid playlist link")
            else:
                download(link, format[formatIndex])


    convertToMP3 = survey.routines.inquire("Convert to MP3? ", default=True)
    print(f"Answered {convertToMP3}.")
    if convertToMP3:
        # Convert all files in audio folder to mp3
        # stream = os.popen('WebmToMp3.py --webm_path "./audio"')
        # output = stream.read()
        # print(output)
        
        # Convert all opus or webm files to mp3
         

        # Delete all files in audio folder with extesion webm if there is another file with the same name but with mp3 extension
        for file in os.listdir("./audio"):
            if file.endswith(".webm") or file.endswith(".opus"):
                webmFile = "./audio/" + file
                mp3File = "./audio/" + file.split(".")[0] + ".mp3"
                command = f'ffmpeg -i "{webmFile}" -vn -ab 128k -ar 44100 -y "{mp3File}"'
                subprocess.call(command, shell=True)
                if os.path.exists("./audio/" + file.split(".")[0] + ".mp3"):
                    os.remove("./audio/" + file)
                    print("Removed: " + file)

