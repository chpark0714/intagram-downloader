from flask import Flask, render_template, request, jsonify
import instaloader
import os

app = Flask(__name__)

class InstagramDownloader:
    def __init__(self):
        self.download_base_path = os.path.join(os.getcwd(), 'downloads')
        self.loader = instaloader.Instaloader(
            download_videos=False,
            download_video_thumbnails=False,
            download_geotags=False,
            download_comments=False,
            save_metadata=False,
            compress_json=False,
            post_metadata_txt_pattern=''
        )
    
    def download(self, username):
        try:
            profile = instaloader.Profile.from_username(self.loader.context, username)
            
            if profile.is_private:
                return {"success": False, "message": "비공개 계정입니다"}
            
            download_path = os.path.join(self.download_base_path, username)
            if not os.path.exists(download_path):
                os.makedirs(download_path)
            
            total_posts = profile.mediacount
            downloaded = 0
            
            for post in profile.get_posts():
                self.loader.download_post(post, download_path)
                downloaded += 1
                
            return {
                "success": True, 
                "message": "다운로드 완료!", 
                "path": download_path,
                "total": downloaded
            }
            
        except Exception as e:
            return {"success": False, "message": str(e)}

downloader = InstagramDownloader()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    username = request.form.get('username')
    if not username:
        return jsonify({"success": False, "message": "사용자명을 입력하세요"})
    
    try:
        profile = instaloader.Profile.from_username(downloader.loader.context, username)
        if profile.is_private:
            return jsonify({"success": False, "message": "비공개 계정입니다"})
        return jsonify({"success": True, "total_posts": profile.mediacount})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

@app.route('/start_download', methods=['POST'])
def start_download():
    username = request.form.get('username')
    if not username:
        return jsonify({"success": False, "message": "사용자명을 입력하세요"})
    
    result = downloader.download(username)
    if result["success"]:
        return jsonify({
            "success": True, 
            "message": "다운로드 완료!", 
            "path": result["path"],
            "total": result["total"]
        })
    return jsonify(result)

if __name__ == '__main__':
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    app.run(debug=True)
