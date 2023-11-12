from keyboard import write, hook_key, start_recording, stop_recording, press_and_release, add_word_listener, unhook_all, get_typed_strings
from GTalk import G_Talk

RETURN_HOOK = None
g_Talk = G_Talk()


def trigger_replacement(record):
    
    # After detecting enter, remove its suppressor
    unhook_all()
    
    capture_string = ''
    for char in get_typed_strings(stop_recording()):
        capture_string += char
    
    # Blank the line. THIS HAS TO BE DONE ON ITS OWN
    # Idk why but it only works like this 
    # NOTE:: +3 for '/g '
    for char in range(len(capture_string) + 3):
        write('\b')

    #Convert string
    print(f'Pure string: {capture_string}')
    g_String = g_Talk.g_talk(capture_string)
    print(f'Converted string: {g_String}')

    # Simulate keypress and submit the message
    write(g_String)
    press_and_release('enter')
    trigger_passive_listen()

def trigger_active_listen():
    print('Listen init')
    RETURN_HOOK = hook_key('\r', trigger_replacement, suppress=True)
    start_recording()

def trigger_passive_listen():
    add_word_listener('/g', trigger_active_listen)





