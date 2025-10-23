"""
Blacklists Blueprint Module

This module defines the Flask blueprint for managing blacklist operations.
It provides endpoints for creating blacklist entries, retrieving blacklist information,
and checking service status.

Routes:
    POST /blacklists - Create a new blacklist entry
    GET /blacklists/<email> - Retrieve blacklist information for a specific email
    GET / - Health check endpoint

All data manipulation endpoints require authentication via request headers.
"""

from flask import Flask, jsonify, request, Blueprint
from blacklists.src.commands.authenticate import Authenticate
from blacklists.src.commands.create_blacklist import CreateBlacklist
from blacklists.src.commands.get_blacklist import GetBlacklist
from blacklists.src.errors.errors import TokenInvalid

# Create the blacklists blueprint for modular route organization
blacklists_blueprint = Blueprint('blacklists', __name__)

@blacklists_blueprint.route('/blacklists', methods=['POST'])
def create():
    """
    Create a new blacklist entry.
    
    This endpoint creates a new blacklist entry with the provided data.
    Requires authentication via request headers.
    
    Request:
        Method: POST
        Headers: Must include authentication token
        Body: JSON data for the blacklist entry
        
    Returns:
        JSON: The created blacklist item
        Status: 201 Created on success
        
    Raises:
        TokenInvalid: If authentication fails
        
    Example:
        POST /blacklists
        Headers: {"Authorization": "Bearer <token>"}
        Body: {"email": "user@example.com", "reason": "spam"}
    """
    # Authenticate user using request headers
    userId = Authenticate(request.headers).execute()

    if not userId:
        raise TokenInvalid()
    
    # Capture client IP address for logging/audit purposes
    ip = request.remote_addr
    
    # Create new blacklist entry with request data and client IP
    item = CreateBlacklist(request.get_json(), ip).execute()

    return jsonify(item), 201

@blacklists_blueprint.route('/blacklists/<email>', methods=['GET'])
def show(email):
    """
    Retrieve blacklist information for a specific email.
    
    This endpoint fetches blacklist data associated with the provided email address.
    Requires authentication via request headers.
    
    Args:
        email (str): The email address to look up in the blacklist
        
    Request:
        Method: GET
        Headers: Must include authentication token
        
    Returns:
        JSON: Blacklist information for the specified email
        Status: 200 OK on success
        
    Raises:
        TokenInvalid: If authentication fails
        
    Example:
        GET /blacklists/user@example.com
        Headers: {"Authorization": "Bearer <token>"}
    """
    # Authenticate user using request headers
    userId = Authenticate(request.headers).execute()

    if not userId:
        raise TokenInvalid()
    
    # Retrieve blacklist information for the specified email
    response = GetBlacklist(email).execute()

    return jsonify(response)

@blacklists_blueprint.route('/', methods=['GET'])
def status():
    """
    Health check endpoint.
    
    This endpoint provides a simple health check to verify that the service
    is running and responsive. No authentication required.
    
    Request:
        Method: GET
        
    Returns:
        JSON: Status message indicating service health
        Status: 200 OK
        
    Example:
        GET /
        Response: {"status": "ok"}
    """
    return jsonify({'status': 'ok'}), 200
