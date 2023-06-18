import pandas as pd
import mysql.connector
import numpy as np

cnx = mysql.connector.connect(user='root', password="Mynewpassword1*",
                              host='127.0.0.1',
                              database='CapstoneProject')

cursor=cnx.cursor()




course_catalog = pd.read_excel("CourseSchema-ferran.xlsx", sheet_name="CourseCatalog")
course_catalog = course_catalog.replace(np.nan, None)
course=pd.read_excel("CourseSchema-ferran.xlsx", sheet_name="Course")
course = course.replace(np.nan, None)
topics=pd.read_excel("CourseSchema-ferran.xlsx", sheet_name="Topics")
topics=topics.replace(np.nan, None)
learning_objectives=pd.read_excel("CourseSchema-ferran.xlsx", sheet_name="LearningObjectives")
learning_objectives = learning_objectives.replace(np.nan, None)
degrees = pd.read_excel("CourseSchema-ferran.xlsx", sheet_name="DegreeTrack")
degrees = degrees.replace(np.nan, None)
restrictions = pd.read_excel("CourseSchema-ferran.xlsx", sheet_name="CourseRestriction")
restrictions = restrictions.replace(np.nan, None)


#insert course_catalog data to sql tables
for index, row in course_catalog.iterrows():
    cursor.execute("INSERT INTO CourseCatalog (course_catalog_id,college,department,style,course_type,course_level,course_number,course_name,course_description,number_credits,requisits,degree_id, \
                   prerequisits, year_taken,semester_taken,restriction_id) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", \
                   (row.CourseCatalogID, row.College, row.Department, row.Style, row.Type ,row.CourseLevel, row.CourseNumber, row.CourseName, row.CourseDescription, row.NumberCredits, row.Prerequisites, row.DegreeId \
                    ,row.Prerequisites, row.year_taken, row.semester_taken, row.restriction_id))

#insert course data to sql tables
for index, row in course.iterrows():
    cursor.execute("INSERT INTO Course (course_id,course_number,CRN,year_,semester,instructorID) values(%s,%s,%s,%s,%s,%s)", \
                   (row.course_id, row.course_number, row.CRN, row.year_, row.semester, row.instructorID))

#insert topics data to sql tables
for index, row in topics.iterrows():
    cursor.execute("INSERT INTO Topics (topic_id,parent,topic_level,shortname,topic_description,course_id) values(%s,%s,%s,%s,%s,%s)", \
                   (row.TopicsID, row.Parent, row.Level, row.ShortName, row.Description, row.course_id))

#insert LearningObjectives data to sql tables
for index, row in learning_objectives.iterrows():
    cursor.execute("INSERT INTO LearningObjectives (learning_objective_id,shortdescription,longdescription,topic_id,lo_source,lo_references,prerequisits) values(%s,%s,%s,%s,%s,%s,%s)", \
                   (row.LearningObjectiveID, row.ShortName, row.LongDescription, row.TopicsID, row.Source, row.Reference, row.Prerequisites))

#insert Degrees data to sql tables
for index, row in degrees.iterrows():
    cursor.execute("INSERT INTO Degrees (degree_id,degree_name,degree_type,degree_description, TotalCredits, credits_fall_1,credits_spring_1,credits_fall_2\
                   ,credits_spring_2,credits_fall_3,credits_spring_3,credits_fall_4,credits_spring_4) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", \
                   (row.ID, row.Name, row.Degree, row.Description, row.TotalCredits, row.credits_fall_1,row.credits_spring_1,row.credits_fall_2\
                    ,row.credits_spring_2,row.credits_fall_3,row.credits_spring_3,row.credits_fall_4,row.credits_spring_4))

#insert CourseRestrictions data to sql tables
for index, row in restrictions.iterrows():
    cursor.execute("INSERT INTO CourseRestrictions (restriction_id,number_credits,parent_id) values(%s,%s,%s)", \
                   (row.restriction_id, row.number_credits, row.parent_id))

cnx.commit()
cursor.close()
cnx.close()

