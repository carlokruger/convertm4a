# convertm4a
a script to convert from m4a format to wav

# Quick setup:

Save it as convert_m4a_to_wav.py.

Install ffmpeg if you don’t already have it:

brew install ffmpeg   # macOS
sudo apt install ffmpeg  # Linux
Run it: python convert_m4a_to_wav.py /path/to/m4a /path/to/wav
It will:
Read every .m4a file in the input folder.
Convert to .wav (44.1 kHz, stereo).
Save to the output folder.


