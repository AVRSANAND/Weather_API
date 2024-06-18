from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


stations = pd.read_csv("data_small/stations.txt", skiprows=17)
table = stations[['STAID','STANAME                                 ']]


@app.route("/")
def home():
    return render_template("index.html", data= table.to_html())


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # df = pd.read_csv(f"data_small/TG_STAID0000{str(station).zfill(2)}.txt")
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze()/ 10
    result = {"station": station,
              "date": date,
              "temperature": temperature}
    return result


@app.route("/api/v1/<station>")
def all_data(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    result = df.to_dict(orient="records")
    return result


@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df['    DATE'] = df['    DATE'].astype(str)
    result = df[df['    DATE'].str.startswith(str(year))].to_dict(orient="records")
    return result


if __name__ == "__main__":
    app.run(debug=True)
