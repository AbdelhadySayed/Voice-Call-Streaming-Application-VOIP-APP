import sounddevice as sd
import scipy.io.wavfile as wav
from playsound import playsound

def record_audio_from_mic(output_file, duration=30):
    """
    Records audio from the microphone and saves it to a file.
    :param output_file: Path to save the recording (e.g., "recording.wav")
    :param duration: Duration of the recording in seconds (default: 60 seconds)
    :return: Path to the saved recording if successful, None otherwise
    """
    try:
        print("Recording... Speak into your microphone.")
        fs = 44100  # Sample rate
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype="int16")
        sd.wait()  # Wait until the recording is finished
        wav.write(output_file, fs, recording)  # Save the recording as a WAV file
        print(f"Recording saved to {output_file}")
        return output_file
    except Exception as e:
        print(f"Error recording audio: {e}")
        return None

def play_recording(file_path):
    """
    Plays the recorded audio file locally.
    :param file_path: Path to the audio file (e.g., "recording.mp3")
    """
    try:
        # Play the audio file
        playsound(file_path)
        print(f"Played recording: {file_path}")
    except Exception as e:
        print(f"Error playing recording: {e}")