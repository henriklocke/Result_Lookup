import pypyodbc #used to run Access queries
import shutil #For copy file
import ctypes
import os # for file operations
import pandas as pd
import sqlite3
import os
import sys

def sql_to_df(sql, full_path):
    print sql
    queryOutput = []
    conn = pypyodbc.win_connect_mdb(full_path)
    cur = conn.cursor()
    df = pd.read_sql(sql, conn)
    cur.close()
    conn.close()
    return df

working_folder = os.getcwd()
mu_path = r"J:\SEWER_AREA_MODELS\NWL\03_SIMULATION_WORK\Phase_2_INI\Model\ReTrace\NWL_Phase2_2040Pop.mdb"

def main(working_folder,mu_path):
##if 1 == 1: #For debugging in idle/pyscripter uncomment this line and comment the above.

    sql = "SELECT ms_DPProfileD.ScheduleID AS Day_Type, ms_DPPatternD.Sqn - 1 AS [Hour], Sum(ms_LALoadAlloc.WaterLoad*ms_DPPatternD.DPValue)/86400 AS Wastewater "
    sql += "FROM ((msm_BItem INNER JOIN (ms_LALoadAlloc INNER JOIN msm_BBoundary ON ms_LALoadAlloc.LoadCategoryNo = msm_BBoundary.LoadCategoryNo) ON msm_BItem.BoundaryID = msm_BBoundary.MUID) "
    sql += "INNER JOIN ms_DPProfileD ON msm_BItem.DPProfileID = ms_DPProfileD.ProfileID) INNER JOIN ms_DPPatternD ON ms_DPProfileD.PatternID = ms_DPPatternD.PatternID "
    sql += "WHERE ms_LALoadAlloc.LoadCategory<>'Baseflow' "
    sql += "GROUP BY ms_DPProfileD.ScheduleID, ms_DPPatternD.Sqn "
    sql += "HAVING ([ms_DPProfileD].[ScheduleID]='Weekdays' Or [ms_DPProfileD].[ScheduleID]='Weekends') AND [ms_DPPatternD].[Sqn]<>0"
    diurnal_wws = sql_to_df(sql,mu_path).rename(columns={'day_type':'Day_Type','hour':'Hour','wastewater':'Wastewater'})

    sql = "SELECT Sum(WaterLoad)/86400 FROM ms_LALoadAlloc WHERE LoadCategory = 'Baseflow'"
    gwi = sql_to_df(sql,mu_path).iloc[0,0]

    sql = "SELECT Sum(WaterLoad)/86400 FROM ms_LALoadAlloc WHERE LoadCategory = 'BSF'"
    bsf = sql_to_df(sql,mu_path).iloc[0,0]
    bsf = 0 if bsf == None else bsf

    gwi_bsf = pd.DataFrame({'Category': ['GWI','BSF'], 'Value': [gwi,bsf]})

    diurnal_wws.to_csv(working_folder + '\\Diurnals.csv', index = False)
    gwi_bsf.to_csv(working_folder + '\\GWI_BSF.csv', index = False)

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])


