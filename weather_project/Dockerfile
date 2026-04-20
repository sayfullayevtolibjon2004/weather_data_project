# 1. Python versiyasini 3.12 qilib belgilaymiz
FROM python:3.12-slim

WORKDIR /app

# 2. Tizim paketlarini yangilash va Driver 18 uchun tayyorlash
RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 \
    && rm -rf /var/lib/apt/lists/*

# 3. Microsoft drayver omborini qo'shish (Debian 12 - Bookworm uchun)
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg \
    && curl https://packages.microsoft.com/config/debian/12/prod.list > /etc/apt/sources.list.d/mssql-release.list

# 4. ODBC Driver 18 ni o'rnatish
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y \
    msodbcsql18 \
    unixodbc-dev \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# 5. Kutubxonalarni o'rnatish
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Loyihani nusxalash
COPY . .

CMD ["python", "app/main.py"]