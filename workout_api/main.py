from fastapi import FastAPI

app = FastAPI(title="WorkoutAPI")

if __name__ == "main":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
