from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

# Data array lagu
songs = [
    {"artist": "The Weeknd", "title": "Blinding Lights", "listening_count": 4619215892},
    {"artist": "Ed Sheeran", "title": "Shape of You", "listening_count": 4150542988},
    {"artist": "Lewis Capaldi", "title": "Someone You Loved", "listening_count": 3724428057},
    {"artist": "Harry Styles", "title": "As It Was", "listening_count": 3685852626},
    {"artist": "The Weeknd", "title": "Starboy", "listening_count": 3644200876},
    {"artist": "Post Malone", "title": "Sunflower", "listening_count": 3643658417},
    {"artist": "Drake", "title": "One Dance", "listening_count": 3462965551},
    {"artist": "The Neighbourhood", "title": "Sweater Weather", "listening_count": 3442390075},
    {"artist": "The Kid LAROI", "title": "STAY", "listening_count": 3395701704},
    {"artist": "Imagine Dragons", "title": "Believer", "listening_count": 3259536490},
    {"artist": "Glass Animals", "title": "Heat Waves", "listening_count": 3229365259},
    {"artist": "Ed Sheeran", "title": "Perfect", "listening_count": 3222122668},
    {"artist": "Tones And I", "title": "Dance Monkey", "listening_count": 3187398899},
    {"artist": "Billie Eilish", "title": "lovely", "listening_count": 3116930791},
    {"artist": "James Arthur", "title": "Say You Won't Let Go", "listening_count": 3105746839},
    {"artist": "Post Malone", "title": "rockstar", "listening_count": 3085722022},
    {"artist": "The Chainsmokers", "title": "Closer", "listening_count": 3078159788},
    {"artist": "The Chainsmokers", "title": "Something Just Like This", "listening_count": 2922873624},
    {"artist": "Harry Styles", "title": "Watermelon Sugar", "listening_count": 2901146832},
    {"artist": "Shawn Mendes", "title": "Señorita", "listening_count": 2892123341},
    {"artist": "Vance Joy", "title": "Riptide", "listening_count": 2888770576},
    {"artist": "Hozier", "title": "Take Me to Church", "listening_count": 2821450551},
    {"artist": "Tom Odell", "title": "Another Love", "listening_count": 2803554359},
    {"artist": "Dua Lipa", "title": "Don't Start Now", "listening_count": 2803208815},
    {"artist": "OneRepublic", "title": "Counting Stars", "listening_count": 2746669985},
    {"artist": "Ed Sheeran", "title": "Photograph", "listening_count": 2737633481},
    {"artist": "Juice WRLD", "title": "Lucid Dreams", "listening_count": 2732329081},
    {"artist": "Coldplay", "title": "Yellow", "listening_count": 2708016376},
    {"artist": "Arctic Monkeys", "title": "I Wanna Be Yours", "listening_count": 2701361446},
    {"artist": "Post Malone", "title": "Circles", "listening_count": 2679958182},
    {"artist": "Taylor Swift", "title": "Cruel Summer", "listening_count": 2668725263},
    {"artist": "Drake", "title": "God's Plan", "listening_count": 2665550722},
    {"artist": "Macklemore", "title": "Can't Hold Us", "listening_count": 2661725492},
    {"artist": "Queen", "title": "Bohemian Rhapsody", "listening_count": 2659779520},
    {"artist": "Travis Scott", "title": "goosebumps", "listening_count": 2658360279},
    {"artist": "Ed Sheeran", "title": "Thinking out Loud", "listening_count": 2644957531},
    {"artist": "Billie Eilish", "title": "bad guy", "listening_count": 2640300245},
    {"artist": "Lord Huron", "title": "The Night We Met", "listening_count": 2633140680},
    {"artist": "Lady Gaga", "title": "Shallow", "listening_count": 2625319023},
    {"artist": "Justin Bieber", "title": "Love Yourself", "listening_count": 2618911985},
    {"artist": "Imagine Dragons", "title": "Thunder", "listening_count": 2585318825},
    {"artist": "The Weeknd", "title": "Die For You", "listening_count": 2569081427},
    {"artist": "John Legend", "title": "All of Me", "listening_count": 2558809927},
    {"artist": "Avicii", "title": "Wake Me Up", "listening_count": 2536464537},
    {"artist": "Imagine Dragons", "title": "Demons", "listening_count": 2523248174},
    {"artist": "The Weeknd", "title": "The Hills", "listening_count": 2506584671},
    {"artist": "Twenty One Pilots", "title": "Stressed Out", "listening_count": 2499719627},
    {"artist": "Coldplay", "title": "Viva La Vida", "listening_count": 2473716275},
    {"artist": "Bruno Mars", "title": "Just the Way You Are", "listening_count": 2443837942},
    {"artist": "J. Cole", "title": "No Role Modelz", "listening_count": 2439143165},
    {"artist": "Eminem", "title": "Without Me", "listening_count": 2437399370},
    {"artist": "Kendrick Lamar", "title": "HUMBLE.", "listening_count": 2429276399},
    {"artist": "The Killers", "title": "Mr. Brightside", "listening_count": 2426611328},
    {"artist": "Passenger", "title": "Let Her Go", "listening_count": 2424707741},
    {"artist": "Bruno Mars", "title": "When I Was Your Man", "listening_count": 2422561288},
    {"artist": "Ariana Grande", "title": "7 rings", "listening_count": 2421233758},
    {"artist": "Eminem", "title": "Lose Yourself", "listening_count": 2405578077},
    {"artist": "Arctic Monkeys", "title": "Do I Wanna Know?", "listening_count": 2401150329},
    {"artist": "Bruno Mars", "title": "That's What I Like", "listening_count": 2387019048},
    {"artist": "Bruno Mars", "title": "Locked out of Heaven", "listening_count": 2372314450},
    {"artist": "Linkin Park", "title": "In the End", "listening_count": 2367946694},
    {"artist": "Olivia Rodrigo", "title": "drivers license", "listening_count": 2355962386},
    {"artist": "Shawn Mendes", "title": "Treat You Better", "listening_count": 2355950637},
    {"artist": "The Police", "title": "Every Breath You Take", "listening_count": 2347892350},
    {"artist": "Miley Cyrus", "title": "Flowers", "listening_count": 2347707657},
    {"artist": "Calvin Harris", "title": "One Kiss", "listening_count": 2342231828},
    {"artist": "DJ Snake", "title": "Let Me Love You", "listening_count": 2334083644},
    {"artist": "French Montana", "title": "Unforgettable", "listening_count": 2328084920},
    {"artist": "Olivia Rodrigo", "title": "good 4 u", "listening_count": 2323719200},
    {"artist": "XXXTENTACION", "title": "SAD!", "listening_count": 2314802714},
    {"artist": "XXXTENTACION", "title": "Jocelyn Flores", "listening_count": 2300485754},
    {"artist": "Marshmello", "title": "Happier", "listening_count": 2296323727},
    {"artist": "Justin Bieber", "title": "Sorry", "listening_count": 2278696677},
    {"artist": "Travis Scott", "title": "SICKO MODE", "listening_count": 2267222367},
    {"artist": "Lil Uzi Vert", "title": "XO Tour Llif3", "listening_count": 2266885573},
    {"artist": "SZA", "title": "Kill Bill", "listening_count": 2257592370},
    {"artist": "Shawn Mendes", "title": "There's Nothing Holdin' Me Back", "listening_count": 2254502418},
    {"artist": "Major Lazer", "title": "Lean On", "listening_count": 2242163853},
    {"artist": "Nirvana", "title": "Smells Like Teen Spirit", "listening_count": 2231048975},
    {"artist": "Dua Lipa", "title": "New Rules", "listening_count": 2227511312},
    {"artist": "Elton John", "title": "Cold Heart", "listening_count": 2226447686},
    {"artist": "Dua Lipa", "title": "Levitating", "listening_count": 2216138404},
    {"artist": "Journey", "title": "Don't Stop Believin' (2022 Remaster)", "listening_count": 2209795879},
    {"artist": "Sam Smith", "title": "Too Good At Goodbyes", "listening_count": 2209637865},
    {"artist": "The Weeknd", "title": "Save Your Tears", "listening_count": 2202333090},
    {"artist": "Sam Smith", "title": "Stay With Me", "listening_count": 2202030765},
    {"artist": "Oasis", "title": "Wonderwall", "listening_count": 2198317283},
    {"artist": "Camila Cabello", "title": "Havana", "listening_count": 2188921975},
    {"artist": "Queen", "title": "Don't Stop Me Now", "listening_count": 2181828430},
    {"artist": "a-ha", "title": "Take on Me", "listening_count": 2161692207},
    {"artist": "Maroon 5", "title": "Memories", "listening_count": 2156812298},
    {"artist": "Mark Ronson", "title": "Uptown Funk", "listening_count": 2154471271},
    {"artist": "Halsey", "title": "Without Me", "listening_count": 2153967374},
    {"artist": "Adele", "title": "Someone Like You", "listening_count": 2147119101},
    {"artist": "Coldplay", "title": "The Scientist", "listening_count": 2129970489},
    {"artist": "Eminem", "title": "Till I Collapse", "listening_count": 2117887565},
    {"artist": "Jung Kook", "title": "Seven", "listening_count": 2115706367},
    {"artist": "Bad Bunny", "title": "DÁKITI", "listening_count": 2104348567},
    {"artist": "Lil Nas X", "title": "INDUSTRY BABY", "listening_count": 2103654527},
    {"artist": "Post Malone", "title": "Congratulations", "listening_count": 2086378426},
    {"artist": "Alan Walker", "title": "Faded", "listening_count": 2084418763},
    {"artist": "Guns N' Roses", "title": "Sweet Child O' Mine", "listening_count": 2083873294},
    {"artist": "Lewis Capaldi", "title": "Before You Go", "listening_count": 2078161189},
    {"artist": "Mike Posner", "title": "I Took A Pill In Ibiza", "listening_count": 2074494267},
    {"artist": "Lukas Graham", "title": "7 Years", "listening_count": 2070704296},
    {"artist": "The Goo Goo Dolls", "title": "Iris", "listening_count": 2066099819},
    {"artist": "Shawn Mendes", "title": "Stitches", "listening_count": 2066016972},
    {"artist": "Mariah Carey", "title": "All I Want for Christmas Is You", "listening_count": 2064819252},
    {"artist": "Roddy Ricch", "title": "The Box", "listening_count": 2064640868},
    {"artist": "Charlie Puth", "title": "We Don't Talk Anymore", "listening_count": 2057739364},
    {"artist": "Sam Smith", "title": "I'm Not The Only One", "listening_count": 2050644847},
]

# Fungsi iteratif untuk mencari lagu
def search_songs_iterative(songs, min_listeners):
    result = []
    for song in songs:
        if song["listening_count"] >= min_listeners:
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
    if songs[index]["listening_count"] >= min_listeners:
        result.append(songs[index])
    # Rekursif ke elemen berikutnya
    return search_songs_recursive(songs, min_listeners, index + 1, result)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/filter-songs", methods=["GET"])
def filter_songs():
    method = request.args.get("method", "iterative")
    min_listeners = int(request.args.get("min_listeners", 0))

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
            "execution_time": f"{execution_time:.6f} detik"
        }), 404

    return jsonify({
        "songs": result,
        "execution_time": f"{execution_time:.6f} detik"
    })

if __name__ == "__main__":
    app.run(debug=True)
