from enum import Enum

class G_Levels(Enum):
    MID_GAR = 1

class G_Talk():

    STATE = None

    MID_GAR_CHAR_DICT = {
        'e': 'e', 'i': 'e', 'u': 'e', 'u': 'e', 'y': 'e', 't': 'e',
        'c': 'k', 'q': 'k', 'x': 'k', 'k': 'k', 
        'j': 'a', 'l': 'r', 'j': 'w', 'a': 'a', 
        's': 'h', 'z': 'h', 'h': 'h', 
        'b': 'f', 'v': 'f', 'p': 'f', 
        'd': 'm', 'f': 'm', 'g': 'm', 'm': 'm', 
                         }

    def __init__(self):
        self.STATE = G_Levels.MID_GAR

    def g_talk(self, string_to_garble: str) -> str:
        g_string = ''
        for char in string_to_garble:
            g_string += self.MID_GAR_CHAR_DICT.get(char, char)
        return g_string



