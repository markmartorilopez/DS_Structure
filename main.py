# Copyright (c) 2023 FIFA - Mark Martori Lopez

import argparse
import os


#### ARGUMENTS
def get_args_parser():
    parser = argparse.ArgumentParser("Players Targeting - FIFA", add_help = False)

    ## Snowflake Connecting
    # Account
    parser.add_argument("-a","--account",
                        type = str)
    # Username
    parser.add_argument("-u","--user",
                        type = str)
    # Password
    parser.add_argument("-p","--password",
                        type = str)
    # Role
    parser.add_argument("-r","--role", default = 1,
                        type=str,
                        help = "Role to be used while managing snowflake database and warehouse.")
    # Warehouse
    parser.add_argument("-w","--warehouse",
                        type = str)
    # Database
    parser.add_argument("-d","--database",
                        type = str)
    # Schema
    parser.add_argument("-s","--schema", 
                        type = str)
    ## Debugging
    parser.add_argument("--debugging", default = False,
                        help = "Logging process.")

    return parser



from snowflake.snowpark import Session


def snowflake_connection(account : str,
                         user : str,
                         password : str,
                         role : str,
                         warehouse : str,
                         database : str,
                         schema : str):
    # Snowpark Session
    connection_parameters = {
        
        "account"  : account,
        "user"     : user,
        "password" : password,
        "role"     : role,
        "warehouse": warehouse,
        "database" : database,
        "schema"   : schema
    }

    return Session.builder.configs(
        connection_parameters
    ).create()


### MAIN
def main(args):
    """
    """
    csv_file = "tests_report.csv"

    session = snowflake_connection(
            args.account,
            args.user,
            args.password,
            args.role,
            args.warehouse,
            args.database,
            args.schema
        )

    print(session.sql("SELECT 1/2").collect())
    
    
    return 1
    

if __name__ == '__main__':
    parser_detr = argparse.ArgumentParser("Players Targeting - FIFA", parents=[get_args_parser()])
    args = parser_detr.parse_args()
    

    done = main(args)    
