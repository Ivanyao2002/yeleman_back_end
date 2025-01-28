FROM python:3.11

LABEL authors="Ivan Yao"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Si le dossier n'existe pas le container le crée et le selectionne
WORKDIR /app

COPY requirements.txt /app/requirements.txt

# ignorer le cache; reduire la taille de l'executable
RUN python -m pip install --upgrade pip &&\
    python -m pip install --no-cache-dir -r requirements.txt

COPY . /app/
COPY src/.env /app/.env

# Le conteneur ecoutera sur le port 8090
EXPOSE 8090

CMD ["python","src/manage.py","runserver","0.0.0.0:8090"]