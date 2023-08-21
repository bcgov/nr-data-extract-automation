-- RAR = riparian areas --
SELECT rda.DEV_ASSESSMENT_ID file_id
     , rda.DEV_NATURE_CODE 
     , rda.ADDRESS_ID 
     , ra.ADDRESS_LINE_1 
     , ra.ADDRESS_LINE_2 
     , ra.ADDRESS_LINE_3 
     , ra.CITY 
     , ra.PROVINCE_STATE 
     , ra.POSTAL_CODE 
     , ra.COUNTRY 
     , rda.REGION_CODE 
     , rrc.DESCRIPTION region
     , rda.MUNICIPALITY_CODE 
     , rm.DESCRIPTION municipality     
     , rda.DEV_CODE 
     , rdc.DESCRIPTION development
     , rda.RIPARIAN_AREA_LENGTH 
     , rda.PROPOSED_START_DATE 
     , rda.PROPOSED_END_DATE 
     , rda.LOCATION_LEGAL_DSC 
     , rda.LOCATION_STREAM_NAME 
     , rda.LOCATION_NEW_WATERSHED_CODE 
     , rda.LOCATION_LATITUDE 
     , rda.LOCATION_LONGITUDE 
     , rda.LOT_AREA 
     , rda.SECTION_9_PART_7_ACTIVITIES_YN 
     , rda.ALL_PROFESSIONALS_QUALIFIED_YN 
     , rda.ASSESSMENT_METHOD_FOLLOWED_YN 
     , rda.CERTIFIED_NO_HADD_YN 
     , rda.COMPLETE_REPORT_ATTACHED_YN
     , rda.RETAIN_ASSESS_REPORT_YN 
     , rda.DFO_AREA_CODE 
     , rdac.DESCRIPTION DFO_AREA_DESCRIPTION
     , rdsc.DESCRIPTION file_status
     , rstc.description stream_type
     , rda.WHO_CREATED 
     , rda.WHEN_CREATED 
     , rda.WHO_UPDATED 
     , rda.WHEN_UPDATED 
     , rda.DEV_AREA 
  FROM rar.RAR_DEV_ASSESSMENTS rda
     , rar.RAR_ADDRESSES ra 
     , rar.RAR_REGION_CDS rrc
     , rar.RAR_DEV_CDS rdc
     , rar.RAR_MUNICIPALITIES rm
     , rar.RAR_DEV_STATUS_CDS rdsc
     , rar.RAR_STREAM_TYPE_CDS rstc
     , rar.RAR_DFO_AREA_CDS rdac 
 WHERE rda.REGION_CODE = rrc.REGION_CODE
   AND rda.ADDRESS_ID = ra.ADDRESS_ID
   AND rda.DEV_CODE = rdc.DEV_CODE
   AND rda.MUNICIPALITY_CODE = rm.MUNICIPALITY_CODE 
   AND rda.DEV_STATUS_CODE = rdsc.DEV_STATUS_CODE 
   AND rda.STREAM_CODE = rstc.STREAM_TYPE_CODE
   AND rda.DFO_AREA_CODE = rdac.DFO_AREA_CODE 
   AND rda.DEV_STATUS_CODE IN ('ACCEPTED', 'SUBMITTED',' UNDER_REVIEW', 'RE_SUBMITTED')
   AND rda.WHEN_CREATED >= TO_DATE('20191101','YYYYMMDD')
 ORDER BY 1