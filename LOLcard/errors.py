ERROR000 = '\
┌──────────────────────────────────────┐\n\
│                ERROR                 │\n\
│               UNKNOWN                │\n\
│          This type of error          │\n\
│            is not defined            │\n\
└──────────────────────────────────────┘'

ERROR400 = '\
┌──────────────────────────────────────┐\n\
│            ERROR CODE 400            │\n\
│             BAD REQUEST              │\n\
│          Please let me know          │\n\
│        if you get this error         │\n\
└──────────────────────────────────────┘'

ERROR401 = '\
┌──────────────────────────────────────┐\n\
│            ERROR CODE 401            │\n\
│             UNAUTHORIZED             │\n\
│          Please let me know          │\n\
│        if you get this error         │\n\
└──────────────────────────────────────┘'

ERROR403 = '\
┌──────────────────────────────────────┐\n\
│            ERROR CODE 403            │\n\
│             UNAUTHORIZED             │\n\
│          Please let me know          │\n\
│        if you get this error         │\n\
└──────────────────────────────────────┘'

ERROR404 = '\
┌──────────────────────────────────────┐\n\
│            ERROR CODE 404            │\n\
│            DATA NOT FOUND            │\n\
│           Cannot find user           │\n\
│        you are trying to find        │\n\
└──────────────────────────────────────┘'

ERROR405 = '\
┌──────────────────────────────────────┐\n\
│            ERROR CODE 405            │\n\
│          METHOD NOT ALLOWED          │\n\
│          Please let me know          │\n\
│        if you get this error         │\n\
└──────────────────────────────────────┘'

ERROR429 = '\
┌──────────────────────────────────────┐\n\
│            ERROR CODE 429            │\n\
│          RATE LIMIT EXCEEDED         │\n\
│    Riot API request rate exceeded,   │\n\
│           please try again           │\n\
└──────────────────────────────────────┘'

ERROR500 = '\
┌──────────────────────────────────────┐\n\
│            ERROR CODE 500            │\n\
│         INTERNAL SERVER ERROR        │\n\
│         Riot API server error        │\n\
│          it is not my fault          │\n\
└──────────────────────────────────────┘'


ERRORMSG = {
    400: ERROR400,
    401: ERROR401,
    403: ERROR403,
    404: ERROR404,
    405: ERROR405,
    429: ERROR429,
    500: ERROR500,
}