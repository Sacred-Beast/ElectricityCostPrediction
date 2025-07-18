from pydantic import BaseModel

class ElectricityInput(BaseModel):
    site_area: float
    structure_type: str
    water_consumption: float
    recycling_rate: float
    utilisation_rate: float
    air_qality_index: float
    issue_reolution_time: float
    resident_count: int
    