FROM python:3.6.12

WORKDIR /home/


ENV STREAMLIT_APP = app.py

COPY requirements.txt .
COPY pip.conf /home/lu/桌面/tp1/pip.conf

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
