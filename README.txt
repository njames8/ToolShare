Files Included:
	manage.py    - file to start up server for website as well as editing other 
	                aspects such as adding a superuser or changing passwords.

	runserver.bat- runs command to start up server for website

	db.sqlite3   - sample database the store users and user information

	All files in toolShare and users directories:
	             - contains .html and .py files used to run and display 
				   the website 		


Requirements for Installation:
		-Python 3 with Django 1.6

	
To access the ToolShare website:
	1. Unzip the toolShare.zip folder
	2. Double click on runserver.bat and leave the cmd window open
	3. Open your favorite web browser
	4. Type http://127.0.0.1:8000 into the url
	5. Press enter
	6. Enjoy your ToolShare experience
	
TROUBLESHOOTING
===============
	  
	- The http://127.0.0.1:8000/about and http://127.0.0.1:8000/contact
	  pages should be accessible by anyone and a user is not required
	  to be logged in in order to see them
	  
	- The administration page is accessible at 	  http://127.0.0.1:8000/admin
	  Username: admin
	  password: admin
	  This admin account should be able to edit all users and databases.
	  
	  ONLY USE THESE CREDENTIALS TO ACCESS THE ADMIN PORTION OF THE SITE
	  DO NOT USE THE ADMIN CREDENTIALS TO LOG INTO TOOLSHARE-IT WILL ERROR OUT
	

==========
Known Bugs
==========

	-When creating a shed or tool, if wrong info is put in, it appears that the tool was created, but it actually wasn't. Click the create button again, and the form is filled out.

	-Can add tools to any sheds

	-

Please contact Nick James at nxj2348@rit.edu about any bugs experienced