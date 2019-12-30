FROM stash1001/openalpr

RUN  apt-get update && apt-get install -y python-pip && apt-get clean
RUN pip install Flask
COPY app.py app.py 
EXPOSE 5000/tcp

entrypoint []
CMD python app.py