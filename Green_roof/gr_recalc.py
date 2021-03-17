
import pandas as pd
import numpy as np

def gr_recalc(scenario, df_base, df_gr, base_weight, gr_weight):

    def gr_calc(b_var,gr_var,b_weight, gr_weight):
        out = np.average([b_var,gr_var], weights=[b_weight,gr_weight])
        return out

    df_base_init = df_base
    base_soildepth = df_base_init.soildepth[1]
    base_sathydr = df_base_init.sathydraulicconduct[1]
    base_albedo = df_base_init.alb[1] # building Albedo
    base_emissivity = df_base_init.emis[1] # building Emissivity
    base_dr1 = df_base_init.storedrainprm.iloc[15] # drainage coeff_1
    base_dr2 = df_base_init.storedrainprm.iloc[22] # drainage coeff_2
    base_st_min = df_base_init.storedrainprm.iloc[1] # Storage Min
    base_st_min2 = df_base_init.storedrainprm.iloc[36] # Storage min 2
    base_st_max = df_base_init.storedrainprm.iloc[29] # Storage Max

    # Green roof from NonVeg
    df_gr_init = df_gr
    gr_soildepth = df_gr_init.soildepth[1]
    gr_sathydr = df_gr_init.sathydraulicconduct[1]
    gr_albedo = df_gr_init.alb[1] # building Albedo
    gr_emissivity = df_gr_init.emis[1] # building Emissivity
    gr_dr1 = df_gr_init.storedrainprm.iloc[15] # drainage coeff_1
    gr_dr2 = df_gr_init.storedrainprm.iloc[22] # drainage coeff_2
    gr_st_min = df_gr_init.storedrainprm.iloc[1] # Storage Min
    gr_st_min2 = df_gr_init.storedrainprm.iloc[35] # Storage Min2
    gr_st_max = df_gr_init.storedrainprm.iloc[29] # Storage Max


    base_list = [base_soildepth,base_sathydr,base_albedo,base_emissivity,base_dr1,base_dr2,base_st_min,base_st_min2,base_st_max]
    gr_list = [gr_soildepth,gr_sathydr,gr_albedo,gr_emissivity,gr_dr1,gr_dr2,gr_st_min,gr_st_min2,gr_st_max]

    scenario.soildepth[1]             = gr_calc(base_list[0],gr_list[0], base_weight, gr_weight)
    scenario.sathydraulicconduct[1]   = gr_calc(base_list[1],gr_list[1], base_weight, gr_weight)
    scenario.alb[1]                   = gr_calc(base_list[2],gr_list[2], base_weight, gr_weight) # building Albedo
    scenario.emis[1]                  = gr_calc(base_list[3],gr_list[3], base_weight, gr_weight)# building Emissivity
    scenario.storedrainprm.iloc[15]   = gr_calc(base_list[4],gr_list[4], base_weight, gr_weight) # drainage coeff_1
    scenario.storedrainprm.iloc[22]   = gr_calc(base_list[5],gr_list[5], base_weight, gr_weight)# drainage coeff_2
    scenario.storedrainprm.iloc[1]    = gr_calc(base_list[6],gr_list[6], base_weight, gr_weight) # Storage Min
    scenario.storedrainprm.iloc[35]   = gr_calc(base_list[7],gr_list[7], base_weight, gr_weight) # Storage Min2
    scenario.storedrainprm.iloc[29]   = gr_calc(base_list[8],gr_list[8], base_weight, gr_weight) # Storage Max

    return scenario