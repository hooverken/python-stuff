FROM python:3

# ARG SP_USERNAME
# ARG SP_PASSWORD
# ENV SP_APPLICATION_ID ${SP_USERNAME}
# ENV SP_APPLICATION_SECRET ${SP_PASSWORD}

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./rotateImageFromBlobContainer.py .

CMD [ "python", "./rotateImageFromBlobContainer.py" ]