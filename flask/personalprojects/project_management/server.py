from flask import Flask, render_template, request, redirect, url_for, session
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)
app.secret_key = "secret"

projects = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        project = request.form["project"]
        deadline = request.form["deadline"]
        progress = request.form["progress"]
        projects.append({"project": project, "deadline": deadline, "progress": progress})
        return redirect(url_for("index"))
    return render_template("index.html", projects=projects)

@app.route("/dashboard")
def dashboard():
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    project_names = [project["project"] for project in projects]
    progress_values = [int(project["progress"]) for project in projects]
    ax.bar(project_names, progress_values)
    ax.set_xlabel("Projects")
    ax.set_ylabel("Progress")
    ax.set_title("Project Progress")
    plt.tight_layout()

    image = io.BytesIO()
    plt.savefig(image, format="png")
    image.seek(0)
    image_base64 = base64.b64encode(image.read()).decode("utf-8")
    image_src = "data:image/png;base64,{}".format(image_base64)

    return render_template("dashboard.html", image=image_src)

if __name__ == "__main__":
    app.run(debug=True)
