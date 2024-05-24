from models.patient_model import Patient
from models.vehicle_model import Vehicle
from repository.load_files.read_json import read_jsons
from typing import Any


class Vehicle_Loader:
    def __init__(self) -> None:
        pass

    def __call__(self, path_file: str, wharehouse: Patient) -> Any:
        array_vehicles : list[Vehicle] = [] 
        try:
            with open(path_file) as file:
                vehicles_objects: list = read_jsons(path_file=path_file)
                if len(vehicles_objects) < 1:
                    raise 'There should be  minimum of an data elements.'
                
                for i, vehicle in enumerate(vehicles_objects):
                    array_vehicles.append(
                        Vehicle(
                            id= i, 
                            MAX_Q= float(vehicle['MAX_Q']), 
                            MIN_Q= float(vehicle['MIN_Q']), 
                            WARE_HOUSE= wharehouse, 
                            VD= float(vehicle['VD']), 
                            FLETE= float(vehicle['FLETE']), 
                            CC= float(vehicle['CC']), 
                            EM= float(vehicle['EM'])
                        )
                    )

        except FileNotFoundError as fnf:
            print(f'The file {path_file} was not found.')
            print(f'{fnf}')
        except Exception as e:
            print(f'Error occurred: {e}')
        finally:
            return array_vehicles