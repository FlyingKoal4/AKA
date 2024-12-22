from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

# Data array lagu
songs = [
    {"title": "Lagu A", "artist": "Penyanyi A", "listeners": 750000},
    {"title": "Lagu B", "artist": "Penyanyi B", "listeners": 450000},
    {"title": "Lagu C", "artist": "Penyanyi C", "listeners": 500000},
    {"title": "Lagu D", "artist": "Penyanyi D", "listeners": 300000},
]

# Fungsi iteratif untuk mencari lagu
def search_songs_iterative(songs, min_listeners):
    result = []
    for song in songs:
        if song["listeners"] >= min_listeners:
            result.append(song)
    return result

# Fungsi rekursif untuk mencari lagu
def search_songs_recursive(songs, min_listeners, index=0, result=None):
    if result is None:
        result = []
    # Basis kasus: jika indeks sudah melewati panjang array
    if index >= len(songs):
        return result
    # Tambahkan lagu jika jumlah pendengar >= min_listeners
    if songs[index]["listeners"] >= min_listeners:
        result.append(songs[index])
    # Rekursif ke elemen berikutnya
    return search_songs_recursive(songs, min_listeners, index + 1, result)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/filter-songs", methods=["GET"])
def filter_songs():
    method = request.args.get("method", "iterative")
    min_listeners = 500000

    start_time = time.time()

    # Pilih metode pencarian
    if method == "recursive":
        result = search_songs_recursive(songs, min_listeners)
    else:
        result = search_songs_iterative(songs, min_listeners)

    end_time = time.time()

    # Hitung waktu eksekusi
    execution_time = end_time - start_time

    if not result:
        return jsonify({
            "message": "Tidak ada lagu yang ditemukan",
            "complexity": "O(n) untuk pencarian iteratif dan rekursif",
            "execution_time": f"{execution_time:.6f} detik"
        }), 404

    return jsonify({
        "songs": result,
        "complexity": "O(n) untuk pencarian iteratif dan rekursif",
        "execution_time": f"{execution_time:.6f} detik"
    })

if __name__ == "__main__":
    app.run(debug=True)
