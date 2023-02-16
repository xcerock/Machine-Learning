#!/bin/bash

SERVER=https://raw.githubusercontent.com/AndresMpa/Computacion_blanda/main/Software/regresiones_lineales/modelo_1
FILENAME=HappinessAlcoholConsumption.csv

wget $SERVER/$FILENAME -P ../data/

if [! -f ../data/$FILENAME]; then
  echo "Unexpected error"
  exit 1
else
  exit 0
fi
