import pygame as p
import sys as s
from time import time as t
from pygame.locals import *

#### Stuff for password checking ####
def check_pass(password: str) -> dict:

	my_dict = {
		'total': None,
		'hasUp': None,
		'hasLow': None,
		'hasNum': None,
		'hasSym': None,
		'numBools': None
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

			# Iterate over all of the characters
			for j in range(len(all_chars)):

				# If the character is found 
				if all_chars[j] == password[i]:
					cracked += all_chars[j]

	# Set the end time
	end = t()
	
	# Total time that it took to crack the password
	total = end - start
	my_dict['total'] = total

	numBools = 0
	# Check the strength of the password
	for i in range(len(cracked)):

		if cracked[i] in upper and not hasUp:
			hasUp = True
			numBools+= 1

		elif cracked[i] in lower and not hasLow:
			hasLow = True
			numBools += 1

		elif cracked[i] in numbers and not hasNum:
			hasNum = True
			numBools += 1

		elif cracked[i] in symbols and not hasSym:
			hasSym = True
			numBools += 1

	# Assign values to the dictionary
	my_dict['hasUp'] = hasUp
	my_dict['hasLow'] = hasLow
	my_dict['hasNum'] = hasNum
	my_dict['hasSym'] = hasSym
	my_dict['numBools'] = numBools

	return my_dict

#### Main loop for the program ####
def main():
	
	# Pygame variables
	# -------------------------

	# Get user's screen size
	disInfo = p.display.Info()

	# Set the screen size and the caption
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
	unifont = p.font.Font('seguisym.ttf', int(txt_size / 2))
	
	box_x = int((max_w - 260) / 2)
	box_y = int(max_h / 2) - 50

	# Our inbut box
	box = p.Rect (
		# Horizontal position
		box_x,
		# Vertical position
		box_y, 
		# Width
		150, 
		# Height
		txt_size
	)

	# Colors for if the box is clicked on or not
	inactive_color = p.Color('darkslategray3')
	active_color = p.Color('darkslategray1')

	# Change the color of the box
	current_color = inactive_color

	# If the box currently active?
	active = False

	# The text that will go into the box
	default_txt = 'Check your password here...'
	text = ''
	clear = ''
	txt_len = len(text)

	# Button variables
	# ----------------------------

	# Pressable button
	button = p.Rect (
		box_x + 50, 
		box_y + 50, 
		150, 
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

	# Text that is given to the user
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
				if box.collidepoint(e.pos):
					active = True
					default_txt = ''

				else:
					active = False

					if txt_len == 0:
						default_txt = 'Check your password here...'

				# Change the color of the box
				current_color = active_color if active else inactive_color
				
				# If the click event occured within the button
				if button.collidepoint(e.pos):
	
					# Check the pasword
					pass_dict = check_pass(clear)

					# Debug text
					debug = 'Debug:\nTotal Time: ' + str(pass_dict['total']) + '\nhasUp: ' + str(pass_dict['hasUp']) + '\nhasLow: ' + str(pass_dict['hasLow']) + '\nhasNum: ' + str(pass_dict['hasNum'])  + '\nhasSym: '  + str(pass_dict['hasSym']) + '\nStrength: ' + str(pass_dict['numBools'])

					# Clear out the text
					text = clear = ''


			# Keyboard event
			if e.type == p.KEYDOWN:
				
				# Check if the box is currently active
				if active:
					# If the user presses Enter
					if e.key == p.K_RETURN:
						# Reset the text to the default
						default_txt = 'Check your password here...'

						# Check the password
						pass_dict = check_pass(clear)
					
						# Debug text		
						debug = 'Debug:\nTotal Time: ' + str(pass_dict['total']) + '\nhasUp: ' + str(pass_dict['hasUp']) + '\nhasLow: ' + str(pass_dict['hasLow']) + '\nhasNum: ' + str(pass_dict['hasNum'])  + '\nhasSym: '  + str(pass_dict['hasSym']) + '\nStrength: ' + str(pass_dict['numBools'])	

						# Clear out the text
						text = clear = ''

					# If the user presses Backspace
					elif e.key == p.K_BACKSPACE:

						# Check if the text to be rendered is within the bounds of the box
						if ((txt_size / 2) * txt_len) <= box.w:
							# Delete a character of text
							text = text[:-1]
							clear = clear[:-1]
						
						# Decrease the length
						txt_len -= 1

						if txt_len < 0:
							txt_len = 0

					else:
						# If the text to be rendered is outside of the bounds of the box
						if ((txt_size / 2) * txt_len + 1) < box.w:
							# Append a password character to the text
							text += '⬤'

						clear += e.unicode
						txt_len += 1
		
		# Color the screen
		screen.fill((30, 30, 30))

		# Change the width of the box if necessary
		width = 300
		box.w = width

		# Draw the elements
		p.draw.rect(screen, current_color, box, 2)
		p.draw.rect(screen, button_color, button, 0)

		# Render the text as a surface
		txt_surf = unifont.render(text, True, current_color)
		txt_surf2 = font.render(default_txt, True, current_color)
		txt_surf3 = font.render(button_text, True, btn_txt_color)
		txt_surf4 = font.render(debug, True, p.Color('white'))
		
		# Blit the text
		screen.blit(txt_surf, (box.x + 5, box.y + 5))
		screen.blit(txt_surf2, (box.x + 5, box.y + 5))
		screen.blit(txt_surf3, (button.x + 20, button.y + 5))
		screen.blit(txt_surf4, (20, 20))

		# Update the screen
		p.display.flip()
		clock.tick(60)

if __name__ == "__main__":
	p.init()
	main()
	p.quit()
