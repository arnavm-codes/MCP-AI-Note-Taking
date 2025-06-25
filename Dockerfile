FROM python:3.12-slim

WORKDIR /app

RUN pip install uv

# copy requirements
COPY requirements.txt /app/

# install dependencies using uv
RUN uv run pip install  --no-cache-dir -r requirements.txt
 
# copy application code
COPY server/note_server.py /app/
COPY notes.txt /app/
COPY .env /app/

# command to run the server
# CMD ["uvicorn", "tools_api_server:app", "--host", "0.0.0.0", "--port", "8001"]
CMD ["uv","run", "note_server.py"]
