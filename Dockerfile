FROM stash1001/alpr-unconstrained-image

RUN pip install Flask
COPY src/ ./


EXPOSE 5000/tcp

entrypoint []
CMD python app.py