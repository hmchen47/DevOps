FROM python:3.5
RUN pip install Flask==0.11.1 redis==2.10.6
RUN useradd -ms /bin/bash james
WORKDIR /app
COPY app /app
RUN chown -R james:james /app/* 
USER james
CMD ["ls", "-al"]
CMD ["chmod", "+rx", "app.py"] 
CMD ["python", "app.py"] 
