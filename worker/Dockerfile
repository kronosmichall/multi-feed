FROM python:3.12

WORKDIR /worker

COPY worker.py /worker
COPY chromedriver.exe /worker
COPY requirements.txt /worker

RUN ["pip", "install" ,"--no-cache-dir", "-r", "requirements.txt"] 
RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "libglib2.0-0", "libnss3", "libgconf-2-4", "libfontconfig1"]
ENV POSTGRES_USER=root
ENV POSTGRES_PASSWORD=root
ENV POSTGRES_DB=multi-feed
ENV IGLOGIN=ZIOMAL123123
ENV IGPASS=ZIOMAL123123pass
ENV DISPLAY=:99

CMD ["python3", "worker.py"]
