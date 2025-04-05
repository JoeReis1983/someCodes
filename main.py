from fastapi import FastAPI
from beginners.bin2dec import binary_to_decimal
from beginners.csv2json import csv_to_json
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "I am a backend and I am running."}

@app.get("/bin2dec/{binary}")
async def bin2dec(binary: str):
    result = binary_to_decimal(binary)
    return {"binary": binary, "decimal": result}

@app.get("/csv2json/{csv_file}")
async def csv2json(csv_file: str):
    json_data = csv_to_json(csv_file)
    return {"csv_file": csv_file, "json_data": json_data}
