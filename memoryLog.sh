#!/bin/bash

# echo "Quanto tempo vai executar (segundos): "
# read timeExe
# end=$((SECONDS+$timeExe))

echo "tempo,       mem, livreMem, swap, livreSwap, cpu, disponivel" > 200kb.csv

while : 
do
    
    # hora=$(date +"%T")
    
    mem=$(free --mega| grep Mem | cut -c28-32)
    livreMem=$(free --mega| grep Mem | cut -c40-44)
    swap=$(free --mega| grep Swap| cut -c29-34)
    livreSwap=$(free --mega| grep Swap| cut -c40-44)
    cpu=$(mpstat | grep all | cut -c21-27 | tr ',' '.')
    disponivel=$(free --mega| grep Mem | cut -c76-80)
    
    echo "$SECONDS,   $mem, $livreMem, $swap, $livreSwap, $cpu, $disponivel" >> 200kb.csv
    
    sleep 1
    
done
