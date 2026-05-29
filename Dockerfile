FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["highrise", "bot:Bot", "64402679da989c06560c4cf6", "d27ef92384b8f1de2cd3b72760e07f36fa21208ee4c7d6e7b81a48737718866a"]
