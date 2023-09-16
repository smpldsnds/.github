import glob
import os


def convert_audio_files(folder_path, destructive):
    print(f"Converting audio files in {folder_path}...")
    # Find all .flac and .wav files
    flac_files = glob.glob(os.path.join(
        folder_path, '**', '*.flac'), recursive=True)
    wav_files = glob.glob(os.path.join(
        folder_path, '**', '*.wav'), recursive=True)

    for file_path in flac_files + wav_files:
        # Convert to .ogg (opus codec)
        file_name = file_path.rsplit('.', 1)[0]
        print(f"Converting {file_path} ({file_name})")

        if destructive:
            os.system(
                f"ffmpeg -i \"{file_path}\" -c:a libopus \"{file_name}.ogg\"")
            os.system(
                f"ffmpeg -i \"{file_path}\" -c:a aac \"{file_name}.m4a\"")
            os.remove(file_path)

    print(f"Done audio file conversion")
