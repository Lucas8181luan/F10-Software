FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    python3-dev \
    libx11-dev \
    xclip \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pyautogui pyperclip

COPY f10-encecja.py .  
CMD ["python", "f10-encecja.py"]  # Mesmo nome do COPY
