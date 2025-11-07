FROM ubuntu:latest
WORKDIR /app
EXPOSE 5000/tcp
COPY hello.py .
COPY hello.sh .
COPY run_flask_app.sh .
RUN apt update
RUN apt install -y sudo
RUN chmod +x hello.sh run_flask_app.sh
RUN ./hello.sh
ENTRYPOINT ["bash", "./run_flask_app.sh"]
