FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN cd /usr/src/app && git clone https://github.com/hooverken/python-stuff.git

CMD [ "python", "./rotateImageFromBlobContainer.py" ]