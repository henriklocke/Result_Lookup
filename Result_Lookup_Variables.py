##AFTER UPDATE AND SAVE YOU MUST RESTART THE KERNEL IN JUPYTER NOTEBOOK TO UPDATE VARIABLES!

##Remember to insert r in front of all paths, e.g. r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Calibration_2022\MODEL"

#PERMANENT CELL 2

master_list = []

# model_area = 'LISA'
# groupby_acronym_owner = False
# joint_plot_header = 'Design Storms'
# model = 'Lisa_Base.sqlite'
# output_folder = r'J:\SEWER_AREA_MODELS\LISA\04_ANALYSIS_WORK\System_Assessment\Design Storms (2022 Population)\Plots'
# result_folder = r"J:\SEWER_AREA_MODELS\LISA\04_ANALYSIS_WORK\System_Assessment\Design Storms (2022 Population)\Results"
# res_list = []
# res_list.append(['2yr 24h No Climate Change','LISA_WWF_EX-2yr-24hr-SCS_2023_PopulationDefault_Network_HD.res1d',1])
# res_list.append(['5yr 24h No Climate Change','LISA_WWF_EX-5yr-24hr-SCS_2023_PopulationDefault_Network_HD.res1d',1])
# res_list.append(['10yr 24h No Climate Change','LISA_WWF_EX-10yr-24hr-SCS_2023_PopulationDefault_Network_HD.res1d',1])
# res_list.append(['25yr 24h No Climate Change','LISA_WWF_EX-25yr-24hr-SCS_2023_PopulationDefault_Network_HD.res1d',1])
# res_list.append(['50yr 24h No Climate Change','LISA_WWF_EX-50yr-24hr-SCS_2023_PopulationDefault_Network_HD.res1d',1])
# res_list.append(['100yr 24h No Climate Change','LISA_WWF_EX-100yr-24hr-SCS_2023_PopulationDefault_Network_HD.res1d',1])
# res_list.append(['200yr 24h No Climate Change','LISA_WWF_EX-200yr-24hr-SCS_2023_PopulationDefault_Network_HD.res1d',1])
# res_list.append(['Dry Weather Flow','DWF_2023_PopulationNetwork_HD.res1d',0])
# res_list.append(['Basic Service Flow','Lisa_BSF_11p2k_2023_Population.res1d',0])
# res_list.append(['Nov 15 2021 Event','LISA_WWF_Nov_15_2021_2023_PopulationDefault_Network_HD.res1d',0])
# master_list.append([model_area,model,result_folder,output_folder,res_list,joint_plot_header,groupby_acronym_owner])


# model_area = 'FSA'
# groupby_acronym_owner = True
# joint_plot_header = 'Design Storms'
# model = 'FSA_Base_2020pop_V049.mdb'
# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Allways_Latest_Master_Model_Simulations\Plots'
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Allways_Latest_Master_Model_Simulations\Model"
# res_list = []
# res_list.append(['2yr 24h No Climate Change','FSA_WWF_EX-2yr-24hr-AES_2020pop_Base.res1d',1])
# res_list.append(['5yr 24h No Climate Change','FSA_WWF_EX-5yr-24hr-AES_2020pop_Base.res1d',1])
# res_list.append(['10yr 24h No Climate Change','FSA_WWF_EX-10yr-24hr-AES_2020pop_Base.res1d',1])
# res_list.append(['Dry Weather Flow','FSA_DWF_2021-07-23_4d_2020pop_Base.res1d',0])
# res_list.append(['Jan 31 2020 Event','FSA_WWF_2020-01-29_6d_2020pop_Base.res1d',0])
# res_list.append(['Nov 15 2021 Event','FSA_WWF_2021-11-12_5d_2020pop_Base.res1d',0])
# master_list.append([model_area,model,result_folder,output_folder,res_list,joint_plot_header,groupby_acronym_owner])


# model_area = 'VSA'
# groupby_acronym_owner = False
# joint_plot_header = 'Design Storms'
# model = 'VSA_BASE_MODEL_2022pop.mdb'
# output_folder = r'\\prdsynfile01\LWS_Modelling\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\21. SYSTEM_ASSESSMENT\DWF_No_Tide\2022\Plots'
# result_folder = r"\\prdsynfile01\LWS_Modelling\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\21. SYSTEM_ASSESSMENT\DWF_No_Tide\2022\Model"
# res_list = []
# res_list.append(['Dry Weather Flow','VSA_DWF_2022pop_Base.res1d',0])
# master_list.append([model_area,model,result_folder,output_folder,res_list,joint_plot_header,groupby_acronym_owner])

model_area = 'NSSA'
groupby_acronym_owner = False
joint_plot_header = 'Design Storms'
model = 'NSSA_Base_2018pop_V062.mdb'
output_folder = r'J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_NSSA\Plots'
result_folder = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_NSSA\Model"
res_list = []
res_list.append(['2yr 24h No Climate Change','NSSA_WWF_EX-2yr-24hr-AES_2018pop_Base.res1d',1])
res_list.append(['5yr 24h No Climate Change','NSSA_WWF_EX-5yr-24hr-AES_2018pop_Base.res1d',1])
res_list.append(['10yr 24h No Climate Change','NSSA_WWF_EX-10yr-24hr-AES_2018pop_Base.res1d',1])
res_list.append(['Dry Weather Flow','NSSA_DWF_2018-07-26_4d_2018pop_Base.res1d',0])
res_list.append(['Nov 25 2018 Event','NSSA_WWF_2018-11-25_3d_2018pop_Base.res1d',0])
res_list.append(['Jan 31 2020 Event','NSSA_WWF_2020-01-29_6d_2018pop_Base.res1d',0])
res_list.append(['Nov 15 2021 Event','NSSA_WWF_2021-11-12_5d_2018pop_Base.res1d',0])
master_list.append([model_area,model,result_folder,output_folder,res_list,joint_plot_header,groupby_acronym_owner])

# model_area = 'NSSA' # For X ADWF
# model = 'NSSA_Base.mdb'
# groupby_acronym_owner = False
# joint_plot_header = 'DWF and X times ADWF'
# output_folder = r'J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\X-ADWF\Plots_No_VFD'
# result_folder = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\X-ADWF\Model"
# res_list = []
# res_list.append(['Dry Weather Flow','NSSA_DWF_2018-07-26_4d_2018pop_Base.res1d',1])
# res_list.append(['3 times ADWF','NSSA_3ADWF_2018pop_Base.res1d',1])
# res_list.append(['3.5 times ADWF','NSSA_3p5ADWF_2018pop_Base.res1d',1])
# res_list.append(['4 times ADWF','NSSA_4ADWF_2018pop_Base.res1d',1])
# res_list.append(['5 times ADWF','NSSA_5ADWF_2018pop_Base.res1d',1])
# master_list.append([model_area,model,result_folder,output_folder,res_list,joint_plot_header,groupby_acronym_owner])

# model_area = 'NSSA' # For X ADWF
# model = 'NSSA_Base.mdb'
# groupby_acronym_owner = False
# joint_plot_header = 'DWF and X times ADWF, VFD'
# output_folder = r'J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\X-ADWF\Plots_VFD'
# result_folder = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\X-ADWF\Model"
# res_list = []
# res_list.append(['Dry Weather Flow','NSSA_DWF_2018-07-26_4d_2018pop_VFD_Base.res1d',1])
# res_list.append(['3 times ADWF','NSSA_3ADWF_2018pop_VFD_Base.res1d',1])
# res_list.append(['3.5 times ADWF','NSSA_3p5ADWF_2018pop_VFD_Base.res1d',1])
# res_list.append(['4 times ADWF','NSSA_4ADWF_2018pop_VFD_Base.res1d',1])
# res_list.append(['5 times ADWF','NSSA_5ADWF_2018pop_VFD_Base.res1d',1])
# master_list.append([model_area,model,result_folder,output_folder,res_list,joint_plot_header,groupby_acronym_owner])