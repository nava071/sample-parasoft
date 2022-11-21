
FROM mcr.microsoft.com/playwright:v1.28.0-focal
WORKDIR /parasoft
COPY . /parasoft
RUN apt-get update && \
    apt-get install -y python3-pip && \
    python3 -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    playwright install --with-deps
ENTRYPOINT ["pytest","-s","-v","--slowmo","500","--output=./results","--video=on","--screenshot=only-on-failure","--browser"]