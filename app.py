from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from projects import Projects
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

def init_db():
    conn = sqlite3.connect('tmhnaprojects.db')
    conn.commit()
    conn.close()

init_db()

@app.route('/', methods=['GET', "POST"])
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    Projects.updateProjectPriorities()
    projects = Projects.getAllProjects()
    return render_template('index.html', message=projects)

@app.route('/addproject', methods=['GET', 'POST'])
def addproject():
    if 'user_id' not in session or session['role'] != 'employee':
        flash("You do not have permission to access this page. Only employees can add projects.", "error")
        return redirect(url_for('index'))

    if request.method =='GET':
        return render_template('addproject.html')

    elif request.method == "POST":
        Name = request.form.get("name", "")
        Description = request.form.get("description", "")
        Expected_ROI = request.form.get("roi", "")
        Potential_Risks = request.form.get("risks", "")
        Expected_Resources_Needed = request.form.get("resources", "")
        Reach = float(request.form.get("reach", ""))
        Impact = float(request.form.get("impact", ""))
        Confidence = float(request.form.get("confidence", ""))
        Effort = float(request.form.get("effort", ""))

        if Name and Description and Expected_ROI and Potential_Risks and Expected_Resources_Needed and Reach and Impact and Confidence and Effort:
            Projects.addProject(Name, Description, Expected_ROI, Potential_Risks, Expected_Resources_Needed, Reach, Impact, Confidence, Effort)
            flash("Project added successfully!", "success")
            return redirect(url_for('index'))
        else:
            flash("Please fill in all of the questions.", "error")
            return render_template('addproject.html', message="Please fill all fields.")

@app.route('/update/<Name>', methods=['GET', 'POST'])
def update(Name):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    project = Projects.getProject(Name)
    if not project or project["Employee_ID"] != session["user_id"] or session['role']=='manager':
        flash("You are not authorized to update this project. Only the creator of this project can update this project.", "error")
        return redirect(url_for('index'))

    if request.method == "POST":
        Description = request.form.get("description", "")
        Expected_ROI = request.form.get("ROI", "")
        Potential_Risks = request.form.get("risks", "")
        Expected_Resources_Needed = request.form.get("resources", "")
        Reach = float(request.form.get("reach", ""))
        Impact = float(request.form.get("impact", ""))
        Confidence = float(request.form.get("confidence", ""))
        Effort = float(request.form.get("effort", ""))

        if Description and Expected_ROI and Potential_Risks and Expected_Resources_Needed and Reach and Impact and Confidence and Effort:
            Projects.updateProject(Name, Description, Expected_ROI, Potential_Risks, Expected_Resources_Needed, Reach, Impact, Confidence, Effort)
            return redirect('/')
        else:
            flash("All fields are required.", "error")

    project = Projects.getProject(Name)
    return render_template('updateproject.html', message=project)

@app.route('/delete/<Name>')
def delete(Name):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    project = Projects.getProject(Name)
    if not project or project["Employee_ID"] != session["user_id"] or session["role"] == "manager":
        flash("You are not authorized to delete this project. Only the creator of this project can delete this project.", "error")
        return redirect('/')

    Projects.deleteProject(Name)
    flash("Project deleted successfully!", "success")
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    return render_template('dashboard.html')

@app.route('/description/<Name>')
def description(Name):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    project = Projects.descriptionProject(Name)
    return render_template('description.html', message=project)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        if not username or not password:
            return render_template('login.html', error="Please fill in all fields")

        # Check in Employee_Table
        employee = Projects.query_user(username, "Employee_Table")
        if employee and employee["Password"] == password:
            session["user_id"] = employee["Employee_ID"]  # Store Employee_ID in session
            session["role"] = "employee"
            session['user_name'] = employee["Username"]
            flash("Logged in successfully as Employee! Welcome " + employee["Username"] + "!", "success")
            return redirect(url_for("index"))  # Redirect to a dashboard page

        # Check in Manager_Table
        manager = Projects.query_user(username, "Manager_Table")
        if manager and manager["Password"] == password:
            session["user_id"] = manager["Manager_ID"] # Store Manager_ID in session
            session["role"] = "manager"
            session['user_name'] = manager["Username"]
            flash("Logged in successfully as Manager! Welcome " + manager["Username"] + "!", "success")
            return redirect(url_for("index"))

        flash("Invalid email or password!", "error")
        return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully!", "success")
    return redirect(url_for("login"))

@app.route("/approve/<Name>", methods=['GET', 'POST'])
def approve(Name):

    project = Projects.statusProject(Name)
    if not project or project["Manager_ID"] != session["user_id"]:
        flash("You are not authorized to update the status of this project. Only the manager of this project can update the status of this project .", "error")
        return redirect(url_for('index'))

    Projects.approveProject(Name)
    return redirect(url_for('index'))

@app.route("/reject/<Name>", methods=['GET', 'POST'])
def reject(Name):

    project = Projects.statusProject(Name)
    if not project or project["Manager_ID"] != session["user_id"]:
        flash("You are not authorized to update the status of this project. Only the manager of this project can update the status of this project .", "error")
        return redirect(url_for('index'))

    Projects.rejectProject(Name)
    return redirect(url_for('index'))

@app.route("/needsinfo/<Name>", methods=['GET', 'POST'])
def needsinfo(Name):

    project = Projects.statusProject(Name)
    if not project or project["Manager_ID"] != session["user_id"]:
        flash("You are not authorized to update the status of this project. Only the manager of this project can update the status of this project .", "error")
        return redirect(url_for('index'))

    Projects.needsinfoProject(Name)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)



