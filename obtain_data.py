import pandas as pd
import mysql.connector
import numpy as np
from itertools import combinations, groupby



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


def connect_database():
    cnx = mysql.connector.connect(user='root', password="Mynewpassword1*",
                              host='127.0.0.1',
                              database='CapstoneProject')
    
    return cnx

# if __name__=='__main__':
#     cnx = connect_database()
#     degree = get_data("Computer Science", cnx)
#     # degree = get_data("Computational Data Science", cnx)
#     create_data(degree, cnx)