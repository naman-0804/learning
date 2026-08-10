FROM python:3.11

WORKDIR /workspace

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install ipykernel

CMD ["sleep", "infinity"]