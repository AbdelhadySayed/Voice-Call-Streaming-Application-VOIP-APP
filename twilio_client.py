from twilio.rest import Client
from constants import ACCOUNT_SID, AUTH_TOKEN, TWILIO_PHONE_NUMBER


# Initialize Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)


def make_call(to_phone_number, message):
    """
    Initiates a phone call to the specified number and records a message.
    :param to_phone_number: The phone number to call (e.g., "+15551234567")
    :param message: The message to play (string)
    :return: Call SID if successful, None otherwise
    """
    try:
        # Validate phone number
        if not to_phone_number.startswith("+"):
            raise ValueError("Phone number must include country code (e.g., +15551234567)")

        # TwiML (Twilio Markup Language) to handle the call flow
        twiml = f"""
        <Response>
            <Say>{message}</Say>
            <Dial>
                <Number>{to_phone_number}</Number>
            </Dial>
            <Record maxLength="60" action="/handle_recording" />
        </Response>
        """

        # Make the call
        call = client.calls.create(
            twiml=twiml,
            to=to_phone_number,
            from_=TWILIO_PHONE_NUMBER
        )

        print(f"Call initiated successfully! Call SID: {call.sid}")
        return call.sid

    except ValueError as ve:
        print(f"Invalid input: {ve}")
        return None
    except Exception as e:
        print(f"Error making the call: {e}")
        return None

def save_recording(call_sid, output_file):
    """
    Fetches the recording associated with the call and saves it to a local file.
    :param call_sid: The SID of the call
    :param output_file: Path to save the recording (e.g., "recording.mp3")
    :return: Path to the saved recording if successful, None otherwise
    """
    try:
        # Wait for the recording to be available
        print("Waiting for recording to be processed...")
        time.sleep(10)  # Wait for 10 seconds (adjust as needed)

        # Fetch the recording associated with the call
        recordings = client.recordings.list(call_sid=call_sid)
        if not recordings:
            print("No recordings found for this call.")
            return None

        # Download the recording
        recording = recordings[0]
        recording_uri = f"https://api.twilio.com{recording.uri.replace('.json', '.mp3')}"
        recording_data = requests.get(recording_uri, auth=(ACCOUNT_SID, AUTH_TOKEN)).content

        # Save the recording to a file
        with open(output_file, "wb") as f:
            f.write(recording_data)
        print(f"Recording saved to {output_file}")
        return output_file
    except Exception as e:
        print(f"Error saving recording: {e}")
        return None