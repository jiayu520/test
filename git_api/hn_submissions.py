import requests

from operator import itemgetter

#执行API调用并存储响应

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Status Code:',r.status_code)

#处理有关每篇文章的信息

submissio_ids = r.json()
submissio_dicts = []
for submissio_id in submissio_ids[:30]:
    #对于没篇文章，都执行一个API调用
    url = 'https://hacker-news.firebaseio.com/v0/item/' + str(submissio_id) +'.json'
    submissio_r = requests.get(url)
    print(submissio_r.status_code)
    response_dict = submissio_r.json()


    submission_dict = {
        'title': response_dict['title'],
        'link': 'https://hacker-news.firebaseio.com/v0/item?id=' + str(submissio_id),
        'comments': response_dict.get('descendants',0)
    }

    submissio_dicts.append(submission_dict)
    submissio_dicts = sorted(submissio_dicts,key=itemgetter('comments'),reverse=True)

for submission_dict in submissio_dicts:
    print("\nTitle",submission_dict['title'])
    print("Discussion link",submission_dict['link'])
    print('Comments',submission_dict['comments'])