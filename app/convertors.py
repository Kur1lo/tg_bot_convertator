from moviepy.editor import *
import aspose.words as aw
from gtts import gTTS
from playsound import playsound


def MP4toMP3(mp4, mp3):                                #"/Full/File/Path/ToSong.mp4"
    FILETOCONVERT = AudioFileClip(mp4)
    ready_file = FILETOCONVERT.write_audiofile(mp3)
    FILETOCONVERT.close()
    return ready_file


def Txt_To_Pdf(txt):
    doc = aw.Document(txt)

    return doc.save("txt-to-pdf.pdf", aw.SaveFormat.PDF)


def Txt_To_Docx(txt):
    doc = aw.Document(txt)

    return doc.save("txt-to-pdf.pdf", aw.SaveFormat.DOCX)


def txt_to_mp3(txt_file):
    file = open('txt_file', 'r')

    s = gTTS(file)
    ready_sample = s.save('sample.mp3')
    return ready_sample
