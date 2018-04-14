from django.http import JsonResponse
from datetime import datetime
import pandas as pd
import os
from .app import swat as app


app_workspace = app.get_app_workspace()
monthly_rch_path = os.path.join(app_workspace.path, 'Output Data', 'output_monthly.rch')
daily_rch_path = os.path.join(app_workspace.path, 'Output Data', 'output_daily.rch')


def extract_rch(start_date, end_date, var, reachid):
    dir = '/Users/Student/Documents/NASA-Goddard/SWAT/Example Data'
    f = open(monthly_rch_path)

    header1 = f.readline()
    header2 = f.readline()
    header3 = f.readline()
    header4 = f.readline()
    header5 = f.readline()
    header6 = f.readline()
    header7 = f.readline()
    header8 = f.readline()
    header9 = f.readline()

    dt_start = datetime.strptime(start_date, '%B %Y')
    dt_end = datetime.strptime(end_date, '%B %Y')

    year_start = dt_start.year
    month_start = dt_start.month
    year_end = dt_end.year
    month_end = dt_end.month

    date_year = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]
    start_year_index = date_year.index(year_start)
    end_year_index = date_year.index(year_end)
    start_index = start_year_index * 12 + month_start - 1
    end_index = end_year_index * 12 + month_end - 1

    variables = ['', 'RCH', 'GIS', 'MON', 'AREAkm2', 'FLOW_INcms', 'FLOW_OUTcms',
                 'EVAPcms', 'TLOSScms', 'SED_INtons', 'SED_OUTtons', 'SEDCONCmg/kg',
                 'ORGN_INkg', 'ORGN_OUTkg', 'ORGP_INkg', 'ORGP_OUTkg', 'NO3_INkg',
                 'NO3_OUTkg', 'NH4_INkg', 'NH4_OUTkg', 'NO2_INkg', 'NO2_OUTkg',
                 'MINP_INkg', 'MINP_OUTkg', 'CHLA_INkg', 'CHLA_OUTkg', 'CBOD_INkg',
                 'CBOD_OUTkg', 'DISOX_INkg', 'DISOX_OUTkg', 'SOLPST_INmg', 'SOLPST_OUTmg',
                 'SORPST_INmg', 'SORPST_OUTmg', 'REACTPSTmg', 'VOLPSTmg', 'SETTLPSTmg',
                 'RESUSP_PSTmg', 'DIFFUSEPSTmg', 'REACBEDPSTmg', 'BURYPSTmg', 'BED_PSTmg',
                 'BACTP_OUTct', 'BACTLP_OUTct', 'CMETAL']

    var_names = ['', 'Reach', 'GIS', 'Month', 'Area (km2)', 'Inflow (cms)', 'Outflow (cms)',
                'Evaporation (cms)', 'Transpiration Loss (cms)', 'Sediment Inflow (tons)', 'Sediment Outflow (tons)',
                'Sediment Concentration (mg/kg)', 'Organic Nitrogen Inflow (kg)', 'Organic Nitrogen Outflow (kg)',
                'Organic Phosphorus Inflow (kg)', 'Organic Phosphorus Outflow (kg)', 'Nitrate Inflow (kg)', 'Nitrate Outflow (kg)'
                ]

    var_index = variables.index(var)
    var_name = var_names[var_index]
    data = []
    for num, line in enumerate(f,1):
        line = line.strip()
        columns = line.split()
        if columns[1] == reachid and 1 <= float(columns[3]) <= 12:
            data.append(float(columns[var_index]))


    daterange = pd.date_range(start_date, end_date, freq='1M')
    daterange = daterange.union([daterange[-1]+1])
    daterange_str = [d.strftime('%b %y') for d in daterange]
    daterange_mil = [int(d.strftime('%s'))*1000 for d in daterange]

    ts = []
    data = data[start_index:end_index + 1]
    i = 0
    while i < len(data):
        ts.append([daterange_mil[i],data[i]])
        i += 1

    rchDict = {'Values': ts, 'Dates':daterange_str, 'ReachID': reachid, 'Variable': var_name}
    return rchDict







