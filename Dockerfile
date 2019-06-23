FROM python:3.6

COPY . .
RUN pip install -r requirements.txt

CMD [ "python", "run_test.py" ]
CMD [ "python", "run.py" ]
