#Version: 13

import arcpy
import os
import ctypes
import pypyodbc #used to run Access queries
import datetime
import shutil
import sqlite3

from datetime import timedelta
import pandas as pd
import numpy as np

def executeQuery(sqls, fullPath):
    conn = pypyodbc.win_connect_mdb(fullPath)
    cur = conn.cursor()
    #print SQL
    if type(sqls) == list:
        for sql in sqls:
            print sql
            cur.execute(sql)
    else:
        sql = sqls
        print sql
        cur.execute(sql)

    cur.close()
    conn.commit()
    conn.close()

def readQuery(SQL, fullPath):
    queryOutput = []
    if ".mdb" in fullPath:
        conn = pypyodbc.win_connect_mdb(fullPath)
    elif ".sqlite" in fullPath:
        conn = sqlite3.connect(fullPath)
        print "connection established with ",fullPath
    else:
        MessageBox(None, "Tool ends." + fullPath + " not recognized as mdb or sqlite", 'Info', 0)
        exit()
    ###################
    cur = conn.cursor()
    print SQL
    cur.execute(SQL)
    while True:
        row = cur.fetchone()
        if not row:
            break
        queryOutput.append(row)
    cur.close()
    conn.commit()
    conn.close()
    return queryOutput

def writeMusFile(layerName,elementList,musPath):
    os.remove(musPath) if os.path.exists(musPath) else None
    file = open(musPath, "w")
    file.write(layerName[:-10] + "\n")
    for c in elementList:
        file.write(str(c) + "\n")
    file.close()

start_timer = datetime.datetime.now()

#User input
model = 'VSA_BASE_MODEL_2015.mdb'

working_folder = os.getcwd()

def main(working_folder,mu_path):
##if 1 == 1: #For debugging in idle/pyscripter uncomment this line and comment the above.

##line_layers = ['msm_Link','msm_Weir','msm_Orifice','msm_Pump','msm_Valve']

    extension = os.path.splitext(mu_path)[1].lower()

    if extension == ".mdb":
        sql = "SELECT MUID, Acronym, TypeNo CrsID, IIf(TypeNo=1,Diameter,IIf(TypeNo=3,Height,0)) AS Pipe_Height, IIF(Length IS Null, SHAPE_Length, Length) AS Pipe_Length, UpLevel, DwLevel, FROMNODE, TONODE FROM msm_Link WHERE Owner = 'GV' AND Acronym <> ''"
    else:
        sql = "SELECT MUID, Acronym, TypeNo, CrsID, CASE TypeNo WHEN 1 THEN Diameter WHEN 3 THEN Height ELSE 0 END AS Pipe_Height, SHAPE_Length AS Pipe_Length, UpLevel, DwLevel, FROMNODEID, TONODEID FROM msm_Link "
        sql += "WHERE Owner = 'GV' AND Acronym <> '' AND Active = 1"
    lines = readQuery(sql,mu_path)




    if extension == ".mdb":
        sql = "SELECT MUID, Acronym, TypeNo, '' as CrsID, IIf(TypeNo=1,Diameter,IIf(TypeNo=3,Height,0)) AS Pipe_Height, SHAPE_Length AS Pipe_Length, InvertLevel AS UpLevel, InvertLevel AS DwLevel, FROMNODE, TONODE FROM msm_Orifice WHERE Acronym <> ''"
    else:
        sql = "SELECT MUID, Acronym, TypeNo, '' as CrsID, CASE TypeNo WHEN 1 THEN Diameter WHEN 3 THEN Height ELSE 0 END AS Pipe_Height, 1 AS Pipe_Length, InvertLevel AS UpLevel, InvertLevel AS DwLevel, FROMNODEID, TONODEID FROM msm_Orifice "
        sql += "WHERE Acronym <> '' AND Active = 1"
    orifices = readQuery(sql,mu_path)
    lines += orifices


    if extension == ".mdb":
        sql = "SELECT MUID, AssetName, CoverTypeNo, TypeNo, GroundLevel, InvertLevel, CriticalLevel FROM msm_Node ORDER BY MUID"
    else:
        sql = "SELECT MUID, AssetName, CoverTypeNo, TypeNo, GroundLevel, InvertLevel, CriticalLevel FROM msm_Node WHERE Active = 1 ORDER BY MUID"
    nodes = readQuery(sql,mu_path)

    if extension == ".mdb":
        sql = "SELECT CrsID, MAX(HX) - MIN(HX) AS CRS_Height FROM ms_CRSD GROUP BY CrsID"
    else:
        sql = "SELECT CrsID, MAX(HX) - MIN(HX) AS CRS_Height FROM ms_CRSD WHERE Active = 1 GROUP BY CrsID"
    crs = readQuery(sql,mu_path)
    crs_df = pd.DataFrame(crs, columns =['CRS', 'CRS_Height'])

    nodes_df = pd.DataFrame(nodes, columns =['Node', 'Asset Name', 'Cover Type', 'Network Type', 'Ground Level', 'Invert Level', 'Safe Operating Head'])
    nodes_df.to_csv(working_folder + "\\ls_nodes.csv", index = False)

    lines_df = pd.DataFrame(lines, columns =['Pipe', 'Acronym', 'TypeNo', 'CRS', 'Height', 'Length', 'UpLevel', 'DwLevel', 'FromNode', 'ToNode'])
    lines_df = pd.merge(lines_df,crs_df,on=['CRS'],how='left')
    lines_df.loc[lines_df['TypeNo'] == 2, 'Height'] = lines_df['CRS_Height']
    lines_df.to_csv(working_folder + "\\ls_pipes.csv", index = False)

##end_timer = datetime.datetime.now()
##duration = end_timer - start_timer
##duration_seconds = duration.seconds
##
##MessageBox = ctypes.windll.user32.MessageBoxA
##MessageBox(None, "Finished in " + str(duration_seconds) + " seconds", 'Info', 0)


if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])

