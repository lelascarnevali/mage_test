#!/bin/bash

# Comando para construir a imagem Docker
docker build -f Docker/Dockerfile --force-rm -t mage-image .

# Comando para criar e executar o contêiner baseado na imagem
docker run -it -p 6789:6789 --rm --name mage mage-image