import gtts
text = input()
voice = gtts.gTTS(text, lang="en", slow=False)
voice.save("assignment9\Voice.mp3")