# my-gpt

画像 URL を受け取り、[DeepDanbooru](https://huggingface.co/spaces/votepurchase/DeepDanbooru) でアニメ画像のタグを返す Flask API。GCP Cloud Run で動作する。

## エンドポイント

### `POST /`

**リクエスト**

```json
{
  "data": "https://example.com/image.png"
}
```

**レスポンス**

```
rating:safe, 1girl, brown_hair, long_hair, ...
```

## ローカル開発

```bash
pip install -r requirements.txt
python mygpt.py
```

## デプロイ

```bash
gcloud run deploy
```

## 設定

`config.py`（git 管理外）に HuggingFace トークンを定義する。

```python
HF_TOKEN = "hf_xxxx..."
```
