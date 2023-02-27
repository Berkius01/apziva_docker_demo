FROM python:3.9

RUN mkdir /code
WORKDIR /code
RUN pip install django==3.2 pyscopg2 pyscopg2-binary selenium webdriver_manager bs4

EXPOSE 8000
CMD ["python3", "mnage.py", "runserver", "0.0.0.0:8000"]
