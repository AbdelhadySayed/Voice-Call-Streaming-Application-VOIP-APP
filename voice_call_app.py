import argparse
import shutil
import os
from datetime import datetime
from constants import DEFAULT_MESSAGE
from twilio_client import make_call, save_recording
from file_utils import create_call_folder, save_text_message
from audio_utils import record_audio_from_mic, play_recording

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Voice Call Streaming Application")
    parser.add_argument("-n", "--number", required=True, help="Phone number to call (e.g., +15551234567)")
    parser.add_argument("-m", "--message", help="Optional message to play (string or audio file URL)")
    parser.add_argument("-r", "--record", action="store_true", help="Record a new message")
    parser.add_argument("--play", help="Play the specified .mp3 file or recorded file")
    args = parser.parse_args()

    # Use the provided message or the hardcoded default message
    message = args.message if args.message else DEFAULT_MESSAGE

    # Create a folder for this call
    folder_path = create_call_folder(args.number)
    if not folder_path:
        print("Failed to create folder. Exiting.")
        return

    # If -r is provided, record a new message
    if args.record:
        print("Please record your message. You have 30 seconds to record.") # change the time if you want to record more
        recording_file = os.path.join(folder_path, f"recording_{datetime.now().strftime('%H%M%S')}.wav")
        if record_audio_from_mic(recording_file, duration=60):
            # Save the text message and recording file path
            save_text_message(folder_path, args.number, message, recording_file)
            print("The recorded message has been saved successfully")
        else:
            # Save the text message with recording status
            save_text_message(folder_path, args.number, message, recording_status="No recording provided or you didn't enable the recording.")
        return

    # If --play is provided, play the specified .mp3 file or recorded file
    if args.play:
        # Check if the provided file exists
        if os.path.exists(args.play):
            play_recording(args.play)
        else:
            print(f"File not found: {args.play}")
        return

    # Make the call and save the default message
    call_sid = make_call(args.number, message)
    if call_sid:
        print("Call was initiated successfully.")
        # Save the text message
        save_text_message(folder_path, args.number, message)
        print("The sent message is: ", message)
    else:
        print("Failed to initiate the call.")

if __name__ == "__main__":
    main()