#Version: 13

import arcpy
import os
import ctypes
import pypyodbc #used to run Access queries
import datetime
import shutil
import sqlite3
import arcpy

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
##model = 'NSSA_Base_2060pop_V064_Seal_VFD.mdb'
model = 'Lisa_Base.sqlite'
has_acronym = True

working_folder = os.getcwd()

mu_path = working_folder + '\\' + model

def main(working_folder,mu_path):
##if 1 == 1: #For debugging in idle/pyscripter uncomment this line and comment the above.

    line_layers = ['msm_Link','msm_Weir','msm_Orifice','msm_Pump','msm_Valve']

    con_csv_nodes = 'Connection_Stats_Nodes.csv'
    con_csv_lines = 'Connection_Stats_Lines.csv'

    extension = os.path.splitext(mu_path)[1].lower()

    if extension == ".mdb":
        fromto = 'FROMNODE, TONODE'
        active_check_link = ''
        active_check = ''
    else:
        fromto = 'FROMNODEID, TONODEID'
        active_check_link = ' WHERE Active = 1 AND Enabled = 1'
        active_check = ' WHERE Active = 1'

    sql = "SELECT MUID, AssetName, CoverTypeNo, TypeNo, GroundLevel, InvertLevel, CriticalLevel FROM msm_Node"  + active_check + " ORDER BY MUID"
    nodes = readQuery(sql,mu_path)

    for i, line_layer in enumerate(line_layers):
        if line_layer == 'msm_Link':
            if has_acronym == True:
                if extension == ".mdb":
                    sql = "SELECT MUID, Acronym, Owner, Element_S, " +  fromto + ", '" + line_layer[4:] + "' AS LAYER, "
                    sql += "IIF(Owner = 'GV' AND Acronym <> '', 'GV_Acronym_' & Acronym, "
                    sql += "IIF(Element_S = 15, 'Municipal_Outfall', "
                    sql += "IIF(Owner <> '', 'Muni_' & Owner, 'Structures_And_Uncategorized'))) AS Folder "
                    sql += "FROM " + line_layer  + " ORDER BY MUID"
                else:
                    sql = "SELECT MUID, Acronym, Owner, Element_S, " +  fromto + ", '" + line_layer[4:] + "' AS LAYER, "
                    sql += "CASE WHEN Owner = 'GV' AND Acronym <> '' THEN 'GV_Acronym_' || Acronym "
                    sql += "WHEN Element_S = 15 THEN 'Municipal_Outfall' "
                    sql += "WHEN Owner <> '' THEN 'Muni_' || Owner ELSE 'Structures_And_Uncategorized' END AS Folder "
                    sql += "FROM " + line_layer  + active_check_link + " ORDER BY MUID"
            else:
                sql = "SELECT MUID, AssetName, Owner, Element_S, " +  fromto + ", '" + line_layer[4:] + "' AS LAYER, 'Structures_And_Uncategorized' AS Folder FROM " + line_layer  + active_check_link + " ORDER BY MUID"
        else:
            sql = "SELECT MUID, AssetName, '' AS Owner, Element_S, " +  fromto + ", '" + line_layer[4:] + "' AS LAYER, 'Structures_And_Uncategorized' AS Folder FROM " + line_layer  + active_check + " ORDER BY MUID"
        if i == 0:
            lines = readQuery(sql,mu_path)
        else:
            lines += readQuery(sql,mu_path)

    nodes_df = pd.DataFrame(nodes, columns =['MUID', 'Asset Name', 'Cover Type', 'Network Type', 'Ground Level', 'Invert Level', 'Safe Operating Head'])
    nodes_df.to_csv(working_folder + "\\" + con_csv_nodes, index = False)

    lines_df = pd.DataFrame(lines, columns =['MUID', 'Acronym', 'Owner', 'Status', 'FromNode', 'ToNode', 'Layer', 'Folder'])
    lines_df.to_csv(working_folder + "\\" + con_csv_lines, index = False)

    arcpy.env.overwriteOutput = True

    if extension == ".mdb":
        msm_Node = mu_path + "\\mu_Geometry\\msm_Node"
    else:

        arcpy.FeatureClassToFeatureClass_conversion (mu_path + "\\msm_Node", working_folder, 'msm_Node.shp')
        msm_Node = working_folder + '\\msm_Node.shp'
        arcpy.DefineProjection_management(msm_Node, "PROJCS['NAD_1983_2011_UTM_Zone_10N',GEOGCS['GCS_NAD_1983_2011',DATUM['D_NAD_1983_2011',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-123.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]")


    Google_Coordinates_shp = working_folder + "\\Google_Coordinates.shp"
    arcpy.Project_management(msm_Node, Google_Coordinates_shp, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "WGS_1984_(ITRF08)_To_NAD_1983_2011", "PROJCS['NAD_1983_2011_UTM_Zone_10N',GEOGCS['GCS_NAD_1983_2011',DATUM['D_NAD_1983_2011',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-123.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]", "NO_PRESERVE_SHAPE", "", "NO_VERTICAL")
    centroids = arcpy.da.FeatureClassToNumPyArray(Google_Coordinates_shp, ("MUID","SHAPE@X","SHAPE@Y"))
    centroids = centroids.tolist()
    centroids_df = pd.DataFrame(centroids, columns =['MUID','X','Y'])
    centroids_df.to_csv(working_folder + '\\Google_Coordinates.csv', index = False)

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])



