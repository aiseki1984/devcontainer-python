FROM python:3.11.9-bookworm
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y zlib1g-dev libzip-dev libpq-dev mariadb-client tzdata zip unzip git wget

# # Go 1.22.2をダウンロードしてインストール
# RUN wget https://go.dev/dl/go1.22.2.linux-amd64.tar.gz -O /tmp/go1.22.2.linux-amd64.tar.gz \
# && tar -C /usr/local -xzf /tmp/go1.22.2.linux-amd64.tar.gz \
# && rm /tmp/go1.22.2.linux-amd64.tar.gz

# # Goのパスを設定
# ENV PATH="/usr/local/go/bin:${PATH}"

# # mailpit コマンドをインストール
# # - インストール先が /root 配下だと Web サーバーから実行できないので、/usr/local/bin へ移動
# RUN go install github.com/axllent/mailpit@latest \
#  && mv /root/go/bin/mailpit /usr/local/bin

WORKDIR /workspace

ADD requirements.txt /workspace
RUN pip install -r requirements.txt