import notable_assessment_utils as utils
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

def transform_string(input_str):
    """
    Takes an input string and applies a transformation
    Returns transformed string
    """
    if not input_str or input_str.strip() == "":
        raise Exception("Input cannot be empty")

    logging.debug("Transforming string: \n" + input_str)
    
    # Perform transform here
    input_str_arr = input_str.split()

    transcribed_text = input_str_arr[0]
    starting_num = 0
    skip_next = False
    sequenceStarted = False
    capitalizeNext  = False
    # Parse the transcibed text
    for i in range(1, len(input_str_arr)):
        # Check if we need to skip iteration due to indexing
        if skip_next == True:
            skip_next = False
            continue

        # If we see "Number", check the next element, unless it is the last element in the array
        if input_str_arr[i].casefold() == "number".casefold() and i != len(input_str_arr):

            if input_str_arr[i+1] in utils.strings_to_int_map.keys():
                #Start of the sequence
                if not sequenceStarted:
                    transcribed_text = transcribed_text + "\n" + str(utils.strings_to_int_map.get(input_str_arr[i+1])) + ". "
                    starting_num = utils.strings_to_int_map.get(input_str_arr[i+1]) + 1
                    skip_next = True
                    sequenceStarted = True
                    capitalizeNext = True
                else:
                    transcribed_text = transcribed_text + " " + input_str_arr[i]
            elif input_str_arr[i+1].casefold() == "next".casefold():
                # New line, but sequence has already started
                transcribed_text = transcribed_text + "\n" + str(starting_num) + ". " 
                starting_num += 1
                skip_next = True
                capitalizeNext = True
        else:
            # No new line needed
            if capitalizeNext == True: 
                transcribed_text = transcribed_text + " " + input_str_arr[i].capitalize()
                capitalizeNext = False
            else: 
                transcribed_text = transcribed_text + " " + input_str_arr[i]


    logging.debug("Transformed string: \n " + transcribed_text)
    return transcribed_text

if __name__ == "__main__":
    input_str = "Patient presents today with several issues. Number one BMI has increased by 10 since their last visit number next patient reports experiencing dizziness several times in the last two weeks. Number next patient has a persistent cough that hasn’t improved for last 4 weeks Number next patient is taking drug number five several times a week"
    transcribed_text = transform_string(input_str)    # Transform string
