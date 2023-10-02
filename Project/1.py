import librosa   
y, s = librosa.load('./left_nvt.wav', sr=16000) 

print(y.shape)