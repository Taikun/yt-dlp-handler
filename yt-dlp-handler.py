import yt_dlp
import os


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
def download(link):
    # get current working directory
    cwd = os.getcwd()

    # Check if music folder exists
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

    stream = os.popen(
        "yt-dlp "
        + " -x -f bestaudio "
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

    # # Get all videos from playlist
    playlist = yt_dlp.YoutubeDL().extract_info(
        "https://www.youtube.com/watch?v=U1NuDWfynbY&list=RDMMU1NuDWfynbY&start_radio=1",
        download=False,
    )["entries"]

    # # Print all videos from playlist
    for video in playlist:
        print(video["title"])
        download(video["webpage_url"])

    # )

    # Convert all files in audio folder to mp3
    stream = os.popen('WebmToMp3.py --webm_path "./audio"')
    output = stream.read()
    print(output)

    # Delete all files in audio folder with extesion webm if there is another file with the same name but with mp3 extension
    for file in os.listdir("./audio"):
        if file.endswith(".webm"):
            if os.path.exists("./audio/" + file.split(".")[0] + ".mp3"):
                os.remove("./audio/" + file)
                print("Removed: " + file)
