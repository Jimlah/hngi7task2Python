FROM python:3.7
ADD . /img_resizer
WORKDIR /img_resizer
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD python api.py