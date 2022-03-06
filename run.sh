#!/bin/bash

for ((i=0;i<=53;i++)) 
do 
    for ((j=0;j<=36;j++))
    do
        echo "${i}_k${j}.csv"
        java -cp "target/grammarviz2-0.0.1-SNAPSHOT-jar-with-dependencies.jar" net.seninp.grammarviz.GrammarVizAnomaly -alg RRA -i dataset_yidong/curves_no_header/${i}_k${j}.csv -w 5 -p 3 -a 3
    done
done