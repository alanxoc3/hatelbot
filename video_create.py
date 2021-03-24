#-- Image to movie.
from moviepy.editor import *
from moviepy.video.VideoClip import *
import numpy as np
import numpy.random as rnd
import hatel

def create_note(freq):
    return lambda t: np.array([
        np.sin(freq * 1 * np.pi * t),
        np.sin(freq * 2 * np.pi * t)
    ]).T.copy(order="C")

def normalize_string(s):
    s = s.lower()
    s = ''.join(filter(lambda c: c in hatel.layout, s))
    s = " ".join(s.strip().split())
    return s + " "

def create_video(output_filename, text):
    text = normalize_string(text)

    bkg = ColorClip(size=(600,600), color=[0, 0, 0])
    bkg = bkg.set_duration(len(text)/4 + .5)

    clips = [bkg]
    audios = []
    for i, letter in enumerate(text):
        duration = .25
        fps = 8

        for freq in hatel.layout[letter]:
            audio = AudioClip(create_note(freq), duration=duration, fps=44100)
            audio = afx.audio_fadeout(audio, duration)
            audio = audio.set_start(i*duration)
            audios.append(audio)

        txt_clip = TextClip(letter, fontsize=300, color='red')
        txt_clip = txt_clip.set_pos('center').set_fps(fps).set_duration(duration)

        txt_clip = txt_clip.set_start(i*duration)
        clips.append(txt_clip)

    final_video = CompositeVideoClip(clips)
    final_audios = CompositeAudioClip(audios)
    final_video = final_video.set_audio(final_audios)
    final_video.write_videofile(output_filename, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
