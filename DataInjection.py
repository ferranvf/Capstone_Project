import pandas as pd
import mysql.connector
import numpy as np

psw = open("/home/ferran/OneDrive/Ordinador/Computational Data Science/Fall 2022/Principles of Data Management/contrasenya",r)
cnx = mysql.connector.connect(user='root', password=psw,
                              host='127.0.0.1',
                              database='CapstoneProject')

cursor=cnx.cursor()




course_catalog = pd.read_excel("CourseSchema.xlsx", sheet_name="CourseCatalog")
course_catalog = course_catalog.replace(np.nan, None)
course=pd.read_excel("CourseSchema.xlsx", sheet_name="Course")
course = course.replace(np.nan, None)
topics=pd.read_excel("CourseSchema.xlsx", sheet_name="Topics")
topics=topics.replace(np.nan, None)
learning_objectives=pd.read_excel("CourseSchema.xlsx", sheet_name="LearningObjectives")
learning_objectives = learning_objectives.replace(np.nan, None)


#insert course_catalog data to sql tables
for index, row in course_catalog.iterrows():
    cursor.execute("INSERT INTO CourseCatalog (course_catalog_id,college,departement,style,course_level,course_number,course_name,course_description,number_credits,requisits) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", \
                   (row.CourseCatalogID, row.College, row.Department, row.Style, row.CourseLevel, row.CourseNumber, row.CourseName, row.CourseDescription, row.NumberCredits, row.Prerequisites))

#insert course data to sql tables
for index, row in course.iterrows():
    cursor.execute("INSERT INTO Course (course_id,course_number,CRN,year_,semester,intructorID) values(%s,%s,%s,%s,%s,%s)", \
                   (row.course_id, row.course_number, row.CRN, row.year_, row.semester, row.instructorID))

#insert topics data to sql tables
for index, row in topics.iterrows():
    cursor.execute("INSERT INTO Topics (topic_id,parent,topic_level,shortname,topic_description,course_id) values(%s,%s,%s,%s,%s,%s)", \
                   (row.TopicsID, row.Parent, row.Level, row.ShortName, row.Description, row.course_id))

#insert LearningObjectives data to sql tables
for index, row in learning_objectives.iterrows():
    cursor.execute("INSERT INTO LearningObjectives (learning_objective_id,shortdescription,longdescription,topic_id,lo_source,lo_references,prerequisits) values(%s,%s,%s,%s,%s,%s,%s)", \
                   (row.LearningObjectiveID, row.ShortName, row.LongDescription, row.TopicsID, row.Source, row.Reference, row.Prerequisites))

cnx.commit()
cursor.close()
cnx.close()

