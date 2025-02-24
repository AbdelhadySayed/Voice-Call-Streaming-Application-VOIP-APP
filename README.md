# Voice Call Streaming Application (VOIP APP)

This is a Python application that establishes a **dynamic voice call** using Twilio's API. The application allows for **two-way communication** It also supports recording messages, saving them locally.

---

## **Table of Contents**
1. [Features](#features)
2. [Why Use Twilio?](#why-use-twilio)
3. [Requirements](#requirements)
4. [Setup](#setup)
5. [Project Structure](#project-structure)
6. [Usage](#usage)
7. [Testing](#testing)

---

## **Features**
- **Dynamic Two-Way Call**: Initiates a call between the caller and callee, allowing for real-time communication.
- **Message Recording**: Records the caller's message and saves it locally.
- **Local Storage**: Saves recordings and text messages in a folder named `calls_[phone_number]_[date]`.
- **Playback**: Allows playback of recorded messages or provided `.mp3` files.
- **Microphone Recording**: Records audio from the microphone if the `-r` flag is used.
- **Hardcoded Default Message**: Uses a default message if no message is provided.

---

## **Why Use Twilio?**
Twilio is a powerful and reliable cloud communications platform that provides APIs for voice, SMS, and other communication channels. Here's why Twilio was chosen for this task:
- **Ease of Use**: Twilio's API is well-documented and easy to integrate with Python.
- **Scalability**: Twilio can handle a large number of calls and recordings efficiently.
- **Reliability**: Twilio provides high-quality voice calls and recordings.
- **Flexibility**: Twilio supports a wide range of features, including call forwarding, voicemail, and more.

---

## **Requirements**
- Python 3.7 or higher
- Twilio account with valid credentials (`ACCOUNT_SID`, `AUTH_TOKEN`, and `TWILIO_PHONE_NUMBER`)
- Required Python libraries:
  - `twilio`
  - `playsound`
  - `sounddevice`
  - `scipy`
  - `requests`
  - `shutil`

---

## **Setup**
1. Install the required Python libraries:
   ```bash
   pip install twilio playsound sounddevice scipy requests shutil
   ```

2. Replace the Twilio credentials in `constants.py` with your own:
   ```python
   # Twilio credentials (replace with your own)
   ACCOUNT_SID = "your_account_sid"
   AUTH_TOKEN = "your_auth_token"
   TWILIO_PHONE_NUMBER = "your_twilio_phone_number"  # Must be a Twilio number
   ```

---

## **Project Structure**
```
voice-call-app/
│
├── voice_call_app.py          # Main script to run the application
├── twilio_client.py           # Handles Twilio API interactions
├── file_utils.py              # Handles file operations (saving recordings, text messages)
├── audio_utils.py             # Handles audio recording and playback
├── constants.py               # Contains constants (e.g., Twilio credentials, default message)
└── phone_day folder           # Include the files saved during calls and testing such as recordings and messages
```

---

## **Usage**
The script supports the following command-line arguments:

| Argument       | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `-n`, `--number` | The phone number to call (e.g., `+15551234567`). **Required**.              |
| `-m`, `--message` | Optional message to play (string or audio file URL).                        |
| `-r`, `--record`  | Record a new message.                                                       |
| `--play`       | Play the specified `.mp3` file or recorded file.                            |

### **Example Commands**
1. **Initiate a Call with a Custom Message**:
   ```bash
   python voice_call_app.py -n +15551234567 -m "Hello, this is a test message."
   ```

2. **Record a New Message**:
   ```bash
   python voice_call_app.py -n +15551234567 -r
   ```

3. **Play a Provided `.mp3` File**:
   ```bash
   python voice_call_app.py -n +15551234567 --play recording.mp3
   ```

4. **Initiate a Call with the Default Message**:
   ```bash
   python voice_call_app.py -n +15551234567
   ```

---

## **Testing**
Here are some test cases to verify the functionality of the application:

### **Test 1: Initiate a Call with a Custom Message**
```bash
python voice_call_app.py -n +16616901167 -m "Hello, how are you"
```

**Output**:
```
Created folder: calls_+16616901167_20250224
Call initiated successfully! Call SID: CAf8570206ab35b8905da7671c1dff6ab9
Call was initiated successfully.
Text message saved to calls_+16616901167_20250224\messages_+16616901167.txt
The sent message is:  Hello, how are you
```

### **Test 2: Play a Provided `.mp3` File**
```bash
python voice_call_app.py -n +16616901167 --play inspiring-piano-music-293598.mp3
```

**Output**:
```
Created folder: calls_+16616901167_20250224
Recording saved to calls_+16616901167_20250224\inspiring-piano-music-293598.mp3
Text message saved to calls_+16616901167_20250224\messages_+16616901167.txt
```

### **Test 3: Record a New Message**
```bash
python voice_call_app.py -n +16616901167 -r
```

**Output**:
```
Created folder: calls_+16616901167_20250224
Please record your message. You have 30 seconds to record.
Recording... Speak into your microphone.
Recording saved to calls_+16616901167_20250224\recording_232507.wav
Text message saved to calls_+16616901167_20250224\messages_+16616901167.txt
The recorded message has been saved successfully
```

---

## **Contributing**
Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## **Contact**
For questions or feedback, please contact:
- **Email**: [Abdelhady Sayed](mailto:abdelhadysayed_p@sci.asu.edu.eg)
- **GitHub**: [AbdelhadySayed](https://github.com/AbdelhadySayed)

