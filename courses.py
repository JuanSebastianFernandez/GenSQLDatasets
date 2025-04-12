import numpy as np
from Data import courses_data
from functions import createData, createTextInsert, createDoc, quite_tildes
import random
random.seed(48)

#----------------------------------- Professors -----------------------------------------
data_professors = createData(courses_data.PROFESSORS, 
                  list(courses_data.COURSES.keys()),  
                  extension=len(courses_data.PROFESSORS), 
                  primary_keys=[0]) 

data_professors_complete = []
for full_name, department in data_professors:
    name = quite_tildes(full_name.split(" ")[0].lower())
    last_name = quite_tildes(full_name.split(" ")[1].lower())
    email = last_name+name+"@university.edu.es"
    data_professors_complete.append((email, full_name, department))
    
sql_text_professors = createTextInsert(data_professors_complete, 
                                     "PROFESSORS", 
                                     ["EMAIL", 
                                      "FULL_NAME", 
                                      "DEPARTMENT"])

createDoc("professors", sql_text_professors)

#----------------------------------- Courses -----------------------------------------
courses = [course for course_list in courses_data.COURSES.values() for course in course_list]
codes = ["".join(random.choices([chr(i) for i in range(65, 91)], k=3)) + str(random.randint(100, 250)) for i in range(500)] # Generated 500 random codes

data_courses = createData(codes,
                          courses,
                          np.arange(1, 7), 
                          extension=400,
                          pay_attention=True,
                          have_present={"professors": {
                                  "data_attention": data_professors_complete, 
                                  "columns_attention": [0], 
                                  "position_data": [3]
                              }},
                          primary_keys=[0])


sql_text_courses = createTextInsert(data_courses, 
                                     "COURSES", 
                                     ["COURSE_CODE", 
                                      "TITLE", 
                                      "CREDITS",
                                      "PROFESSOR_EMAIL"])


createDoc("courses", sql_text_courses)

#----------------------------------- Students -----------------------------------------
data_students = createData(courses_data.STUDENTS,
                          list(courses_data.COURSES.keys()),
                          extension=len(courses_data.STUDENTS),
                          primary_keys=[0])

data_students_complete = []
for full_name, department in data_students:
    name = quite_tildes(full_name.split(" ")[0].lower())
    last_name = quite_tildes(full_name.split(" ")[1].lower())
    email = last_name+name+"@university.edu.es"
    data_students_complete.append((email, full_name, department))

sql_text_students = createTextInsert(data_students_complete, 
                                     "STUDENTS", 
                                     ["STUDENT_EMAIL", 
                                      "FULL_NAME", 
                                      "MAJOR"])
createDoc("students", sql_text_students)

#----------------------------------- Enrollments -----------------------------------------
semesters = [f"{season}{year}" for year in range(2020, 2026) for season in ["Spring", "Fall"]]

data_enrollments = createData(semesters,
                              extension=800,
                              pay_attention=True,
                              have_present={"students":{
                                                "data_attention": data_students_complete, 
                                                "columns_attention":[0], 
                                                "position_data":[0]
                                                },
                                            "code_course":{
                                                "data_attention": data_courses, 
                                                "columns_attention":[0], 
                                                "position_data":[1]
                                                }},
                              primary_keys=[0,1,2])

sql_text_enrollments = createTextInsert(data_enrollments,
                                        "ENROLLMENTS",
                                        ["STUDENT_EMAIL",
                                         "COURSE_CODE",
                                         "SEMESTER"])

createDoc("enrollments", sql_text_enrollments)