#first we create the virtual environment
python3 -m venv opendotaenv

#then we need to activate the environment
source opendotaenv/bin/activate

#we always add the newly installed libraries to requirements file
pip freeze > requirements.txt

#then we install the requirements 
pip install -r requirements.txt

#now you can run the .py files from terminal
python test_1.py