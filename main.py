from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

# Define a route with a path operation decorator
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# Example data
folders = [
    {"id": 1, "uid": "nErXDvCkzz", "title": "Department ABC"},
    {"id": 2, "uid": "k3S1cklGk", "title": "Department RND"},
]

# Common endpoint to handle both folderUid and documentUid
@app.get("/uids/{uid_type}/{uid}", response_model=dict)
async def get_uid(uid_type: str, uid: str, authorization: str = Header(None)):
    # Simplified Authorization check
    if not authorization or authorization != "Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk":
        raise HTTPException(status_code=401, detail="Unauthorized")

    # Select the appropriate data based on uid_type
    data = next((folder for folder in folders if folder["uid"] == uid), None)

    # Check if the UID was found
    if data is None:
        raise HTTPException(status_code=404, detail="UID not found")

    return data
