
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated

class UserInput(BaseModel):
    site_area: Annotated[int, Field(...,gt=0,lt=5000, description="Site area in square meters")]
    structure_type: Annotated[
        Literal["Mixed-use", "Residential", "Commercial", "Industrial"], 
        Field(...,description="Type of structure")
    ]
    water_consumption: Annotated[int, Field(...,gt=0, lt=10000,description="Water consumption in liters")]
    recycling_rate: Annotated[int, Field(...,gt=0, le=90, description="Recycling rate in percentage")]
    utilisation_rate: Annotated[int, Field(...,gt=0, le=100, description="Utilisation rate in percentage")]
    air_quality_index: Annotated[int, Field(...,gt=0,le=200,description='air quality')] 
    issue_resolution_time: Annotated[int, Field(...,gt=0,le=72, description="Issue resolution time in hours")]
    resident_count: Annotated[int, Field(...,gt=0, le=489,description="Number of residents")]

    @computed_field
    @property
    def water_efficiency(self) -> float:
        return (self.recycling_rate * self.utilisation_rate) / self.water_consumption
    @computed_field
    @property
    def structure_type_numeric(self) -> int:
        structure_mapping = {
            "Mixed-use": 1,
            "Residential": 2,
            "Commercial": 3,
            "Industrial": 4
        }
        return structure_mapping[self.structure_type]
    





   
