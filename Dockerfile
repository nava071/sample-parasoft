
FROM mcr.microsoft.com/playwright:v1.28.0-focal
WORKDIR /parasoft
COPY . /parasoft
RUN apt-get update && \
    apt-get install -y python3-pip && \
    python3 -m pip install --upgrade pip && \
    pip install -r requirements.txt && \
    playwright install --with-deps
# CMD ['pytest', '-s', '-v', '--browser', 'firefox', '--headed', '--slowmo', '500', '--output=.\output', '--video=on', '--screenshot=only-on-failure']