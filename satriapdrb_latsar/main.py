from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/monev")
def monev():
    return render_template("monev.html")

@app.route("/data_source")
def data_source():
    return render_template("data_source.html")

@app.route("/pdrb_lapus")
def pdrb_lapus():
    return render_template("pdrb_lapus.html")

@app.route("/pdrb_pengeluaran")
def pdrb_pengeluaran():
    return render_template("pdrb_pengeluaran.html")

@app.route("/admin_teknis")
def admin_teknis():
    return render_template("admin_teknis.html")

@app.route("/panduan")
def panduan():
    return render_template("panduan.html")
if __name__ == "__main__":
    app.run(debug=True)
