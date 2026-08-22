import torch, torchaudio
print(torch.__version__, torchaudio.__version__)
wav, sr = torchaudio.load(r"dataset_ex3\music_wav\SOME_FILE.wav")  # pick any real file from your dataset
print(wav.shape, sr)