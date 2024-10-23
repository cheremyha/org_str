FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /doc_app
ADD . /doc_app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Command to build container and start it.
# docker build --tag docker_org_str .
# docker-compose up
# docker-compose up -d --build
# docker-compose down --volumes