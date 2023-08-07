FROM ubuntu:20.04

COPY requirements.txt ./

RUN apt update && apt upgrade -y 
RUN apt install telnet vim git python3 python3-pip -y --no-install-recommends openjdk-11-jre

RUN pip3 install -r ./requirements.txt

# Excluir a pasta Mage-Development, se ela existir
RUN rm -rf ./Mage-Development

# Criando um Mock do S3 para um lake
RUN mkdir -p ./S3/Gold
RUN mkdir -p ./S3/Silver
RUN mkdir -p ./S3/Bronze

# Executar o comando git clone
RUN git clone https://github.com/lecarnevali/Mage-Development.git

CMD mage start Mage-Development
