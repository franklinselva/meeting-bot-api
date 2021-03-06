import os
import signal
import subprocess
import sys
import time
import tkinter as tk
import wave
from signal import SIGINT

import cv2
import ffmpeg
import numpy as np
import pyaudio
import pyautogui
from PIL import ImageGrab


def locateAndClick(imgUrl, delay=0):

    loc = pyautogui.locateCenterOnScreen(imgUrl)

    if delay > 0:
        time.sleep(delay)

    pyautogui.click(loc)


def startRecordScreenProcess(outFileName, width, height):

    pid = os.fork()

    if pid == 0:
        stop = False

        def sigHandler(signal, frame):
            stop = True

        signal.signal(SIGINT, sigHandler)

        fourcc = cv2.VideoWriter_fourcc(*'MP4V')

        vid = cv2.VideoWriter(outFileName, fourcc, 30, (width, height))

        while not stop:
            img = ImageGrab.grab(bbox=(0, 0, width, height))
            frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

            vid.write(frame)

        vid.release()
        sys.exit(0)
    else:
        return pid


def startRecordAudioProcess(outFileName):

    pid = os.fork()

    if pid == 0:

        stop = False

        def sigHandler(signal, frame):
            nonlocal stop
            stop = True

        signal.signal(SIGINT, sigHandler)

        p = pyaudio.PyAudio()

        systemSoundIndex = None

        for i in range(p.get_device_count()):

            device = p.get_device_info_by_index(i)

            if device["name"] == "pulse":
                systemSoundIndex = i
                break

        stream = p.open(format=pyaudio.paInt16, channels=2, rate=44100, input=True,
                        frames_per_buffer=1024, input_device_index=systemSoundIndex)

        waveFile = wave.open(outFileName, 'wb')

        waveFile.setnchannels(2)
        waveFile.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        waveFile.setframerate(44100)

        while not stop:
            data = stream.read(1024)
            waveFile.writeframes(data)

        waveFile.close()
        sys.exit(0)
    else:
        return pid


def zoomBot(basepath, meetingid, meetingpasscode, duration, filename):

    sub = subprocess.Popen("zoom")

    time.sleep(4)
    locateAndClick(basepath + "icons/meeting_join.png", 1)
    pyautogui.click()
    locateAndClick(basepath + "icons/meeting_id_input.png", 1)
    pyautogui.write(meetingid)
    locateAndClick(basepath + "icons/meeting_id_join.png")
    locateAndClick(basepath + "icons/meeting_password_input.png", 1)
    pyautogui.write(meetingpasscode)
    locateAndClick(basepath + "icons/meeting_password_join.png")

    win = tk.Tk()

    screenPid = startRecordScreenProcess(
        "out.mp4", win.winfo_screenwidth(), win.winfo_screenheight())
    audioPid = startRecordAudioProcess("out.wav")

    time.sleep(int(duration * 60))

    os.kill(screenPid, SIGINT)
    os.kill(audioPid, SIGINT)
    try:
        os.waitpid(screenPid, os.WEXITED)
        os.waitpid(audioPid, os.WEXITED)
    except:
        pass

    video = ffmpeg.input('out.mp4')
    audio = ffmpeg.input('out.wav')
    try:
        os.remove(filename)
    except:
        pass

    out = ffmpeg.output(video, audio, filename, vcodec='copy',
                        acodec='aac', strict='experimental')
    out.run()

    os.remove("out.mp4")
    os.remove("out.wav")

    return


if __name__ == "__main__":

    win = tk.Tk()
    basepath = "/".join(sys.argv[0].split('/')[:-1])

    if len(basepath) != 0:
        basepath += "/"

    print(basepath)

    zoomBot(basepath, 6390672848, '2p5kg8', 2, 'test_sample')