from parser_utils import parse_date

#File Names 
fname_personal = "data/personal_info.csv"
fname_employment = "data/employment.csv"
fname_vehicles = "data/vehicles.csv"
fname_update_status = "data/update_status.csv"

fnames = (fname_personal, fname_employment, fname_vehicles, fname_update_status)

#Parsers
parser_personal = (str, str, str, str, str)
parser_employment = (str, str, str, str)
parser_vehicle = (str, str, str, int)
parser_update_status = (str, parse_date, parse_date)

parsers = (
            parser_personal, parser_employment, 
            parser_vehicle, parser_update_status
          )

#Named Tuple Names
class_name_personal = "Personal"
class_name_employment = "Employment"
class_name_vehicle =  "Vehicle"
class_name_update_status = "UpdateStatus"

class_names = (
                class_name_personal, class_name_employment, 
                class_name_vehicle, class_name_update_status
              ) 

#Field Inclusion/Exclusion
fields_compress_personal = (True, True, True, True, True)
fields_compress_employment = (True, True, True, False)
fields_compress_vehicle = (False, True, True, True)
fields_compress_update_status = (False, True, True)
compress_fields = (
                    fields_compress_personal, fields_compress_employment,
                    fields_compress_vehicle, fields_compress_update_status
                    )

