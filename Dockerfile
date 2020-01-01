FROM stash1001/openalpr

RUN  apt-get update && apt-get install -y python3-pip && apt-get clean
RUN pip3 install Flask
COPY src/ ./

# Copy python 2 module to python3 dir
RUN cp -R /usr/lib/python2.7/dist-packages/openalpr /usr/lib/python3/dist-packages/openalpr 

EXPOSE 5000/tcp

entrypoint []
CMD python3 app.py