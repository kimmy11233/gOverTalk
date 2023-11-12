from keyboard import wait, add_hotkey, record, write, hook_key, start_recording, stop_recording, unhook_key, press_and_release, add_word_listener, unhook_all

RETURN_HOOK = None
def trigger_replacement(r):
    str = ''
    for op in r:
        write('\b')
        str += 'm'
    print(f'Writing: {str}')
    write(str)
    press_and_release('enter')

def report(e): 
    print('Listen Kill init')
    unhook_all()
    trigger_replacement(stop_recording())
    add_word_listener('/g', begin_listen)

def begin_listen():
    print('Listen init')
    RETURN_HOOK = hook_key('\r', report, suppress=True)
    start_recording()



if __name__ == '__main__':

    add_word_listener('/g', begin_listen)
    
    
    wait()
    



