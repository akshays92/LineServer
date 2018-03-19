echo "Indexing $1 on server"
python3 ./Indexer.py $1
echo "Total number of lines: "
wc -l $1