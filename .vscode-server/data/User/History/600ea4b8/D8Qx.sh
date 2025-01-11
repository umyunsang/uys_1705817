#!/bin/bash

VIRTUAL_ENV="/home/uys_1705817/api/venv"  # 가상환경 경로
FLASK_COMMAND="flask run --host=0.0.0.0 --port=15022"  # Flask 실행 명령
LOG_FILE="flask.log"
PID_FILE="flask.pid"

case "$1" in
    start)
        if [ -d "$VIRTUAL_ENV" ]; then
            source "$VIRTUAL_ENV/bin/activate"
        else
            echo "가상환경을 찾을 수 없습니다: $VIRTUAL_ENV"
            exit 1
        fi

        if [ -f "$PID_FILE" ] && kill -0 $(cat "$PID_FILE") 2>/dev/null; then
            echo "Flask 서버가 이미 실행 중입니다."
            exit 1
        fi

        echo "Flask 서버 시작 중..."
        nohup $FLASK_COMMAND > "$LOG_FILE" 2>&1 &
        echo $! > "$PID_FILE"
        echo "Flask 서버가 시작되었습니다. (PID: $(cat $PID_FILE))"
        ;;

    stop)
        if [ -f "$PID_FILE" ] && kill -0 $(cat "$PID_FILE") 2>/dev/null; then
            echo "Flask 서버 종료 중... (PID: $(cat $PID_FILE))"
            kill $(cat "$PID_FILE")
            rm "$PID_FILE"
            echo "Flask 서버가 종료되었습니다."
        else
            echo "실행 중인 Flask 서버를 찾을 수 없습니다."
        fi
        ;;

    *)
        echo "사용법: $0 {start|stop}"
        exit 1
        ;;
esac
