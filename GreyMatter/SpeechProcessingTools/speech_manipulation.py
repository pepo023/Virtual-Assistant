def check_message(check, speech_text):
    """"
    This function checks if the items in the list (specified in argument) are
    present in the user's input speech. Is "check" a subset of the user's input?
    """
    words_of_message = speech_text.split()  # separate input string into list of strings
    if set(check).issubset(set(words_of_message)):  # set removes any duplicates from word list
        return True
    else:
        return False
