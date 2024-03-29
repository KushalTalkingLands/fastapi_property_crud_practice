from enum import Enum
from pydantic import BaseModel
from typing import Optional

# Enum for property categories
class PropertyCategory(str, Enum):
    Farm = "Farm"
    Residential = "Residential"
    Commercial = "Commercial"

# Model for property
class PropertyModel(BaseModel):
    property_name: str
    property_description: str
    property_category: PropertyCategory