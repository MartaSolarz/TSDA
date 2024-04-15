#!/bin/bash

# 1)
wget https://wolnelektury.pl/media/book/txt/zemsta.txt -O zemsta.txt

# 2)
grep -n "^AKT" zemsta.txt

# 3)
NUMBERS=($(grep -n "^AKT" zemsta.txt | cut -d':' -f1))
NUMBERS+=($(wc -l < zemsta.txt))

for (( i=0; i<${#NUMBERS[@]}-1; i++ )); do
  LINES=$((${NUMBERS[$i+1]} - ${NUMBERS[$i]} + 1))
  head -n ${NUMBERS[$i+1]} zemsta.txt | tail -n $LINES > "akt$((i+1)).txt"
done

# 4)
for FILE in akt*.txt; do
  echo "Scen w $FILE: $(grep -c "^SCENA" $FILE)"
done

# *3)
NUMBERS=($(grep -n "^AKT" zemsta.txt | cut -d':' -f1))
NUMBERS+=($(wc -l < zemsta.txt))

for (( i=0; i<${#NUMBERS[@]}-1; i++ )); do
  START=${NUMBERS[$i]}
  END=$((${NUMBERS[$i+1]}-1))
  sed -n "${START},${END}p" zemsta.txt > "akt$((i+1)).txt"
done

# 5)
echo "Liczba wystąpień 'Mocium panie': $(grep -io "mocium panie" zemsta.txt | wc -l)"
