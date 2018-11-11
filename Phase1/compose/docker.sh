osascript -e 'tell app "Terminal"
    activate
    do script "cd /Users/shefali9222/Documents/GitHub/Docker/Phase1/compose" & ";" & "docker-compose build" & ";" & "docker-compose up"
end tell'
