FROM python:3.12

WORKDIR /worker

COPY worker.py /worker
COPY chromedriver.exe /worker
COPY requirements.txt /worker

RUN ["pip", "install" ,"--no-cache-dir", "-r", "requirements.txt"] 

ENV POSTGRES_USER=root
ENV POSTGRES_PASSWORD=root
ENV POSTGRES_DB=multi-feed
ENV IGLOGIN=ZIOMAL123123
ENV IGPASS=ZIOMAL123123pass

CMD ["python3", "worker.py"]
