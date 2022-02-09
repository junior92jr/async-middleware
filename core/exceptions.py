from rest_framework.exceptions import APIException

class RepeatedUrlHashException(APIException):
    status_code = 424
    default_detail = "The unique Url Hash is repeated."
    default_code = "repeated_url_hash"