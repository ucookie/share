FROM python:3.9.6-slim-buster

COPY data /workdir/data
COPY server/main3.py /workdir/main.py

RUN sed -i s@/[a-z]*.debian.org/@/mirrors.aliyun.com/@g /etc/apt/sources.list \
    && pip3 config set global.index-url https://mirrors.aliyun.com/pypi/simple \
    && apt-get update -y \
    && pip3 install --no-cache-dir web.py==0.62 Pillow==8.3.1 tensorflow==2.5.0 \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone \
    && rm -rf /var/cache/apt/* \
    && rm -rf /root/.cache \
    && rm -rf /tmp/*

ENV PYTHONUNBUFFERED 1
WORKDIR /workdir
EXPOSE 8888

CMD ["python3", "main.py"]

# docker build -t practice:latest -f build/Dockerfile .