FROM python
COPY . /cucciapi.py

EXPOSE 80

CMD [ "python","cucciapi.py" ]