from gradio_client import Client

def mygpt():
  try:
    print('関数の開始')
    
    # 受信したテキストを代入
    recieved_image_url = 'https://i.ibb.co/Kct0fWG/f2c78bc02587.jpg'
    print('受信したURL', recieved_image_url)

    # 解析の開始
    client = Client("votepurchase/DeepDanbooru")
    result = client.predict(
      recieved_image_url,
      0.5,
      api_name="/predict"
    )

    response = result[-1]

    # 結果の出力
    print(response)

  except Exception as e:
    print('error', e)
    return f'Error: {e}'