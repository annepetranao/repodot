from potassium import Potassium, Request, Response
import os

app = Potassium("my_app")

@app.handler("/")
def handler(context: dict, request: Request) -> Response:
    # Execute the echo command
    os.system('echo "You are the best"')

    # Return a simple JSON response
    return Response(
        json={"message": "Check the runtime logs to see the echo command output."},
        status=200
    )

if __name__ == "__main__":
    app.serve()
