# 데이터 파트
from urllib.request import Request, urlopen
import json
import os
# 다운로드 기능(without_mask, with_mask, mask)

def download_image(kind):
    if kind == 'without_mask':
        api_url = 'https://api.github.com/repos/prajnasb/observations/contents/experiements/data/without_mask?ref=master'
        headers = {'User-Agent': 'Mozilla/5.0'}

        request = Request(api_url, headers=headers)
        response = urlopen(request)
        directory_bytes = response.read()
        directory_str = directory_bytes.decode('utf-8')

        contents = json.loads(directory_str)

        for i in range(len(contents)):
            content = contents[i]

            request = Request(content['download_url'])
            response = urlopen(request)
            image_data = response.read()

            if not os.path.exists('data'):
                os.mkdir('data')
            if not os.path.exists('data/without_mask'):
                os.mkdir('data/without_mask')

            image_file = open('data/without_mask/' + content['name'], 'wb')
            image_file.write(image_data)
            image_file.close()
            print('without_mask 다운로드중(' + str(i+1) + '/' + str(len(contents)) + '):' + content['name'])
        print('without_mask 이미지 다운로드 완료')
    elif kind == 'with_mask':
        pass
    elif kind == 'mask':
        pass


# 마스크 합성



# 데이터 생성
if __name__ == '__main__':
    download_image('without_mask')




