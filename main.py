import requests
import json

url = 'https://datasearchj-es.kasys.org/exp_vector_search/_search'
res = requests.get(url, stream=True)

data = json.loads(res.text)
hits = data['hits']['hits']
sub_list = []
for hit in hits:
    sub_list.append(hit['_source'])
with open('data/posts/posts.json', encoding='utf-8', mode='w+') as f:
    json.dump(sub_list, f, indent=2)