FROM python:3.9

#Copy files needed for the app to run
COPY ./Webapp /Webapp
COPY ./Launch_Codes/keys.json /Webapp/keys.json
WORKDIR /Webapp
RUN pip install -r requirements.txt

#The EXPOSE instruction informs Docker that the container listens on the specified network ports at runtime.
EXPOSE 8000

CMD ["gunicorn", "-c", "gunicorn.conf.py", "wsgi:app"]