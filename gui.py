# Gamer moment
import pygame as p

# System level module for program args, i/o, exits, etc
import sys as s

# Helper function library that contains objects to render
from HelperFunctions import textbox as tb

# For tracking how long it takes to brute force the password
from time import time as t

# Local variables in pygame for event handling
from pygame.locals import *

#### Stuff for password checking ####

######################################
# check_pass(password) 
# 
# Checks a password string to see if
# if fulfills certain requirements.
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
		'totalTime': None,

		# Password has uppercase letters
		'hasUp': None,

		# Password has lowercase letters
		'hasLow': None,

		# Password contains one or more numbers
		'hasNum': None,

		# Password contains one or more symbols
		'hasSym': None,

		# The 'strength' score of your password
		'strength': None
	}

	# Strings of possible characters
	upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	lower = 'abcdefghijklmnopqrstuvwxyz'
	numbers = '1234567890'
	symbols = '`-=[]\;\',./~!@#$%^&*()_+{}|:"<>?'
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

	# When we ended cracking the password
	end = start

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
	total = end - start
	my_dict['totalTime'] = total

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
	my_dict['hasUp'] = hasUp
	my_dict['hasLow'] = hasLow
	my_dict['hasNum'] = hasNum
	my_dict['hasSym'] = hasSym
	my_dict['strength'] = strength

	return my_dict

#### Main loop for the program ####
def main():
	
	# Pygame variables
	# -------------------------

	# Get user's screen size
	disInfo = p.display.Info()

	# Set the screen size and the window caption
	max_w = disInfo.current_w - 50
	max_h = disInfo.current_h - 50
	screen = p.display.set_mode((max_w, max_h))
	p.display.set_caption('Password Manager')
	
	# Timer for frames per second
	clock = p.time.Clock()

	# Input box variables
	# ---------------------------

	# A default text size
	txt_size = 32

	# Default font
	font = p.font.Font(None, txt_size)

	# Font for unicode symbols
	unifont = 'seguisym.ttf'
	
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
	box = tb(p.Rect(box_x, box_y, 300, txt_size), 3, current_color, default_txt, unifont, 16, current_color)

	# Length of text contained inside of the box
	txt_len = len(box.getText())

	# Button variables
	# ----------------------------

	# Pressable button
	button = p.Rect (
		int(box_x + (box_x/8)), 
		int(box_y + (box_y/8)), 
		145, 
		txt_size
	)

	# The color of the button
	button_color = p.Color('white')

	# Text that goes on the button
	button_text = 'Enter'
	btn_txt_color = p.Color('black')
	
	# Password checking variables
	# -----------------------------
	
	# The dict that holds the information about the password check
	pass_dict = { }

	# Debug text that includes the password check variables
	debug = ''

	# Text that is given to the user upon checking their password
	feedback = ''


	# Main activity loop
	running = True
	while running:
		
		# Events that are in the event queue
		for e in p.event.get():
			
			# If the user quits the program
			if e.type == QUIT:
				running = False

			# Click event
			if e.type == p.MOUSEBUTTONDOWN:
				
				# If the click event occurred within the text box
				if box.getBox().collidepoint(e.pos):
					# The box is now active and ready for input
					active = True

					# Clear out the old text
					box.setText('')
					txt_len = 0
					clear = ''
				
				# Otherwise the box should be inactive
				else:
					# Will no longer accept input
					active = False
					
					# Set the box text back to the default
					if txt_len == 0:
						box.setText(default_txt)

				# Change the color of the box
				current_color = active_color if active else inactive_color
				
				# If the click event occured within the button
				if button.collidepoint(e.pos):
	
					# Check the pasword
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
						
						# Decrease the length
						txt_len -= 1
						
						# Ensure that length stays within correct bounds
						if txt_len < 0:
							txt_len = 0
					
					# Check if the unicode is a function key or not
					# (Shift, Tab, etc. will result in '' when checking the unicode)
					elif e.unicode != '':
						# If the text to be rendered is inside of the bounds of the box
						if (box.getFontSize() * (txt_len + 1)) < box.getBox().w:
							# Append a password character to the text
							box.setText(box.getText() + '⬤')
						
						# Append the unicode character to our cleartext
						clear += e.unicode

						# Increase the length
						txt_len += 1
		
		# Color the screen
		screen.fill((30, 30, 30))

		# Draw the elements
		box.drawBox(screen)
		p.draw.rect(screen, button_color, button, 0)

		# Render the text as a surface
		txt_surf1 = box.createRender()
		txt_surf2 = font.render(button_text, True, btn_txt_color)
		
		#### DEBUG DICTIONARY PRINTING ####

		# Position variables
		temp_x = 20
		temp_y = 20

		# Debug text
		debug = 'Debug:'

		# Render as surface
		temp_surf = font.render(debug, True, p.Color('white'))

		# Blit text to the screen
		screen.blit(temp_surf, (temp_x, temp_y))
		
		# Check the password check dictionary
		for key in pass_dict:
			# Render each key in a new line
			temp_y += txt_size + 5

			# Grab the value from the dictionary
			debug = f'{key}: {pass_dict[key]}'

			# Render as surface
			temp_surf = font.render(debug, True, p.Color('white'))

			# Blit text to screen
			screen.blit(temp_surf, (temp_x, temp_y))
		
		# Blit text to screen
		box.blit(screen, txt_surf1)
		screen.blit(txt_surf2, (int(button.x + (button.w / 4)), button.y + 5))

		# Update the screen
		p.display.flip()

		# Ensure the clock is in line with 60 frames per second
		clock.tick(60)

if __name__ == "__main__":
	# Initialize pygame for our system
	p.init()

	# Run the main
	main()

	# If we exit the main loop, quit the program
	p.quit()
