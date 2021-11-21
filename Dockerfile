FROM ubuntu
WORKDIR */Lab2
COPY lotto_example.py .
EXPOSE 8080
CMD ["html","testHelloWorld.html"]