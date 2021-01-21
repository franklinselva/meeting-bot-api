import os
from sys import argv
from transcriber import transcribe_gcs

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./config/service-client-rk.json"

#Runs transcription for each file inside the specified directory
def auto_run(directory):
    """ Enables the transcribing part from video to text

    Args:
        directory ([string]): [Give the directory of the video file]
    """
    
    files = os.listdir(directory)
    for file in files:
        os.rename(os.path.join(directory, file), os.path.join(directory, file.replace(' ', '_')))#Removes any spaces in the file names

    for file in os.listdir(directory):     # Get each .mp4 file in directory and run transcription
        if file.endswith(".mp4"):
            file_path = os.path.join(directory, file)
            transcribe_gcs(file_path)
            print(file_path)
        else:
            continue

if __name__ == "__main__":
    directory = ""

    try:
        print ("Unknown Directory!!! Getting a default sample video sample...")
        directory = "./data"
    except Exception as e:
        pass
    auto_run(directory)