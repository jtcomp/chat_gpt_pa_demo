### installing pyaudio
- `brew install portaudio`
- Installing pyaudio can be a pain, you have to manually tell it where `portaudio.h` is - might need to change the paths:
`LDFLAGS="-L/opt/homebrew/Cellar/portaudio/19.7.0/lib" CFLAGS="-I/opt/homebrew/Cellar/portaudio/19.7.0/include" pip install pyaudio`