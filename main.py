from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # df = pd.read_csv(f"data_small/TG_STAID0000{str(station).zfill(2)}.txt")
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE']== date]['   TG'].squeeze()/ 10
    result = {"station": station,
              "date": date,
              "temperature": temperature}
    return result


if __name__ == "__main__":
    app.run(debug=True)