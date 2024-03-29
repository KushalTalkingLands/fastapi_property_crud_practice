import logging
from fastapi import FastAPI, HTTPException
from property_operations import create_property, read_property, update_property, delete_property
from models import PropertyModel

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Create property
@app.post("/properties/")
async def create_property_route(property: PropertyModel):
    try:
        return create_property(property)
    except Exception as e:
        logger.exception("Error creating property")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Get property by ID
@app.get("/properties/{property_id}")
async def read_property_route(property_id: str):
    try:
        return read_property(property_id)
    except HTTPException as e:
        logger.warning(f"Property with id {property_id} not found")
        raise
    except Exception as e:
        logger.exception("Error reading property")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Update property by ID
@app.put("/properties/{property_id}")
async def update_property_route(property_id: str, property: PropertyModel):
    try:
        return update_property(property_id, property)
    except HTTPException as e:
        logger.warning(f"Property with id {property_id} not found")
        raise
    except Exception as e:
        logger.exception("Error updating property")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Delete property by ID
@app.delete("/properties/{property_id}")
async def delete_property_route(property_id: str):
    try:
        return delete_property(property_id)
    except HTTPException as e:
        logger.warning(f"Property with id {property_id} not found")
        raise
    except Exception as e:
        logger.exception("Error deleting property")
        raise HTTPException(status_code=500, detail="Internal Server Error")