##AFTER UPDATE AND SAVE YOU MUST RESTART THE KERNEL IN JUPYTER NOTEBOOK TO UPDATE VARIABLES!

##Remember to insert r in front of all paths, e.g. r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Calibration_2022\MODEL"

#All setups, initialize lists to not throw error if undefined.
name_shortenings = []
pipe_ls_exclusions = []
element_filter = []
master_list = []
wwtp_pipe = ''
outfall_summary = ''
mus_path = ''
delay_hours = 0 #Only for the timeconsuming result lookup script, used if the sims are done after hours, to run the tool afterwards.
python_installation = r"C:\Python27\ArcGIS10.7\python.exe"

# #FSA always latest
# model_area = 'FSA'
# wwtp_pipe = '52458'
# groupby_acronym_owner = True
# pipe_ls_exclusions = ['55773','55778','55783','55788','55796','55799','55803']
# model = 'FSA_Base_2021pop_V170.sqlite'
# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_FSA\HTML_Plots'
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_FSA\Model"
# outfall_summary = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Calibration_2022\WWF_Calibration_Reports\FSA_Calibration_Specs\Outfall_Summary_No_Recapture.csv"
# element_filter = []
# res_list = []
# res_list.append(['2yr 24h No Climate Change','FSA_GA_EX-2y-24h-AES_2021p_Base-DSS1Default_Network_HD.res1d','Design Storms'])
# res_list.append(['5yr 24h No Climate Change','FSA_GA_EX-5y-24h-AES_2021p_Base-DSS2Default_Network_HD.res1d','Design Storms'])
# res_list.append(['10yr 24h No Climate Change','FSA_GA_EX-10y-24h-AES_2021p_Base-DSS3Default_Network_HD.res1d','Design Storms'])
# res_list.append(['25yr 24h No Climate Change','FSA_GA_EX-25y-24h-AES_2021p_Base-DSS16Default_Network_HD.res1d','Design Storms'])
# res_list.append(['Dry Weather Flow','FSA_DWF_2021-07-22_4d_2021pop_BaseDefault_Network_HD.res1d','Dry Weather Flow'])
# res_list.append(['Jan 31 2020 Event','FSA_WWF_2020-01-29_6d_2021pop_BaseDefault_Network_HD.res1d','Jan 31 2020 Event'])
# res_list.append(['Nov 15 2021 Event','FSA_WWF_2021-11-12_5d_2021pop_BaseDefault_Network_HD.res1d','Nov 15 2021 Event'])
# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions,element_filter,name_shortenings,wwtp_pipe,outfall_summary,mus_path])


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# #FSA New West Balance
# model_area = 'FSA'
# wwtp_pipe = '52458'
# groupby_acronym_owner = True
# pipe_ls_exclusions = ['55773','55778','55783','55788','55796','55799','55803']
# model = 'FSA_2023pop_V157.sqlite'
# output_folder = r'J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\New_West_Captured\HTML_Plots'
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\LTS\Model_2023-4"
# outfall_summary = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\New_West_Captured\Outfall_Summary_NewWestOnly.csv"
# # mus_path = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\BLNI2_In_Line_Storage\HTML_GATE_SPLIT_SAPP4p5\Maps_And_CSS\Selections.mus"
# element_filter = []
# res_list = []

# res_list.append(['July 1 2023 - July 1 2024','FSA_WWF_2023-07-01_366d_2023pop_BaseDefault_Network_HD.res1d','LTS'])
# res_list.append(['July 1 2022 - July 1 2023','FSA_WWF_2022-07-01_365d_2023pop_Base.res1d','LTS'])
# res_list.append(['Jan 1 2021 - Jan 1 2022','FSA_WWF_2021-01-01_365d_2021pop_NewSapp_Base.res1d','LTS'])


# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions,element_filter,name_shortenings,wwtp_pipe,outfall_summary,mus_path])


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#FSA misc
model_area = 'FSA'
wwtp_pipe = '52458'
groupby_acronym_owner = True
pipe_ls_exclusions = ['55773','55778','55783','55788','55796','55799','55803']
model = 'FSA_2030pop_V147_Joshua_Info.sqlite'
output_folder = r'\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\REQUESTS\Joshua Redmond_ SYC2_HGL Modelling\HTML_Plots'
result_folder = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\REQUESTS\Joshua Redmond_ SYC2_HGL Modelling\Model_Joshua"
outfall_summary = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Calibration_2022\WWF_Calibration_Reports\FSA_Calibration_Specs\Outfall_Summary_No_Recapture.csv"
mus_path = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\REQUESTS\Joshua Redmond_ SYC2_HGL Modelling\Model_Joshua\Stoney_Creek_Elements_Joint.mus"
element_filter = []
res_list = []

res_list.append(['10yr 24h No Climate Change, Base','FSA_GA_EX-10y-24h-AES_2030p_Base-DSS19Default_Network_HD.res1d','Design Storms'])
res_list.append(['10yr 24h No Climate Change, 250 mm','FSA_GA_EX-10y-24h-AES_2030p_250mm_Base-DSS17Default_Network_HD.res1d','Design Storms'])
res_list.append(['10yr 24h No Climate Change, 550 mm','FSA_GA_EX-10y-24h-AES_2030p_550mm_Base-DSS17Default_Network_HD.res1d','Design Storms'])

res_list.append(['Jan 31 2020 Event, Base','FSA_WWF_2020-01-29_6d_2030pop_BaseDefault_Network_HD.res1d','Jan 31 2020 Event'])
res_list.append(['Jan 31 2020 Event, 250 mm','FSA_WWF_2020-01-29_6d_2030pop_250mm_BaseDefault_Network_HD.res1d','Jan 31 2020 Event'])
res_list.append(['Jan 31 2020 Event, 550 mm','FSA_WWF_2020-01-29_6d_2030pop_550mm_BaseDefault_Network_HD.res1d','Jan 31 2020 Event'])

res_list.append(['Nov 15 2021 Event, Base','FSA_WWF_2021-11-12_5d_2030pop_BaseDefault_Network_HD.res1d','Nov 15 2021 Event'])
res_list.append(['Nov 15 2021 Event, 250 mm','FSA_WWF_2021-11-12_5d_2030pop_250mm_BaseDefault_Network_HD.res1d','Nov 15 2021 Event'])
res_list.append(['Nov 15 2021 Event, 550 mm','FSA_WWF_2021-11-12_5d_2030pop_550mm_BaseDefault_Network_HD.res1d','Nov 15 2021 Event'])

master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions,element_filter,name_shortenings,wwtp_pipe,outfall_summary,mus_path])


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# #VSA Key Flows HGL
# model_area = 'VSA'
# wwtp_pipe = '51836'
# groupby_acronym_owner = True
# pipe_ls_exclusions = []
# model = 'VSA_BASE_MODEL_2025_Backup304_DWF_No_Tide.mdb'
# output_folder = r'J:\SEWER_AREA_MODELS\VSA\03_SIMULATION_WORK\Key_Flow_HGL_GIS_Sim_VSA\HTML_Plots'
# result_folder = r"J:\SEWER_AREA_MODELS\VSA\03_SIMULATION_WORK\Key_Flow_HGL_GIS_Sim_VSA\Model"
# outfall_summary = r"J:\SEWER_AREA_MODELS\VSA\03_SIMULATION_WORK\Key_Flow_HGL_GIS_Sim_VSA\HTML_Plots\Maps_And_CSS\Outfall_Summary_No_Recapture.csv"

# element_filter = []
# res_list = []
# res_list.append(['Dry Weather Flow, 2025pop','VSA_DWF_No_Tide_2025pop_Base.res1d','','Dry Weather Flow','VSA_BASE_MODEL_2025_Backup304_DWF_No_Tide.mdb'])
# res_list.append(['2yr 24h NoCC, 2025pop','VSA_WWF_EX-2yr-24hr-SCS1A_2025pop_Base.res1d','Design Storms','VSA_Runoff_EX-2yr-24hr-SCS1A_BaseRR.res1d','VSA_BASE_MODEL_2025_Backup304_DWF_No_Tide.mdb'])
# res_list.append(['5yr 24h NoCC, 2025pop','VSA_WWF_EX-5yr-24hr-SCS1A_2025pop_Base.res1d','Design Storms','VSA_Runoff_EX-5yr-24hr-SCS1A_BaseRR.res1d','VSA_BASE_MODEL_2025_Backup304_DWF_No_Tide.mdb'])
# res_list.append(['10yr 24h NoCC, 2025pop','VSA_WWF_EX-10yr-24hr-SCS1A_2025pop_Base.res1d','Design Storms','VSA_Runoff_EX-10yr-24hr-SCS1A_BaseRR.res1d','VSA_BASE_MODEL_2025_Backup304_DWF_No_Tide.mdb'])
# res_list.append(['25yr 24h NoCC, 2025pop','VSA_WWF_EX-25yr-24hr-SCS1A_2025pop_Base.res1d','Design Storms','VSA_Runoff_EX-25yr-24hr-SCS1A_BaseRR.res1d','VSA_BASE_MODEL_2025_Backup304_DWF_No_Tide.mdb'])

# res_list.append(['Dry Weather Flow, 2030pop','VSA_DWF_No_Tide_2030pop_Base.res1d','Dry Weather Flow','','VSA_BASE_MODEL_2030_Backup304_DWF_No_Tide.mdb'])
# res_list.append(['2yr 24h NoCC, 2030pop','VSA_WWF_EX-2yr-24hr-SCS1A_2030pop_Base.res1d','Design Storms','VSA_Runoff_EX-2yr-24hr-SCS1A_BaseRR.res1d','VSA_BASE_MODEL_2030_Backup304_DWF_No_Tide.mdb'])
# res_list.append(['5yr 24h NoCC, 2030pop','VSA_WWF_EX-5yr-24hr-SCS1A_2030pop_Base.res1d','Design Storms','VSA_Runoff_EX-5yr-24hr-SCS1A_BaseRR.res1d','VSA_BASE_MODEL_2030_Backup304_DWF_No_Tide.mdb'])
# res_list.append(['10yr 24h NoCC, 2030pop','VSA_WWF_EX-10yr-24hr-SCS1A_2030pop_Base.res1d','Design Storms','VSA_Runoff_EX-10yr-24hr-SCS1A_BaseRR.res1d','VSA_BASE_MODEL_2030_Backup304_DWF_No_Tide.mdb'])
# res_list.append(['25yr 24h NoCC, 2030pop','VSA_WWF_EX-25yr-24hr-SCS1A_2030pop_Base.res1d','Design Storms','VSA_Runoff_EX-25yr-24hr-SCS1A_BaseRR.res1d','VSA_BASE_MODEL_2030_Backup304_DWF_No_Tide.mdb'])

# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions,element_filter,name_shortenings,wwtp_pipe,outfall_summary,mus_path])

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@




# #FSA Key Flows HGL
# model_area = 'FSA'
# wwtp_pipe = '52458'
# groupby_acronym_owner = True
# pipe_ls_exclusions = ['55773','55778','55783','55788','55796','55799','55803']
# model = 'FSA_2025pop_V164.sqlite'
# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Key_Flow_HGL_GIS_Sim_FSA\HTML_Plots'
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Key_Flow_HGL_GIS_Sim_FSA\Model"
# outfall_summary = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Calibration_2022\WWF_Calibration_Reports\FSA_Calibration_Specs\Outfall_Summary_No_Recapture.csv"
# element_filter = []
# res_list = []
# res_list.append(['Dry Weather Flow, 2025pop','FSA_DWF_2021-07-22_4d_2025pop_BaseDefault_Network_HD.res1d','Dry Weather Flow'])
# res_list.append(['2yr 24h NoCC, 2025pop','FSA_GA_EX-2y-24h-AES_2025p_Base-DSS1Default_Network_HD.res1d','Design Storms'])
# res_list.append(['5yr 24h NoCC, 2025pop','FSA_GA_EX-5y-24h-AES_2025p_Base-DSS2Default_Network_HD.res1d','Design Storms'])
# res_list.append(['10yr 24h NoCC, 2025pop','FSA_GA_EX-10y-24h-AES_2025p_Base-DSS3Default_Network_HD.res1d','Design Storms'])
# res_list.append(['25yr 24h NoCC, 2025pop','FSA_GA_EX-25y-24h-AES_2025p_Base-DSS16Default_Network_HD.res1d','Design Storms'])

# res_list.append(['Dry Weather Flow, 2030pop','FSA_DWF_2021-07-22_4d_2030pop_2030_NetworkDefault_Network_HD.res1d','Dry Weather Flow'])
# res_list.append(['2yr 24h NoCC, 2030pop','FSA_GA_EX-2y-24h-AES_2030p_F_2030_Network-DSS4Default_Network_HD.res1d','Design Storms'])
# res_list.append(['5yr 24h NoCC, 2030pop','FSA_GA_EX-5y-24h-AES_2030p_F_2030_Network-DSS5Default_Network_HD.res1d','Design Storms'])
# res_list.append(['10yr 24h NoCC, 2030pop','FSA_GA_EX-10y-24h-AES_2030p_F_2030_Network-DSS6Default_Network_HD.res1d','Design Storms'])
# res_list.append(['25yr 24h NoCC, 2030pop','FSA_GA_EX-25y-24h-AES_2030p_F_2030_Network-DSS17Default_Network_HD.res1d','Design Storms'])

# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions,element_filter,name_shortenings,wwtp_pipe,outfall_summary,mus_path])


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


#NSSA Key Flows HGL
# model_area = 'NSSA'
# wwtp_pipe = '54959_a'
# groupby_acronym_owner = True
# pipe_ls_exclusions = []
# model = 'NSSA_2025pop_V93.sqlite'
# output_folder = r'J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\Key_Flow_HGL_GIS_Sim_NSSA\HTML_Plots'
# result_folder = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\Key_Flow_HGL_GIS_Sim_NSSA\Model"
# outfall_summary = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_NSSA\HTML_Plots\Maps_And_CSS\Outfall_Summary.csv"

# element_filter = []
# res_list = []
# res_list.append(['Dry Weather Flow, 2025pop','NSSA_DWF_2018-07-26_4d_2025pop_BaseDefault_Network_HD.res1d','Dry Weather Flow'])
# res_list.append(['2yr 24h NoCC, 2025pop','NSSA_GA_EX-2y-24h-AES_2025p_Base-DSS1Default_Network_HD.res1d','Design Storms'])
# res_list.append(['5yr 24h NoCC, 2025pop','NSSA_GA_EX-5y-24h-AES_2025p_Base-DSS2Default_Network_HD.res1d','Design Storms'])
# res_list.append(['10yr 24h NoCC, 2025pop','NSSA_GA_EX-10y-24h-AES_2025p_Base-DSS3Default_Network_HD.res1d','Design Storms'])
# res_list.append(['25yr 24h NoCC, 2025pop','NSSA_GA_EX-25y-24h-AES_2025p_Base-DSS10Default_Network_HD.res1d','Design Storms'])

# res_list.append(['Dry Weather Flow, 2030pop','NSSA_DWF_2018-07-26_4d_2030pop_BaseDefault_Network_HD.res1d','Dry Weather Flow'])
# res_list.append(['2yr 24h NoCC, 2030pop','NSSA_GA_EX-2y-24h-AES_2030p_Base-DSS1Default_Network_HD.res1d','Design Storms'])
# res_list.append(['5yr 24h NoCC, 2030pop','NSSA_GA_EX-5y-24h-AES_2030p_Base-DSS2Default_Network_HD.res1d','Design Storms'])
# res_list.append(['10yr 24h NoCC, 2030pop','NSSA_GA_EX-10y-24h-AES_2030p_Base-DSS3Default_Network_HD.res1d','Design Storms'])
# res_list.append(['25yr 24h NoCC, 2030pop','NSSA_GA_EX-25y-24h-AES_2030p_Base-DSS10Default_Network_HD.res1d','Design Storms'])

# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions,element_filter,name_shortenings,wwtp_pipe,outfall_summary,mus_path])

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# #LISA Key Flows HGL
# model_area = 'LISA'
# wwtp_pipe = 'Link_16'
# groupby_acronym_owner = True
# pipe_ls_exclusions = []
# model = 'LISA_2025pop_V21.sqlite'
# output_folder = r'J:\SEWER_AREA_MODELS\LISA\03_SIMULATION_WORK\Key_Flow_HGL_GIS_Sim_LISA\HTML_Plots'
# result_folder = r"J:\SEWER_AREA_MODELS\LISA\03_SIMULATION_WORK\Key_Flow_HGL_GIS_Sim_LISA\Model"
# outfall_summary = r"J:\SEWER_AREA_MODELS\LISA\03_SIMULATION_WORK\Key_Flow_HGL_GIS_Sim_LISA\HTML_Plots\Maps_And_CSS\Outfall_Summary.csv"

# element_filter = []
# res_list = []
# res_list.append(['Dry Weather Flow, 2025pop','LISA_DWF_2025pop_2025Default_Network_HD.res1d','Dry Weather Flow'])
# res_list.append(['2yr 24h NoCC, 2025pop','LISA_WWF_EX-2yr-24hr-SCS_2025pop_2025Default_Network_HD.res1d','Design Storms'])
# res_list.append(['5yr 24h NoCC, 2025pop','LISA_WWF_EX-5yr-24hr-SCS_2025pop_2025Default_Network_HD.res1d','Design Storms'])
# res_list.append(['10yr 24h NoCC, 2025pop','LISA_WWF_EX-10yr-24hr-SCS_2025pop_2025Default_Network_HD.res1d','Design Storms'])
# res_list.append(['25yr 24h NoCC, 2025pop','LISA_WWF_EX-25yr-24hr-SCS_2025pop_2025Default_Network_HD.res1d','Design Storms'])

# res_list.append(['Dry Weather Flow, 2030pop','LISA_DWF_2030pop_2030Default_Network_HD.res1d','Dry Weather Flow'])
# res_list.append(['2yr 24h NoCC, 2030pop','LISA_WWF_EX-2yr-24hr-SCS_2030pop_2030Default_Network_HD.res1d','Design Storms'])
# res_list.append(['5yr 24h NoCC, 2030pop','LISA_WWF_EX-5yr-24hr-SCS_2030pop_2030Default_Network_HD.res1d','Design Storms'])
# res_list.append(['10yr 24h NoCC, 2030pop','LISA_WWF_EX-10yr-24hr-SCS_2030pop_2030Default_Network_HD.res1d','Design Storms'])
# res_list.append(['25yr 24h NoCC, 2030pop','LISA_WWF_EX-25yr-24hr-SCS_2030pop_2030Default_Network_HD.res1d','Design Storms'])

# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions,element_filter,name_shortenings,wwtp_pipe,outfall_summary,mus_path])


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



# # #FSA BSF Sealed VFD
# model_area = 'FSA'

# wwtp_pipe = '52458'
# groupby_acronym_owner = True
# pipe_ls_exclusions = ['55773','55778','55783','55788','55796','55799','55803']
# model = 'FSA_2030pop_V164_VFD.sqlite' #Trace longitudinal section; can be any model in the model folder.
# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_0\HTML_Plots_V164_V' #create this folder and include the file "Maps_and_CSS" to the empty folder
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_0\Model_Master_V164_V" #model folder input
# outfall_summary = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Calibration_2022\WWF_Calibration_Reports\FSA_Calibration_Specs\Outfall_Summary_No_Recapture.csv"

# element_filter = []
# res_list = []


# res_list.append(['1 I/I, 2030 Pop','FSA_BSF_11p2k_2030pop_V_2030_NetworkDefault_Network_HD.res1d','1 * I/I'])
# res_list.append(['2 I/I, 2030 Pop','FSA_BSF_22p4k_2030pop_V_2030_NetworkDefault_Network_HD.res1d','2 * I/I'])
# res_list.append(['3 I/I, 2030 Pop','FSA_BSF_33p6k_2030pop_V_2030_NetworkDefault_Network_HD.res1d','3 * I/I'])
# # res_list.append(['4 I/I, 2030 Pop','FSA_BSF_44p8k_2030pop_V_2030_NetworkDefault_Network_HD.res1d','4 * I/I'])
# res_list.append(['1 I/I, 2040 Pop','FSA_BSF_11p2k_2040pop_V_2030_NetworkDefault_Network_HD.res1d','1 * I/I'])
# res_list.append(['2 I/I, 2040 Pop','FSA_BSF_22p4k_2040pop_V_2030_NetworkDefault_Network_HD.res1d','2 * I/I'])
# res_list.append(['3 I/I, 2040 Pop','FSA_BSF_33p6k_2040pop_V_2030_NetworkDefault_Network_HD.res1d','3 * I/I'])
# # res_list.append(['4 I/I, 2040 Pop','FSA_BSF_44p8k_2040pop_V_2030_NetworkDefault_Network_HD.res1d','4 * I/I'])
# res_list.append(['1 I/I, 2050 Pop','FSA_BSF_11p2k_2050pop_V_2030_NetworkDefault_Network_HD.res1d','1 * I/I'])
# res_list.append(['2 I/I, 2050 Pop','FSA_BSF_22p4k_2050pop_V_2030_NetworkDefault_Network_HD.res1d','2 * I/I'])
# res_list.append(['3 I/I, 2050 Pop','FSA_BSF_33p6k_2050pop_V_2030_NetworkDefault_Network_HD.res1d','3 * I/I'])
# # res_list.append(['4 I/I, 2050 Pop','FSA_BSF_44p8k_2050pop_V_2030_NetworkDefault_Network_HD.res1d','4 * I/I'])
# res_list.append(['1 I/I, 2060 Pop','FSA_BSF_11p2k_2060pop_V_2030_NetworkDefault_Network_HD.res1d','1 * I/I'])
# res_list.append(['2 I/I, 2060 Pop','FSA_BSF_22p4k_2060pop_V_2030_NetworkDefault_Network_HD.res1d','2 * I/I'])
# res_list.append(['3 I/I, 2060 Pop','FSA_BSF_33p6k_2060pop_V_2030_NetworkDefault_Network_HD.res1d','3 * I/I'])
# # res_list.append(['4 I/I, 2060 Pop','FSA_BSF_44p8k_2060pop_V_2030_NetworkDefault_Network_HD.res1d','4 * I/I'])
# res_list.append(['1 I/I, 2070 Pop','FSA_BSF_11p2k_2070pop_V_2030_NetworkDefault_Network_HD.res1d','1 * I/I'])
# res_list.append(['2 I/I, 2070 Pop','FSA_BSF_22p4k_2070pop_V_2030_NetworkDefault_Network_HD.res1d','2 * I/I'])
# res_list.append(['3 I/I, 2070 Pop','FSA_BSF_33p6k_2070pop_V_2030_NetworkDefault_Network_HD.res1d','3 * I/I'])
# # res_list.append(['4 I/I, 2070 Pop','FSA_BSF_44p8k_2070pop_V_2030_NetworkDefault_Network_HD.res1d','4 * I/I'])

# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions,element_filter,name_shortenings,wwtp_pipe,outfall_summary,mus_path])

# #

###########################################################################################################################################


##########################################################################################


# # #########


# # #FSA BSF Sealed VFD
# model_area = 'FSA'

# wwtp_pipe = '52458'
# mus_path = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\Model_V147_Sealed_VFD_AIWWTP_17cms_Upsize_RX_SSD\RX.mus"
# groupby_acronym_owner = True
# pipe_ls_exclusions = ['55773','55778','55783','55788','55796','55799','55803']
# model = 'FSA_2030pop_V147_BSF_16p8k_Sealed_VFD.sqlite' #Trace longitudinal section; can be any model in the model folder.
# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\HTML_Plots_V147_Sealed_VFD_AIWWTP_17cms_Upsize_RX_Test_SSD' #create this folder and include the file "Maps_and_CSS" to the empty folder
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\Model_V147_Sealed_VFD_AIWWTP_17cms_Upsize_RX_SSD" #model folder input
# outfall_summary = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Calibration_2022\WWF_Calibration_Reports\FSA_Calibration_Specs\Outfall_Summary_No_Recapture.csv"

# element_filter = []
# res_list = []

# res_list.append(['RX 1.2 m','FSA_BSF_16p8k_2075pop_S_V_2030_NetworkDefault_Network_HD_1p2.res1d','1.5 * I/I, 2075 pop'])
# res_list.append(['RX 1.3 m','FSA_BSF_16p8k_2075pop_S_V_2030_NetworkDefault_Network_HD_1p3.res1d','1.5 * I/I, 2075 pop'])
# res_list.append(['RX 1.5 m','FSA_BSF_16p8k_2075pop_S_V_2030_NetworkDefault_Network_HD_1p5.res1d','1.5 * I/I, 2075 pop'])
# res_list.append(['RX 1.7 m','FSA_BSF_16p8k_2075pop_S_V_2030_NetworkDefault_Network_HD_1p7.res1d','1.5 * I/I, 2075 pop'])



# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions,element_filter,name_shortenings,wwtp_pipe,outfall_summary,mus_path])

# #########

# # #FSA BSF Sealed VFD
# model_area = 'FSA'

# wwtp_pipe = '52458'
# groupby_acronym_owner = True
# pipe_ls_exclusions = ['55773','55778','55783','55788','55796','55799','55803']
# model = 'FSA_2030pop_V147_BSF_16p8k_Sealed_VFD.sqlite' #Trace longitudinal section; can be any model in the model folder.
# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\HTML_Plots_V147_Sealed_VFD_AIWWTP_17cms_Upsize_RX' #create this folder and include the file "Maps_and_CSS" to the empty folder
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\Model_V147_Sealed_VFD_AIWWTP_17cms_Upsize_RX" #model folder input
# outfall_summary = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Calibration_2022\WWF_Calibration_Reports\FSA_Calibration_Specs\Outfall_Summary_No_Recapture.csv"

# element_filter = []
# res_list = []

# res_list.append(['1.5 I/I, 2030 Pop','FSA_BSF_16p8k_2030pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.5 * I/I'])
# res_list.append(['1.5 I/I, 2040 Pop','FSA_BSF_16p8k_2040pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.5 * I/I'])
# res_list.append(['1.5 I/I, 2050 Pop','FSA_BSF_16p8k_2050pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.5 * I/I'])
# res_list.append(['1.5 I/I, 2060 Pop','FSA_BSF_16p8k_2060pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.5 * I/I'])
# # res_list.append(['1.5 I/I, 2070 Pop','FSA_BSF_16p8k_2070pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.5 * I/I'])
# res_list.append(['1.5 I/I, 2075 Pop','FSA_BSF_16p8k_2075pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.5 * I/I'])


# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions,element_filter,name_shortenings,wwtp_pipe,outfall_summary])

# #########

# # #FSA BSF Sealed VFD
# model_area = 'FSA'

# wwtp_pipe = '52458'
# groupby_acronym_owner = True
# pipe_ls_exclusions = ['55773','55778','55783','55788','55796','55799','55803']
# model = 'FSA_2030pop_V147_BSF_16p8k_Sealed_VFD.sqlite' #Trace longitudinal section; can be any model in the model folder.
# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\HTML_Plots_V147_Sealed_VFD_AIWWTP_17cms_Upsize_RX_SSD' #create this folder and include the file "Maps_and_CSS" to the empty folder
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\Model_V147_Sealed_VFD_AIWWTP_17cms_Upsize_RX_SSD" #model folder input
# outfall_summary = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Calibration_2022\WWF_Calibration_Reports\FSA_Calibration_Specs\Outfall_Summary_No_Recapture.csv"

# element_filter = []
# res_list = []

# res_list.append(['1.5 I/I, 2030 Pop','FSA_BSF_16p8k_2030pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.5 * I/I'])
# res_list.append(['1.5 I/I, 2040 Pop','FSA_BSF_16p8k_2040pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.5 * I/I'])
# res_list.append(['1.5 I/I, 2050 Pop','FSA_BSF_16p8k_2050pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.5 * I/I'])
# res_list.append(['1.5 I/I, 2060 Pop','FSA_BSF_16p8k_2060pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.5 * I/I'])
# # res_list.append(['1.5 I/I, 2070 Pop','FSA_BSF_16p8k_2070pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.5 * I/I'])
# res_list.append(['1.5 I/I, 2075 Pop','FSA_BSF_16p8k_2075pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.5 * I/I'])


# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions,element_filter,name_shortenings,wwtp_pipe,outfall_summary,mus_path])

# # #########


###########################################################################################################################################


# #NWL
# model_area = 'NWL'

# wwtp_pipe = 'NWL_2129'
# groupby_acronym_owner = True
# pipe_ls_exclusions = []
# model = 'NWL_Phase2_2040Pop.mdb' #Trace longitudinal section; can be any model in the model folder.
# output_folder = r'J:\SEWER_AREA_MODELS\NWL\03_SIMULATION_WORK\Phase_2_INI\HTML_Plots' #create this folder and include the file "Maps_and_CSS" to the empty folder
# result_folder = r"J:\SEWER_AREA_MODELS\NWL\03_SIMULATION_WORK\Phase_2_INI\Model" #model folder input
# outfall_summary = r"J:\SEWER_AREA_MODELS\NWL\03_SIMULATION_WORK\Phase_2_INI\Model\ReTrace\Outfall_Summary_NWL.csv"

# element_filter = []
# res_list = []

# res_list.append(['2yr-24hr NoCC, 2040 Pop, Regular Cover/PS','NWL_WWF_EX-2yr-24hr-AES_2040pop_Base.res1d','Design Storm','NWL_Runoff_EX-2yr-24hr-AES_BaseRR.res1d'])
# res_list.append(['5yr-24hr NoCC, 2040 Pop, Regular Cover/PS','NWL_WWF_EX-5yr-24hr-AES_2040pop_Base.res1d','Design Storm','NWL_Runoff_EX-5yr-24hr-AES_BaseRR.res1d'])
# res_list.append(['2yr-24hr NoCC, 2040 Pop, Sealed VFD','NWL_WWF_EX-2yr-24hr-AES_2040pop_S_V_Base.res1d','Design Storm','NWL_Runoff_EX-2yr-24hr-AES_BaseRR.res1d'])
# res_list.append(['5yr-24hr NoCC, 2040 Pop, Sealed VFD','NWL_WWF_EX-5yr-24hr-AES_2040pop_S_V_Base.res1d','Design Storm','NWL_Runoff_EX-5yr-24hr-AES_BaseRR.res1d'])

# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions,element_filter,name_shortenings,wwtp_pipe,outfall_summary,mus_path])

# # ###########################################################################################################################################


# #FSA BSF Not Sealed No VFD
# model_area = 'FSA'

# wwtp_pipe = '52458'
# groupby_acronym_owner = True
# pipe_ls_exclusions = ['55773','55778','55783','55788','55796','55799','55803']
# model = 'FSA_2030pop_V147_BSF_16p8k.sqlite' #Trace longitudinal section; can be any model in the model folder.
# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\HTML_Plots_V147_Not_Sealed_No_VFD' #create this folder and include the file "Maps_and_CSS" to the empty folder
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\Model_V147_Not_Sealed_No_VFD" #model folder input
# outfall_summary = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Calibration_2022\WWF_Calibration_Reports\FSA_Calibration_Specs\Outfall_Summary_No_Recapture.csv"

# element_filter = []
# res_list = []


# res_list.append(['1.4 I/I, 2040 Pop','FSA_BSF_15p68k_2040pop_2030_NetworkDefault_Network_HD.res1d','X * I/I'])
# res_list.append(['1.3 I/I, 2050 Pop','FSA_BSF_14p56k_2050pop_2030_NetworkDefault_Network_HD.res1d','X * I/I'])
# res_list.append(['1.2 I/I, 2060 Pop','FSA_BSF_13p44k_2060pop_2030_NetworkDefault_Network_HD.res1d','X * I/I'])
# res_list.append(['1.1 I/I, 2070 Pop','FSA_BSF_12p32k_2070pop_2030_NetworkDefault_Network_HD.res1d','X * I/I'])
# res_list.append(['1.0 I/I, 2075 Pop','FSA_BSF_11p2k_2075pop_2030_NetworkDefault_Network_HD.res1d','X * I/I'])


# res_list.append(['1.5 I/I, 2030 Pop','FSA_BSF_16p8k_2030pop_2030_NetworkDefault_Network_HD.res1d','1.5 * I/I'])
# res_list.append(['1.5 I/I, 2040 Pop','FSA_BSF_16p8k_2040pop_2030_NetworkDefault_Network_HD.res1d','1.5 * I/I'])
# res_list.append(['1.5 I/I, 2050 Pop','FSA_BSF_16p8k_2050pop_2030_NetworkDefault_Network_HD.res1d','1.5 * I/I'])
# res_list.append(['1.5 I/I, 2060 Pop','FSA_BSF_16p8k_2060pop_2030_NetworkDefault_Network_HD.res1d','1.5 * I/I'])
# # res_list.append(['1.5 I/I, 2070 Pop','FSA_BSF_16p8k_2070pop_2030_NetworkDefault_Network_HD.res1d','1.5 * I/I'])
# res_list.append(['1.5 I/I, 2075 Pop','FSA_BSF_16p8k_2075pop_2030_NetworkDefault_Network_HD.res1d','1.5 * I/I'])


# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions,element_filter,name_shortenings,wwtp_pipe,outfall_summary,mus_path])

# # # ###########################################################################################################################################

# # #FSA BSF Sealed VFD
# model_area = 'FSA'

# wwtp_pipe = '52458'
# groupby_acronym_owner = True
# pipe_ls_exclusions = ['55773','55778','55783','55788','55796','55799','55803']
# model = 'FSA_2030pop_V147_BSF_16p8k_Sealed_VFD.sqlite' #Trace longitudinal section; can be any model in the model folder.
# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\HTML_Plots_V147_Sealed_VFD_AIWWT_17cms' #create this folder and include the file "Maps_and_CSS" to the empty folder
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\Model_V147_Sealed_VFD_AIWWTP_17cms" #model folder input
# outfall_summary = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Calibration_2022\WWF_Calibration_Reports\FSA_Calibration_Specs\Outfall_Summary_No_Recapture.csv"

# element_filter = []
# res_list = []


# res_list.append(['1.4 I/I, 2040 Pop','FSA_BSF_15p68k_2040pop_S_V_2030_NetworkDefault_Network_HD.res1d','X * I/I'])
# res_list.append(['1.3 I/I, 2050 Pop','FSA_BSF_14p56k_2050pop_S_V_2030_NetworkDefault_Network_HD.res1d','X * I/I'])
# res_list.append(['1.2 I/I, 2060 Pop','FSA_BSF_13p44k_2060pop_S_V_2030_NetworkDefault_Network_HD.res1d','X * I/I'])
# res_list.append(['1.1 I/I, 2070 Pop','FSA_BSF_12p32k_2070pop_S_V_2030_NetworkDefault_Network_HD.res1d','X * I/I'])
# res_list.append(['1.0 I/I, 2075 Pop','FSA_BSF_11p2k_2075pop_S_V_2030_NetworkDefault_Network_HD.res1d','X * I/I'])

# res_list.append(['1.5 I/I, 2030 Pop','FSA_BSF_16p8k_2030pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.5 * I/I'])
# res_list.append(['1.5 I/I, 2040 Pop','FSA_BSF_16p8k_2040pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.5 * I/I'])
# res_list.append(['1.5 I/I, 2050 Pop','FSA_BSF_16p8k_2050pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.5 * I/I'])
# res_list.append(['1.5 I/I, 2060 Pop','FSA_BSF_16p8k_2060pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.5 * I/I'])
# # res_list.append(['1.5 I/I, 2070 Pop','FSA_BSF_16p8k_2070pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.5 * I/I'])
# res_list.append(['1.5 I/I, 2075 Pop','FSA_BSF_16p8k_2075pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.5 * I/I'])


# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions,element_filter,name_shortenings,wwtp_pipe,outfall_summary,mus_path])


###########################################################################################################################################


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# # #FSA Sys As not sealed not vfd
# model_area = 'FSA'
# groupby_acronym_owner = True
# pipe_ls_exclusions = ['55773','55778','55783','55788','55796','55799','55803']
# model = 'FSA_2060pop_V131_No_Tide.sqlite'
# element_filter = []
# wwtp_pipe = '52458'

# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\System_Assessment\TestNoTide'
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\System_Assessment\TestNoTide"
# outfall_summary = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\System_Assessment\TestNoTide\Outfall_Summary_No_Recapture.csv"

# res_list = []

# res_list.append(['Nov 15 2021, 2060 Pop','FSA_WWF_2021-11-12_5d_2060pop_NoTide_2030_NetworkDefault_Network_HD.res1d','Nov 15 2021 Storm'])

# name_shortenings = []
# name_shortenings.append(['Dry Weather Flow','DWF'])
# name_shortenings.append([' Design',''])
# name_shortenings.append([' Storm',''])
# name_shortenings.append(['Times','*'])
# name_shortenings.append(['Three','3'])
# name_shortenings.append(['Basic Service Flow','BSF'])

# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions,element_filter,name_shortenings,wwtp_pipe,outfall_summary,mus_path])



# ##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# # #FSA BSF
# model_area = 'FSA'

# wwtp_pipe = '52458'
# groupby_acronym_owner = True
# pipe_ls_exclusions = ['55773','55778','55783','55788','55796','55799','55803']
# model = 'FSA_2030pop_V138_BSF_11p2k_Sealed_VFD.sqlite'
# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\HTML_Plots_V138'
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\Model_V138_Sealed_VFD"
# outfall_summary = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Calibration_2022\WWF_Calibration_Reports\FSA_Calibration_Specs\Outfall_Summary_No_Recapture.csv"

# element_filter = []
# res_list = []
# # res_list.append(['1.45 I/I, 2030 Pop','FSA_BSF_16p24k_2030pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.15-1.45 * I/I'])
# # res_list.append(['1.35 I/I, 2040 Pop','FSA_BSF_15p12k_2040pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.15-1.45 * I/I'])
# # res_list.append(['1.25 I/I, 2050 Pop','FSA_BSF_14k_2050pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.15-1.45 * I/I'])
# # res_list.append(['1.15 I/I, 2076 Pop','FSA_BSF_12p88k_2076pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.15-1.45 * I/I'])
# # res_list.append(['1 I/I, 2076 Pop, No SSG/SSJ','FSA_BSF_11p2k_2076pop_S_V_No_SSG_SSJ2_2030_NetworkDefault_Network_HD.res1d','1 * I/I'])

# res_list.append(['1 I/I, 2030 Pop','FSA_BSF_11p2k_2030pop_S_V_2030_NetworkDefault_Network_HD.res1d','1 * I/I'])
# res_list.append(['1 I/I, 2040 Pop','FSA_BSF_11p2k_2040pop_S_V_2030_NetworkDefault_Network_HD.res1d','1 * I/I'])
# res_list.append(['1 I/I, 2050 Pop','FSA_BSF_11p2k_2050pop_S_V_2030_NetworkDefault_Network_HD.res1d','1 * I/I'])
# res_list.append(['1 I/I, 2076 Pop','FSA_BSF_11p2k_2076pop_S_V_2030_NetworkDefault_Network_HD.res1d','1 * I/I'])

# res_list.append(['1.25 I/I, 2030 Pop','FSA_BSF_14k_2030pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.25 * I/I'])
# res_list.append(['1.25 I/I, 2040 Pop','FSA_BSF_14k_2040pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.25 * I/I'])
# res_list.append(['1.25 I/I, 2050 Pop','FSA_BSF_14k_2050pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.25 * I/I'])
# res_list.append(['1.25 I/I, 2076 Pop','FSA_BSF_14k_2076pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.25 * I/I'])

# res_list.append(['1.3 I/I, 2030 Pop','FSA_BSF_14p56k_2030pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.3 * I/I'])
# res_list.append(['1.3 I/I, 2040 Pop','FSA_BSF_14p56k_2040pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.3 * I/I'])
# res_list.append(['1.3 I/I, 2050 Pop','FSA_BSF_14p56k_2050pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.3 * I/I'])
# res_list.append(['1.3 I/I, 2076 Pop','FSA_BSF_14p56k_2076pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.3 * I/I'])

# res_list.append(['1.4 I/I, 2030 Pop','FSA_BSF_15p68k_2030pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.4 * I/I'])
# res_list.append(['1.4 I/I, 2040 Pop','FSA_BSF_15p68k_2040pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.4 * I/I'])
# res_list.append(['1.4 I/I, 2050 Pop','FSA_BSF_15p68k_2050pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.4 * I/I'])
# res_list.append(['1.4 I/I, 2076 Pop','FSA_BSF_15p68k_2076pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.4 * I/I'])

# res_list.append(['1.5 I/I, 2030 Pop','FSA_BSF_16p8k_2030pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.5 * I/I'])
# res_list.append(['1.5 I/I, 2040 Pop','FSA_BSF_16p8k_2040pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.5 * I/I'])
# res_list.append(['1.5 I/I, 2050 Pop','FSA_BSF_16p8k_2050pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.5 * I/I'])
# res_list.append(['1.5 I/I, 2076 Pop','FSA_BSF_16p8k_2076pop_S_V_2030_NetworkDefault_Network_HD.res1d','1.5 * I/I'])

# res_list.append(['2 I/I, 2030 Pop','FSA_BSF_22p4k_2030pop_S_V_2030_NetworkDefault_Network_HD.res1d','2 * I/I'])
# res_list.append(['2 I/I, 2040 Pop','FSA_BSF_22p4k_2040pop_S_V_2030_NetworkDefault_Network_HD.res1d','2 * I/I'])
# res_list.append(['2 I/I, 2050 Pop','FSA_BSF_22p4k_2050pop_S_V_2030_NetworkDefault_Network_HD.res1d','2 * I/I'])
# res_list.append(['2 I/I, 2076 Pop','FSA_BSF_22p4k_2076pop_S_V_2030_NetworkDefault_Network_HD.res1d','2 * I/I'])

# # res_list.append(['2.3 I/I, 2030 Pop','FSA_BSF_25p76k_2030pop_S_V_2030_NetworkDefault_Network_HD.res1d','2.3 * I/I'])
# # res_list.append(['2.3 I/I, 2040 Pop','FSA_BSF_25p76k_2040pop_S_V_2030_NetworkDefault_Network_HD.res1d','2.3 * I/I'])
# # res_list.append(['2.3 I/I, 2050 Pop','FSA_BSF_25p76k_2050pop_S_V_2030_NetworkDefault_Network_HD.res1d','2.3 * I/I'])
# # res_list.append(['2.3 I/I, 2076 Pop','FSA_BSF_25p76k_2076pop_S_V_2030_NetworkDefault_Network_HD.res1d','2.3 * I/I'])
# # res_list.append(['2.5 I/I, 2030 Pop','FSA_BSF_28k_2030pop_S_V_2030_NetworkDefault_Network_HD.res1d','2.5 * I/I'])
# # res_list.append(['2.5 I/I, 2040 Pop','FSA_BSF_28k_2040pop_S_V_2030_NetworkDefault_Network_HD.res1d','2.5 * I/I'])
# # res_list.append(['2.5 I/I, 2050 Pop','FSA_BSF_28k_2050pop_S_V_2030_NetworkDefault_Network_HD.res1d','2.5 * I/I'])
# # res_list.append(['2.5 I/I, 2076 Pop','FSA_BSF_28k_2076pop_S_V_2030_NetworkDefault_Network_HD.res1d','2.5 * I/I'])
# # res_list.append(['3 I/I, 2030 Pop','FSA_BSF_33p6k_2030pop_S_V_2030_NetworkDefault_Network_HD.res1d','3 * I/I'])
# # res_list.append(['3 I/I, 2040 Pop','FSA_BSF_33p6k_2040pop_S_V_2030_NetworkDefault_Network_HD.res1d','3 * I/I'])
# # res_list.append(['3 I/I, 2050 Pop','FSA_BSF_33p6k_2050pop_S_V_2030_NetworkDefault_Network_HD.res1d','3 * I/I'])
# # res_list.append(['3 I/I, 2076 Pop','FSA_BSF_33p6k_2076pop_S_V_2030_NetworkDefault_Network_HD.res1d','3 * I/I'])
# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions,element_filter,name_shortenings,wwtp_pipe,outfall_summary,mus_path])

# # # ##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# # #FSA Sys As not sealed not vfd
# model_area = 'FSA'
# groupby_acronym_owner = True
# pipe_ls_exclusions = ['55773','55778','55783','55788','55796','55799','55803']
# model = 'FSA_2030pop_V131.sqlite'
# element_filter = []
# wwtp_pipe = '52458'

# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\System_Assessment\HTML_Plots'
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\System_Assessment\FSA_System_Assessment"
# outfall_summary = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Calibration_2022\WWF_Calibration_Reports\FSA_Calibration_Specs\Outfall_Summary_No_Recapture.csv"

# res_list = []
# res_list.append(['Dry Weather Flow, 2021 Pop','FSA_DWF_2021-07-22_4d_2021pop_BaseDefault_Network_HD.res1d','Dry Weather Flow'])
# res_list.append(['Dry Weather Flow, 2030 Pop','FSA_DWF_2021-07-22_4d_2030pop_2030_NetworkDefault_Network_HD.res1d','Dry Weather Flow'])
# res_list.append(['Dry Weather Flow, 2040 Pop','FSA_DWF_2021-07-22_4d_2040pop_2030_NetworkDefault_Network_HD.res1d','Dry Weather Flow'])
# res_list.append(['Dry Weather Flow, 2050 Pop','FSA_DWF_2021-07-22_4d_2050pop_2030_NetworkDefault_Network_HD.res1d','Dry Weather Flow'])
# res_list.append(['Dry Weather Flow, 2060 Pop','FSA_DWF_2021-07-22_4d_2060pop_2030_NetworkDefault_Network_HD.res1d','Dry Weather Flow'])

# res_list.append(['Basic Service Flow, 2021 Pop','FSA_BSF_11p2k_2021pop_BaseDefault_Network_HD.res1d','Basic Service Flow'])
# res_list.append(['Basic Service Flow, 2030 Pop','FSA_BSF_11p2k_2030pop_2030_NetworkDefault_Network_HD.res1d','Basic Service Flow'])
# res_list.append(['Basic Service Flow, 2040 Pop','FSA_BSF_11p2k_2040pop_2030_NetworkDefault_Network_HD.res1d','Basic Service Flow'])
# res_list.append(['Basic Service Flow, 2050 Pop','FSA_BSF_11p2k_2050pop_2030_NetworkDefault_Network_HD.res1d','Basic Service Flow'])
# res_list.append(['Basic Service Flow, 2060 Pop','FSA_BSF_11p2k_2060pop_2030_NetworkDefault_Network_HD.res1d','Basic Service Flow'])


# res_list.append(['2yr-24hr NoCC, 2021 Pop','FSA_GA_EX-2y-24h-AES_2021p_Base-DSS1Default_Network_HD.res1d','2yr-24hr Design Storm'])
# res_list.append(['2yr-24hr NoCC, 2030 Pop','FSA_GA_EX-2y-24h-AES_2030p_F_2030_Network-DSS4Default_Network_HD.res1d','2yr-24hr Design Storm'])
# res_list.append(['2yr-24hr 2050M, 2040 Pop','FSA_GA_2050M-2y-24h-AES_2040p_F_2030_Network-DSS7Default_Network_HD.res1d','2yr-24hr Design Storm'])
# res_list.append(['2yr-24hr 2050H, 2040 Pop','FSA_GA_2050H-2y-24h-AES_2040p_F_2030_Network-DSS10Default_Network_HD.res1d','2yr-24hr Design Storm'])
# res_list.append(['2yr-24hr 2050H, 2050 Pop','FSA_GA_2050H-2y-24h-AES_2050p_F_2030_Network-DSS10Default_Network_HD.res1d','2yr-24hr Design Storm'])
# res_list.append(['2yr-24hr 2050H, 2060 Pop','FSA_GA_2050H-2y-24h-AES_2060p_F_2030_Network-DSS10Default_Network_HD.res1d','2yr-24hr Design Storm'])
# res_list.append(['2yr-24hr 2100H, 2060 Pop','FSA_GA_2100H-2y-24h-AES_2060p_F_2030_Network-DSS13Default_Network_HD.res1d','2yr-24hr Design Storm'])

# res_list.append(['5yr-24hr NoCC, 2021 Pop','FSA_GA_EX-5y-24h-AES_2021p_Base-DSS2Default_Network_HD.res1d','5yr-24hr Design Storm'])
# res_list.append(['5yr-24hr NoCC, 2030 Pop','FSA_GA_EX-5y-24h-AES_2030p_F_2030_Network-DSS5Default_Network_HD.res1d','5yr-24hr Design Storm'])
# res_list.append(['5yr-24hr 2050M, 2040 Pop','FSA_GA_2050M-5y-24h-AES_2040p_F_2030_Network-DSS8Default_Network_HD.res1d','5yr-24hr Design Storm'])
# res_list.append(['5yr-24hr 2050H, 2040 Pop','FSA_GA_2050H-5y-24h-AES_2040p_F_2030_Network-DSS11Default_Network_HD.res1d','5yr-24hr Design Storm'])
# res_list.append(['5yr-24hr 2050H, 2050 Pop','FSA_GA_2050H-5y-24h-AES_2050p_F_2030_Network-DSS11Default_Network_HD.res1d','5yr-24hr Design Storm'])
# res_list.append(['5yr-24hr 2050H, 2060 Pop','FSA_GA_2050H-5y-24h-AES_2060p_F_2030_Network-DSS11Default_Network_HD.res1d','5yr-24hr Design Storm'])
# res_list.append(['5yr-24hr 2100H, 2060 Pop','FSA_GA_2100H-5y-24h-AES_2060p_F_2030_Network-DSS14Default_Network_HD.res1d','5yr-24hr Design Storm'])

# res_list.append(['10yr-24hr NoCC, 2021 Pop','FSA_GA_EX-10y-24h-AES_2021p_Base-DSS3Default_Network_HD.res1d','10yr-24hr Design Storm'])
# res_list.append(['10yr-24hr NoCC, 2030 Pop','FSA_GA_EX-10y-24h-AES_2030p_F_2030_Network-DSS6Default_Network_HD.res1d','10yr-24hr Design Storm'])
# res_list.append(['10yr-24hr 2050M, 2040 Pop','FSA_GA_2050M-10y-24h-AES_2040p_F_2030_Network-DSS9Default_Network_HD.res1d','10yr-24hr Design Storm'])
# res_list.append(['10yr-24hr 2050H, 2040 Pop','FSA_GA_2050H-10y-24h-AES_2040p_F_2030_Network-DSS12Default_Network_HD.res1d','10yr-24hr Design Storm'])
# res_list.append(['10yr-24hr 2050H, 2050 Pop','FSA_GA_2050H-10y-24h-AES_2050p_F_2030_Network-DSS12Default_Network_HD.res1d','10yr-24hr Design Storm'])
# res_list.append(['10yr-24hr 2050H, 2060 Pop','FSA_GA_2050H-10y-24h-AES_2060p_F_2030_Network-DSS12Default_Network_HD.res1d','10yr-24hr Design Storm'])
# res_list.append(['10yr-24hr 2100H, 2060 Pop','FSA_GA_2100H-10y-24h-AES_2060p_F_2030_Network-DSS15Default_Network_HD.res1d','10yr-24hr Design Storm'])

# res_list.append(['Jan 31 2020, 2021 Pop','FSA_WWF_2020-01-29_6d_2021pop_BaseDefault_Network_HD.res1d','Jan 31 2020 Storm'])
# res_list.append(['Jan 31 2020, 2030 Pop','FSA_WWF_2020-01-29_6d_2030pop_2030_NetworkDefault_Network_HD.res1d','Jan 31 2020 Storm'])
# res_list.append(['Jan 31 2020, 2040 Pop','FSA_WWF_2020-01-29_6d_2040pop_2030_NetworkDefault_Network_HD.res1d','Jan 31 2020 Storm'])
# res_list.append(['Jan 31 2020, 2050 Pop','FSA_WWF_2020-01-29_6d_2050pop_2030_NetworkDefault_Network_HD.res1d','Jan 31 2020 Storm'])
# res_list.append(['Jan 31 2020, 2060 Pop','FSA_WWF_2020-01-29_6d_2060pop_2030_NetworkDefault_Network_HD.res1d','Jan 31 2020 Storm'])


# res_list.append(['Nov 15 2021, 2021 Pop','FSA_WWF_2021-11-12_5d_2021pop_BaseDefault_Network_HD.res1d','Nov 15 2021 Storm'])
# res_list.append(['Nov 15 2021, 2030 Pop','FSA_WWF_2021-11-12_5d_2030pop_2030_NetworkDefault_Network_HD.res1d','Nov 15 2021 Storm'])
# res_list.append(['Nov 15 2021, 2040 Pop','FSA_WWF_2021-11-12_5d_2040pop_2030_NetworkDefault_Network_HD.res1d','Nov 15 2021 Storm'])
# res_list.append(['Nov 15 2021, 2050 Pop','FSA_WWF_2021-11-12_5d_2050pop_2030_NetworkDefault_Network_HD.res1d','Nov 15 2021 Storm'])
# res_list.append(['Nov 15 2021, 2060 Pop','FSA_WWF_2021-11-12_5d_2060pop_2030_NetworkDefault_Network_HD.res1d','Nov 15 2021 Storm'])

# name_shortenings = []
# name_shortenings.append(['Dry Weather Flow','DWF'])
# name_shortenings.append([' Design',''])
# name_shortenings.append([' Storm',''])
# name_shortenings.append(['Times','*'])
# name_shortenings.append(['Three','3'])
# name_shortenings.append(['Basic Service Flow','BSF'])

# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions,element_filter,name_shortenings,wwtp_pipe,outfall_summary,mus_path])

# # # #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# #FSA Sys As sealed vfd
# model_area = 'FSA'
# groupby_acronym_owner = True
# pipe_ls_exclusions = ['55773','55778','55783','55788','55796','55799','55803']
# model = 'FSA_2030pop_V131_Sealed_VFD.sqlite'
# wwtp_pipe = '52458'

# output_folder = r'\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\System_Assessment\HTML_Plots_Sealed_VFD'
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\System_Assessment\FSA_System_Assessment_All_Sealed_VFD"
# element_filter = []
# res_list = []
# res_list.append(['Dry Weather Flow, 2021 Pop','FSA_DWF_2021-07-22_4d_2021pop_S_V_BaseDefault_Network_HD.res1d','Dry Weather Flow'])
# res_list.append(['Dry Weather Flow, 2030 Pop','FSA_DWF_2021-07-22_4d_2030pop_S_V_2030_NetworkDefault_Network_HD.res1d','Dry Weather Flow'])
# res_list.append(['Dry Weather Flow, 2040 Pop','FSA_DWF_2021-07-22_4d_2040pop_S_V_2030_NetworkDefault_Network_HD.res1d','Dry Weather Flow'])
# res_list.append(['Dry Weather Flow, 2050 Pop','FSA_DWF_2021-07-22_4d_2050pop_S_V_2030_NetworkDefault_Network_HD.res1d','Dry Weather Flow'])
# res_list.append(['Dry Weather Flow, 2060 Pop','FSA_DWF_2021-07-22_4d_2060pop_S_V_2030_NetworkDefault_Network_HD.res1d','Dry Weather Flow'])

# # res_list.append(['Three Times ADWF, 2021 Pop','FSA_3ADWF_2021pop_S_V_BaseDefault_Network_HD.res1d','Three Times ADWF'])
# # res_list.append(['Three Times ADWF, 2030 Pop','FSA_3ADWF_2030pop_S_V_2030_NetworkDefault_Network_HD.res1d','Three Times ADWF'])
# # res_list.append(['Three Times ADWF, 2040 Pop','FSA_3ADWF_2040pop_S_V_2030_NetworkDefault_Network_HD.res1d','Three Times ADWF'])
# # res_list.append(['Three Times ADWF, 2050 Pop','FSA_3ADWF_2050pop_S_V_2030_NetworkDefault_Network_HD.res1d','Three Times ADWF'])
# # res_list.append(['Three Times ADWF, 2060 Pop','FSA_3ADWF_2060pop_S_V_2030_NetworkDefault_Network_HD.res1d','Three Times ADWF'])

# res_list.append(['Basic Service Flow, 2021 Pop','FSA_BSF_11p2k_2021pop_S_V_BaseDefault_Network_HD.res1d','Basic Service Flow'])
# res_list.append(['Basic Service Flow, 2030 Pop','FSA_BSF_11p2k_2030pop_S_V_2030_NetworkDefault_Network_HD.res1d','Basic Service Flow'])
# res_list.append(['Basic Service Flow, 2040 Pop','FSA_BSF_11p2k_2040pop_S_V_2030_NetworkDefault_Network_HD.res1d','Basic Service Flow'])
# res_list.append(['Basic Service Flow, 2050 Pop','FSA_BSF_11p2k_2050pop_S_V_2030_NetworkDefault_Network_HD.res1d','Basic Service Flow'])
# res_list.append(['Basic Service Flow, 2060 Pop','FSA_BSF_11p2k_2060pop_S_V_2030_NetworkDefault_Network_HD.res1d','Basic Service Flow'])

# res_list.append(['2yr-24hr NoCC, 2021 Pop','FSA_GA_EX-2y-24h-AES_2021p_S_V_Base-DSS1Default_Network_HD.res1d','2yr-24hr Design Storm'])
# res_list.append(['2yr-24hr NoCC, 2030 Pop','FSA_GA_EX-2y-24h-AES_2030p_F_S_V_2030_Network-DSS4Default_Network_HD.res1d','2yr-24hr Design Storm'])
# res_list.append(['2yr-24hr 2050M, 2040 Pop','FSA_GA_2050M-2y-24h-AES_2040p_F_S_V_2030_Network-DSS7Default_Network_HD.res1d','2yr-24hr Design Storm'])
# res_list.append(['2yr-24hr 2050H, 2040 Pop','FSA_GA_2050H-2y-24h-AES_2040p_F_S_V_2030_Network-DSS10Default_Network_HD.res1d','2yr-24hr Design Storm'])
# res_list.append(['2yr-24hr 2050H, 2050 Pop','FSA_GA_2050H-2y-24h-AES_2050p_F_S_V_2030_Network-DSS10Default_Network_HD.res1d','2yr-24hr Design Storm'])
# res_list.append(['2yr-24hr 2050H, 2060 Pop','FSA_GA_2050H-2y-24h-AES_2060p_F_S_V_2030_Network-DSS10Default_Network_HD.res1d','2yr-24hr Design Storm'])
# res_list.append(['2yr-24hr 2100H, 2060 Pop','FSA_GA_2100H-2y-24h-AES_2060p_F_S_V_2030_Network-DSS13Default_Network_HD.res1d','2yr-24hr Design Storm'])

# res_list.append(['5yr-24hr NoCC, 2021 Pop','FSA_GA_EX-5y-24h-AES_2021p_S_V_Base-DSS2Default_Network_HD.res1d','5yr-24hr Design Storm'])
# res_list.append(['5yr-24hr NoCC, 2030 Pop','FSA_GA_EX-5y-24h-AES_2030p_F_S_V_2030_Network-DSS5Default_Network_HD.res1d','5yr-24hr Design Storm'])
# res_list.append(['5yr-24hr 2050M, 2040 Pop','FSA_GA_2050M-5y-24h-AES_2040p_F_S_V_2030_Network-DSS8Default_Network_HD.res1d','5yr-24hr Design Storm'])
# res_list.append(['5yr-24hr 2050H, 2040 Pop','FSA_GA_2050H-5y-24h-AES_2040p_F_S_V_2030_Network-DSS11Default_Network_HD.res1d','5yr-24hr Design Storm'])
# res_list.append(['5yr-24hr 2050H, 2050 Pop','FSA_GA_2050H-5y-24h-AES_2050p_F_S_V_2030_Network-DSS11Default_Network_HD.res1d','5yr-24hr Design Storm'])
# res_list.append(['5yr-24hr 2050H, 2060 Pop','FSA_GA_2050H-5y-24h-AES_2060p_F_S_V_2030_Network-DSS11Default_Network_HD.res1d','5yr-24hr Design Storm'])
# res_list.append(['5yr-24hr 2100H, 2060 Pop','FSA_GA_2100H-5y-24h-AES_2060p_F_S_V_2030_Network-DSS14Default_Network_HD.res1d','5yr-24hr Design Storm'])

# res_list.append(['10yr-24hr NoCC, 2021 Pop','FSA_GA_EX-10y-24h-AES_2021p_S_V_Base-DSS3Default_Network_HD.res1d','10yr-24hr Design Storm'])
# res_list.append(['10yr-24hr NoCC, 2030 Pop','FSA_GA_EX-10y-24h-AES_2030p_F_S_V_2030_Network-DSS6Default_Network_HD.res1d','10yr-24hr Design Storm'])
# res_list.append(['10yr-24hr 2050M, 2040 Pop','FSA_GA_2050M-10y-24h-AES_2040p_F_S_V_2030_Network-DSS9Default_Network_HD.res1d','10yr-24hr Design Storm'])
# res_list.append(['10yr-24hr 2050H, 2040 Pop','FSA_GA_2050H-10y-24h-AES_2040p_F_S_V_2030_Network-DSS12Default_Network_HD.res1d','10yr-24hr Design Storm'])
# res_list.append(['10yr-24hr 2050H, 2050 Pop','FSA_GA_2050H-10y-24h-AES_2050p_F_S_V_2030_Network-DSS12Default_Network_HD.res1d','10yr-24hr Design Storm'])
# res_list.append(['10yr-24hr 2050H, 2060 Pop','FSA_GA_2050H-10y-24h-AES_2060p_F_S_V_2030_Network-DSS12Default_Network_HD.res1d','10yr-24hr Design Storm'])
# res_list.append(['10yr-24hr 2100H, 2060 Pop','FSA_GA_2100H-10y-24h-AES_2060p_F_S_V_2030_Network-DSS15Default_Network_HD.res1d','10yr-24hr Design Storm'])

# res_list.append(['Jan 31 2020, 2021 Pop','FSA_WWF_2020-01-29_6d_2021pop_S_V_BaseDefault_Network_HD.res1d','Jan 31 2020 Storm'])
# res_list.append(['Jan 31 2020, 2030 Pop','FSA_WWF_2020-01-29_6d_2030pop_S_V_2030_NetworkDefault_Network_HD.res1d','Jan 31 2020 Storm'])
# res_list.append(['Jan 31 2020, 2040 Pop','FSA_WWF_2020-01-29_6d_2040pop_S_V_2030_NetworkDefault_Network_HD.res1d','Jan 31 2020 Storm'])
# res_list.append(['Jan 31 2020, 2050 Pop','FSA_WWF_2020-01-29_6d_2050pop_S_V_2030_NetworkDefault_Network_HD.res1d','Jan 31 2020 Storm'])
# res_list.append(['Jan 31 2020, 2060 Pop','FSA_WWF_2020-01-29_6d_2060pop_S_V_2030_NetworkDefault_Network_HD.res1d','Jan 31 2020 Storm'])

# res_list.append(['Nov 15 2021, 2021 Pop','FSA_WWF_2021-11-12_5d_2021pop_S_V_BaseDefault_Network_HD.res1d','Nov 15 2021 Storm'])
# res_list.append(['Nov 15 2021, 2030 Pop','FSA_WWF_2021-11-12_5d_2030pop_S_V_2030_NetworkDefault_Network_HD.res1d','Nov 15 2021 Storm'])
# res_list.append(['Nov 15 2021, 2040 Pop','FSA_WWF_2021-11-12_5d_2040pop_S_V_2030_NetworkDefault_Network_HD.res1d','Nov 15 2021 Storm'])
# res_list.append(['Nov 15 2021, 2050 Pop','FSA_WWF_2021-11-12_5d_2050pop_S_V_2030_NetworkDefault_Network_HD.res1d','Nov 15 2021 Storm'])
# res_list.append(['Nov 15 2021, 2060 Pop','FSA_WWF_2021-11-12_5d_2050pop_S_V_2030_NetworkDefault_Network_HD.res1d','Nov 15 2021 Storm'])

# name_shortenings = []
# name_shortenings.append(['Dry Weather Flow','DWF'])
# name_shortenings.append([' Design',''])
# name_shortenings.append([' Storm',''])
# name_shortenings.append(['Times','*'])
# name_shortenings.append(['Three','3'])
# name_shortenings.append(['Basic Service Flow','BSF'])

# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions,element_filter,name_shortenings,wwtp_pipe,outfall_summary,mus_path])

# # ##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# #NSSA always latest
# model_area = 'NSSA'
# groupby_acronym_owner = True
# pipe_ls_exclusions = []
# wwtp_pipe = '54959_a'
# model = 'NSSA_Base_2018pop_V087.sqlite'
# output_folder = r'J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_NSSA\HTML_Plots'
# result_folder = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_NSSA\Model"

# # model = 'NSSA_BaseV74.sqlite'
# # output_folder = r'J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_NSSA\HTML_Plots_Backup\V074'
# # result_folder = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_NSSA\Model\Backup_V074"

# outfall_summary = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_NSSA\HTML_Plots\Maps_And_CSS\Outfall_Summary.csv"
# element_filter = []
# res_list = []
# res_list.append(['Dry Weather Flow','NSSA_DWF_2018-07-26_4d_2018pop_BaseDefault_Network_HD.res1d','Dry Weather Flow'])
# res_list.append(['2yr-24hr NoCC','NSSA_GA_EX-2y-24h-AES_2018p_Base-DSS1Default_Network_HD.res1d','Design Storms'])
# res_list.append(['5yr-24hr NoCC','NSSA_GA_EX-5y-24h-AES_2018p_Base-DSS2Default_Network_HD.res1d','Design Storms'])
# res_list.append(['10yr-24hr NoCC','NSSA_GA_EX-10y-24h-AES_2018p_Base-DSS3Default_Network_HD.res1d','Design Storms'])
# res_list.append(['Nov 25 2018 Storm','NSSA_WWF_2018-11-25_3d_2018pop_BaseDefault_Network_HD.res1d','Nov 25 2018 Storm'])
# res_list.append(['Jan 31 2020 Storm','NSSA_WWF_2020-01-29_6d_2018pop_BaseDefault_Network_HD.res1d','Jan 31 2020 Storm'])
# res_list.append(['Nov 15 2021 Storm','NSSA_WWF_2021-11-12_5d_2018pop_BaseDefault_Network_HD.res1d','Nov 15 2021 Storm'])

# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions,element_filter,name_shortenings,wwtp_pipe,outfall_summary,mus_path])


##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# #NSSA Sys As not sealed not vfd
# model_area = 'NSSA'
# groupby_acronym_owner = True
# pipe_ls_exclusions = []
# model = 'NSSA_Base_2020pop.mdb'

# output_folder = r'J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\SYSTEM_ASSESSMENT\HTML_Plots'
# result_folder = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\SYSTEM_ASSESSMENT\NSSA_SYSTEM_ASSESSMENT"
# element_filter = []
# res_list = []
# res_list.append(['Dry Weather Flow, 2020 Population','NSSA_DWF_2018-07-26_4d_2020pop_Base.res1d','Dry Weather Flow'])
# res_list.append(['Dry Weather Flow, 2030 Population','NSSA_DWF_2018-07-26_4d_2030pop_Base.res1d','Dry Weather Flow'])
# res_list.append(['Dry Weather Flow, 2040 Population','NSSA_DWF_2018-07-26_4d_2040pop_Base.res1d','Dry Weather Flow'])
# res_list.append(['Dry Weather Flow, 2050 Population','NSSA_DWF_2018-07-26_4d_2050pop_Base.res1d','Dry Weather Flow'])
# res_list.append(['Three Times ADWF, 2020 Population','NSSA_3ADWF_2020p_Base.res1d','Three Times ADWF'])
# res_list.append(['Three Times ADWF, 2030 Population','NSSA_3ADWF_2030p_Base.res1d','Three Times ADWF'])
# res_list.append(['Three Times ADWF, 2040 Population','NSSA_3ADWF_2040p_Base.res1d','Three Times ADWF'])
# res_list.append(['Three Times ADWF, 2050 Population','NSSA_3ADWF_2050p_Base.res1d','Three Times ADWF'])
# res_list.append(['Basic Service Flow, 2020 Population','NSSA_BSF_11p2k_2020p_Base.res1d','Basic Service Flow'])
# res_list.append(['Basic Service Flow, 2030 Population','NSSA_BSF_11p2k_2030p_Base.res1d','Basic Service Flow'])
# res_list.append(['Basic Service Flow, 2040 Population','NSSA_BSF_11p2k_2040p_Base.res1d','Basic Service Flow'])
# res_list.append(['Basic Service Flow, 2050 Population','NSSA_BSF_11p2k_2050p_Base.res1d','Basic Service Flow'])

# res_list.append(['2yr-24hr NoCC, 2020 Population','NSSA_GA_EX-2y-24h-AES_2020p_Base.res1d','2yr-24hr Design Storm'])
# res_list.append(['2yr-24hr NoCC, 2030 Population','NSSA_GA_EX-2y-24h-AES_2030p_Base.res1d','2yr-24hr Design Storm'])
# res_list.append(['2yr-24hr 2050M, 2040 Population','NSSA_GA_2050M-2y-24h-AES_2040p_Base.res1d','2yr-24hr Design Storm'])
# res_list.append(['2yr-24hr 2050H, 2040 Population','NSSA_GA_2050H-2y-24h-AES_2040p_Base.res1d','2yr-24hr Design Storm'])
# res_list.append(['2yr-24hr 2050H, 2050 Population','NSSA_GA_2050H-2y-24h-AES_2050p_Base.res1d','2yr-24hr Design Storm'])

# res_list.append(['5yr-24hr NoCC, 2020 Population','NSSA_GA_EX-5y-24h-AES_2020p_Base.res1d','5yr-24hr Design Storm'])
# res_list.append(['5yr-24hr NoCC, 2030 Population','NSSA_GA_EX-5y-24h-AES_2030p_Base.res1d','5yr-24hr Design Storm'])
# res_list.append(['5yr-24hr 2050M, 2040 Population','NSSA_GA_2050M-5y-24h-AES_2040p_Base.res1d','5yr-24hr Design Storm'])
# res_list.append(['5yr-24hr 2050H, 2040 Population','NSSA_GA_2050H-5y-24h-AES_2040p_Base.res1d','5yr-24hr Design Storm'])
# res_list.append(['5yr-24hr 2050H, 2050 Population','NSSA_GA_2050H-5y-24h-AES_2050p_Base.res1d','5yr-24hr Design Storm'])

# res_list.append(['10yr-24hr NoCC, 2020 Population','NSSA_GA_EX-10y-24h-AES_2020p_Base.res1d','10yr-24hr Design Storm'])
# res_list.append(['10yr-24hr NoCC, 2030 Population','NSSA_GA_EX-10y-24h-AES_2030p_Base.res1d','10yr-24hr Design Storm'])
# res_list.append(['10yr-24hr 2050M, 2040 Population','NSSA_GA_2050M-10y-24h-AES_2040p_Base.res1d','10yr-24hr Design Storm'])
# res_list.append(['10yr-24hr 2050H, 2040 Population','NSSA_GA_2050H-10y-24h-AES_2040p_Base.res1d','10yr-24hr Design Storm'])
# res_list.append(['10yr-24hr 2050H, 2050 Population','NSSA_GA_2050H-10y-24h-AES_2050p_Base.res1d','10yr-24hr Design Storm'])

# res_list.append(['Jan 3 2019 Storm, 2020 Population','NSSA_WWF_2019-01-02_3d_2020pop_Base.res1d','Jan 3 2019 Storm'])
# res_list.append(['Jan 3 2019 Storm, 2030 Population','NSSA_WWF_2019-01-02_3d_2030pop_Base.res1d','Jan 3 2019 Storm'])
# res_list.append(['Jan 3 2019 Storm, 2040 Population','NSSA_WWF_2019-01-02_3d_2040pop_Base.res1d','Jan 3 2019 Storm'])
# res_list.append(['Jan 3 2019 Storm, 2050 Population','NSSA_WWF_2019-01-02_3d_2050pop_Base.res1d','Jan 3 2019 Storm'])
# res_list.append(['Nov 15 2021 Storm, 2020 Population','NSSA_WWF_2021-11-12_5d_2020pop_Base.res1d','Nov 15 2021 Storm'])
# res_list.append(['Nov 15 2021 Storm, 2030 Population','NSSA_WWF_2021-11-12_5d_2030pop_Base.res1d','Nov 15 2021 Storm'])
# res_list.append(['Nov 15 2021 Storm, 2040 Population','NSSA_WWF_2021-11-12_5d_2040pop_Base.res1d','Nov 15 2021 Storm'])
# res_list.append(['Nov 15 2021 Storm, 2050 Population','NSSA_WWF_2021-11-12_5d_2050pop_Base.res1d','Nov 15 2021 Storm'])
# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions,element_filter,name_shortenings,wwtp_pipe,outfall_summary,mus_path])
##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# #NSSA Sys As sealed vfd
# model_area = 'NSSA'
# groupby_acronym_owner = True
# pipe_ls_exclusions = []
# model = 'NSSA_Base_2020pop_Sealed_VFD.mdb'

# output_folder = r'J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\SYSTEM_ASSESSMENT\HTML_Plots_Bolted_VFD'
# result_folder = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\SYSTEM_ASSESSMENT\NSSA_SYSTEM_ASSESSMENT_ALL_BOLTED_VFD"
# element_filter = []
# res_list = []
# res_list.append(['Dry Weather Flow, 2020 Population','NSSA_DWF_2018-07-26_4d_2020pop_S_V_Base.res1d','Dry Weather Flow'])
# res_list.append(['Dry Weather Flow, 2030 Population','NSSA_DWF_2018-07-26_4d_2030pop_S_V_Base.res1d','Dry Weather Flow'])
# res_list.append(['Dry Weather Flow, 2040 Population','NSSA_DWF_2018-07-26_4d_2040pop_S_V_Base.res1d','Dry Weather Flow'])
# res_list.append(['Dry Weather Flow, 2050 Population','NSSA_DWF_2018-07-26_4d_2050pop_S_V_Base.res1d','Dry Weather Flow'])
# res_list.append(['Dry Weather Flow, 2060 Population','NSSA_DWF_2018-07-26_4d_2060pop_S_V_Base.res1d','Dry Weather Flow'])
# res_list.append(['Three Times ADWF, 2020 Population','NSSA_3ADWF_2020p_S_V_Base.res1d','Three Times ADWF'])
# res_list.append(['Three Times ADWF, 2030 Population','NSSA_3ADWF_2030p_S_V_Base.res1d','Three Times ADWF'])
# res_list.append(['Three Times ADWF, 2040 Population','NSSA_3ADWF_2040p_S_V_Base.res1d','Three Times ADWF'])
# res_list.append(['Three Times ADWF, 2050 Population','NSSA_3ADWF_2050p_S_V_Base.res1d','Three Times ADWF'])
# res_list.append(['Three Times ADWF, 2060 Population','NSSA_3ADWF_2060p_S_V_Base.res1d','Three Times ADWF'])
# res_list.append(['Basic Service Flow, 2020 Population','NSSA_BSF_11p2k_2020p_S_V_Base.res1d','Basic Service Flow'])
# res_list.append(['Basic Service Flow, 2030 Population','NSSA_BSF_11p2k_2030p_S_V_Base.res1d','Basic Service Flow'])
# res_list.append(['Basic Service Flow, 2040 Population','NSSA_BSF_11p2k_2040p_S_V_Base.res1d','Basic Service Flow'])
# res_list.append(['Basic Service Flow, 2050 Population','NSSA_BSF_11p2k_2050p_S_V_Base.res1d','Basic Service Flow'])
# res_list.append(['Basic Service Flow, 2060 Population','NSSA_BSF_11p2k_2060p_S_V_Base.res1d','Basic Service Flow'])

# res_list.append(['2yr-24hr NoCC, 2020 Population','NSSA_GA_EX-2y-24h-AES_2020p_S_V_Base.res1d','2yr-24hr Design Storm'])
# res_list.append(['2yr-24hr NoCC, 2030 Population','NSSA_GA_EX-2y-24h-AES_2030p_S_V_Base.res1d','2yr-24hr Design Storm'])
# res_list.append(['2yr-24hr 2050M, 2040 Population','NSSA_GA_2050M-2y-24h-AES_2040p_S_V_Base.res1d','2yr-24hr Design Storm'])
# res_list.append(['2yr-24hr 2050H, 2040 Population','NSSA_GA_2050H-2y-24h-AES_2040p_S_V_Base.res1d','2yr-24hr Design Storm'])
# res_list.append(['2yr-24hr 2050H, 2050 Population','NSSA_GA_2050H-2y-24h-AES_2050p_S_V_Base.res1d','2yr-24hr Design Storm'])
# res_list.append(['2yr-24hr 2050H, 2060 Population','NSSA_GA_2050H-2y-24h-AES_2060p_S_V_Base.res1d','2yr-24hr Design Storm'])

# res_list.append(['5yr-24hr NoCC, 2020 Population','NSSA_GA_EX-5y-24h-AES_2020p_S_V_Base.res1d','5yr-24hr Design Storm'])
# res_list.append(['5yr-24hr NoCC, 2030 Population','NSSA_GA_EX-5y-24h-AES_2030p_S_V_Base.res1d','5yr-24hr Design Storm'])
# res_list.append(['5yr-24hr 2050M, 2040 Population','NSSA_GA_2050M-5y-24h-AES_2040p_S_V_Base.res1d','5yr-24hr Design Storm'])
# res_list.append(['5yr-24hr 2050H, 2040 Population','NSSA_GA_2050H-5y-24h-AES_2040p_S_V_Base.res1d','5yr-24hr Design Storm'])
# res_list.append(['5yr-24hr 2050H, 2050 Population','NSSA_GA_2050H-5y-24h-AES_2050p_S_V_Base.res1d','5yr-24hr Design Storm'])
# res_list.append(['5yr-24hr 2050H, 2060 Population','NSSA_GA_2050H-5y-24h-AES_2060p_S_V_Base.res1d','5yr-24hr Design Storm'])

# res_list.append(['10yr-24hr NoCC, 2020 Population','NSSA_GA_EX-10y-24h-AES_2020p_S_V_Base.res1d','10yr-24hr Design Storm'])
# res_list.append(['10yr-24hr NoCC, 2030 Population','NSSA_GA_EX-10y-24h-AES_2030p_S_V_Base.res1d','10yr-24hr Design Storm'])
# res_list.append(['10yr-24hr 2050M, 2040 Population','NSSA_GA_2050M-10y-24h-AES_2040p_S_V_Base.res1d','10yr-24hr Design Storm'])
# res_list.append(['10yr-24hr 2050H, 2040 Population','NSSA_GA_2050H-10y-24h-AES_2040p_S_V_Base.res1d','10yr-24hr Design Storm'])
# res_list.append(['10yr-24hr 2050H, 2050 Population','NSSA_GA_2050H-10y-24h-AES_2050p_S_V_Base.res1d','10yr-24hr Design Storm'])
# res_list.append(['10yr-24hr 2050H, 2060 Population','NSSA_GA_2050H-10y-24h-AES_2060p_S_V_Base.res1d','10yr-24hr Design Storm'])

# res_list.append(['Jan 3 2019 Storm, 2020 Population','NSSA_WWF_2019-01-02_3d_2020pop_S_V_Base.res1d','Jan 3 2019 Storm'])
# res_list.append(['Jan 3 2019 Storm, 2030 Population','NSSA_WWF_2019-01-02_3d_2030pop_S_V_Base.res1d','Jan 3 2019 Storm'])
# res_list.append(['Jan 3 2019 Storm, 2040 Population','NSSA_WWF_2019-01-02_3d_2040pop_S_V_Base.res1d','Jan 3 2019 Storm'])
# res_list.append(['Jan 3 2019 Storm, 2050 Population','NSSA_WWF_2019-01-02_3d_2050pop_S_V_Base.res1d','Jan 3 2019 Storm'])
# res_list.append(['Jan 3 2019 Storm, 2060 Population','NSSA_WWF_2019-01-02_3d_2060pop_S_V_Base.res1d','Jan 3 2019 Storm'])
# res_list.append(['Nov 15 2021 Storm, 2020 Population','NSSA_WWF_2021-11-12_5d_2020pop_S_V_Base.res1d','Nov 15 2021 Storm'])
# res_list.append(['Nov 15 2021 Storm, 2030 Population','NSSA_WWF_2021-11-12_5d_2030pop_S_V_Base.res1d','Nov 15 2021 Storm'])
# res_list.append(['Nov 15 2021 Storm, 2040 Population','NSSA_WWF_2021-11-12_5d_2040pop_S_V_Base.res1d','Nov 15 2021 Storm'])
# res_list.append(['Nov 15 2021 Storm, 2050 Population','NSSA_WWF_2021-11-12_5d_2050pop_S_V_Base.res1d','Nov 15 2021 Storm'])
# res_list.append(['Nov 15 2021 Storm, 2060 Population','NSSA_WWF_2021-11-12_5d_2060pop_S_V_Base.res1d','Nov 15 2021 Storm'])
# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions,element_filter,name_shortenings,wwtp_pipe,outfall_summary,mus_path])



##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# model_area = 'NSSA'
# # joint_plot_header = 'Design Storm'
# pipe_ls_exclusions = []
# groupby_acronym_owner = True
# model = 'NSSA_Base_2060pop_V064_Seal_VFD.mdb'
# output_folder = r'J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\Requests\MV UAI Taban Sowlati MCR MacKay Outfall Lynn Siphon\HTML_Plots'
# result_folder = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\Requests\MV UAI Taban Sowlati MCR MacKay Outfall Lynn Siphon\MODEL"
# element_filter = []
# res_list = []
# # Parameters (result description shows up in the legend, result file name, result grouping only for result_lookup not for long sections)
# res_list.append(['5yr 24h 2050H, 2060pop','NSSA_WWF_2050H-5yr-24hr-AES_2060pop_S_V_Base.res1d','5yr 24h Design Storm'])
# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions,element_filter])

# #MIKE+ comparison
# model_area = 'FSA'
# groupby_acronym_owner = True
# pipe_ls_exclusions = ['55773','55778','55783','55788','55796','55799','55803']
# # joint_plot_header = 'Design Storms'
# model = 'FSA_Base_2020pop_V049.mdb'
# res_list = []

# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\MU_Classic_To_MIKE+_Sim_Compare\MIKEPLUS_2023_March_2023\Plots_Base'
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\MU_Classic_To_MIKE+_Sim_Compare\MIKEPLUS_2023_March_2023\Model"
# # res_list.append(['Classic','FSA_DWF_2021-07-22_3d_2020pop_Base.res1d','Dry Weather Flow, 2020pop'])
# # res_list.append(['MIKE+','FSA_DWF_2021-07-22_3d_2020pop_BaseResult_file_8.res1d','Dry Weather Flow, 2020pop'])
# res_list.append(['Classic','FSA_WWF_2021-11-12_5d_2020pop_Base.res1d','Nov 15 2021 Storm', '2020pop'])
# res_list.append(['MIKE+','FSA_WWF_2021-11-12_5d_2020pop_BaseResult_file_5.res1d','Nov 15 2021 Storm', '2020pop'])

# # output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\MU_Classic_To_MIKE+_Sim_Compare\MIKEPLUS_2023_March_2023\Plots_BurnabyLake'
# # result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\MU_Classic_To_MIKE+_Sim_Compare\MIKEPLUS_2023_March_2023\Model"
# # result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\MU_Classic_To_MIKE+_Sim_Compare\MIKEPLUS_2023_March_2023\Model"
# # res_list.append(['Classic','FSA_WWF_2100H-5yr-24hr-AES_2060pop_V_BurnabyLake.res1d','5yr 24h Design Storm, VFD, 2060pop'])
# # res_list.append(['MIKE+','FSA_WWF_2100H-5yr-24hr-AES_2060pop_V_BurnabyLakeResult_file_5','5yr 24h Design Storm, VFD, 2060pop'])

# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions,element_filter,name_shortenings,wwtp_pipe,outfall_summary,mus_path])


##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# model_area = 'FSA'
# groupby_acronym_owner = True
# pipe_ls_exclusions = ['55773','55778','55783','55788','55796','55799','55803']
# # joint_plot_header = 'Design Storms'
# model = 'FSA_Base_2020pop_V049.mdb'
# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\System_Assessment\HTML_Plots'
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\System_Assessment\FSA_System_Assessment"
# element_filter = []
# res_list = []
# res_list.append(['3 * ADWF, 2020pop','FSA_3ADWF_2020pop_Base.res1d','Three Times ADWF'])
# res_list.append(['3 * ADWF, 2030pop','FSA_3ADWF_2030pop_BurnabyLake.res1d','Three Times ADWF'])
# res_list.append(['3 * ADWF, 2040pop','FSA_3ADWF_2040pop_BurnabyLake.res1d','Three Times ADWF'])
# res_list.append(['3 * ADWF, 2050pop','FSA_3ADWF_2050pop_BurnabyLake.res1d','Three Times ADWF'])
# res_list.append(['3 * ADWF, 2060pop','FSA_3ADWF_2060pop_BurnabyLake.res1d','Three Times ADWF'])
# res_list.append(['DWF, 2020pop','FSA_DWF_2021-07-22_3d_2020pop_Base.res1d','Dry Weather Flow'])
# res_list.append(['DWF, 2030pop','FSA_DWF_2021-07-22_3d_2030pop_BurnabyLake.res1d','Dry Weather Flow'])
# res_list.append(['DWF, 2040pop','FSA_DWF_2021-07-22_3d_2040pop_BurnabyLake.res1d','Dry Weather Flow'])
# res_list.append(['DWF, 2050pop','FSA_DWF_2021-07-22_3d_2050pop_BurnabyLake.res1d','Dry Weather Flow'])
# res_list.append(['DWF, 2060pop','FSA_DWF_2021-07-22_3d_2060pop_BurnabyLake.res1d','Dry Weather Flow'])
# res_list.append(['Nov 15 2021, 2020pop','FSA_WWF_2021-11-12_5d_2020pop_Base.res1d','Nov 15 2021 Storm'])
# res_list.append(['Nov 15 2021, 2030pop','FSA_WWF_2021-11-12_5d_2030pop_BurnabyLake.res1d','Nov 15 2021 Storm'])
# res_list.append(['Nov 15 2021, 2040pop','FSA_WWF_2021-11-12_5d_2040pop_BurnabyLake.res1d','Nov 15 2021 Storm'])
# res_list.append(['Nov 15 2021, 2050pop','FSA_WWF_2021-11-12_5d_2050pop_BurnabyLake.res1d','Nov 15 2021 Storm'])
# res_list.append(['Nov 15 2021, 2060pop','FSA_WWF_2021-11-12_5d_2060pop_BurnabyLake.res1d','Nov 15 2021 Storm'])
# res_list.append(['2yr 24h NoCC , 2020pop','FSA_WWF_EX-2yr-24hr-AES_2020pop_Base.res1d','2yr 24h Design Storm'])
# res_list.append(['2yr 24h NoCC , 2030pop','FSA_WWF_EX-2yr-24hr-AES_2030pop_BurnabyLake.res1d','2yr 24h Design Storm'])
# res_list.append(['2yr 24h 2050H, 2040pop','FSA_WWF_2050H-2yr-24hr-AES_2040pop_BurnabyLake.res1d','2yr 24h Design Storm'])
# res_list.append(['2yr 24h 2050H, 2050pop','FSA_WWF_2050H-2yr-24hr-AES_2050pop_BurnabyLake.res1d','2yr 24h Design Storm'])
# res_list.append(['2yr 24h 2100H, 2060pop','FSA_WWF_2100H-2yr-24hr-AES_2060pop_BurnabyLake.res1d','2yr 24h Design Storm'])
# res_list.append(['5yr 24h NoCC, 2020pop','FSA_WWF_EX-5yr-24hr-AES_2020pop_Base.res1d','5yr 24h Design Storm'])
# res_list.append(['5yr 24h NoCC, 2030pop','FSA_WWF_EX-5yr-24hr-AES_2030pop_BurnabyLake.res1d','5yr 24h Design Storm'])
# res_list.append(['5yr 24h 2050H, 2040pop','FSA_WWF_2050H-5yr-24hr-AES_2040pop_BurnabyLake.res1d','5yr 24h Design Storm'])
# res_list.append(['5yr 24h 2050H, 2050pop','FSA_WWF_2050H-5yr-24hr-AES_2050pop_BurnabyLake.res1d','5yr 24h Design Storm'])
# res_list.append(['5yr 24h 2100H, 2060pop','FSA_WWF_2100H-5yr-24hr-AES_2060pop_BurnabyLake.res1d','5yr 24h Design Storm'])
# res_list.append(['10yr 24h NoCC, 2020pop','FSA_WWF_EX-10yr-24hr-AES_2020pop_Base.res1d','10yr 24h Design Storm'])
# res_list.append(['10yr 24h NoCC, 2030pop','FSA_WWF_EX-10yr-24hr-AES_2030pop_BurnabyLake.res1d','10yr 24h Design Storm'])
# res_list.append(['10yr 24h 2050H, 2040pop','FSA_WWF_2050H-10yr-24hr-AES_2040pop_BurnabyLake.res1d','10yr 24h Design Storm'])
# res_list.append(['10yr 24h 2050H, 2050pop','FSA_WWF_2050H-10yr-24hr-AES_2050pop_BurnabyLake.res1d','10yr 24h Design Storm'])
# res_list.append(['10yr 24h 2100H, 2060pop','FSA_WWF_2100H-10yr-24hr-AES_2060pop_BurnabyLake.res1d','10yr 24h Design Storm'])
# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions,element_filter,name_shortenings,wwtp_pipe,outfall_summary,mus_path])
##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# model_area = 'LISA'
# groupby_acronym_owner = False
# pipe_ls_exclusions = []
# joint_plot_header = 'Design Storms'
# model = 'Lisa_Base.sqlite'
# output_folder = r'J:\SEWER_AREA_MODELS\LISA\04_ANALYSIS_WORK\System_Assessment\Design Storms (2022 Population)\Plots'
# result_folder = r"J:\SEWER_AREA_MODELS\LISA\04_ANALYSIS_WORK\System_Assessment\Design Storms (2022 Population)\Results"
# res_list = []
# res_list.append(['2yr 24h No Climate Change','LISA_WWF_EX-2yr-24hr-SCS_2023_PopulationDefault_Network_HD.res1d','Design Storms'])
# res_list.append(['5yr 24h No Climate Change','LISA_WWF_EX-5yr-24hr-SCS_2023_PopulationDefault_Network_HD.res1d','Design Storms'])
# res_list.append(['10yr 24h No Climate Change','LISA_WWF_EX-10yr-24hr-SCS_2023_PopulationDefault_Network_HD.res1d','Design Storms'])
# res_list.append(['25yr 24h No Climate Change','LISA_WWF_EX-25yr-24hr-SCS_2023_PopulationDefault_Network_HD.res1d','Design Storms'])
# res_list.append(['50yr 24h No Climate Change','LISA_WWF_EX-50yr-24hr-SCS_2023_PopulationDefault_Network_HD.res1d','Design Storms'])
# res_list.append(['100yr 24h No Climate Change','LISA_WWF_EX-100yr-24hr-SCS_2023_PopulationDefault_Network_HD.res1d','Design Storms'])
# res_list.append(['200yr 24h No Climate Change','LISA_WWF_EX-200yr-24hr-SCS_2023_PopulationDefault_Network_HD.res1d','Design Storms'])
# res_list.append(['Dry Weather Flow','DWF_2023_PopulationNetwork_HD.res1d','Dry Weather Flow'])
# res_list.append(['Basic Service Flow','Lisa_BSF_11p2k_2023_Population.res1d','Basic Service Flow'])
# res_list.append(['Nov 15 2021 Event','LISA_WWF_Nov_15_2021_2023_PopulationDefault_Network_HD.res1d','Nov 15 2021 Event'])
# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions,element_filter,name_shortenings,wwtp_pipe,outfall_summary,mus_path])

##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# model_area = 'VSA'
# groupby_acronym_owner = False
# joint_plot_header = 'Design Storms'
# model = 'VSA_BASE_MODEL_2022pop.mdb'
# output_folder = r'\\prdsynfile01\LWS_Modelling\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\21. SYSTEM_ASSESSMENT\DWF_No_Tide\2022\Plots'
# result_folder = r"\\prdsynfile01\LWS_Modelling\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\21. SYSTEM_ASSESSMENT\DWF_No_Tide\2022\Model"
# res_list = []
# res_list.append(['Dry Weather Flow','VSA_DWF_2022pop_Base.res1d',0])
# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions,element_filter,name_shortenings,wwtp_pipe,outfall_summary,mus_path])
##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# model_area = 'NSSA'
# groupby_acronym_owner = True
# joint_plot_header = 'Design Storms'
# model = 'NSSA_Base_2018pop_V062.mdb'
# output_folder = r'J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_NSSA\Plots'
# result_folder = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_NSSA\Model"
# res_list = []
# res_list.append(['2yr 24h No Climate Change','NSSA_WWF_EX-2yr-24hr-AES_2018pop_Base.res1d',1])
# res_list.append(['5yr 24h No Climate Change','NSSA_WWF_EX-5yr-24hr-AES_2018pop_Base.res1d',1])
# res_list.append(['10yr 24h No Climate Change','NSSA_WWF_EX-10yr-24hr-AES_2018pop_Base.res1d',1])
# res_list.append(['Dry Weather Flow','NSSA_DWF_2018-07-26_4d_2018pop_Base.res1d',0])
# res_list.append(['Nov 25 2018 Event','NSSA_WWF_2018-11-25_3d_2018pop_Base.res1d',0])
# res_list.append(['Jan 31 2020 Event','NSSA_WWF_2020-01-29_6d_2018pop_Base.res1d',0])
# res_list.append(['Nov 15 2021 Event','NSSA_WWF_2021-11-12_5d_2018pop_Base.res1d',0])
# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions,element_filter,name_shortenings,wwtp_pipe,outfall_summary,mus_path])
##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# model_area = 'NSSA' # For X ADWF
# model = 'NSSA_Base_With_shapelength_orifice_acronym.sqlite'
# groupby_acronym_owner = False

# wwtp_pipe = '54959_a'
# groupby_acronym_owner = True

# outfall_summary = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\X-BSF\HTML_Plots_V79\Maps_And_CSS\Outfall_Summary_No_Recapture.csv"

# output_folder = r'J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\X-BSF\HTML_Plots_V79_Sealed_VFD'
# result_folder = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\X-BSF\Model_V79_Sealed_VFD"
# res_list = []
# res_list.append(['1 I/I, 2030 Pop','NSSA_BSF_11p2k_2030pop_S_V_BaseDefault_Network_HD.res1d','1 * I/I'])
# res_list.append(['1 I/I, 2040 Pop','NSSA_BSF_11p2k_2040pop_S_V_BaseDefault_Network_HD.res1d','1 * I/I'])
# res_list.append(['1 I/I, 2050 Pop','NSSA_BSF_11p2k_2050pop_S_V_BaseDefault_Network_HD.res1d','1 * I/I'])
# res_list.append(['1 I/I, 2060 Pop','NSSA_BSF_11p2k_2060pop_S_V_BaseDefault_Network_HD.res1d','1 * I/I'])
# res_list.append(['1.2 I/I, 2030 Pop','NSSA_BSF_13p44k_2030pop_S_V_BaseDefault_Network_HD.res1d','1.2 * I/I'])
# res_list.append(['1.2 I/I, 2040 Pop','NSSA_BSF_13p44k_2040pop_S_V_BaseDefault_Network_HD.res1d','1.2 * I/I'])
# res_list.append(['1.2 I/I, 2050 Pop','NSSA_BSF_13p44k_2050pop_S_V_BaseDefault_Network_HD.res1d','1.2 * I/I'])
# res_list.append(['1.2 I/I, 2060 Pop','NSSA_BSF_13p44k_2060pop_S_V_BaseDefault_Network_HD.res1d','1.2 * I/I'])
# res_list.append(['1.5 I/I, 2030 Pop','NSSA_BSF_16p8k_2030pop_S_V_BaseDefault_Network_HD.res1d','1.5 * I/I'])
# res_list.append(['1.5 I/I, 2040 Pop','NSSA_BSF_16p8k_2040pop_S_V_BaseDefault_Network_HD.res1d','1.5 * I/I'])
# res_list.append(['1.5 I/I, 2050 Pop','NSSA_BSF_16p8k_2050pop_S_V_BaseDefault_Network_HD.res1d','1.5 * I/I'])
# res_list.append(['1.5 I/I, 2060 Pop','NSSA_BSF_16p8k_2060pop_S_V_BaseDefault_Network_HD.res1d','1.5 * I/I'])
# res_list.append(['2 I/I, 2030 Pop','NSSA_BSF_22p4k_2030pop_S_V_BaseDefault_Network_HD.res1d','2 * I/I'])
# res_list.append(['2 I/I, 2040 Pop','NSSA_BSF_22p4k_2040pop_S_V_BaseDefault_Network_HD.res1d','2 * I/I'])
# res_list.append(['2 I/I, 2050 Pop','NSSA_BSF_22p4k_2050pop_S_V_BaseDefault_Network_HD.res1d','2 * I/I'])
# res_list.append(['2 I/I, 2060 Pop','NSSA_BSF_22p4k_2060pop_S_V_BaseDefault_Network_HD.res1d','2 * I/I'])
# res_list.append(['2.5 I/I, 2030 Pop','NSSA_BSF_28k_2030pop_S_V_BaseDefault_Network_HD.res1d','2.5 * I/I'])
# res_list.append(['2.5 I/I, 2040 Pop','NSSA_BSF_28k_2040pop_S_V_BaseDefault_Network_HD.res1d','2.5 * I/I'])
# res_list.append(['2.5 I/I, 2050 Pop','NSSA_BSF_28k_2050pop_S_V_BaseDefault_Network_HD.res1d','2.5 * I/I'])
# res_list.append(['2.5 I/I, 2060 Pop','NSSA_BSF_28k_2060pop_S_V_BaseDefault_Network_HD.res1d','2.5 * I/I'])

# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions,element_filter,name_shortenings,wwtp_pipe,outfall_summary,mus_path])
##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
