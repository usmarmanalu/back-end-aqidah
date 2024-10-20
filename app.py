from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrape_doctors(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    doctors = []
    days_of_week = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

    for doctor_div in soup.find_all("div", class_="card"):
        img_tag = doctor_div.find("img")
        image = img_tag["src"] if img_tag else None
        name_tag = doctor_div.find("h6")
        name = name_tag.text.strip() if name_tag else "Nama tidak tersedia"

        schedule_table = doctor_div.find_next("table")
        schedule = []

        if schedule_table:
            for row in schedule_table.find_all("tr")[1:]:
                day = row.find("th").text.strip()
                time = row.find_all("td")
                times = [td.text.strip() for td in time if td.text.strip() != "- - -"]  # Menghindari jadwal kosong
                if times:  # Tambahkan hanya jika ada jam yang tersedia
                    schedule.append(f"{day}: {', '.join(times)}")

        # Menggabungkan jadwal menjadi string tunggal hanya jika ada jadwal yang valid
        schedule_str = "\n".join(schedule) if schedule else "Jadwal tidak tersedia"

        doctors.append({
            "image": image,
            "name": name,
            "schedule": schedule_str  # Jadwal menjadi string biasa
        })

    return doctors


@app.route('/doctors-anak', methods=['GET'])
def get_doctors_anak():
    url = "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiQU5BIn0.4mn-CHZtv1Ger_2L_jonfDcnADP8Va4GzfQ_NNeZwVU"
    doctors = scrape_doctors(url)
    return jsonify(doctors)

@app.route('/doctors-anastesi', methods=['GET'])
def get_doctors_anastesi():
    url = "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiQU5UIn0.q_Rg12NeKiR3tcSw2Qd-3beL2ttm5dsiLNFJxOzBA5k"
    doctors = scrape_doctors(url)
    return jsonify(doctors)

@app.route('/doctors-bedah', methods=['GET'])
def get_doctors_bedah():
    url = "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiQkVEIn0.ohdLEPnqtGCsd0atK_F5jWfz1sqnRO8G1FSCykkHvlU"
    doctors = scrape_doctors(url)
    return jsonify(doctors)

@app.route('/doctors-gigidanmulut', methods=['GET'])
def get_doctors_gigidanmulut():
    url = "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiR0lHIn0._fQGxUAOsuys5Iu_xZJuuPQtKS2zr6I1WBFOhyyJkiw"
    doctors = scrape_doctors(url)
    return jsonify(doctors)

@app.route('/doctors-penyakitdalam', methods=['GET'])
def get_doctors_penyakitdalam():
    url = "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiSU5UIn0.KwMKBvDub6dV5jHrGj_WaBZ8D22Ny2otsKNIs4a7hiY"
    doctors = scrape_doctors(url)
    return jsonify(doctors)

@app.route('/doctors-kulitdankelamin', methods=['GET'])
def get_doctors_kulitdankelamin():
    url = "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiS0xUIn0.qvPnfHw0h5CEQ2izgUOrKgisREcH1wlB1SE0KC6vChg"
    doctors = scrape_doctors(url)
    return jsonify(doctors)

@app.route('/doctors-mata', methods=['GET'])
def get_doctors_mata():
    url = "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiTUFUIn0.yckN3KwDN9abT6gstg9lI8Z4P5PoiVuoz5dQz5D4UVE"
    doctors = scrape_doctors(url)
    return jsonify(doctors)

@app.route('/doctors-kandungan', methods=['GET'])
def get_doctors_kandungan():
    url = "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiT0JHIn0.knHD2ybbhDNXG5vkciQcRYVkCJknDByUSKlm0iQXdIw"
    doctors = scrape_doctors(url)
    return jsonify(doctors)

@app.route('/doctors-patologiklinik', methods=['GET'])
def get_doctors_patologiklinik():
    url = "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiUEFLIn0.TaSkLk2QTXMOPfmFCKvjsAoqyUhISZrc-pgAnrVmyLA"
    doctors = scrape_doctors(url)
    return jsonify(doctors)

@app.route('/doctors-paru', methods=['GET'])
def get_doctors_paru():
    url = "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiUEFSIn0.3UtGzb_b9XBDQB5UCbc-w8YEkZ86_a-t7f_myKw8uMg"
    doctors = scrape_doctors(url)
    return jsonify(doctors)

@app.route('/doctors-radiologi', methods=['GET'])
def get_doctors_radiologi():
    url = "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiUkRPIn0.fAu37NlT_AD2hmqn4dRY9ENg5UqVqE3BOZlp1RHgkto"
    doctors = scrape_doctors(url)
    return jsonify(doctors)

@app.route('/doctors-saraf', methods=['GET'])
def get_doctors_saraf():
    url = "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiU0FSIn0.SgiVnpAcTSvBnLURNES9kbpEOCSLBzRR7-cN_vScbm8"
    doctors = scrape_doctors(url)
    return jsonify(doctors)

@app.route('/doctors-tht-kl', methods=['GET'])
def get_doctors_thtkl():
    url = "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiVEhUIn0.DzQOKuOe9IjRS3a-NrwU200vW9_k1TFJcwPSXuE5t5w"
    doctors = scrape_doctors(url)
    return jsonify(doctors)

@app.route('/doctors-psikologi', methods=['GET'])
def get_doctors_psikologi():
    url = "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiMTAxIn0.VncL-YgcepzuzZal-zEusOZvaq5r89TdLJWi3q7Xhus"
    doctors = scrape_doctors(url)
    return jsonify(doctors)

@app.route('/doctors-konservasi-gigi', methods=['GET'])
def get_doctors_konservasi_gigi():
    url = "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiMTcwNzQ0NDMxMCJ9.JShbr-XctB8NoCjokSBs6iDEEou_kuW0EGT3xwr3X5g"
    doctors = scrape_doctors(url)
    return jsonify(doctors)

@app.route('/doctors-kedokteran-jiwa', methods=['GET'])
def get_doctors_kedokteran_jiwa():
    url = "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiMTcxNDk3Mjg5MiJ9.Ig6c5B4cXqRHivDA8zHUoa4XTVJHEhgHAK5J5UasThg"
    doctors = scrape_doctors(url)
    return jsonify(doctors)


if __name__ == '__main__':
    app.run(debug=True)