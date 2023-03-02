import json
from elasticsearch import Elasticsearch

# Elasticsearchインスタンスを作成
es = Elasticsearch(
    'https://datasearchj-es.kasys.org/',
    basic_auth=('kasys', 'Kasys20191201')
)
#マッピング情報の取得
response = es.indices.get_mapping(index="kdb_20221002")

with open('data/posts/index.json', 'w+') as f:
    json.dump(response, f)
# レスポンスの整形
print(json.dumps(response, indent=2))