# Created by: Nicholas Brean
# Created on: September 2017
# Created for: ICS3UR-1
# This program Calculates the circumference of any circle

import ui

def calculate_Circumfrance(sender):
	#radius
	
	#extra variables
	PI = 3.14
	
	#input
	radius = int(view['Radius_TextField'].text)
	
	#process
	area = 2*PI*radius
	
	#output
	view['answer_label'].text = 'The Area of the circle is: ' + str(area) + ' cm'

view = ui.load_view()
view.present('sheet')
