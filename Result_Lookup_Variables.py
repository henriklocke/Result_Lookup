##AFTER UPDATE AND SAVE YOU MUST RESTART THE KERNEL IN JUPYTER NOTEBOOK TO UPDATE VARIABLES!

##Remember to insert r in front of all paths, e.g. r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Calibration_2022\MODEL"

#PERMANENT CELL 2

master_list = []

##FSA BSF
model_area = 'FSA'
groupby_acronym_owner = True
pipe_ls_exclusions = ['55773','55778','55783','55788','55796','55799','55803']
model = 'FSA_Base_2030pop_V061_BurnabyLake.mdb'
output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\HTML_Plots'
result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\Model"
res_list = []
res_list.append(['1 * BSF, 2020 pop','FSA_BSF_11p2k_2020pop_Base.res1d','BSF'])
res_list.append(['2 * BSF, 2020 pop','FSA_BSF_22p4k_2020pop_Base.res1d','BSF'])
res_list.append(['3 * BSF, 2020 pop','FSA_BSF_33p6k_2020pop_Base.res1d','BSF'])
res_list.append(['4 * BSF, 2020 pop','FSA_BSF_44p8k_2020pop_Base.res1d','BSF'])

res_list.append(['1 * BSF, 2030 pop','FSA_BSF_11p2k_2030pop_2030_Network.res1d','BSF'])
res_list.append(['2 * BSF, 2030 pop','FSA_BSF_22p4k_2030pop_2030_Network.res1d','BSF'])
res_list.append(['3 * BSF, 2030 pop','FSA_BSF_33p6k_2030pop_2030_Network.res1d','BSF'])
res_list.append(['4 * BSF, 2030 pop','FSA_BSF_44p8k_2030pop_2030_Network.res1d','BSF'])

res_list.append(['1 * BSF, 2040 pop','FSA_BSF_11p2k_2040pop_2030_Network.res1d','BSF'])
res_list.append(['2 * BSF, 2040 pop','FSA_BSF_22p4k_2040pop_2030_Network.res1d','BSF'])
res_list.append(['3 * BSF, 2040 pop','FSA_BSF_33p6k_2040pop_2030_Network.res1d','BSF'])
res_list.append(['4 * BSF, 2040 pop','FSA_BSF_44p8k_2040pop_2030_Network.res1d','BSF'])

master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions])

# #NSSA Sys As not sealed not vfd
# model_area = 'NSSA'
# groupby_acronym_owner = True
# pipe_ls_exclusions = []
# model = 'NSSA_Base_2020pop.mdb'

# output_folder = r'J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\SYSTEM_ASSESSMENT\HTML_Plots'
# result_folder = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\SYSTEM_ASSESSMENT\NSSA_SYSTEM_ASSESSMENT"

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
# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions])

# #NSSA Sys As sealed vfd
# model_area = 'NSSA'
# groupby_acronym_owner = True
# pipe_ls_exclusions = []
# model = 'NSSA_Base_2020pop_Sealed_VFD.mdb'

# output_folder = r'J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\SYSTEM_ASSESSMENT\HTML_Plots_Bolted_VFD'
# result_folder = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\SYSTEM_ASSESSMENT\NSSA_SYSTEM_ASSESSMENT_ALL_BOLTED_VFD"

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
# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions])

# #MIKE+ comparison
# model_area = 'NSSA'
# groupby_acronym_owner = True
# pipe_ls_exclusions = []
# model = 'NSSA_Base.mdb'
# res_list = []

# output_folder = r'J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\MIKE_PLUS_TEST_2023p1_HL\Model\HTML_Plots'
# result_folder = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\MIKE_PLUS_TEST_2023p1_HL\Model\NSSA_Base_m1d - Result Files"

# res_list.append(['DWF, Classic','NSSA_DWF_2018-07-26_4d_2018pop_Base_Classic.res1d','Dry Weather Flow'])
# res_list.append(['DWF, MIKE+','NSSA_DWF_2018-07-26_4d_2018pop_BaseDefault_Network_HD.res1d','Dry Weather Flow'])

# res_list.append(['Nov 15 21, Classic','NSSA_WWF_2021-11-12_5d_2018pop_Base_Classic.res1d','Nov 15 2021 Storm'])
# res_list.append(['Nov 15 21, M+','NSSA_WWF_2021-11-12_5d_2018pop_BaseDefault_Network_HD.res1d','Nov 15 2021 Storm'])
# res_list.append(['Nov 15 21, M+, Hotstart RDI','NSSA_WWF_2021-11-12_5d_2018pop_RDIHot_BaseDefault_Network_HD.res1d','Nov 15 2021 Storm'])

# res_list.append(['10yr 24h, Classic','NSSA_WWF_EX-10yr-24hr-AES_2018pop_Base_Classic.res1d','10yr 24h Design Storm'])
# res_list.append(['10yr 24h, MIKE+','NSSA_ZO_EX-10y-24h-AES_2018p_BaseDefault_Network_HD.res1d','10yr 24h Design Storm'])

# res_list.append(['5yr 24h, Classic','NSSA_WWF_EX-5yr-24hr-AES_2018pop_Base_Classic.res1d','5yr 24h Design Storm'])
# res_list.append(['5yr 24h, MIKE+','NSSA_ZO_EX-5y-24h-AES_2018p_BaseDefault_Network_HD.res1d','5yr 24h Design Storm'])

# res_list.append(['2yr 24h, Classic','NSSA_WWF_EX-2yr-24hr-AES_2018pop_Base_Classic.res1d','2yr 24h Design Storm'])
# res_list.append(['2yr 24h, MIKE+','NSSA_ZO_EX-2y-24h-AES_2018p_BaseDefault_Network_HD.res1d','2yr 24h Design Storm'])

# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions])


# model_area = 'FSA'
# groupby_acronym_owner = True
# pipe_ls_exclusions = ['55773','55778','55783','55788','55796','55799','55803']
# model = 'FSA_Base_V059_2020pop.mdb'
# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_FSA\HTML_Plots'
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_FSA\Model"
# res_list = []
# res_list.append(['2yr 24h No Climate Change','FSA_GA_EX-2y-24h-AES_2020p_Base.res1d','Design Storms'])
# res_list.append(['5yr 24h No Climate Change','FSA_GA_EX-5y-24h-AES_2020p_Base.res1d','Design Storms'])
# res_list.append(['10yr 24h No Climate Change','FSA_GA_EX-10y-24h-AES_2020p_Base.res1d','Design Storms'])
# res_list.append(['Dry Weather Flow','FSA_DWF_2021-07-22_3d_2020pop_Base.res1d','Dry Weather Flow'])
# res_list.append(['Jan 31 2020 Event','FSA_WWF_2020-01-29_6d_2020pop_Base.res1d','Jan 31 2020 Event'])
# res_list.append(['Nov 15 2021 Event','FSA_WWF_2021-11-12_5d_2020pop_Base.res1d','Nov 15 2021 Event'])
# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions])


# model_area = 'FSA'
# groupby_acronym_owner = True
# pipe_ls_exclusions = ['55773','55778','55783','55788','55796','55799','55803']
# # joint_plot_header = 'Design Storms'
# model = 'FSA_Base_2060pop_V050_BurnabyLake_VFD_Sealed.mdb'
# output_folder = r'\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\System_Assessment_Special_Runs\HTML_Plots\Sealed_VFD_Version50'
# result_folder = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\System_Assessment_Special_Runs\Sealed_VFD_Version50"
# res_list = []

# res_list.append(['Jan 31 2020, 2020pop','FSA_WWF_2020-01-29_6d_2020pop_V_S_Base.res1d','Jan 31 2020 Storm'])
# # res_list.append(['Jan 31 2020, 2030pop','FSA_WWF_2020-01-29_6d_2030pop_V_S_BurnabyLake.res1d','Jan 31 2020 Storm'])
# # res_list.append(['Jan 31 2020, 2060pop','FSA_WWF_2020-01-29_6d_2060pop_V_S_BurnabyLake.res1d','Jan 31 2020 Storm'])
# # res_list.append(['Nov 15 2021, 2020pop','FSA_WWF_2021-11-12_5d_2020pop_V_S_Base.res1d','Nov 15 2021 Storm'])
# # res_list.append(['Nov 15 2021, 2030pop','FSA_WWF_2021-11-12_5d_2030pop_V_S_BurnabyLake.res1d','Nov 15 2021 Storm'])
# # res_list.append(['Nov 15 2021, 2060pop','FSA_WWF_2021-11-12_5d_2060pop_V_S_BurnabyLake.res1d','Nov 15 2021 Storm'])
# # res_list.append(['2yr 24h NoCC, 2020pop','FSA_WWF_EX-2yr-24hr-AES_2020pop_V_S_Base.res1d','2yr 24h Design Storm'])
# # res_list.append(['2yr 24h NoCC, 2030pop','FSA_WWF_EX-2yr-24hr-AES_2030pop_V_S_BurnabyLake.res1d','2yr 24h Design Storm'])
# # res_list.append(['2yr 24h 2050H, 2060pop','FSA_WWF_2050H-2yr-24hr-AES_2060pop_V_S_BurnabyLake.res1d','2yr 24h Design Storm'])
# # res_list.append(['2yr 24h 2100H, 2060pop','FSA_WWF_2100H-2yr-24hr-AES_2060pop_V_S_BurnabyLake.res1d','2yr 24h Design Storm'])
# # res_list.append(['5yr 24h NoCC, 2020pop','FSA_WWF_EX-5yr-24hr-AES_2020pop_V_S_Base.res1d','5yr 24h Design Storm'])
# # res_list.append(['5yr 24h NoCC, 2030pop','FSA_WWF_EX-5yr-24hr-AES_2030pop_V_S_BurnabyLake.res1d','5yr 24h Design Storm'])
# # res_list.append(['5yr 24h 2050H, 2060pop','FSA_WWF_2050H-5yr-24hr-AES_2060pop_V_S_BurnabyLake.res1d','5yr 24h Design Storm'])
# # res_list.append(['5yr 24h 2100H, 2060pop','FSA_WWF_2100H-5yr-24hr-AES_2060pop_V_S_BurnabyLake.res1d','5yr 24h Design Storm'])
# # res_list.append(['10yr 24h NoCC, 2020pop','FSA_WWF_EX-10yr-24hr-AES_2020pop_V_S_Base.res1d','10yr 24h Design Storm'])
# # res_list.append(['10yr 24h NoCC, 2030pop','FSA_WWF_EX-10yr-24hr-AES_2030pop_V_S_BurnabyLake.res1d','10yr 24h Design Storm'])
# # res_list.append(['10yr 24h 2050H, 2060pop','FSA_WWF_2050H-10yr-24hr-AES_2060pop_V_S_BurnabyLake.res1d','10yr 24h Design Storm'])
# # res_list.append(['10yr 24h 2100H, 2060pop','FSA_WWF_2100H-10yr-24hr-AES_2060pop_V_S_BurnabyLake.res1d','10yr 24h Design Storm'])
# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions])

# model_area = 'NSSA'
# # joint_plot_header = 'Design Storm'
# pipe_ls_exclusions = []
# groupby_acronym_owner = True
# model = 'NSSA_Base_2060pop_V064_Seal_VFD.mdb'
# output_folder = r'J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\Requests\MV UAI Taban Sowlati MCR MacKay Outfall Lynn Siphon\HTML_Plots'
# result_folder = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\Requests\MV UAI Taban Sowlati MCR MacKay Outfall Lynn Siphon\MODEL"
# res_list = []
# # Parameters (result description shows up in the legend, result file name, result grouping only for result_lookup not for long sections)
# res_list.append(['5yr 24h 2050H, 2060pop','NSSA_WWF_2050H-5yr-24hr-AES_2060pop_S_V_Base.res1d','5yr 24h Design Storm'])
# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions])

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

# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner])

# model_area = 'FSA'
# groupby_acronym_owner = True
# pipe_ls_exclusions = ['55773','55778','55783','55788','55796','55799','55803']
# # joint_plot_header = 'Design Storms'
# model = 'FSA_Base_2020pop_V049.mdb'
# output_folder = r'\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Hyetograph_Trial\Plots'
# result_folder = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Hyetograph_Trial\Model"
# res_list = []

# res_list.append(['NoCC, 2030pop, Standard','FSA_WWF_EX-5yr-24hr-AES_2030pop_BurnabyLake.res1d','5yr 24h Design Storm'])
# res_list.append(['NoCC, 2030pop, Trial','FSA_WWF_Gauges-5yr-24hr-AES_2030pop_BurnabyLake.res1d','5yr 24h Design Storm'])
# res_list.append(['2050H, 2060pop, Standard','FSA_WWF_2050H-5yr-24hr-AES_2060pop_BurnabyLake.res1d','5yr 24h Design Storm'])
# res_list.append(['2050H, 2060pop, Trial','FSA_Gauges-2050H-5yr-24hr-AES_2060p_BurnabyLake.res1d','5yr 24h Design Storm'])
# res_list.append(['2050H, 2060pop, VFD, Standard','FSA_WWF_2050H-5yr-24hr-AES_2060pop_V_BurnabyLake.res1d','5yr 24h Design Storm'])
# res_list.append(['2050H, 2060pop, VFD, Trial','FSA_Gauges_2050H-5yr-24hr-AES_2060p_V_BurnabyLake.res1d','5yr 24h Design Storm'])
# res_list.append(['2100H, 2060pop, Standard','FSA_WWF_2100H-5yr-24hr-AES_2060pop_BurnabyLake.res1d','5yr 24h Design Storm'])
# res_list.append(['2100H, 2060pop, Trial','FSA_Gauges-2100H-5yr-24hr-AES_2060p_BurnabyLake.res1d','5yr 24h Design Storm'])
# res_list.append(['2100H, 2060pop, VFD, Standard','FSA_WWF_2100H-5yr-24hr-AES_2060pop_V_BurnabyLake.res1d','5yr 24h Design Storm'])
# res_list.append(['2100H, 2060pop, VFD, Trial','FSA_Gauges_2100H-5yr-24hr-AES_2060p_V_BurnabyLake.res1d','5yr 24h Design Storm'])
# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner])

# model_area = 'FSA'
# groupby_acronym_owner = True
# pipe_ls_exclusions = ['55773','55778','55783','55788','55796','55799','55803']
# # joint_plot_header = 'Design Storms'
# model = 'FSA_Base_2020pop_V049.mdb'
# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\System_Assessment\HTML_Plots_VFD'
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\System_Assessment\FSA_System_Assessment"
# res_list = []
# res_list.append(['2050H CC, 2060pop, VFD','FSA_WWF_2050H-5yr-24hr-AES_2060pop_V_BurnabyLake.res1d','5yr 24h Design Storm, VFD'])
# res_list.append(['2100H CC, 2060pop, VFD','FSA_WWF_2100H-5yr-24hr-AES_2060pop_V_BurnabyLake.res1d','5yr 24h Design Storm, VFD'])
# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions])

# model_area = 'FSA'
# groupby_acronym_owner = True
# pipe_ls_exclusions = ['55773','55778','55783','55788','55796','55799','55803']
# # joint_plot_header = 'Design Storms'
# model = 'FSA_Base_2020pop_V049.mdb'
# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\System_Assessment\HTML_Plots'
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\System_Assessment\FSA_System_Assessment"
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
# # master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions])

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
# master_list.append([model_area,model,result_folder,output_folder,res_list,groupby_acronym_owner,pipe_ls_exclusions])



# model_area = 'VSA'
# groupby_acronym_owner = False
# joint_plot_header = 'Design Storms'
# model = 'VSA_BASE_MODEL_2022pop.mdb'
# output_folder = r'\\prdsynfile01\LWS_Modelling\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\21. SYSTEM_ASSESSMENT\DWF_No_Tide\2022\Plots'
# result_folder = r"\\prdsynfile01\LWS_Modelling\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\21. SYSTEM_ASSESSMENT\DWF_No_Tide\2022\Model"
# res_list = []
# res_list.append(['Dry Weather Flow','VSA_DWF_2022pop_Base.res1d',0])
# master_list.append([model_area,model,result_folder,output_folder,res_list,joint_plot_header,groupby_acronym_owner])

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
# master_list.append([model_area,model,result_folder,output_folder,res_list,joint_plot_header,groupby_acronym_owner,pipe_ls_exclusions])

# model_area = 'NSSA' # For X ADWF
# model = 'NSSA_Base_2018pop_V062_3xADWF.mdb'
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
# master_list.append([model_area,model,result_folder,output_folder,res_list,joint_plot_header,groupby_acronym_owner,pipe_ls_exclusions])

# model_area = 'NSSA' # For X ADWF
# model = 'NSSA_Base_2018pop_V062_3xADWF.mdb'
# groupby_acronym_owner = False
# joint_plot_header = 'DWF and X times ADWF, VFD'
# output_folder = r'J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\X-ADWF\Plots_VFD'
# result_folder = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\X-ADWF\Model"
# res_list = []
# res_list.append(['Dry Weather Flow','NSSA_DWF_2018-07-26_4d_2018pop_V_Base.res1d',1])
# res_list.append(['3 times ADWF','NSSA_3ADWF_2018pop_V_Base.res1d',1])
# res_list.append(['3.5 times ADWF','NSSA_3p5ADWF_2018pop_V_Base.res1d',1])
# res_list.append(['4 times ADWF','NSSA_4ADWF_2018pop_V_Base.res1d',1])
# res_list.append(['5 times ADWF','NSSA_5ADWF_2018pop_V_Base.res1d',1])
# master_list.append([model_area,model,result_folder,output_folder,res_list,joint_plot_header,groupby_acronym_owner,pipe_ls_exclusions])