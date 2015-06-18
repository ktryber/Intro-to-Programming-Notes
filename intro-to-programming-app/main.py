#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import urllib
import cgi

from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext.webapp.template import render
from os import path


import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"))

class Handler(webapp2.RequestHandler):

	def get(self):
		title = "Kris Tryber Intro to Programming"
		user = users.get_current_user()

		template_vars = {
			'title': title,
			'user': user,
			'login': users.create_login_url(self.request.uri),
            'logout': users.create_logout_url(self.request.uri),
		}

		# renders my base html page
		template = JINJA_ENVIRONMENT.get_template('base.html')
		self.response.out.write(template.render(template_vars))


	

class Stage1(Handler):
	def get(self):
		title = "Kris Tryber Intro to Programming Stage 1"
		user = users.get_current_user()

		concepts_1_1 = [

		["HTML Notes", "Browsers are built to read pages of HTML code that then display text. HTML is written with a series of elements and tags that are organized in tree like structures from biggest to smallest. CSS then comes in to make that content have color, borders, flexible structure so that webpages can be viewed on different screen sizes, etc." ]
		]
		 
		concepts_1_2 = [

		["Inline vs. Block Elements", "HTML elements can either be inline or block.<h3>Inline</h3><p>Elements that appear inline with the text and do not have an invisible box around them.</p><ul><li>span</li><li>a</li><li>img</li></ul><h3>Block</h3><p>Elements that have invisible boxes around them, most important for taking a mockup from a pdf format to HTML.</p><ul><li>h1,h2,h3</li><li>p</li><li>div</li></ul>"],

		["Text Editor", "I'm using Sublime Text, I've used it while learning PHP and Wordpress."],

		["HTML Structure", "HTML code is written in a tree like structure to provide easier code readability. The indentation within the code presents to code in a readable fashion and allows you to stay organized when you have multiple elements working together."],

		["Box Model", "<p>The Box model:<br><span class=""margin-color"">Margin</span> - Surrounds the box and serves as the space between the boxes<br><span class=""border-color"">Border</span> - Borders the padding and the content<br><span class=""padding-color"">Padding</span> - The padding clears the area around the content and takes the background color of the box, protects the content in the box.<br><span class=""content-color"">Content</span> - This is the image or the text or the center of the box model.<br> </p><div class=""outer-box""><div id=""box-model"" class=""box"">Content...   </div></div>"],

		["Box Sizing Techniques", "<ol><li>Set box sizes in percentages rather than pixels so that it changes with the browser size.</li><li>Set the box-sizing attribute to border-box for every element. see the CSS for the code.</li><li>Boxes are block style elements so before adjusting they will always take the whole width of the page. adding the display:flex; code to the surrounding div will allow them to appear next to each other.</li></ol>"],

		["Code, Test, Refine", "<ol><li>Look for natural boxes</li><li>Look for repeated styles and semantic elements</li><li>Write your HTML</li><li>Apply styles from biggest to smallest</li><li>Fix things</li></ol>"],

		["Looking for errors in HTML and CSS", "<ul><li><a href=""http://validator.w3.org/#validate_by_input"">To verify HTML</a></li><li><a href=""http://jigsaw.w3.org/css-validator/#validate_by_input"">To verify CSS</a></li></ul>" ]

		]
		

		#variables to pass into the template
		template_vars = {
			'title': title,
			'user': user,
			'login': users.create_login_url(self.request.uri),
            'logout': users.create_logout_url(self.request.uri),
            'concepts_1_1': concepts_1_1,
            'concepts_1_2': concepts_1_2,
		}
		template = JINJA_ENVIRONMENT.get_template('stage1.html')
		self.response.out.write(template.render(template_vars))

		


	

class Stage2(Handler):
	def get(self):
		title = "Kris Tryber Intro to Programming Stage 2"
		user = users.get_current_user()
		concepts_2_1 = [

		["Notes Link", "<a href=""https://www.evernote.com/shard/s250/nl/32113319/ebce4900-4c30-46bb-a628-6d7a8801125a/"">Stage 2 Lesson 1:Evernote Notes</a>"],

		["Programming Intro", "The programs you'll write in this class will be Python code. Those will be input to another program which is a Python interpreter that follows the instructions in your code and it does that by following the instruction in its code... and you'll be able to run all that using your web browser.<ul><li>Computers need programs to tell them what to do.</li><li>The computer will need a very precise sequence of steps to tell it how to behave.</li><li>Python is an interpreter that takes our code and tells the computer how to react.</li><li>We have to use exact grammar and everything must be spelled perfectly for the code to actually figure out what we want it to do. It cannot guess like a human would based on the information given.</li></ul>"],

		["Python Grammar", "Examples:Python grammer to arithmetic expressions<br>Expression > Expression Operator Expression<br>Expression > Number<br> Operator > +<br>Operator > *<br>Number > 0,1...<br>Expression > (Expression)<br><br>example:<br> Expression<br>Expression Operator Expression<br>Number + Number<br>1 + 1<br><br>Expression<br> Expression Operator Expression<br>Expr Opr Expr + Number<br>Number * Expr Opr Expr<br>2 * 1+1<br>" ]

		]

		concepts_2_2 = [

		["Notes Link", "<a href=""https://www.evernote.com/shard/s250/nl/32113319/f23bfc48-77a7-4a9f-8ce5-16949690d093/"">Stage 2 Lesson 2:Evernote Notes</a>"],

		["Varable Assignment", "<ul><li>To introduce a variable to python you need to use an ""Assignment Statement"".</li><li>Variable names can only have letters, numbers and underscores and must begin with an underscore or letter.</li></ul><p>example: name = expression<br>speed_of_light = 299792458<br>billionth = 1.0 / 1000000000<br></p><ul><li>= means assignment, think of it as an arrow.</li><li>When you use the same variable name later in Python code with a different value the old variable will still exist but it will be overwritten with the new variable value.</li></ul>"],

		["Strings", "A sequence of characters surrounded by single quotes or double quotes. You can 'start the string' in single quotes and ""end the string"" in double quotes.  If a string starts with a single quote it must end in a single quote and vice vera.<br>ex:<br>print 'Hello'<br>print ""Hello"""],

		["Concatenation", "Close your strings and put a spcae and plus symbol between them.<br>ex:<br>'Hello'"" + "'!'"" " = " "Hello!"""],

		["Indexing Strings", "string[expression]<br>ex:<br>'udacity'[1+1] -- 'a'<br><br>name = 'kris'<br>print name[0] -- 'k'"], 

		["Selecting Sub-Sequences", "string[expression>:expression]<br>s         number        number <br><br>- String that is a subsequence of the characters in s starting from position start and ending with position stop<br>ex:<br>word = 'assume'<br>print word[3] prints u<br>print word[3:4] prints u<br>print word[4:6] prints me<br>print word[4:] prints me<br>print word[:2] prints as<br>print word[:] prints assume<br><br>-If you want to add something to your selection like an uppercase ""A"" instead of a lower case a like in our variable ""word"" you would need to select ""ssume"" and concatenate it with ""A"". ex:<br><br>ex:<br>print 'A' + word[1:]"],

		["Finding Strings in Strings", "Find is a method in Python.<br>string.find(string) = number that gives first position in search string where the target string appears. If the target is not found it will output -1.<br><br>"],

		["Adding Parameters to Find", "string.find(string,number) = If there are multiple occurences of your find you can decide where to start the results of your find with a number parameter."],

		]

		concepts_2_3 = [

		["Notes Link", "<a href=""https://www.evernote.com/shard/s250/nl/32113319/1b77d660-998b-4538-b5c9-297f4865dc14/"">Stage 2 Lesson 3:Evernote Notes</a>"],

		["Functions and Procedures", "- def = Define<br>- Using Procedures:<br>procedure(input, input, input)<br>return output<br><br>ex:<br>def sum3(c, d, e):<br>return c + d + e<br><br>print sum3(1,2,3)<br>print sum3(93,53,70)<br>"],
										
		]

		concepts_2_4 = [

		["Equality Comparisons", "Equalities in Python produce a true or false (boo lean) result. You can use less than, Greater than, less than or equal to, greater than or equal to and is not equal to (!=).<br><br>Double equal is ""equal to""."],

		["if", "If allows you to write code that executes equality statements."], 

		["else", "Else statements will run when the if statement is not true.  Is 1 greater than 2, if yes true else false."],

		["While", "While loops allow us to execute a test expression within a procedure over and over again until as long as it is true, when it becomes false it will stop and continue to the next piece of code.<br><br>Break: Allows a while loop to stop even if it is true so you can get out of the loop and execute the following code."],

		]

		concepts_2_5 = [

		["Notes Link", "<a href=""https://www.evernote.com/l/APphiRXQFChEeJVHvnLyy1P0w18cfmMmFYw"">Stage 2 Lesson 5: Evernot Notes</a>"],

		["String vs. List", "A string is a sequence of characters and a list can be a sequence of anything. you can access things in a list by indexing similiar to how you would index a string."],

		["Mutation", "Allows you to change the value of the elements inside a list after it has been created."],

		["Aliasing", "Having two different ways to refer to the same object in programming. If you have two variables that refer to the same object it will change the value for both variables."],

		["Append", "A method that adds a new element to the end of a list. It mutates an existing list instead of creating a new list to add the new element."],

		["len()", "Short for length, pass in an object that you want to know the length for."],

		["Index", "Index can be used to produce the position of an element within a list. If it's true it wil  return the postion if th's false it will produce an error. In lesson 5 we used index with an if statement thus allowing us to produce an else without error.<br><br>if t in p:return p.index(t)else:return -1"],

		["Add AND Assignment Operator", "Adds the right operand to the left operand and assigns the result to the left operaand. c += is equivalent to c = c + a"]
		]


		template_vars = {
			'title': title,
			'user': user,
			'login': users.create_login_url(self.request.uri),
            'logout': users.create_logout_url(self.request.uri),
            'concepts_2_1': concepts_2_1,
            'concepts_2_2': concepts_2_2,
            'concepts_2_3': concepts_2_3,
            'concepts_2_4': concepts_2_4,
            'concepts_2_5': concepts_2_5,
		}
		template = JINJA_ENVIRONMENT.get_template('stage2.html')
		self.response.out.write(template.render(template_vars))

class Stage3(Handler):
	def get(self):
		title = "Kris Tryber Intro to Programming"
		user = users.get_current_user()
		template_vars = {
			'title': title,
			'user': user,
			'login': users.create_login_url(self.request.uri),
            'logout': users.create_logout_url(self.request.uri),
		}
		template = JINJA_ENVIRONMENT.get_template('stage3.html')
		self.response.out.write(template.render(template_vars))

class Stage4(Handler):
	def get(self):
		title = "Kris Tryber Intro to Programming"

		lesson_title_boxes = ["Lesson 1", "Lesson 2"]
		titles = ["one", "two"]

	


		user = users.get_current_user()
		template_vars = {
			'title': title,
			'lesson_title_boxes': lesson_title_boxes,
			'titles': titles,
			'user': user,
			'login': users.create_login_url(self.request.uri),
            'logout': users.create_logout_url(self.request.uri),
		}
		template = JINJA_ENVIRONMENT.get_template('stage4.html')
		self.response.out.write(template.render(template_vars))

app = webapp2.WSGIApplication([

('/', Handler),
('/stage1', Stage1),
('/stage2', Stage2),
('/stage3', Stage3),
('/stage4', Stage4),
], debug=True)


