#!/usr/bin/env python2.7
        
def execute(ranger_policy_helper):
    logger = ranger_policy_helper.getLogger()
    
    logger.info('Testing Ranger export-import functions')
    
    ranger_config_dict = {
        "output_folder_path": "/tmp",
        "ssl_cert_path": "/var/lib/ambari-server/keys/schnonpun1.nprodbdsdbpvtsn.nprodbdsvcn.oraclevcn.com.crt"
    }
    
    ranger_policy_helper.export_ranger_policies(ranger_config_dict)
    logger.info('If you see this function did run.')
