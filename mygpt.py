import os
from flask import Flask, request
from flask_cors import CORS
from gradio_client import Client, handle_file
from config import HF_TOKEN

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def main():
  try:
    print('関数の開始')
    
    # 受信したテキストを代入
    request_dict = request.get_json()
    recieved_image_url = str(request_dict['data'])
    print('受信したURL', recieved_image_url)

    # 解析の開始
    client = Client(
      "votepurchase/DeepDanbooru",
      token=HF_TOKEN
    )
    result = client.predict(
      image=handle_file(recieved_image_url),
      score_threshold=0.5,
      api_name="/predict"
    )
    print(result[-1])

    response = result[-1]

    # 結果の出力
    return response

  except Exception as e:
    print('error', e)
    return f'Error: {e}'
  
if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))