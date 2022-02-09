from datetime import datetime
from hashlib import blake2b


def generate_unique_string(key_string):
    """
    Function that Generates unique string based on string and haslib.
    """
    
    current_timestamp_str = datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")

    return blake2b(
        key="{key_string}-{current_timestamp_str}".format(
            key_string=key_string, 
            current_timestamp_str=current_timestamp_str).encode("utf-8"), 
        digest_size=4).hexdigest().upper()
