echo "Indexing $1 on server"
python3 ./Indexer.py $1
echo "Total number of lines: "
wc -l $1
python3 ./server_v1.py