from GreyMatter.SenseCells.stt import stt
import time


def hey_assistant():

    prompt_status = 0   # This variable signals that no prompt has been received by the user.

    while prompt_status == 0:
        time.sleep(1)   # Defines how often assistant will check for "hey assistant"
        speech_text = stt()
        if speech_text == "no prompt":
            print("I'm sleeping...")
            """
            Do nothing, because the user hasn't prompted you
            """
            time.sleep(3)   # Delay for 3 seconds
        elif speech_text == "hey assistant":
            print("What can I do?")
            speech_text = stt()
            if speech_text == "no prompt":
                print("You left me waiting again...")
                """
                Do nothing
                """
                time.sleep(3)
            else:
                prompt_status = 1   # A prompt was received

    return speech_text


