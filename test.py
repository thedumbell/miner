import requests

url = "https://filebin.net/mf83v1xqgk0d3rll/data.dat"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers, allow_redirects=True, stream=True)

if response.status_code == 200:
    with open("data.dat", "wb") as dosya:
        for chunk in response.iter_content(chunk_size=8192):
            dosya.write(chunk)
    print("Dosya başarıyla indirildi: data.dat")
else:
    print(f"İndirme başarısız! HTTP {response.status_code}")
