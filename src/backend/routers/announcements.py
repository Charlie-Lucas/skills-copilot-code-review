"""
Endpoints for announcements in the High School Management System API
"""

from fastapi import APIRouter
from typing import Dict, Any, Optional

from ..database import announcements_collection

router = APIRouter(
    prefix="/announcements",
    tags=["announcements"]
)


@router.get("", response_model=Dict[str, Any])
@router.get("/", response_model=Dict[str, Any])
def get_announcements() -> Dict[str, Any]:
    """
    Get all active announcements
    
    Returns a dictionary with announcement data including message and display settings
    """
    announcements = {}
    for announcement in announcements_collection.find({"active": True}):
        announcement_id = announcement['_id']
        announcement_copy = {k: v for k, v in announcement.items() if k != '_id'}
        announcements[announcement_id] = announcement_copy
    
    return announcements
