FROM python:3.7


COPY ./chorder_app /chorder_app

WORKDIR /chorder_app

RUN pip install fastapi uvicorn
RUN pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "chorder_api:chorder", "--host", "0.0.0.0", "--port", "80"]

