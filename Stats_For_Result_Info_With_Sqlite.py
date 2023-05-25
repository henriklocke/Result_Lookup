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
    ###ADDED FOR SQLITE
    print "enter in the execute Query"
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
        #queryOutput.append(row[0])
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
model = 'Lisa_Base.sqlite'
has_acronym = True

working_folder = os.getcwd()

cs_before = 'NAD_1983_2011_UTM_Zone_10N'
cs_after = 'GCS_WGS_1984'
read_projection_from = 'FSA_South_Base.mdb'

##outCS = arcpy.SpatialReference('GCS WGS 1984')

dsc = arcpy.Describe(working_folder + '\\' + read_projection_from + '\\msm_Node')
coord_sys = dsc.spatialReference

line_layers = ['msm_Link','msm_Weir','msm_Orifice','msm_Pump','msm_Valve']

con_csv_nodes = 'Connection_Stats_Nodes.csv'
con_csv_lines = 'Connection_Stats_Lines.csv'

MUPath = working_folder + '\\' + model

extension = os.path.splitext(MUPath)[1].lower()

import_layers = ['msm_Node'] + line_layers
if extension == ".sqlite":
    mdb_path = os.path.splitext(MUPath)[0] + '.mdb'
    mdb_name = os.path.splitext(model)[0] + '.mdb'
    os.remove(mdb_path) if os.path.exists(mdb_path) else None
    arcpy.CreatePersonalGDB_management(working_folder, mdb_name)
    for import_layer in import_layers:
        arcpy.FeatureClassToFeatureClass_conversion (MUPath+ "\\" + import_layer, mdb_path, import_layer)
##    cs_before = arcpy.SpatialReference(cs_before)
    arcpy.DefineProjection_management(mdb_path + '\\msm_Node', coord_sys)

if extension == ".mdb":
    fromto = 'FROMNODE, TONODE'
    active_check = ''
else:
    fromto = 'FROMNODEID, TONODEID'
    active_check_link = ' WHERE Active = 1 AND Enabled = 1'
    active_check = ' WHERE Active = 1'

sql = "SELECT MUID, AssetName, CoverTypeNo, TypeNo, GroundLevel, InvertLevel, CriticalLevel FROM msm_Node"  + active_check + " ORDER BY MUID"
nodes = readQuery(sql,MUPath)

for i, line_layer in enumerate(line_layers):
    if line_layer == 'msm_Link':
        if has_acronym == True:
            sql = "SELECT MUID, Acronym, " +  fromto + ", '" + line_layer[4:] + "' AS LAYER FROM " + line_layer  + active_check_link + " ORDER BY MUID"
        else:
            sql = "SELECT MUID, AssetName, " +  fromto + ", '" + line_layer[4:] + "' AS LAYER FROM " + line_layer  + active_check_link + " ORDER BY MUID"
    else:
        sql = "SELECT MUID, AssetName, " +  fromto + ", '" + line_layer[4:] + "' AS LAYER FROM " + line_layer  + active_check + " ORDER BY MUID"
    if i == 0:
        lines = readQuery(sql,MUPath)
    else:
        lines += readQuery(sql,MUPath)

nodes_df = pd.DataFrame(nodes, columns =['MUID', 'Asset Name', 'Cover Type', 'Network Type', 'Ground Level', 'Invert Level', 'Safe Operating Head'])
nodes_df.to_csv(working_folder + "\\" + con_csv_nodes, index = False)

lines_df = pd.DataFrame(lines, columns =['MUID', 'Acronym', 'FromNode', 'ToNode', 'Layer'])
lines_df.to_csv(working_folder + "\\" + con_csv_lines, index = False)

end_timer = datetime.datetime.now()
duration = end_timer - start_timer
duration_seconds = duration.seconds

MessageBox = ctypes.windll.user32.MessageBoxA
MessageBox(None, "Finished in " + str(duration_seconds) + " seconds", 'Info', 0)




