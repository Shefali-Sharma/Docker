osascript -e 'tell app "Terminal"
    do script "docker build -t friendlyhello ."
    do script "docker run -p 4005:80 friendlyhello"
end tell'
echo 'Hi there!'


    