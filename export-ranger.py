#!/usr/bin/env python2.7
        
def execute(ranger_policy_helper):
    logger = ranger_policy_helper.getLogger()
    
    logger.info('Testing Ranger export-import functions')
    
    ranger_config_dict = {
    "output_folder_path": "/tmp",
    "output_file_format": "json"
    }
    
    ranger_policy_helper.export_ranger_policies(ranger_config_dict)