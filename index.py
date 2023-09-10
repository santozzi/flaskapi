from src import init_app


app = init_app()

if __name__ == "__main__":
    print(__name__)
    app.run(debug=True, port=4000)