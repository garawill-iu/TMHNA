import sqlite3
from functools import wraps

from flask import session, flash, redirect, url_for


class Projects:
    def __init__(self, Priority="", Project_ID="", ProjectName="", Reach="", Impact="", Confidence="", Effort="", RiceScore="", EmployeeID="", ApprovalStatus="", ROI="", Risks="", Resources="", username=""):
        self.__priority = Priority
        self.__projectid = Project_ID
        self.__projectname = ProjectName
        self.__reach = Reach
        self.__impact = Impact
        self.__confidence = Confidence
        self.__effort = Effort
        self.__ricescore = RiceScore
        self.employeeid = EmployeeID
        self.__approvalstatus = ApprovalStatus
        self.__roi = ROI
        self.__risks = Risks
        self.__resources = Resources
        self.__username = username

    # Priority
    def get_priority(self):
        return self.__priority

    def set_priority(self, value):
        self.__priority = value

    #Project_ID
    def get_projectid(self):
        return self.__projectid

    def set_projectid(self, value):
        self.__projectid = value

    # ProjectName
    def get_projectname(self):
        return self.__projectname

    def set_projectname(self, value):
        self.__projectname = value

    # Reach
    def get_reach(self):
        return self.__reach

    def set_reach(self, value):
        self.__reach = value

    # Impact
    def get_impact(self):
        return self.__impact

    def set_impact(self, value):
        self.__impact = value

    # Confidence
    def get_confidence(self):
        return self.__confidence

    def set_confidence(self, value):
        self.__confidence = value

    # Effort
    def get_effort(self):
        return self.__effort

    def set_effort(self, value):
        self.__effort = value

    # RiceScore
    def get_ricescore(self):
        return self.__ricescore

    def set_ricescore(self, value):
        self.__ricescore = value

    # EmployeeID
    def get_employeeid(self):
        return self.__employeeid

    def set_employeeid(self, value):
        self.__employeeid = value

    # ApprovalStatus
    def get_approvalstatus(self):
        return self.__approvalstatus

    def set_approvalstatus(self, value):
        self.__approvalstatus = value

    # Expected ROI
    def get_roi(self):
        return self.__roi

    def set_roi(self, value):
        self.__roi = value

    # Potential Risks
    def get_risks(self):
        return self.__risks

    def set_risks(self, value):
        self.__risks = value

    # Expected Resources Needed
    def get_resources(self):
        return self.__resources

    def set_resources(self, value):
        self.__resources = value

    #username
    def get_username(self):
        return self.__username

    def set_username(self, value):
        self.__username = value

    @classmethod
    def updateProjectPriorities(cls):
        conn = sqlite3.connect("tmhnaprojects.db")
        cursor = conn.cursor()

        cursor.execute('SELECT COUNT(*) FROM Project_Table')
        project_count = cursor.fetchone()[0]

        if project_count == 0:
            conn.close()
            return None

        # Fetch all projects ordered by Rice_Score in descending order
        cursor.execute('SELECT * FROM Project_Table ORDER BY Rice_Score DESC')
        allProjects = cursor.fetchall()

        # Update priority for each project
        for index, project in enumerate(allProjects):
            new_priority = index + 1  # Priority starts from 1
            project_id = project[0]  # Assuming the first column is the unique project ID
            cursor.execute('UPDATE Project_Table SET Priority = ? WHERE Project_ID = ?', (new_priority, project_id))

        # Commit changes and close connection
        conn.commit()
        conn.close()

    @classmethod
    def getAllProjects(cls):
        conn = sqlite3.connect("tmhnaprojects.db")
        cursor = conn.cursor()
        cursor.execute('SELECT Priority, Project_Name, Expected_ROI, Reach, Impact, Confidence, Effort, Rice_Score, Employee_ID, Approval_Status FROM Project_Table ORDER BY Priority ASC')
        allProjects = cursor.fetchall()

        projectsDict = []

        for i in allProjects:
            p = { "priority": i[0], "project_name": i[1], "expected_roi": i[2], "reach": i[3], "impact": i[4], "confidence": i[5], "effort": i[6], "rice_score": i[7], "employee_id": i[8], "approval_status": i[9]}
            projectsDict.append(p)

        conn.close()
        return projectsDict

    @classmethod
    def addProject(cls, Name, Description, Expected_ROI, Potential_Risks, Expected_Resources_Needed, Reach, Impact, Confidence, Effort):
        conn = sqlite3.connect('tmhnaprojects.db')

        employee_id = session["user_id"]
        ric = Reach * Impact * Confidence
        RICE = round((ric/Effort), 0)
        Approval = "Pending"

        statement = 'INSERT INTO Project_Table (Project_Name, Description, Expected_ROI, Potential_Risks, Expected_Resources_Needed, Reach, Impact, Confidence, Effort, Rice_Score, Employee_ID, Approval_Status) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        cur = conn.cursor()
        cur.execute(statement, (Name, Description, Expected_ROI, Potential_Risks, Expected_Resources_Needed, Reach, Impact, Confidence, Effort, RICE, employee_id, Approval,))
        conn.commit()
        conn.close()

    @classmethod
    def updateProject(cls, Name, Description, Expected_ROI, Potential_Risks, Expected_Resources_Needed, Reach, Impact, Confidence, Effort):
        conn = sqlite3.connect("tmhnaprojects.db")
        statement = 'UPDATE Project_Table SET Project_Name=?, Description=?, Expected_ROI=?, Potential_Risks=?, Expected_Resources_Needed=?, Reach=?, Impact=?, Confidence=?, Effort=?, Rice_Score=? WHERE Project_Name=?'
        cur = conn.cursor()

        ric = Reach * Impact * Confidence
        RICE = round((ric/Effort), 0)

        cur.execute(statement, (Name, Description, Expected_ROI, Potential_Risks, Expected_Resources_Needed, Reach, Impact, Confidence, Effort, RICE, Name))
        conn.commit()
        conn.close()

    @classmethod
    def getProject(cls, Name):
        conn = sqlite3.connect("tmhnaprojects.db")
        cur = conn.cursor()
        cur.execute('SELECT Project_Name, Description, Expected_ROI, Potential_Risks, Expected_Resources_Needed, Reach, Impact, Confidence, Effort, Employee_ID FROM Project_Table WHERE Project_Name=?', (Name,))
        row = cur.fetchone()
        conn.close()

        if row:
            return{"Project_Name": row[0], "Description": row[1], "Expected_ROI": row[2], "Potential_Risks": row[3], "Expected_Resources_Needed": row[4], "Reach": row[5], "Impact": row[6], "Confidence": row[7], "Effort": row[8], "Employee_ID": row[9]}
        return None

    @classmethod
    def deleteProject(cls, Name):
        conn = sqlite3.connect("tmhnaprojects.db")
        statement = 'DELETE FROM Project_Table WHERE Project_Name=?'
        cur = conn.cursor()
        cur.execute(statement, (Name,))
        conn.commit()
        conn.close()

    @classmethod
    def descriptionProject(cls, Name):
        conn = sqlite3.connect("tmhnaprojects.db")
        cur = conn.cursor()

        # Query to get project details and join with Employee_Table to get Employee_Name
        query = """
            SELECT 
                p.Project_Name, 
                p.Description, 
                p.Expected_ROI, 
                p.Potential_Risks, 
                p.Expected_Resources_Needed, 
                p.Reach, 
                p.Impact, 
                p.Confidence, 
                p.Effort, 
                p.Rice_Score, 
                p.Employee_ID, 
                e.Employee_Name, 
                p.Priority, 
                p.Approval_Status,
                e.Manager_ID,
                m.Manager_Name
            FROM Project_Table p
            LEFT JOIN Employee_Table e ON p.Employee_ID = e.Employee_ID
            LEFT JOIN Manager_Table m ON e.Manager_ID = m.Manager_ID
            WHERE p.Project_Name = ?
        """
        cur.execute(query, (Name,))
        row = cur.fetchone()
        conn.close()

        # Check if a result was found and return the data
        if row:
            return {
                "Project_Name": row[0],
                "Description": row[1],
                "Expected_ROI": row[2],
                "Potential_Risks": row[3],
                "Expected_Resources_Needed": row[4],
                "Reach": row[5],
                "Impact": row[6],
                "Confidence": row[7],
                "Effort": row[8],
                "Rice_Score": row[9],
                "Employee_ID": row[10],
                "Employee_Name": row[11],
                "Priority": row[12],
                "Approval_Status": row[13],
                "Manager_ID": row[14],
                "Manager_Name": row[15]
            }
        return None

    @classmethod
    def query_user(cls, username, table_name):
        conn = sqlite3.connect("tmhnaprojects.db")
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM {table_name} WHERE Username = ?', (username,))
        row = cur.fetchone()
        conn.close()

        if row and table_name == 'Employee_Table':
            return{"Employee_ID": row[0], "Employee_Name": row[1], "Category_ID": row[2], "Manager_ID": row[3], "Email": row[4], "Phone": row[5], "Username": row[6], "Password": row[7]}
        elif row and table_name == 'Manager_Table':
            return{"Manager_ID": row[0], "Manager_Name": row[1], "Category_ID": row[2], "Email": row[3], "Phone": row[4], "Username": row[5], "Password": row[6]}
        else:
            return None

    @classmethod
    def role_required(cls, role):
        def wrapper(func):
            @wraps(func)
            def decorated_view(*args, **kwargs):
                if "user_id" not in session or session.get("role") != role:
                    flash("Unauthorized access!", "error")
                    return redirect(url_for("login"))
                return func(*args, **kwargs)

            return decorated_view

        return wrapper

    @classmethod
    def statusProject(cls, Name):
        conn = sqlite3.connect("tmhnaprojects.db")
        cursor = conn.cursor()
        sql = """SELECT p.Project_Name, e.Manager_ID
            FROM Project_Table p
            LEFT JOIN Employee_Table e ON p.Employee_ID = e.Employee_ID
            WHERE p.Project_Name = ?
        """
        cursor.execute(sql, (Name,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return {"Project_Name": row[0], "Manager_ID": row[1]}
        return None

    @classmethod
    def approveProject(cls, Name):
        conn = sqlite3.connect("tmhnaprojects.db")
        Approval = "Approved"

        statement = 'UPDATE Project_Table SET Approval_Status=? WHERE Project_Name=?'
        cur = conn.cursor()
        cur.execute(statement, (Approval, Name))
        conn.commit()
        conn.close()

    @classmethod
    def rejectProject(cls, Name):
        conn = sqlite3.connect("tmhnaprojects.db")
        Approval = "Rejected"

        statement = 'UPDATE Project_Table SET Approval_Status=? WHERE Project_Name=?'
        cur = conn.cursor()
        cur.execute(statement, (Approval, Name))
        conn.commit()
        conn.close()
    @classmethod
    def needsinfoProject(cls, Name):
        conn = sqlite3.connect("tmhnaprojects.db")
        Approval = "Needs More Information"

        statement = 'UPDATE Project_Table SET Approval_Status=? WHERE Project_Name=?'
        cur = conn.cursor()
        cur.execute(statement, (Approval, Name))
        conn.commit()
        conn.close()



