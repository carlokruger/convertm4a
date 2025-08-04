# m4a-to-wav Converter

This is a simple Python + ffmpeg script that converts `.m4a` audio files to `.wav` format.  
It uses fixed directories for input and output:

```
project-root/
├── convert_m4a_to_wav.py  # The conversion script
├── input/                 # Place your .m4a files here
└── output/                # Converted .wav files will appear here
```

---

## Step-by-Step Instructions (Mac & Linux/Ubuntu)

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/m4a-to-wav.git
   cd m4a-to-wav
   ```

2. **Ensure the Input/Output Folders Exist**  
   These should already be in the repo. If not, create them:
   ```bash
   mkdir input output
   ```

3. **Install ffmpeg**

   **macOS (Homebrew)**:
   ```bash
   brew install ffmpeg
   ```

   **Ubuntu/Debian**:
   ```bash
   sudo apt update
   sudo apt install ffmpeg python3
   ```

   **Verify installation**:
   ```bash
   ffmpeg -version
   ```

4. **Place `.m4a` Files in the Input Directory**
   ```
   input/
   ├── track1.m4a
   ├── track2.m4a
   └── podcast.m4a
   ```

5. **Run the Script**
   ```bash
   python3 convert_m4a_to_wav.py
   ```

   The script will:
   - Read all `.m4a` files from the `input/` directory
   - Convert them to `.wav` (44.1 kHz, stereo)
   - Save them in the `output/` directory

6. **Check the Output**
   ```
   output/
   ├── track1.wav
   ├── track2.wav
   └── podcast.wav
   ```

---

## Notes
- The script **only processes `.m4a` files** in the `input/` directory (non-recursive).
- Both `input/` and `output/` directories must exist before running.
- To modify for other formats, update the `.endswith()` filter in the script.

---

