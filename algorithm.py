import pandas as pd
import mysql.connector
import numpy as np



def get_data(degree, cnx):
    query = "select * from Degrees where degree_name='{}'".format(degree)
    degree = pd.read_sql(query, cnx)
    return degree['degree_id'].values[0], degree['TotalCredits'].values[0]

def create_paths(degree_id, total_credits,cnx):
    query = ("select * from CourseCatalog where degree_id = {}").format(degree_id)
    courses = pd.read_sql(query, cnx)
    print(courses)


def connect_database():
    psw = open("/home/ferran/OneDrive/Ordinador/Computational Data Science/Fall 2022/Principles of Data Management/contrasenya","r").read()
    print(psw)
    cnx = mysql.connector.connect(user='root', password="Mynewpassword1*",
                              host='127.0.0.1',
                              database='CapstoneProject')
    
    return cnx

if __name__=='__main__':
    cnx = connect_database()
    degree_id, total_credits = get_data("Computer Science", cnx)
    create_paths(degree_id,total_credits, cnx)