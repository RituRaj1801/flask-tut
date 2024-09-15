from flask import Flask, request, jsonify, render_template
import youtube_dl

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    try:
        data = request.get_json()
        video_url = data['url']

        # Logic for downloading the video
        ydl_opts = {
            'format': 'best',
            'outtmpl': './%(title)s.%(ext)s'
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        return jsonify({"message": "Download started!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
