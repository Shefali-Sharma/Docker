PID=$!
sleep 2
kill PID
docker build -t friendlyhello .
docker run -p 4200:80 friendlyhello