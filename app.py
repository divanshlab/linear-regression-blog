from flask import Flask, render_template, request
from model.model import predict_marks, predict_pass_fail

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    pass_prediction = None

    if request.method == "POST":

        study_hours = float(request.form["study_hours"])
        model_type = request.form["model_type"]

        # Linear Regression
        if model_type == "linear":
            prediction = predict_marks(study_hours)

        # Logistic Regression
        elif model_type == "logistic":
            pass_prediction = predict_pass_fail(study_hours)

    return render_template(
        "index.html",
        prediction=prediction,
        pass_prediction=pass_prediction
    )


if __name__ == "__main__":
    app.run(debug=True)