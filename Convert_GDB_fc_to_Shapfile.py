########################################################################################################################
# File name: CBI_Data_Catalog_Script.py 
# Author: CBI Data Catalog Auto-generated Script  
# Date created:  Tue Apr 21 2020 08:28:52 GMT-0700 (Pacific Daylight Time)
# Date last modified: Tue Apr 21 2020 08:28:52 GMT-0700 (Pacific Daylight Time)
# Python Version: 2.7
# Description:
# This script was automatically generated by the CBI Data Catalog. It will perform the requested actions (clip, project,
# copy) on all the datasets that were visible at the time this script was created. 
######################################################################################################################## 

import arcpy
import arcpy.sa
import os

output_folder_mike = r"P:\Projects3\CDT-CEQA_California_2019_mike_gough\Tasks\CEQA_Parcel_Exemptions\Data\Intermediate\Shapefile_Conversions\Mike"
datasets_mike = [
    #r"Database Connections\CBI Outputs.sde\cbioutputs.mike_gough.sacramento_parcels_requirements_and_exemptions",
    r"Database Connections\CBI Intermediate.sde\cbiintermediate.mike_gough.urban_area_prc_21094_5",
    r"Database Connections\CBI Intermediate.sde\cbiintermediate.mike_gough.CA_Rare_Threatened_or_Endangered_Erase_Impervious_del_fields",
    #r"\\loxodonta\gis\Source_Data\biota\state\CA\CNDDB\20200201\gis_com\cnddb.shp",
    r"Database Connections\CBI Outputs.sde\cbioutputs.mike_gough.urbanized_area_prc_21071",
    r"Database Connections\CBI Inputs.sde\cbiinputs.mike_gough.CA_TIGER_2019_incorporated_cities_with_TIGER_2017_population",
    r"Database Connections\CBI Inputs.sde\cbiinputs.mike_gough.CA_Fld_Haz_Ar_pre_floodplain_project",
    r"\\loxodonta\gis\Source_Data\inlandWaters\state\CA\California_Coastal_Zone\ds990\ds990.gdb\ds990",
    #r"\\loxodonta\gis\Source_Data\biota\national\USFWS_Critical_Habitat\crithab_all_layers\CRITHAB_POLY.shp",
    #r"\\loxodonta\gis\Source_Data\boundaries\state\CA\MPO_Boundaries\Metropolitan Planning Organization (MPO), California\data\commondata\metopolitan_planning_organization_mpo\MPO_2013.shp",
    #r"\\loxodonta\gis\Source_Data\society\state\CA\CENSUS_Blocks_2010_with_Population\tabblock2010_06_pophu\tabblock2010_06_pophu.shp",
    r"Database Connections\CBI Inputs.sde\cbiinputs.mike_gough.sacramento_parcels",
    r"\\loxodonta\gis\Source_Data\transportation\state\CA\Infill_VMT\mpk_contents\v106\tazcstdm.gdb\TAZ_CSTDM",
    r"\\loxodonta\gis\Source_Data\transportation\state\CA\Infill_VMT\mpk_contents\v106\basedata.gdb\ADM_DOF_Opportunity_Zones",
    r"\\loxodonta\gis\Source_Data\transportation\state\CA\Infill_VMT\mpk_contents\v106\vectors.gdb\Stations\HSR_Statewide_Stations_Public_Map",
    #r"\\loxodonta\gis\Source_Data\transportation\state\CA\Infill_VMT\mpk_contents\commondata\amtrak_stations\Amtrak_Stations.shp",
    #r"\\loxodonta\gis\Source_Data\transportation\state\CA\Infill_VMT\mpk_contents\commondata\rail_sta_13\Rail_Sta_13.shp",
    r"\\loxodonta\gis\Source_Data\transportation\state\CA\Infill_VMT\mpk_contents\v106\gtfs.gdb\half_mile_d1",
    r"\\loxodonta\gis\Source_Data\transportation\state\CA\Infill_VMT\mpk_contents\v106\gtfs.gdb\MileDissolve_1",
    #r"\\loxodonta\gis\Source_Data\transportation\state\CA\Infill_VMT\mpk_contents\commondata\2010_adjusted_urban_area\2010_adjusted_urban_area.shp",
    r"\\loxodonta\gis\Source_Data\boundaries\state\CA\Infill_VMT_boundaries\mpk_contents\v106\default1.gdb\opparea_joined",
    #r"\\loxodonta\gis\Source_Data\boundaries\state\CA\County_Boundaries\ca-county-boundaries\CA_Counties\CA_Counties_TIGER2016.shp",
]

datasets_kai = [
    r"Database Connections\CBI Intermediate.sde\cbiintermediate.kai_foster.Existing_High_Quality_Transit_Cooridor",
    #r"\\loxodonta\gis\Source_Data\transportation\region\MPO\SACOG\SACGOG_StopsForOPR_ExistingAndTIP.shp",
    #r"\\loxodonta\gis\Source_Data\transportation\state\CA\High_Quality_Transit_Cooridors\High_Quality_Transit_Cooridors.shp",
    #r"\\loxodonta\gis\Source_Data\planningCadastre\region\CA_MPOs\SACGO\SACOG_Specific_Plans\specific_plans_OPR\specific_plans_OPR.shp",
    #r"\\loxodonta\gis\Source_Data\transportation\region\MPO\SACOG\High_Quality_Transit_2036.shp",
    #r"\\loxodonta\gis\Source_Data\transportation\region\MPO\SACOG\TotalVMT12_perCapita.shp",
    #r"\\loxodonta\gis\Source_Data\boundaries\region\MPO\SCAG\Specific_Plan_Boundary_SCAG.shp",
    #r"\\loxodonta\gis\Source_Data\environment\state\CA\Fire_Hazard_Severity_Zones_2017\fhszs06_3.shp",
    #r"\\loxodonta\gis\Source_Data\boundaries\state\CA\BOEcitycounty_20190805\BOEcitycounty_20190805.shp",
    r"\\loxodonta\gis\Source_Data\boundaries\state\CA\State_Conservancies\ds1754\ds1754.gdb\ds1754",
    r"\\loxodonta\gis\Source_Data\boundaries\state\CA\Incorporated_Cities\incorp19_1\incorp19_1.gdb\incorp19_1",
    #r"\\loxodonta\gis\Source_Data\transportation\state\CA\TransportationAnalysisZones_CSTDM\TAZ_CSTDM.shp",
    r"Database Connections\CBI Inputs.sde\cbiinputs.kai_foster.CA_ProtectedArea_Mask_CEQA_exp",
    #r"\\loxodonta\gis\Source_Data\environment\national\United_States\EPA_RSEIv237_Public_Release_Data\RSEI_v237.shp",
    #r"\\loxodonta\gis\Source_Data\environment\state\CA\TrackingCA_WaterSystem\service_areas\service_areas.shp",
    #r"\\loxodonta\gis\Source_Data\environment\state\CA\EPA_TRI\EPA_TRI_sites.shp",
    #r"\\loxodonta\gis\Source_Data\geoscientificinformation\state\CA\Liquefaction_Susceptibility\Liquefaction_susceptibility.shp",
    #r"\\loxodonta\gis\Source_Data\inlandWaters\state\CA\DWR\SPFC_Planning_Area_20100301\SPFC_Planning_Area_20100301.shp",
    #r"\\loxodonta\gis\Source_Data\transportation\state\CA\MPOs\MTC\Public_Lands_for_Workforce_Housing_2018\Public_Lands_for_Workforce_Housing_2018.shp",
    #r"\\loxodonta\gis\Source_Data\transportation\state\CA\MPOs\MTC\Parcel_Hazard_Exposure\Parcel_Hazard_Exposure.shp",
    #r"\\loxodonta\gis\Source_Data\geoscientificinformation\state\CA\Fault_Activity\GDM_006_FAM_750k_v2_GIS\shapefiles\FAM_Qt_Faults.shp",
    #r"\\loxodonta\gis\Source_Data\inlandWaters\state\CA\DWR\Systemwide_Planning_Area_20101007\Systemwide_Planning_Area_20101007.shp",
    #r"\\loxodonta\gis\Source_Data\transportation\state\CA\MPOs\AMBAG\Monterey_Railroad\Railroad.shp",
    #r"\\loxodonta\gis\Source_Data\transportation\state\CA\MPOs\MTC\Bay_Area_Ferry_Terminals\Ferry_Terminals.shp",
    #r"\\loxodonta\gis\Source_Data\transportation\state\CA\MPOs\MTC\Infill_Opportunity_Zone_Eligibility_2017 (1)\Infill_Opportunity_Zone_Eligibility_2017.shp",
    #r"\\loxodonta\gis\Source_Data\transportation\state\CA\MPOs\MTC\Lifeline_Routes\Lifeline_Routes.shp",
    #r"\\loxodonta\gis\Source_Data\transportation\state\CA\Metropolitan_Transportation_Commission\Transit_Priority_Areas_2014\Transit_Priority_Areas_2014.shp",
    #r"\\loxodonta\gis\Source_Data\transportation\state\CA\Metropolitan_Transportation_Commission\Transit_Priority_Project_Eligible_Areas_2017\Transit_Priority_Project_Eligible_Areas_2017.shp",
]

output_folder_kai = r"P:\Projects3\CDT-CEQA_California_2019_mike_gough\Tasks\CEQA_Parcel_Exemptions\Data\Intermediate\Shapefile_Conversions\Kai"

# Convert each GDB Feature Class to a shapefile.
for dataset in datasets_kai:
    try:
        desc = arcpy.Describe(dataset)
        basename = desc.baseName.split(".")[-1]
        print "Dataset: " + basename
        dataset_copy = output_folder_kai + os.sep + basename + ".shp"
        if not arcpy.Exists(dataset_copy):
            print "Copying " + basename + "..."
            arcpy.CopyFeatures_management(dataset, dataset_copy)
            print "Success\n"
    except Exception as e:
        print e
