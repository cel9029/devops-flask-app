FROM ubuntu:latest
WORKDIR /app
EXPOSE 5000/tcp
COPY hello.py .
COPY hello.sh .
COPY run_flask_app.sh .
RUN apt update
RUN apt install -y sudo
RUN ./hello.sh
ENTRYPOINT ["./run_flask_app.sh"]
