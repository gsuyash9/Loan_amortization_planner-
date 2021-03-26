# Requirements
  Python 3.6
  And additional requirements are in requirements.txt and will be installed through the below steps

# How to get started
  Download and install python 3.6 and git
# Download
  Go to https://loan-amortization-planner.herokuapp.com/
# Run
	# Install virtualenv
  		on Ubuntu: $ sudo apt install python-virtualenv
		on Windows Powershell $ pip install virtualenv
	
   	# Create a virtual environment
		on Ubuntu: $ virtualenv env -p python3.6
  		on Windows: $ virtualenv env
   	# Activate the env:
		on Ubuntu: $ source env/bin/activate
  		on Windows: $ ./env/scripts/activate
   	# Install the requirements: 
  		$ pip install -r requirements.txt
  
  	Make migrations $ python manage.py makemigrations

  	Migrate the changes to the database $ python manage.py migrate

  	Run the server $ python manage.py runserver --noreload

