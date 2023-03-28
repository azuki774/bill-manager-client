FROM python:3.11-bullseye
RUN python -m pip install --upgrade pip
COPY requirement.txt /requirement.txt
RUN pip install -r /requirement.txt
COPY src/ /src/
ENTRYPOINT ["python3", "-u", "/src/main.py"]
