# m4a-to-wav Converter

This is a simple Python + ffmpeg script that converts `.m4a` audio files to `.wav` format.  
It automatically ensures the necessary `input` and `output` directories exist.

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

2. **Install ffmpeg**

   **macOS (Homebrew)**:
   ```bash
   brew install ffmpeg
   ```

   **Ubuntu/Debian**:
   ```bash
   sudo apt update
   sudo apt install ffmpeg python3 python3-venv
   ```

   **Verify installation**:
   ```bash
   ffmpeg -version
   ```

3. **Create and Activate a Python Virtual Environment**
   ```bash
   python3 -m venv m4a-to-wav
   source m4a-to-wav/bin/activate
   ```

4. **Place `.m4a` Files in the Input Directory**  
   You do **not** need to create the `input` or `output` directories manually — the script will create them if missing.  
   Example:
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
   - Ensure `input/` and `output/` directories exist (create them if missing)
   - Read all `.m4a` files from the `input/` directory
   - Convert them to `.wav` (44.1 kHz, stereo)
   - Save them in the `output/` directory
   - Print a summary of how many files were converted

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
- Both `input/` and `output/` directories will be auto-created if they do not exist.
- To modify for other formats, update the `.endswith()` filter in the script.

---

## License
This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.  
You are free to use, modify, and share the code under the terms of the GPL-3.0 license.  
See the [LICENSE](https://www.gnu.org/licenses/gpl-3.0.en.html) file for details.
