#-- Image to movie.
from moviepy.editor import *
from moviepy.video.VideoClip import *
import numpy as np
import numpy.random as rnd

def create_note(freq):
    return lambda t: np.array([
        np.sin(freq * 2 * np.pi * t),
        np.sin(freq * 4 * np.pi * t)
    ]).T.copy(order="C")


text = "what is up you?"

bkg = ColorClip(size=(600,600), color=[0, 0, 0])
bkg = bkg.set_duration(len(text)/4)

clips = [bkg]
audios = []
for i, letter in enumerate(text):
    duration = .25
    fps = 8

    note = rnd.random_sample()*100
    audio_frame = create_note(440 + 20 * i)
    audio = AudioClip(audio_frame, duration=duration, fps=44100)
    audio = audio.set_start(i*duration)
    audios.append(audio)

    txt_clip = TextClip(letter, fontsize=300, color='red')
    txt_clip = txt_clip.set_pos('center').set_fps(fps).set_duration(duration)

    txt_clip = txt_clip.set_start(i*duration)
    clips.append(txt_clip)

final_video = CompositeVideoClip(clips)
final_audios = CompositeAudioClip(audios)
final_video = final_video.set_audio(final_audios)
final_video.write_videofile('my_video.mp4')
