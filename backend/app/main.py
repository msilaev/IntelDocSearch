"""Main module for the FastAPI application."""

import logging
import sys
import os

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi import APIRouter, UploadFile, File, HTTPException

from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router as api_router  # Import the router correctly

from fastapi.responses import JSONResponse


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"], 
    allow_headers=["*"],
)
#app.add_middleware(
#    ApiKeyMiddleware
#)

# Set up logging
logger = logging.getLogger(__name__ )
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))
# logger.info('Api is starting...')

# Routes
app.include_router(api_router)

@app.get("/routes/")
async def get_routes():
    return app.routes


@app.get("/")
def read_root():
    return {"message": "Welcome to the Intelligent Document Search API!"}

# File Upload Route

#@app.post("/upload/")
#async def upload_file(file: UploadFile = File(...)):
#    try:
#        contents = await file.read()
#        filename = file.filename

#        with open(f"app/uploads/{filename}", "wb") as f:
#            f.write(contents)

#        return {"message": f"File '{filename}' uploaded successfully!"}
#    except Exception as e:
#        return JSONResponse(content={"error": str(e)}, status_code=500)


#@app.post("/upload/")
#async def upload_document(file: UploadFile = File(...)):
#    try:
#        file_location = f"app/uploads/{file.filename}"
#        os.makedirs(os.path.dirname(file_location), exist_ok=True)
#        
#        with open(file_location, "wb") as file_object:
#            file_object.write(await file.read())

#        return {"filename": file.filename, "content_type": file.content_type, "message": "File uploaded successfully"}
    
#    except Exception as e:
#        return {"error": str(e)}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    except WebSocketDisconnect:
        print("WebSocket connection closed")

