# ~ - ~ # ~ - ~ # KSP Mission Console # ~ - ~ # ~ - ~ #

# KSP Mission Console v1.0.
# Created by よし | Overlord.
# Edit this code at your own risk of corruption or loss of data.

# Any deleted text files will be re-created by the code every time you run. Please do not attempt to create these files
# by yourself. These files are case specific and required to be what they are called to run properly. Thank you.

# Any Suggestions for Additions send to me here: よし | Overlord#2862

## Code Keys:

# 01 - Imports & Important Modules
# 02 - File Checks
# 03 - UI Functions
# 04 - Login & Register
# 05 - Add Kerbal Function
# 06 - Add Mission Function
# 07 - End Mission Function
# 08 - Individual Kerbal Editing Function

# Code Keys are numeric identifiers for big segments of code, or important parts.
# These segments are coded to make it easier to find and edit for updates or fixes.
# If you get any errors, please DM me the Code Key of said segment and the error message.

# ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ #

# 01:
# Imports & Important Modules

import random

import hashlib

import sys

from time import sleep

# ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ #

# 02:
# File Checks

try: # Try will attempt to run the code in the indented section underneath.
    open('kerbals.txt','x') # If kerbals.txt does not exist, then this line will create a file called 'kerbals.txt'
except Exception: # If an error is raised:
    pass # Continue to the next part. Pass does nothing.

try: # Try will attempt to run the code in the indented section underneath.
    open('missions.txt','x') # If missions.txt does not exist, then this line will create a file called 'kerbals.txt'
except Exception: # If an error is raised:
    pass # Continue to the next part. Pass does nothing.

try: # Try will attempt to run the code in the indented section underneath.
    open('login.txt','x') # If login.txt does not exist, then this line will create a file called 'kerbals.txt'
except Exception: # If an error is raised:
    pass # Continue to the next part. Pass does nothing.

# ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ #

# 03:
# UI Functions

def typeword(x):
    word = x # Word equals x.
    for letters in x: # For every letter in x.
        sleep(0.06) # Wait for 0.06 seconds.
        sys.stdout.write(letters) # Write letters on the same line.

def typeloading(x):
    sys.stdout.write(f'\nLoading {x}') # Type 'Loading {x}' with x being what is in the brackets on the same line.
    word = '...' # Word equals '...'
    for letters in word: # For every letter in word.
        sleep(0.5) # Wait for 0.5 seconds.
        sys.stdout.write(letters) # Write letters on the same line.

typeword('~ - # KSP Mission Console # - ~\n') # Type the title before the rest of the code runs.

# ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ #

# 04:
# Login & Register

linespacer = 0

loginstuff = []

with open('login.txt','r') as file:
    for lines in file:
        linespacer += 1
        if linespacer % 2 == 0:
            loginstuff.append(lines[0:len(lines)])
        else:
            loginstuff.append(lines[0:len(lines)-1])
        
# Login Segment

login = False
registered = False

if login == False and len(loginstuff) > 0:
    typeloading('Login Data')
    print('\n')

while login == False:
    if len(loginstuff) > 0:
        username = input('Enter your Username to login.\nUsername: ')
        hashname = hashlib.sha256(username.encode('utf8')).hexdigest()
        if hashname == loginstuff[0]:
            print(' ')
            password = input('Enter your Password to login.\nPassword: ')
            hashword = hashlib.sha256(password.encode('utf8')).hexdigest()
            if hashword == loginstuff[1]:
                login = True
                registered = True
                typeword('\nLogin Complete.\n')
            else:
                print('\nPassword Incorrect. Please retry in 3 seconds.\n')
                sleep(3)
        else:
            print('\nUsername Incorrect. Please retry in 3 seconds.\n')
            sleep(3)
    else:
        registered = False
        login = True

# Register Segment

if registered == False:
    typeloading('Register System')
    while registered == False:
        username = input('\n\nEnter a Username to register with.\nUsername: ')
        hashname = hashlib.sha256(username.encode('utf-8')).hexdigest()
        password = input('\n\nEnter a Password to register with.\nPassword: ')
        hashword = hashlib.sha256(password.encode('utf-8')).hexdigest()
        with open('login.txt','a') as file:
            file.write(f'{hashname}\n')
            file.write(f'{hashword}')
        print('\n\nRegistered Successfully. Welcome to the KSP Console.')
        sleep(2)
        registered = True

# ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ #

# 05.
# Add Kerbal Function

def addnewkerbal():
    kerbaldata = []
    with open('kerbals.txt','r') as file:
        for lines in file:
            kerbaldata.append(lines)

    typeloading('Kerbal Data')

    print('\n')

    kerbalname = input('Enter the name of the new Kerbal.\nName: ')
    print(' ')
    kerbaloccupation = input('Enter the occupation of the new Kerbal.\nName: ')
    kerballocation = 'KSC'
    kerbalmission = 'None'
    kerbalstatus = 'Alive'

    kerbaldata.append('-\n')
    kerbaldata.append(f'Name: {kerbalname}\n')
    kerbaldata.append(f'Occupation: {kerbaloccupation}\n')
    kerbaldata.append(f'Mission: {kerbalmission}\n')
    kerbaldata.append(f'Location: {kerballocation}\n')
    kerbaldata.append(f'Status: {kerbalstatus}\n')
    kerbaldata.append('-\n\n')

    with open('kerbals.txt','r+') as file:
        file.truncate(0)
    
    with open('kerbals.txt','a') as file:
        for lines in kerbaldata:
            file.write(lines)

    print('\nKerbal Registration Complete.\n')

# ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ #

# 06
# Add New Mission Function

def addnewmission():
    missiondata = []
    kerbaldata = []

    with open('missions.txt','r') as file:
        for lines in file:
            missiondata.append(lines)

    with open('kerbals.txt','r') as file:
        for lines in file:
            kerbaldata.append(lines)

    print(' ')
    typeloading('Mission Data')

    missionname = input('\n\nEnter the missions name.\nName: ')
    missionlocation = input('\nEnter the mission location.\nLocation: ')

    kerbalcount = int(input('\nEnter kerbal count for this mission.\nNumber: '))

    activekerbals = []

    kerbalset = False
    kerbalnumber = 0

    while kerbalset == False:
        for x in range(kerbalcount):
            kerbalnumber += 1
            addkerbal = input(f'\nEnter Kerbal {kerbalnumber}.\nName: ')
            for lines in kerbaldata:
                if addkerbal in lines:
                    if 'None' in kerbaldata[kerbaldata.index(lines)+2]:
                        activekerbals.append(addkerbal)
                        position = kerbaldata.index(lines)
                        kerbaldata[position+2] = f'Mission: {missionname}\n'
                        kerbaldata[position+3] = f'Location: {missionlocation}\n'
                    else:
                        print('\nYou can not add an active Kerbal to another mission. Retry in 2 seconds.\n')
                        sleep(2)
                        kerbalnumber = kerbalnumber - 1
                    
                    if kerbalnumber == kerbalcount:
                        kerbalset = True
                    else:
                        pass

                    break
                    

                    
                    


    missiondata.append('-\n')
    missiondata.append(f'Mission Name: {missionname}\n')
    missiondata.append(f'Mission Location: {missionlocation}\n\n')
    missiondata.append(f'Kerbals ({str(len(activekerbals))}):\n')
    for x in range(len(activekerbals)):
        missiondata.append(f'Kerbal {str(x+1)}: {activekerbals[x]}\n')
    missiondata.append(f'-\n\n')

    with open('missions.txt','r+') as file:
        file.truncate(0)
    
    with open('missions.txt','a') as file:
        for lines in missiondata:
            file.write(lines)

    with open('kerbals.txt','r+') as file:
        file.truncate(0)
    
    with open('kerbals.txt','a') as file:
        for lines in kerbaldata:
            file.write(lines)
    
    typeword('\nMission Setup Complete.\n')

# ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ #

# 07.
# End Mission Function

def endmission():

    kerbaldata = []
    missiondata = []

    with open('kerbals.txt','r') as file:
        for lines in file:
            kerbaldata.append(lines)
    
    with open('missions.txt','r') as file:
        for lines in file:
            missiondata.append(lines)

    print(' ')
    typeloading('Mission Data')
    print(' ')

    missionremove = input('\n\nEnter the Mission Name you wish to remove.\nMission Name: ')

    for lines in kerbaldata:
        if missionremove in lines:
            kerbaldata[kerbaldata.index(lines)+1] = 'Location: KSC\n'
            kerbaldata[kerbaldata.index(lines)] = 'Mission: None\n'

    for lines in missiondata:
        if missionremove in lines and len(lines) == 15 + len(missionremove):
            missionpos = missiondata.index(lines)

            missiondata.pop(missionpos + 6)
            missiondata.pop(missionpos + 5)
            missiondata.pop(missionpos + 4)
            missiondata.pop(missionpos + 3)
            missiondata.pop(missionpos + 2)
            missiondata.pop(missionpos + 1)
            missiondata.pop(missionpos - 1)
            missiondata.pop(missiondata.index(lines))

    with open('kerbals.txt','r+') as file:
        file.truncate(0)
    
    with open('missions.txt','r+') as file:
        file.truncate(0)

    with open('kerbals.txt','a') as file:
        for lines in kerbaldata:
            file.write(lines)
    
    with open('missions.txt','a') as file:
        for lines in missiondata:
            file.write(lines)

    print('\nSuccessfully Removed Mission\n')
    sleep(0.5)


# ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ #

# 08.
# Individual Editing Function

def individualkerbaledit():
    kerbaldata = []

    with open('kerbals.txt','r') as file:
        for lines in file:
            kerbaldata.append(lines)

    print(' ')
    typeloading('Kerbal Data')
    print('\n')

    kerbalname = input('Enter the name of the Kerbal you want to edit.\nName: ')

    valid = True

    for lines in kerbaldata:
        if kerbalname in lines:
            position = kerbaldata.index(lines)
    
    if 'None' not in kerbaldata[position+2]:
        valid = False
        print('\nYou can not edit Kerbals while they are Active. Returning to Menu.')
        sleep(1.5)

    active = True

    if valid == True:
        while active == True:
            print(' ')
            for x in range(-1,6):
                print(kerbaldata[position+x])
            choice = input('\nType a category to change. Type STOP to end.\nInput: ').title()
            if choice.upper() == 'STOP':
                active = False
                continue
            change = input(f'\nWhat would you like to change {choice} to?\nInput: ')
            for x in range(position, position+5):
                if choice in kerbaldata[x]:
                    kerbaldata[x] = f'{choice}: {change}\n'
                else:
                    pass
        

    with open('kerbals.txt','r+') as file:
        file.truncate(0)
    
    with open('kerbals.txt','a') as file:
        for lines in kerbaldata:
            file.write(lines)

# ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ #

# ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ #

# ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ #

currentmissions = 0
kerbalonmissions = 0

with open('missions.txt','r') as file:
    for lines in file:
        if 'Mission Name' in lines:
            currentmissions += 1
        if 'Kerbal' in lines:
            kerbalonmissions += 1

kerbalonmissions -= currentmissions

if login == True:
    print('\n# ~ - ~ - ~ - ~ - ~ #')
    typeword(f'\nWelcome Back {username}\n')
    typeword(f'\nYou Have: {str(currentmissions)} active missions.')
    typeword(f'\nYou Have: {str(kerbalonmissions)} active kerbals on missions.\n')

while login == True:
    print('\n# ~ - ~ - ~ - ~ - ~ #\n')

    typeword('Type KERBAL to enter Kerbal Configuration.\n')
    typeword('Type MISSION to enter Mission Configuration.\n')
    typeword('Type EXIT to exit the program.\n')
    choice = input('\nChoice: ').upper()

    if choice == 'KERBAL':
        print('\n# ~ - ~ - ~ - ~ - ~ #')
        typeloading('Kerbal Config Menu')
        while choice == 'KERBAL':
            print('\n')
            typeword('Type ADD to register a new Kerbal.\n')
            typeword('Type EDIT to edit a specific Kerbal.\n')
            typeword('Type BACK to go back to the main console.\n')
            kerbalchoice = input('\nChoice: ').upper()
            if kerbalchoice == 'ADD':
                addnewkerbal()
                kerbalchoice = ' '
            if kerbalchoice == 'EDIT':
                individualkerbaledit()
                kerbalchoice = ' '
            if kerbalchoice == 'BACK':
                choice = ' '
            else:
                choice = ' '

    if choice == 'MISSION':
        print('\n# ~ - ~ - ~ - ~ - ~ #')
        typeloading('Mission Config Menu')
        while choice == 'MISSION':
            print('\n')
            typeword('Type NEW to add a new Mission.\n')
            typeword('Type REMOVE to remove an active Mission.\n')
            typeword('Type BACK to go back to the main console.\n')
            missionchoice = input('\nChoice: ').upper()
            if missionchoice == 'NEW':
                addnewmission()
                missionchoice = ' '
            if missionchoice == 'REMOVE':
                endmission()
                missionchoice = ' '
            if missionchoice == 'BACK':
                choice = ' '
            else:
                pass

    if choice == 'EXIT':
        exitsure = input('\nAre you sure you want to exit?\nChoice: ')
        if exitsure.title() == 'Yes':
            exit()
        if exitsure.title() == 'No':
            pass
            choice = ' '
        else:
            pass
            choice = ' '
