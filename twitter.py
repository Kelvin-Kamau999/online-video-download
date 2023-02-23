import requests
from bs4 import BeautifulSoup
from pathlib import Path

# github.com/erfanhs

# download with twittervideodownloader.com
class Downloader:

    def __init__(self, output_dir='./output/'):
        
        output_dir = Path(output_dir)
        Path.mkdir(output_dir, parents = True, exist_ok = True)
        self.output_dir = str(output_dir)
        
        self.session = requests.Session()
        self.csrf = self.session.get('http://twittervideodownloader.com').cookies['csrftoken']


    def download_video(self, tweet_url):
    
        tweet_url = tweet_url.split('?', 1)[0]

        result = self.session.post('http://twittervideodownloader.com/download', data={'tweet': tweet_url, 'csrfmiddlewaretoken': self.csrf})
        
        if result.status_code == 200:
        
            bs = BeautifulSoup(result.text, 'html.parser')
            video_element = bs.find('a', string='Download Video')
            
            if video_element is None:
                print('video not found !')
            else:
                video_url = video_element['href']
                tweet_id = tweet_url.split('/')[-1]
                fname = tweet_id + '.mp4'
                
                download_result = self.session.get(video_url, stream = True) 
                with open(Path(self.output_dir) / Path(fname), 'wb') as video_file:
                    for chunk in download_result.iter_content(chunk_size=1024*1024):
                         # writing one chunk at a time to video file 
                         if chunk:
                             video_file.write(chunk)
                    video_file.close()
        else:
            print('an error in downloading video! status code: ' + result.status_code)