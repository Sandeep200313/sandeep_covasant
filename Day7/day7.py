'''Question-16:
Sharing of content 
@app.route("/updatefortoday", methods=['GET','POST'])#http://localhost:5000/updatefortoday
@app.route("/share", methods=['GET'])#http://localhost:5000/share
@app.route("/clearnotepadtxt", methods=['GET'])#http://localhost:5000/clearnotepadtxt'''

from flask import Flask, request, render_template, redirect, url_for
scratchpad_data = "initial scratchpad content"

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def dashboard():
    global scratchpad_data
    return render_template("index.html", content=scratchpad_data)

@app.route("/writetoday", methods=["GET", "POST"]) 
def writetoday():
    global scratchpad_data
    if request.method == 'POST':
        updated_data = request.form.get("content", "")
        scratchpad_data = updated_data
        return redirect(url_for("dashboard"))
    return render_template("write.html", content=scratchpad_data)

@app.route("/preview", methods=["GET"])  
def preview():
    return render_template("preview.html", content=scratchpad_data)

@app.route("/resetpad", methods=["GET"])  
def resetpad():
    global scratchpad_data
    scratchpad_data = ""
    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.run(debug=True)
