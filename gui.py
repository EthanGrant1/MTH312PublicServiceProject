# Gamer moment
from ctypes.wintypes import RGB
from re import S
import pygame as p

# import cryptography functions
import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import base64
from os import urandom as r

#import math library
import math

import webbrowser

#from sqlalchemy import true

# System level module for program args, i/o, exits, etc.
# import sys as s

# Helper function library that contains objects to render
from HelperFunctions import textbox as tb

# For tracking how long it takes to brute force the password
from time import time as t

# Local variables in pygame for event handling
from pygame.locals import *

# Initalizes pygame
p.init()

# Timer for frames per second
clock = p.time.Clock()

#Set the screen size and the window caption
max_w = 800
max_h = 600
screen = p.display.set_mode((max_w, max_h))
p.display.set_caption('Password Manager')

# Font for unicode symbols
unifont = 'seguisym.ttf'

# Pygame fonts
p.font.init()

def main():

    #Main activity
    running = True
    while running:
        # fills the screen with black color
        screen.fill("black")

        # Menu title font and words
        titleFont = p.font.SysFont('Helvetica', 60)
        title = titleFont.render('Password Encryption Utility', False, (195,145,205))
       
        # Draw the title on the screen
        screen.blit(title, (40,120))
        
        # The first option in the menu
        option_1 = tb(p.Rect(250,238,300,42), 0, 'black', 'PASSWORD CHECKER', unifont, 30, 'white')

        # The second option
        option_2 = tb(p.Rect(180,320,460,42), 0, 'black', 'PASSWORD MANAGER FEATURES', unifont, 30, 'white')

        # Developers
        developer = tb(p.Rect(20,550,460,42), 0, 'black', 'Developed by Alec, Brennan, Ethan, Jochen', unifont, 15, 'green')

        # Draw textboxes on the screen
        option_1.drawText(screen)
        option_2.drawText(screen)
        developer.drawText(screen)

        # Events that are in the event queue
        for e in p.event.get():

            # If the user quits the program
            if e.type == QUIT:
                running = False
            
            # Click event
            if e.type == p.MOUSEBUTTONDOWN:

                # If click event occured within option_1 box
                if option_1.getBox().collidepoint(e.pos):
                    option_one()
                # If click event occured with option_2 box
                if option_2.getBox().collidepoint(e.pos):
                    option_two()
                    
                    

        # Updates the screen
        p.display.update()

        # Ensure the clock is in line with 60 frames per second
        clock.tick(60)



def option_one():
# calculate encryption values for mock encryption
    superSecurePassword = 'MonkeyMagentaRocketBenzene'

    # Randomly generated "salt" byte string
    mySalt = r(16)

    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                     length=32,
                     salt=mySalt,
                     iterations=100000,
                     backend=default_backend()
                     )
    key = base64.urlsafe_b64encode(kdf.derive(superSecurePassword.encode()))
    fernet = Fernet(key)

    # Input box variables
    # ---------------------------
    clear = ''

    # A default text size
    txt_size = 32

    # Box position variables
    box_x = int((max_w - 260) / 2)
    box_y = int(max_h / 2) - 50

    # Colors for if the box is clicked on or not
    inactive_color = 'darkslategray3'
    active_color = 'darkslategray1'

    # Change the color of the box
    current_color = inactive_color

    # Is the box currently active?
    active = False

    # The text that will go into the box
    default_txt = 'Check your password here...'

    # Our input box
    box = tb(p.Rect(box_x-40, box_y-4, 300, txt_size), 3, current_color, default_txt, unifont, 16, 'black')

    # Length of text contained inside the box
    txt_len = len(box.getText())

    # Button variables
    # ----------------------------

    # Buttons are simply filled text boxes with static variables
    button = tb(p.Rect(int(box_x + (box_x / 8)), int(box_y + (box_y / 8)), 145, txt_size), 0, 'white', 'Enter', None,
                32, 'black')

    # Password storing boxes
    # -----------------------------
    stickyNoteTitle = tb(p.Rect(0, (max_h / 3 * 2) - 40, max_w / 3, 40), 0, 'black', 'That sticky note on your monitor',
        unifont, 16, 'white')
    stickyNote = tb(p.Rect(0, max_h / 3 * 2, max_w / 3, (max_h / 3) - 40), 0, 'cyan', '', unifont, 16, 'black')
    stickyNoteSubtitle = tb(p.Rect(0, max_h - 40, max_w / 3, 40), 0, 'black', 'Easy to remember - for anyone',
        unifont, 16, 'red')

    notepadFileTitle = tb(p.Rect(max_w / 3, (max_h / 3 * 2) - 40, max_w / 3, 40), 0, 'black', 'Notepad file on your desktop',
        unifont, 16, 'white')
    notepadFile = tb(p.Rect(max_w / 3, max_h / 3 * 2, max_w / 3, (max_h / 3) - 40), 0, 'white', '', unifont, 16, 'black')
    notepadFileSubtitle = tb(p.Rect(max_w / 3, max_h - 40, max_w / 3, 40), 0, 'black', 'Security by obscurity, I guess?',
        unifont, 16, 'red')

    passwordMngrTitle = tb(p.Rect(max_w / 3 * 2, (max_h / 3 * 2) - 40, max_w / 3, 40), 0, 'black',
        'A "real" password manager', unifont, 16, 'white')
    passwordMngr = tb(p.Rect(max_w / 3 * 2, (max_h / 3 * 2), max_w / 3, (max_h / 3) - 40), 0, 'gold', '', unifont, 16, 'black')
    passwordMngrSubtitle = tb(p.Rect(max_w / 3 * 2, max_h - 40, max_w / 3, 40), 0, 'black', 
        'Practically unbreakable', unifont, 16, 'green')

    # Password checking variables
    # -----------------------------

    # The dict that holds the information about the password check
    pass_dict = {}

    # Debug text that includes the password check variables
    # debug = ''

    # Text that is given to the user upon checking their password
    # TODO: Add feedback text about best practices of password management
    feedback = ''

    # Main activity loop
    running = True
    while running:
        # Color the screen
        # screen.fill((30, 30, 30))
        screen.fill('black')
        # Back button to go to the menu
        OPTIONS_BACK  = tb(p.Rect(20, 20, 45, 20), 0, 'black', 'BACK', None, 20, 'white')
        # Changes back button color
        OPTIONS_BACK.setBoxColor(p.Color(30,30,30))
        # Blits back button onto the screen
        OPTIONS_BACK.drawText(screen)


        # Events that are in the event queue
        for e in p.event.get():

            # If the user quits the program
            if e.type == QUIT:
                running = False

            # Click event
            if e.type == p.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.getBox().collidepoint(e.pos):
                    running = False

                # If the click event occurred within the text box
                if box.getBox().collidepoint(e.pos):
                    # The box is now active and ready for input
                    active = True

                    # Clear out the old text
                    box.setText('')
                    txt_len = 0
                    clear = ''

                # Otherwise, the box should be inactive
                else:
                    # Will no longer accept input
                    active = False

                    # Set the box text back to the default
                    if txt_len == 0:
                        box.setText(default_txt)

                # Change the color of the box
                current_color = active_color if active else inactive_color

                box.setBoxColor(current_color)

                # If the click event occurred within the button
                if button.getBox().collidepoint(e.pos):
                    # Set the password manager box text to the encrypted text
                    passwordMngr.setText(bytes.decode(fernet.encrypt(str.encode(clear))))

                    # Check the password
                    pass_dict = check_pass(clear)

                    # Clear out the text
                    box.setText('')
                    txt_len = 0
                    clear = ''
                

            # Keyboard event
            if e.type == p.KEYDOWN:

                # Check if the box is currently active
                if active:
                    # If the user presses Enter
                    if e.key == p.K_RETURN:
                        
                        # Reset the text to the default
                        box.setText(default_txt)

                        passwordMngr.setText(bytes.decode(fernet.encrypt(str.encode(clear))))

                        # Check the password
                        pass_dict = check_pass(clear)

                        # Clear out the text
                        box.setText('')
                        txt_len = 0
                        clear = ''
                        

                    # If the user presses Backspace
                    elif e.key == p.K_BACKSPACE:

                        # Check if the text to be rendered is within the bounds of the box
                        if ((txt_size / 2) * txt_len) <= box.getBox().w:
                            # Delete a character of text
                            box.setText(box.getText()[:-1])
                            clear = clear[:-1]
                            stickyNote.setText(clear)

                        # Decrease the length
                        txt_len -= 1

                        # Ensure that length stays within correct bounds
                        if txt_len < 0:
                            txt_len = 0

                    # Check if the unicode is a function key or not
                    # (Shift, Tab, etc. will result in '' when checking the unicode)
                    elif e.unicode != '':
                        # If the text to be rendered is inside the bounds of the box
                        if (box.getFontSize() * (txt_len + 1)) < box.getBox().w:
                            # Append a password character to the text
                            box.setText(box.getText() + '???')

                        # Append the unicode character to our clear text
                        clear += e.unicode
                        stickyNote.setText(clear)
                        notepadFile.setText(clear)

                        # Increase the length
                        txt_len += 1


        # DEBUG DICTIONARY PRINTING #

        # Position variables
        temp_x = 20
        temp_y = 50

        # Debug text
        # debug = 'Your password needs: '

        # Render as surface
        

        # temp variable to blit 'debug' onto screen
        counter = 0
        debug = 'Your password needs: '
        temp_surf = p.font.Font(None, txt_size + 5).render(debug, True, p.Color('green'))

        #counter to check if password fulfills all the requirement (upper, lower, symbol)
        fCounter = 4

        # Check the password check dictionary
        for key in pass_dict:
            #blit 'debug' to screen along with the first key in the dictionary
            if counter == 0:
                screen.blit(temp_surf, (temp_x, temp_y))

            # Add total time to crack on screen (FORMATTING STUFF)
            if key == 'Total Time':
                debug = 'How long would it take for BRUTE'
                temp_surf = p.font.Font(None, 25).render(debug, True, p.Color('red'))
                screen.blit(temp_surf, (500, 75))
                debug = 'FORCE to find your password?'
                temp_surf = p.font.Font(None, 25).render(debug, True, p.Color('red'))
                screen.blit(temp_surf,(500, 100 )) 
                debug = f'{pass_dict[key]}'
                temp_surf = p.font.Font(None, 25).render(debug, True, p.Color('red'))
                screen.blit(temp_surf,(500, 125 )) 
            
            # Blit what the password is missing to the screen
            if pass_dict[key] == False:
                temp_y += txt_size + 5
                debug = '- ' + f'{key}'
                temp_surf = p.font.Font(None, txt_size).render(debug, True, p.Color('white'))
                screen.blit(temp_surf, (temp_x, temp_y))
            #Tracking if password fulfills all the requirement
            elif pass_dict[key] == True: 
                fCounter-=1

            # If password has upper, lower, number, and letter (FORMATING.....)
            if fCounter == 0:
                Hide = tb(p.Rect(20,50, 500, 25), 0, 'black', '', unifont, 23, 'black')
                Hide.drawText(screen)
                temp_y += txt_size + 5
                debug = 'Your password looks strong :)'
                temp_surf = p.font.Font(None, txt_size + 5).render(debug, True, p.Color('green'))
                screen.blit(temp_surf, (temp_x, temp_y))
                temp_y += txt_size + 5
                debug = '- Make sure NOT to use your NAME'
                temp_surf = p.font.Font(None, txt_size).render(debug, True, p.Color('white'))
                screen.blit(temp_surf, (temp_x, temp_y))
                temp_y+=txt_size + 5
                debug ='  and COMMON words for passwords'
                temp_surf = p.font.Font(None, txt_size).render(debug, True, p.Color('white'))
                screen.blit(temp_surf, (temp_x, temp_y))
                fCounter-=1

            counter+=1

        # draw text boxes on screen        
        box.drawText(screen)
        button.drawText(screen)
        stickyNoteTitle.drawText(screen)
        stickyNote.drawText(screen)
        stickyNoteSubtitle.drawText(screen)
        notepadFileTitle.drawText(screen)
        notepadFile.drawText(screen)
        notepadFileSubtitle.drawText(screen)
        passwordMngrTitle.drawText(screen)
        passwordMngr.drawText(screen)
        passwordMngrSubtitle.drawText(screen)

        # Update the screen
        p.display.flip()

        # Ensure the clock is in line with 60 frames per second
        clock.tick(60)

def option_two():
    # Loads the image
    arrow = p.image.load('arrow.png')
    output = tb(p.Rect(4,450, max_w + 20, max_h/2), 0, 'white', '', unifont, 23, 'black')
    sha = p.image.load("sha.png")
    pbk = p.image.load("pbk.png")
    DEFAULT_SHA_SIZE = (380, 250)
    DEFAULT_PBK_SIZE = (380, 250)
    sha = p.transform.scale(sha, DEFAULT_SHA_SIZE)
    pbk = p.transform.scale(pbk, DEFAULT_PBK_SIZE)

    # Main activity
    running = True
    while running:
        # Fills the screen with grey color
        screen.fill("white")
        #backgroundTop = p.draw.rect(screen, 'blue', p.Rect(0, 0, max_w, max_h),  4, 3)
        masterPasswordBorder = p.draw.rect(screen, 'blue', p.Rect(18, 131, 312, 33),  2, 4)
        passwordBorder = p.draw.rect(screen, 'blue', p.Rect(495, 122, 248, 58),  2, 4) 


        # Back Button
        OPTIONS_BACK  = tb(p.Rect(20, 20, 45, 20), 0, 'white', 'BACK', None, 20, 'black')
        OPTIONS_BACK.drawText(screen)

        # Draw image to the screen
        #screen.blit(image, (90,10))

        #MASTER PASSWORD
        masterPasswordFont = p.font.SysFont('Times New Roman', 32)
        masterPassword = masterPasswordFont.render('MASTER PASSWORD', False, 'black')
        masterRect = masterPassword.get_rect(topleft=(20,130))

        #PASSWORD Vault
        # passwordVaultFont = p.font.SysFont('Times New Roman', 20) 
        # passwordVault = passwordVaultFont.render('PASSWORD VAULT', False, 'red')
        # passwordRect = passwordVault.get_rect(topleft=(400,20))

        #Encrypted Password
        EncryptedPassword = tb(p.Rect(500,128,240,50),0, 'white', 'PASSWORDS', None, 50,'red')

        PageTitle  = tb(p.Rect(40, 50, max_w - 80, 60), 0, 'white', 'HOW DOES A PASSWORD MANAGER WORK?', None, 47, 'red')
        
        website_link = tb(p.Rect(5, 570, max_w - 80, 22), 0, 'white', 'CLICK HERE TO LEARN MORE ABOUT PASSWORD MANAGER ENCRYPTION (AES 256)', None, 20, 'red') 
        PageTitle.drawText(screen)
        screen.blit(masterPassword,masterRect)
        screen.blit(arrow, (340,108))
        output.drawText(screen)    
        screen.blit(sha, (-1, 200))
        screen.blit(pbk, (400, 200))
        website_link.drawText(screen)
        # screen.blit(passwordVault,passwordRect)
        EncryptedPassword.drawText(screen)
        
        
        # Events that are in the event queue
        for e in p.event.get():
            # If the user quits the program
            if e.type == QUIT:
                running = False

            #CLICK EVENT
            if e.type == p.MOUSEBUTTONDOWN:
                # If the click even occured within the back button
                if OPTIONS_BACK.getBox().collidepoint(e.pos):
                    running = False
                if masterRect.collidepoint(e.pos):
                    output.setText('[MASTER KEY]                                                                                                                >used to accessed the passwords stored in the password vault                              >only have to memorize one MASTER PASSWORD to access all passwords')
                if EncryptedPassword.getBox().collidepoint(e.pos):
                    output.setText('[PASSWORD MANAGER]                                                                                               >passwords are stored in encrypted vault                                                                  >most password manager generates random secure password to avoid                  repeated password                                                                                                     >autofill feature means no need to memorize all the different passwords')
                if website_link.getBox().collidepoint(e.pos):
                    webbrowser.open(r"https://www.n-able.com/blog/aes-256-encryption-algorithm)")
                    

        # Update the screen
        p.display.flip() 

        # Ensure the clock is in line with 60 frames per second
        clock.tick(60)

# Stuff for password checking #

######################################
# check_pass(password)
#
# Checks a password string to see if
# it fulfills certain requirements.
# Will also attempt to brute force
# crack the password.
#
# password: str is our password to
# check
#
# Returns a dictionary of values
######################################
def check_pass(password: str) -> dict:
    # Initialize a dictionary
    my_dict = {
        # Time that it took to crack the password   
        'Total Time': None,

        # Password has uppercase letters
        'Upper Case': None,

        # Password has lowercase letters
        'Lower Case': None,

        # Password contains one or more numbers
        'Number': None,

        # Password contains one or more symbols
        'Symbol': None,

        # The 'strength' score of your password
        'strength': None
    }

    # Calculate the length
    length_error = len(password) < 8
    
    

    # Strings of possible characters
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '1234567890'
    symbols = '`-=[]\\;\',./~!@#$%^&*()_+{}|:"<>? '
    all_chars = upper + lower + numbers + symbols

    # Some boolean values to check the strength of our password
    hasUp = False
    hasLow = False
    hasNum = False
    hasSym = False

    # Cracked password
    cracked = ''

    # When we started cracking the password
    start = t()

    # Attempt to crack it
    while cracked != password:
        for i in range(len(password)):

            # Iterate over all possible characters
            for j in range(len(all_chars)):

                # If the character is found
                if all_chars[j] == password[i]:
                    cracked += all_chars[j]

    # Set the end time
    end = t()

    # Total time that it took to crack the password
    # trunc shortens integer
    total = round(end - start, 7)

    my_dict['Total Time'] = str(total) + ' s'

    strength = 0
    # Check the strength of the password
    for i in range(len(cracked)):

        # Check if the password contains uppercase letters
        if cracked[i] in upper and not hasUp:
            hasUp = True
            strength += 1

        # Check if the password contains lowercase letters
        elif cracked[i] in lower and not hasLow:
            hasLow = True
            strength += 1

        # Check if the password contains any numbers
        elif cracked[i] in numbers and not hasNum:
            hasNum = True
            strength += 1

        # Check if the password contains any symbols
        elif cracked[i] in symbols and not hasSym:
            hasSym = True
            strength += 1

    # Assign a strength value based on length and amount of variance
    strength = strength * len(password)

    # Assign values to the dictionary
    my_dict['Upper Case'] = hasUp
    my_dict['Lower Case'] = hasLow
    my_dict['Number'] = hasNum
    my_dict['Symbol'] = hasSym
    my_dict['strength'] = strength
    
        

    return my_dict


if __name__ == "__main__":
    # Run the main
    main()

    # If we exit the main loop, quit the program
    p.quit()




