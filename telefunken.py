import requests

def send_remote_api_call(ip, port, id):
    task.executor(requests.post, 'http://' + ip + ':' + str(port) + '/apps/vr/remote', headers={'Host': ip + ':' + str(port)}, data='<remote><key code="' + str(id) + '"/></remote>')

@service
def telefunken_remote(action='', ip='', port=0):
    if action == '0':
        send_remote_api_call(ip, port, 1000)
    elif action == '1':
        send_remote_api_call(ip, port, 1001)
    elif action == '2':
        send_remote_api_call(ip, port, 1002)
    elif action == '3':
        send_remote_api_call(ip, port, 1003)
    elif action == '4':
        send_remote_api_call(ip, port, 1004)
    elif action == '5':
        send_remote_api_call(ip, port, 1005)
    elif action == '6':
        send_remote_api_call(ip, port, 1006)
    elif action == '7':
        send_remote_api_call(ip, port, 1007)
    elif action == '8':
        send_remote_api_call(ip, port, 1008)
    elif action == '9':
        send_remote_api_call(ip, port, 1009)
    elif action == 'back':
        send_remote_api_call(ip, port, 1010)
    elif action == 'screen_resolution':
        send_remote_api_call(ip, port, 1011)
    elif action == 'power':
        send_remote_api_call(ip, port, 1012)
    elif action == 'mute':
        send_remote_api_call(ip, port, 1013)
    elif action == 'language':
        send_remote_api_call(ip, port, 1015)
    elif action == 'volume_up':
        send_remote_api_call(ip, port, 1016)
    elif action == 'volume_down':
        send_remote_api_call(ip, port, 1017)
    elif action == 'info':
        send_remote_api_call(ip, port, 1018)
    elif action == 'down':
        send_remote_api_call(ip, port, 1019)
    elif action == 'up':
        send_remote_api_call(ip, port, 1020)
    elif action == 'left':
        send_remote_api_call(ip, port, 1021)
    elif action == 'right':
        send_remote_api_call(ip, port, 1022)
    elif action == 'stop':
        send_remote_api_call(ip, port, 1024)
    elif action == 'play_pause':
        send_remote_api_call(ip, port, 1025)
    elif action == 'rewind':
        send_remote_api_call(ip, port, 1027)
    elif action == 'fast_forward':
        send_remote_api_call(ip, port, 1028)
    elif action == 'subtitles':
        send_remote_api_call(ip, port, 1031)
    elif action == 'close':
        send_remote_api_call(ip, port, 1037)
    elif action == 'favourites':
        send_remote_api_call(ip, port, 1040)
    elif action == 'timer':
        send_remote_api_call(ip, port, 1042)
    elif action == 'quick_menu':
        send_remote_api_call(ip, port, 1043)
    elif action == 'app_dashboard':
        send_remote_api_call(ip, port, 1046)
    elif action == 'epg':
        send_remote_api_call(ip, port, 1047)
    elif action == 'menu':
        send_remote_api_call(ip, port, 1048)
    elif action == 'pause':
        send_remote_api_call(ip, port, 1049)
    elif action == 'yellow':
        send_remote_api_call(ip, port, 1050)
    elif action == 'record':
        send_remote_api_call(ip, port, 1051)
    elif action == 'blue':
        send_remote_api_call(ip, port, 1052)
    elif action == 'ok':
        send_remote_api_call(ip, port, 1053)
    elif action == 'green':
        send_remote_api_call(ip, port, 1054)
    elif action == 'red':
        send_remote_api_call(ip, port, 1055)
    elif action == 'image_source':
        send_remote_api_call(ip, port, 1056)
    elif action == 'mediabrowser':
        send_remote_api_call(ip, port, 1057)
    elif action == 'text':
        send_remote_api_call(ip, port, 1255)
