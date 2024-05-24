from dtos.packaging import PackagingOut
from dtos.caregiver import CaregiverOut
from dtos.vehicle import VehicleOut
from typing import List, Optional

async def bin_packing_heuristic(caregivers: list[CaregiverOut], vehicles: List[VehicleOut]) -> Optional[List[PackagingOut]]:

    vehicles_packing: List[PackagingOut] = []
    caregivers_assigned: List[CaregiverOut] = []  

    for idx, vehicle in enumerate(vehicles):
        max_capacity = vehicle.capacity
        current_capacity = 0
        caregivers_selected: List[CaregiverOut] = []
        max_skill = 0

        for caregiver in caregivers:

            if caregiver not in caregivers_assigned:

                if current_capacity < max_capacity:
                    caregivers_selected.append(caregiver)
                    caregivers_assigned.append(caregiver)
                    current_capacity += 1
                    max_skill += caregiver.skill

        vehicles_packing.append(
            PackagingOut(
                id= idx, 
                reg_num= vehicle.reg_num, 
                MAX_Q= max_skill, 
                MIN_Q= 0, 
                VD= vehicle.average_speed, 
                FLETE= vehicle.freight_km, 
                CC= 0.35, 
                EM= 2.7, 
                caregivers= caregivers_selected
            )
        )



    return vehicles_packing


