# Importing Libraries
import serial
import time
from datetime import datetime
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import sqlite3
from sqlite3 import Error


def dowykresu(con):
    c=con.cursor()
    p=[]
    t=[]
    for i in c.execute("SELECT value FROM pomiary").fetchall():
        pom= str(i)[1:]
        pom=pom[:-2]
        #print(pom)
        p.append(round(float(pom),3))

    return p

try:
    conn = sqlite3.connect('SW.db')
except Error as e:
    print(e)


tablica = dowykresu(conn)

def main():
    st.title('PcHa')
    substance1 = st.selectbox('First substrate:', d.base_list + d.acid_list)
    chart1 = pd.DataFrame({"Target PH": tablica})
    st.line_chart(chart1)

if __name__ == "__main__":
    main()