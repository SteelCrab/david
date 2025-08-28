# david
## 반달곰 커피 홈페이지
[AWS](https://aws.amazon.com/ko/)

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Amazon_Web_Services_Logo.svg/1200px-Amazon_Web_Services_Logo.svg.png" width="100" alt="AWS Logo">

* 오디오 출력 소스코드
  ```python
    lang = request.args.get('lang', DEFAULT_LANG)
    fp = BytesIO()
    gTTS(text, "com", lang).write_to_fp(fp)
    encoded_audio_data = base64.b64encode(fp.getvalue())
  ```

  #  이미지
  ![](images/image.png)
  # 사이즈 100x100
    <img src="images/image.png" width="100" height="100" alt="작은 이미지">