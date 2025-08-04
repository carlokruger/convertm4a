import os
import subprocess

INPUT_DIR = "input"
OUTPUT_DIR = "output"

def ensure_directories():
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def convert_m4a_to_wav():
    files_converted = 0
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(".m4a"):
            input_path = os.path.join(INPUT_DIR, filename)
            output_filename = os.path.splitext(filename)[0] + ".wav"
            output_path = os.path.join(OUTPUT_DIR, output_filename)

            command = [
                "ffmpeg",
                "-i", input_path,
                "-ar", "44100",
                "-ac", "2",
                output_path
            ]

            try:
                result = subprocess.run(command, check=True, capture_output=True, text=True)
                print(f"Converted: {filename} → {output_filename}")
                files_converted += 1
            except subprocess.CalledProcessError as e:
                print(f"Error converting {filename}:")
                print(e.stderr)

    if files_converted == 0:
        print("No .m4a files found in the input directory.")

def main():
    ensure_directories()
    convert_m4a_to_wav()

if __name__ == "__main__":
    main()
