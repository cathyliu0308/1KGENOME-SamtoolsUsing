#!/bin/bash

function process()
{
	filename=ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/phase3/data/$1/alignment/$2
        wget $filename
	wget $filename.bai

	samtools view -u $2 $3:$4-$5 | samtools mpileup -f $6 - > $2.mpileup
	#./samtools view -u $2 $3:$4-$5 | ./samtools mpileup -f $6 - > $2.mpileup
	./read_count $2.mpileup data/$2.read_count $4 $5

	rm $2.mpileup
        rm $2
	rm $2.bai
}

if [ ! -f read_count ]
then
        g++ -o read_count read_count.cpp
fi

if [ ! -d data ]
then
        mkdir data
fi

if [ ! -f cat_all_read_count ]
then
        g++ -o cat_all_read_count cat_all_read_count.cpp
fi

while read sample
do
	read file
	process $sample $file $3 $4 $5 $6 &
    while (( $(jobs | wc -l) >= $1 )); do
        sleep 0.1
        jobs > /dev/null
    done
done < $2

wait

./cat_all_read_count $2 > cat_command.sh

bash cat_command.sh > chr$3.$4-$5.read_count
