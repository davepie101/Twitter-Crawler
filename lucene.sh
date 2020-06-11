mkdir index
echo "Injecting data into Lucene"
python3 index.py 
echo "Starting web application"
python3 app.py