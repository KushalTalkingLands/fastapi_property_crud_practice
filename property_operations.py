import logging
from fastapi import HTTPException
from bson import ObjectId
from models import PropertyModel
from db import collection

# Configure logging
logger = logging.getLogger(__name__)

# Create property
def create_property(property: PropertyModel):
    try:
        property_dict = property.dict()
        result = collection.insert_one(property_dict)
        return {"message": "Property created successfully", "id": str(result.inserted_id)}
    except Exception as e:
        logger.exception("Error creating property")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Get property by ID
def read_property(property_id: str):
    try:
        property_data = collection.find_one({"_id": ObjectId(property_id)})
        property_data['_id'] = str(property_data['_id'])
        # return "Propery found "
        if property_data:
            return property_data
        else:
            raise HTTPException(status_code=404, detail="Property not found")
    except Exception as e:
        logger.exception("Error reading property")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Update property by ID
def update_property(property_id: str, property: PropertyModel):
    try:
        property_dict = property.dict()
        result = collection.update_one({"_id": ObjectId(property_id)}, {"$set": property_dict})
        if result.modified_count == 1:
            return {"message": "Property updated successfully"}
        else:
            raise HTTPException(status_code=404, detail="Property not found")
    except Exception as e:
        logger.exception("Error updating property")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Delete property by ID
def delete_property(property_id: str):
    try:
        result = collection.delete_one({"_id": ObjectId(property_id)})
        if result.deleted_count == 1:
            return {"message": "Property deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Property not found")
    except Exception as e:
        logger.exception("Error deleting property")
        raise HTTPException(status_code=500, detail="Internal Server Error")