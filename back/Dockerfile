FROM python:3.12

WORKDIR /back

COPY app.py /back
COPY requirements.txt /back

RUN ["pip", "install" ,"--no-cache-dir", "-r", "requirements.txt"] 

EXPOSE 5000

# CMD ["flask", "run"]
CMD ["python3", "app.py"]
