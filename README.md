# HACS PyScript Telefunken

## installation
1. Install HACS
2. Add PyScript as a custom repository
3. Install PyScript as integration (allow imports)
4. Restart Home Assistant
5. Copy the `telefunken.py` file to the `config/pyscript` folder
6. Restart HACS

## usage
1. Find out the IP address of your Telefunken TV (e.g. look it up in your router or in the TV settings)
2. Test the port with `curl -H 'Host: IP_ADDRESS' --data '<remote><key code="1013"/></remote>' http://IP_ADDRESS:56789/apps/vr/remote`. This should mute the TV if everything is working correctly.
3. Use service `python_script.telefunken` with the following data:
```
action: mute
ip: IP_ADDRESS
port: 56789
```
4. Integrate the service inside your automations

## parameters
- 0
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- back
- screen_resolution
- power
- mute
- language
- volume_up
- volume_down
- info
- down
- up
- left
- right
- stop
- play_pause
- rewind
- fast_forward
- subtitles
- close
- favourites
- timer
- quick_menu
- app_dashboard
- epg
- menu
- pause
- yellow
- record
- blue
- ok
- green
- red
- image_source
- mediabrowser
- text

## credits
- https://thomaskekeisen.de/de/blog/telefunken-openhab-tv-fernseher-smart-home/
- https://github.com/custom-components/pyscript
- https://hacs-pyscript.readthedocs.io/en/stable/tutorial.html#writing-your-first-script
- https://hacs-pyscript.readthedocs.io/en/latest/reference.html#avoiding-event-loop-i-o
