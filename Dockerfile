FROM python:3

WORKDIR /usr/src/app

RUN pip install pillow
RUN pip install requests

COPY . .

CMD [ "python", "./rotateImageFromBlobContainer.py" ]
