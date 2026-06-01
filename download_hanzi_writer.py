# download_hanzi_writer.py
import urllib.request
import os

os.makedirs("static/hanzi-writer", exist_ok=True)

# Download CSS
urllib.request.urlretrieve(
    "https://cdn.jsdelivr.net/npm/hanzi-writer@2.3.0/dist/hanzi-writer.min.css",
    "static/hanzi-writer/hanzi-writer.min.css"
)
print("✅ Downloaded hanzi-writer.min.css")

# Download JS
urllib.request.urlretrieve(
    "https://cdn.jsdelivr.net/npm/hanzi-writer@2.3.0/dist/hanzi-writer.min.js",
    "static/hanzi-writer/hanzi-writer.min.js"
)
print("✅ Downloaded hanzi-writer.min.js")

print("Done! Files saved to static/hanzi-writer/")