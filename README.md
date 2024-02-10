# FastSpeech 2 - PyTorch Implementation

This is a PyTorch implementation of Microsoft's text-to-speech system [**FastSpeech 2: Fast and High-Quality End-to-End Text to Speech**](https://arxiv.org/abs/2006.04558v1). 
This project is based on [xcmyz's implementation](https://github.com/xcmyz/FastSpeech) of FastSpeech.

## Dependencies
You can install the Python dependencies with
```
python -m venv <virtual-environment-name>
source env/bin/activate
pip3 install -r requirements.txt
```
Install Auto Subtitle
```
pip install git+https://github.com/YJ-20/auto-subtitle-llama
```

## TTS Model
You have to download the [pretrained model](https://drive.google.com/drive/folders/1DOhZGlTLMbbAAFZmZGDdc77kz1PloS7F?usp=sharing) LibriTTS and put it in ``output/ckpt/LibriTTS/``.
Then rename the file to ``800000.pth.tar``