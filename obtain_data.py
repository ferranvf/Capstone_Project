import pandas as pd
import mysql.connector
import numpy as np



def get_data(degree, cnx):
    query = "select * from Degrees where degree_name='{}'".format(degree)
    degree = pd.read_sql(query, cnx)
    return degree

def create_data(degree, cnx):
    query = ("select * from CourseCatalog where degree_id = {}").format(degree['degree_id'].values[0])
    courses = pd.read_sql(query, cnx)           
    courses['degree'] = [degree['degree_name'].values[0]]*courses.shape[0]
    
    restrictions_id = courses[~courses['restriction_id'].isna()]['restriction_id'].unique()
    if len(restrictions_id) == 1:
        q = "select * from CourseRestrictions where restriction_id in ({})".format(restrictions_id[0])
    elif len(restrictions_id) > 1:
        q = "select * from CourseRestrictions where restriction_id in {}".format(tuple(restrictions_id))
    
    restrictions = pd.read_sql(q, cnx)
    df = courses.merge(restrictions, on='restriction_id', how='left')
    df = df.replace({np.nan: "No restrictions"})
    return df

def create_data2(degree,cnx):
    query = ("select * from CourseCatalog where degree_id = {}").format(degree['degree_id'].values[0])
    courses = pd.read_sql(query, cnx)
    courses['degree'] = [degree['degree_name'].values[0]]*courses.shape[0]
    
    if len(courses['course_catalog_id']) ==1:
        q = "select * from Topics where course_id in ({})".format(courses['course_catalog_id'].values[0])
    elif len(courses['course_catalog_id']) > 1:
        q = "select * from Topics where course_id in {}".format(tuple(courses['course_catalog_id'].values))
    topics = pd.read_sql(q, cnx)
    topics_id = topics['topic_id'].unique()
    if len(topics_id) ==1:
        q = "select * from LearningObjectives where topic_id in ({})".format(topics_id[0])
    elif len(topics_id) > 1:
        q = "select * from LearningObjectives where topic_id in {}".format(tuple(topics_id))
    
    learningobjectives = pd.read_sql(q,cnx)
    
    learningobjectives =  learningobjectives.merge(topics, on='topic_id')
    return(learningobjectives.merge(courses, left_on='course_id', right_on='course_catalog_id'))

def connect_database():
    cnx = mysql.connector.connect(user='root', password="Mynewpassword1*",
                              host='127.0.0.1',
                              database='CapstoneProject')
    
    return cnx
