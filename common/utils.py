import hashlib
from datetime import datetime


def generate_unique_string(key_string):
    """
    Function that Generates unique string based on string and haslib.
    """
    
    current_timestamp_str = datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")

    key = "{key_string}-{current_timestamp_str}".format(
            key_string=key_string, 
            current_timestamp_str=current_timestamp_str)
    
    return hashlib.sha1(key.encode('utf-8')).hexdigest()[:8].upper()
