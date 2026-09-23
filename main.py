# Python + streamlit Project 
# Motive of this project is to revise important Pythons concept
# University Management System 

import streamlit as st

# config the main app page
st.set_page_config(
    page_title = "University System",
    layout = "wide"
)
st.title("University  Management")
# create empty list of colleges
if "college" not in st.session_state:
    st.session_state.college = []

menu_choice = st.sidebar.radio(
    "SELECT OPTION",
    (
        "Create College",
        "Add Student",
        "Add Teachers",
        "Display Students",
        "Display Teacher",
        "List of Colleges"
    )
)

#coolege class is storing college name and students and teachers list
class college:
    def __init__(self,cname):
        self.cname = cname
        self.students = []
        self.teachers = []
    
    
    def add_student(self, s):
        self.students.append(s)
    def add_teacher(self,t):
        self.teachers.append(t)
    
class person:
    def __init__(self,name,branch):



        self.branch = branch
        self.name = name

class student(person):
    def __init__(self,roll,sname,branch):
        self.rollno = roll
        super().__init__(sname,branch)
class teacher(person):
    def __init__(self,subject,tname,branch):
        self.subject = subject
        super().__init__(tname,branch)
    


# used upon college name,college class object is find 
def find_college(cname):
    for c in st.session_state.college:
        if c.cname == cname:
            return c
    return None


if menu_choice == "Create College":
    cname = st.text_input("Enter new College name")
    if st.button("CREATE"):
        clg_obj = college(cname) # creating a college class object
        st.session_state.college.append(clg_obj) # storing a college class class objectin college list
        st.success(f"College created successfully:{cname}")

elif menu_choice == "Add Student":
    if not st.session_state.college:
        st.info("Please add the college first")

    else:
        clgname = st.selectbox("Choose College",[c.cname for c in st.session_state.college])
        roll = st.number_input("Enter Your Rollno", min_value = 1, max_value = 100)
        sname = st.text_input("Enter Student name")
        branch = st.text_input("Enter your branch")
        if st.button("ADD STUDENT"):
            if not (roll and sname and clgname and branch):
                st.error("Please fill the blanks")
            else:
                clg_obj = find_college(clgname)  # find the college object based upon college name
                stu_obj = student(roll, sname,branch)
                clg_obj.add_student(stu_obj)
                st.success("Student added successfully")

elif menu_choice == "Add Teachers":
    if not st.session_state.college:
        st.info("Please add the college first")

    else:
        clgname = st.selectbox("Choose College",[c.cname for c in st.session_state.college])
        subject = st.text_input("Enter Your subject")
        tname = st.text_input("Enter Teacher name")
        branch = st.text_input("Enter your branch")
        if st.button("ADD Teacher"):
            if not (subject and tname and clgname and branch):
                st.error("Please fill the blanks")
            else:
                clg_obj = find_college(clgname)  # find the college object based upon college name
                teacher_obj = teacher(subject,tname,branch)
                clg_obj.add_teacher(teacher_obj)
                st.success("Teacher added successfully")

elif menu_choice == "Display Students":
    if not st.session_state.college:
        st.info("Please add the college first")
    else:
        clgname = st.selectbox("Choose college",[c.cname for c in st.session_state.college])
        clg_ob = find_college(clgname)
        st.subheader(f"List of students : {clgname}")
        if clg_ob.students:
            for i,s in enumerate(clg_ob.students):
                st.write(s.rollno," : ",s.name)
        else:
            st.warning("No student record found")
    

elif menu_choice == "Display Teacher":
    if not st.session_state.college:
        st.info("Please add the college first")
    else:
        clgname = st.selectbox("Choose college",[c.cname for c in st.session_state.college])
        clg_ob = find_college(clgname)
        st.subheader(f"List of Teacher : {clgname}")
        if clg_ob.teachers:
            for i,t in enumerate(clg_ob.teachers):
                st.write(i," : ",t.name)
        else:
            st.warning("No teachers record found")

elif menu_choice == "List of Colleges":
    st.subheader("List of colleges")
    if not st.session_state.college:
        st.info("Please add the college first")
    else:
        for i, c in enumerate(st.session_state.college,1):
            st.write(f"{i} : {c.cname}")