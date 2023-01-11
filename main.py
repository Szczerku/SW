# Importing Libraries
import serial
import time
from datetime import datetime
import streamlit as st
import pandas as pd
import numpy as np
import math
import sqlite3
from sqlite3 import Error


def stw_tabele(con, T):
     try:
         c = con.cursor()
         c.execute(T)
     except Error as e:
        print(e)

def insert_wartosc(con, w):
     sql = ''' INSERT INTO pomiary(time,value)
     VALUES(?,?) '''
     cur = con.cursor()
     cur.execute(sql, w)
     con.commit()
     return cur.lastrowid


def pokaz_baze(con):
    c=con.cursor()
    print(c.execute("SELECT * FROM pomiary").fetchall())



arduino = serial.Serial(port='COM6', baudrate=9600, timeout=1)
data = []
chart_data = []

try:
    conn = sqlite3.connect('SW.db')
except Error as e:
    print(e)

delete="DELETE FROM pomiary"
stw_tabele(conn, delete)
sql_stw_tablice = " CREATE TABLE IF NOT EXISTS pomiary ( id integer PRIMARY KEY AUTOINCREMENT, time DATETIME NOT NULL, value float); "
stw_tabele(conn, sql_stw_tablice)
arduino.readline().decode("ascii").strip()
for i in range(10):
    if data.append(float(arduino.readline().decode("ascii").strip())) == '':
        data.append(0)
    else:
        data.append(float(arduino.readline().decode("ascii").strip()))
while len(data)<1000:
    data.append(float(arduino.readline().decode("ascii").strip()))
    t = datetime.now().strftime("%H:%M:%S")

    suma = sum(data[-10:])-max(data[-10:])-min(data[-10:])
    x=suma / 8

    print('DODANY WIERSZ: Czas ', t, ' Wartosc ', x)
    insert_wartosc(conn, (t, x))
    #pokaz_baze(conn)

