FROM python:3.9

#Copy files needed for the app to run
COPY ./Bakerapp /Bakerapp
COPY ./Launch_Codes/client_secrets.json /Bakerapp/client_secrets.json
WORKDIR /Bakerapp
RUN pip install -r requirements.txt

#The EXPOSE instruction informs Docker that the container listens on the specified network ports at runtime.
EXPOSE 8000

CMD ["gunicorn", "-c", "gunicorn.conf.py", "wsgi:app"]