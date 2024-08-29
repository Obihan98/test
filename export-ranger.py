#!/usr/bin/env python2.7
        
def execute(ranger_policy_helper):
    logger = ranger_policy_helper.getLogger()
    
    logger.info('Testing Ranger export-import functions')
    
    ranger_config_dict = {
        "output_folder_path": "/tmp",  # Mandatory param, exports output file to /tmp folder
        "service_list": "ranger",  # Optional param, exports policies only from hdfs and hive services.
        "exported_policies_file_name": "ranger-policy-output"
    }
    
    ranger_policy_helper.export_ranger_policies(ranger_config_dict)
