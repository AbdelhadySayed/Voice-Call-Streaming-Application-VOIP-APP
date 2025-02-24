import os
from datetime import datetime

def create_call_folder(phone_number):
    """
    Creates a folder to store call recordings and text files for the day.
    :param phone_number: The phone number that was called
    :return: Path to the created folder
    """
    try:
        # Create a folder with the phone number and date
        timestamp = datetime.now().strftime("%Y%m%d")
        folder_name = f"calls_{phone_number}_{timestamp}"
        os.makedirs(folder_name, exist_ok=True)
        print(f"Created folder: {folder_name}")
        return folder_name
    except Exception as e:
        print(f"Error creating folder: {e}")
        return None

def save_text_message(folder_path, phone_number, message, recording_file=None, recording_status=None):
    """
    Saves the phone number and sent message in a text file.
    :param folder_path: Path to the folder where the text file will be saved
    :param phone_number: The phone number that was called
    :param message: The message that was sent (optional)
    :param recording_file: Path to the recording file (optional)
    :param recording_status: Status of the recording (optional)
    :return: Path to the saved text file if successful, None otherwise
    """
    try:
        # Create or append to the text file
        text_file_path = os.path.join(folder_path, f"messages_{phone_number}.txt")
        with open(text_file_path, "a") as f:
            f.write(f"Phone Number: {phone_number}\n")
            f.write(f"Message: {message}\n")
            if recording_file:
                f.write(f"Recording: {recording_file}\n")
            if recording_status:
                f.write(f"Recording Status: {recording_status}\n")
            f.write("\n")  # Add a separator between entries
        print(f"Text message saved to {text_file_path}")
        return text_file_path
    except Exception as e:
        print(f"Error saving text message: {e}")
        return None