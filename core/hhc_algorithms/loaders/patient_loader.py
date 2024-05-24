from models.patient_model import Patient
from models.time_window_model import TimeWindow
from models.location_model import Location, EuclideanLocation
from repository.load_files.read_json import read_jsons
from typing import Any


class Patient_Loader:
    def __init__(self) -> None:
        pass

    def __call__(self, path_file: str) -> Any:
        array_patients : list[Patient] = [] 
        try:
            with open(path_file) as file:
                patients_objects: list = read_jsons(path_file=path_file)
                if len(patients_objects) < 2:
                    raise 'There should be a minimum of two data elements.'
                wharehouse_object = patients_objects[0]
                wharehouse = Patient(
                    id= wharehouse_object['_id'], 
                    loc= EuclideanLocation(
                        x=float(wharehouse_object['loc']['x']),
                        y=float(wharehouse_object['loc']['y']),
                    ), 
                    tw= TimeWindow(
                        a=float(wharehouse_object['tw']['a']),
                        b=float(wharehouse_object['tw']['b']),
                    ), 
                    service_time= float(wharehouse_object['serviceTime']), 
                    demand=float(wharehouse_object['demand']), 
                    isWarehouse= True
                )
                array_patients.append(wharehouse) # the wharehouse was loaded
                #loads patients objects
                for i, patients in enumerate(patients_objects[1:]):
                    
                    array_patients.append(Patient(
                        id= i + 1, 
                        loc= EuclideanLocation(
                            x=float(patients['loc']['x']),
                            y=float(patients['loc']['y']),
                        ), 
                        tw= TimeWindow(
                            a=float(patients['tw']['a']),
                            b=float(patients['tw']['b']),
                        ), 
                        service_time= float(patients['serviceTime']), 
                        demand=float(patients['demand']), 
                        isWarehouse= False
                    ))
        except FileNotFoundError as fnf:
            print(f'The file {path_file} was not found.')
        except Exception as e:
            print(f'Error occurred: {e}')
        finally:
            return array_patients
        

    


