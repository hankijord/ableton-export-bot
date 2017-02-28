import pyautogui, subprocess, time, logging

projectName = 'MySong'
soloLocations = []
retina = True

# Switch window to Ableton Live
def switchToAbleton():
    pyautogui.keyDown('command')
    pyautogui.press('tab')
    print 'Looking for Live icon...'
    time.sleep(1)
    button = pyautogui.locateCenterOnScreen('img/live.png', grayscale=True)
    pyautogui.moveTo(button[0]/2, button[1]/2)
    pyautogui.keyUp('command')
    return

# Get The Locations of the Solo-ed tracks
def getSoloLocations():
    print 'Looking for solo-ed tracks...'
    locations = pyautogui.locateAllOnScreen('img/solo.png', grayscale=True)
    if locations == None:
        pyautogui.alert('You need to solo the tracks you want to export.')
        exit()
    return locations

# Generic function to click an image
def clickFromImage(imageName):
    button = pyautogui.locateCenterOnScreen(imageName, grayscale=True)
    x = button[0]
    y = button[1]
    if retina == True:
        x = x / 2
        y = y / 2
    pyautogui.moveTo(x,y)
    pyautogui.click()
    return "Clicked {0}".format(imageName)

# Exports a track based on a solo location
def export(location, count):
    # Solo the track
    x = (location[0] + (location[2] / 2)) / 2
    y = (location[1] + (location[3] / 2)) / 2
    pyautogui.moveTo(x, y)
    pyautogui.click()
    
    # Export the track
    pyautogui.hotkey('command','shift','r')
    pyautogui.press('enter')
    pyautogui.typewrite(str(count) + ' ' + projectName)
    pyautogui.press('enter')
    
    print 'Beginning export: '+str(count) + ' ' + projectName+'.'

    # Wait till finished export
    time.sleep(1)
    while True:
        location = pyautogui.locateOnScreen('img/loading.png') 
        if location != None:
            print 'Still exporting...'
        else:
            print 'Finished exporting: '+str(count) + ' ' + projectName+'.'
            break

    # Unsolo the track
    pyautogui.moveTo(x, y)
    pyautogui.click()
    return 

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
    print 'Started Ableton Export Bot.'
    global projectName
    projectName = pyautogui.prompt(text='Enter the project name', title='Ableton Export Bot', default='')

    # Check Retina Display
    if subprocess.call("system_profiler SPDisplaysDataType | grep 'retina'", shell=True) == 0:
        retina = True
    else:
        retina = False

    switchToAbleton()
    # Delay while switching
    time.sleep(1)
    
    global soloLocations
    soloLocations = list(getSoloLocations())
    print 'Found ' + str(len(soloLocations)) + ' solo-ed tracks.'

    # Unclick all the solobuttons
    for location in soloLocations:
        x = (location[0] + (location[2] / 2)) / 2
        y = (location[1] + (location[3] / 2)) / 2
        pyautogui.moveTo(x, y)
        pyautogui.click()

    # Export tracks
    i = 1
    for location in soloLocations:
        export(location, i)
        i += 1
        
    print 'Export complete!'
    return

main()
