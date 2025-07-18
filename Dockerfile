FROM public.ecr.aws/docker/library/python:alpine3.18
WORKDIR /app
COPY app.py .
RUN pip install flask
CMD ["python3", "app.py"]
