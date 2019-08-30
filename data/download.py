import urllib.request
import requests

def down():

    for i in range(5):
        url ='http://119.23.72.247:443/AllCard/?format=json&page={}'.format(i+1)
        datas = requests.get(url).json()['results']
        for  data in datas:
            print(data['card_image'])
            print((data['card_min_image']))
            # print()

            opener = urllib.request.build_opener()
            opener.addheaders = [('User-agent',
                                  'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10')]
            urllib.request.install_opener(opener)


            urllib.request.urlretrieve(data['card_image'], 'F:/HearthStone/media/card_image/{}'.format(data['card_image'].split('/')[-1]))
            urllib.request.urlretrieve(data['card_min_image'], 'F:/HearthStone/media/card_min_image/{}'.format(data['card_min_image'].split('/')[-1]))



if __name__ == '__main__':
   down()