# m4a-to-wav Converter Script - Version 1.0

import os
import subprocess
import argparse

def convert_m4a_to_wav(verbose=False):
    input_dir = "input"
    output_dir = "output"

    # Create directories if they don't exist
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    # List all .m4a files in the input directory
    files = [f for f in os.listdir(input_dir) if f.lower().endswith(".m4a")]

    if not files:
        print("No .m4a files found in the input directory.")
        return

    converted_count = 0

    for file in files:
        input_path = os.path.join(input_dir, file)
        output_file = os.path.splitext(file)[0] + ".wav"
        output_path = os.path.join(output_dir, output_file)

        command = [
            "ffmpeg",
            "-i", input_path,
            "-ar", "44100",  # Set sample rate
            "-ac", "2",      # Stereo
            output_path,
            "-y"  # Overwrite output files without asking
        ]

        try:
            if verbose:
                # Show ffmpeg output in real time
                subprocess.run(command, check=True)
            else:
                # Suppress ffmpeg output but capture errors
                subprocess.run(command, check=True, capture_output=True, text=True)
            converted_count += 1
            print(f"Converted: {file} -> {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {file}: {e}")
            if not verbose:
                print(e.stderr)

    print(f"\n✅ Conversion complete. {converted_count} file(s) converted.")

def main():
    parser = argparse.ArgumentParser(description="Convert .m4a files to .wav format")
    parser.add_argument("--verbose", action="store_true", help="Show ffmpeg output while converting")
    args = parser.parse_args()

    convert_m4a_to_wav(verbose=args.verbose)

if __name__ == "__main__":
    main()