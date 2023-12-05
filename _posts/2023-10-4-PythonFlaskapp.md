---
title: Write-Up Play with python flask app
date: 2023-10-4 7:55:00 +0700
categories: [CTF, FIA-FPTU, Write-Up]
tags: [web, write-up, ctf]     # TAG names should always be lowercase
pin: true
---
# Play with python flask app
## **Tổng quan**

- Để giải được challenge này, ta cần vận dụng kiến thức về các lỗi bảo mật như
    - IDOR
    - SSTI
    - Crack JWT
    - Python
    - Kĩ thuật bypass login
- công cụ: Burpsuite, Webhook, Kali linux

## Phân tích bài

- Truy cập vào trang web, ta thấy giao diện login,

<img src="/assets/writeup/cookie/Play With python/Play with python flask app/0.png">
- Việc đầu tiên các bạn có thể dùng công cụ quét directory ẩn trên linux, tuy nhiên lần này mình dùng auto scan của burpsuite
    - Chuột phải, chọn Do active scan
        
<img src="/assets/writeup/cookie/Play With python/Play with python flask app/1.png">
        
    - phát hiện thư mục `/robots.txt`
    
<img src="/assets/writeup/cookie/Play With python/Play with python flask app/2.png">
    
- Truy cập vào ta tiếp tục phát hiện thêm `/backup`

<img src="/assets/writeup/cookie/Play With python/Play with python flask app/3.png">

- Tuy nhiên vì ko phải là FIA_Hacker nên ta đã bị chặn, hãy dùng burpsuite để bypass bằng cách thay đổi UserAgent

<img src="/assets/writeup/cookie/Play With python/Play with python flask app/4.png">

- Sau khi truy cập thì ta phát hiện mã nguồn của `/login`
- và tìm được đoạn đầu tiên của flag `# First part: [FIA{]`
    
<img src="/assets/writeup/cookie/Play With python/Play with python flask app/5.png">
    
- Kiểm tra mã nguồn và phân tích

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', error="")
    elif request.method == 'POST':  # string
        if len(request.values["username"]) >= 40:  # len(string) >= 40
            return render_template('login.html', error="Username is too long!")
        elif len(request.values["username"].upper()) <= 50:  # len(STRING) <= 50
            return render_template('login.html', error="Username is too short!")
        else:
            try:
                name = request.values["name"]
            except KeyError:
                name = request.values["username"]
            user = {
                "username": request.values["username"],
                "password": request.values["password"],
                "name": name,
                "balance": 1
            }
            access_token = create_access_token(
                identity=user, expires_delta=timedelta(hours=24))
            response = make_response(redirect(url_for('home')))
            response.set_cookie('access_token', access_token)
            return response
```

**Đoạn code thực hiện như sau:**

- Kiểm tra độ dài username, nếu >= 40 ký tự thì báo lỗi quá dài
- Kiểm tra độ dài username sau khi viết hoa, nếu <= 50 ký tự thì báo lỗi quá ngắn
- Lấy username và password từ request
- Tạo user object với các trường cần thiết
- Tạo access token dựa trên user object, hết hạn sau 24h
- Tạo response redirect tới `'/home'`
- Set cookie 'access_token' cho response

Tức là ở đây, ta chỉ cần thỏa điều kiện của username thì có thể đăng nhập được mà không cần quan tâm tới mật khẩu hoặc database. Tuy nhiên đọc qua yêu cầu thì có vẻ bất khả thi, lúc này mình tìm kiếm trên mạng thì phát hiện một số ký tự khi chuyển sang chữ hoa thì độ dài thay đổi 😗

- Ký tự đó chính là `'ß'` khi chuyển thành chữ hoa độ dài tăng gấp đôi từ 1 lên 2.
- Dùng 39 ký tự 'ß' làm username, vừa đủ điều kiện độ dài ban đầu, nhưng khi chuyển hoa thành 78 ký tự cũng vừa đủ điều kiện thứ 2.
- Dùng payload sau: `ßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßß` làm tên đăng nhập, password để là gì cũng được.

<img src="/assets/writeup/cookie/Play With python/Play with python flask app/6.png">

- Sau khi truy cập được vào, check source thì ta phát hiện được đoạn flag thứ 2

<img src="/assets/writeup/cookie/Play With python/Play with python flask app/7.png">

`<!-- Second part: [_e@sy_l0g1n_byp@$$] -→`

- Sau khi thử check qua toàn bộ chức năng của nó, có vẻ như mỗi chức năng sẽ ẩn giấu 1 flag và ta cần phải khai thác được toàn bộ lỗi của các chức năng đó, mình sẽ bắt đầu với phần

## `/secure_money_transfer VÀ /money_transfer`

<img src="/assets/writeup/cookie/Play With python/Play with python flask app/8.png">

- Có vẻ như việc ta làm là phải khiến cho số dư lớn hơn số trong hình, mình thử chuyển cho user 100 đồng thì báo thành công, tuy nhiên chuyện gì sẽ xảy ra nếu ta thử chuyển giá trị là âm?

<img src="/assets/writeup/cookie/Play With python/Play with python flask app/9.png">

- Lúc này mình thử ngay ý tưởng.

<img src="/assets/writeup/cookie/Play With python/Play with python flask app/10.png">

- kết quả là vẫn chuyển thành công.

<img src="/assets/writeup/cookie/Play With python/Play with python flask app/11.png">

- Mình thử sang phần `/money_transfer` thì thấy được rằng flag cũng đã hiện ✌🏼
    
<img src="/assets/writeup/cookie/Play With python/Play with python flask app/12.png">
    
- Tìm được flag thứ 3 là `[_f@ke]`và flag thứ 4 là `[_b3_r1ch]`

## `/**user/0**`

- Truy cập vào thì mình phát hiện được rằng ta có thể thay đổi `/user/0` thành `/1` hoặc `/2` để có thể xem được profile của các user khác nhau. Từ đó ta kết luận được rằng phần này đã bị lỗi IDOR (Insecure Direct Object Reference)

<img src="/assets/writeup/cookie/Play With python/Play with python flask app/13.png">

- Lúc này việc ta cần làm là dò xem trong các id user có id nào ta có thể khai thác được không, trong nhiều trường hợp thì userID đó sẽ chứa nhiều thông tin nhạy cảm hoặc userID đã bị xóa…
- Lúc này mình sẽ dùng chức năng Intruder của burpsuite để bruteforce tìm id user ẩn.

<img src="/assets/writeup/cookie/Play With python/Play with python flask app/14.png">

- Đầu tiên ta bôi đen số 1 và chọn add

<img src="/assets/writeup/cookie/Play With python/Play with python flask app/15.png">

- Sau đó chuyển qua tab Payloads và chỉnh như hình

<img src="/assets/writeup/cookie/Play With python/Play with python flask app/16.png">

- Chuyển tới tab setting, vì flag sẽ có dạng là `Second part: [flag nè]` , biết được luôn có chữ part ở trong, ta qua tab settings và chỉnh ở mục **Grep - Match** thêm vào chữ part

<img src="/assets/writeup/cookie/Play With python/Play with python flask app/17.png">

- Sau đó chọn Start Attack, kết quả sẽ được hiển thị như sau

<img src="/assets/writeup/cookie/Play With python/Play with python flask app/18.png">

- Như hình thì có vẻ như ID 1304 chính là id mà ta cần tìm !

<img src="/assets/writeup/cookie/Play With python/Play with python flask app/19.png">

- Kiểm tra respone trả về thì ta tìm được flag thứ 5 là `[_@and_IDOR]`

## `/whatismyname`

- Khi truy cập vào thì ta biết được trang web sẽ trả về tên của người dùng, lúc này ta thử dùng '{ { 7*7 } }' nhưng chèn vào tên, ta sẽ thay đổi tên thành như sau

<img src="/assets/writeup/cookie/Play With python/Play with python flask app/20.png">

- Lúc này flag sẽ xuất hiện
- Flag thứ 6 là **`[_ez_$$T1]`**

<img src="/assets/writeup/cookie/Play With python/Play with python flask app/21.png">

`/admin`

- Truy cập vào thì có vẻ như ta không có quyền vào

<img src="/assets/writeup/cookie/Play With python/Play with python flask app/22.png">

- Thử f12 thì mình tìm được Access_token của bài này.

<img src="/assets/writeup/cookie/Play With python/Play with python flask app/23.png">

- Sử dụng JWT để decode thì có vẻ như đây là 1 đoạn mã JSON, lúc này thì chúng ta cần tìm được secret_key để có thể khai thác lỗi này.

<img src="/assets/writeup/cookie/Play With python/Play with python flask app/24.png">

- Ta lưu accessToken vào 1 file `.txt` trên linux, và tiến hành tìm secretKey bằng hashcat với payload sau
    
    `hashcat -m 16500 -a 0 tuandeptrai.txt /usr/share/wordlists/rockyou.txt`
    
- Tìm được secretKey là `chamberofsecrets-vipera_evanesca`
- Tiến hành thay đổi và nhập accessToken mới

<img src="/assets/writeup/cookie/Play With python/Play with python flask app/25.png">

- Thay vào và reload trang admin

<img src="/assets/writeup/cookie/Play With python/Play with python flask app/26.png">

- Ta đã tìm được flag thứ 7 là `[_cr@ck_jwt]`

## **`/challenging_with_unbelievable_difficulty`**

- Khi truy cập vào thì đường dẫn báo lỗi, có vẻ như đường dẫn này không tồn tại

<img src="/assets/writeup/cookie/Play With python/Play with python flask app/27.png">

- Tuy nhiên sau khi test 1 lúc thì mình phát hiện trang web đã bị lỗi XSS, thử khai thác thêm lỗi này thì mình không tìm được gì T__T

<img src="/assets/writeup/cookie/Play With python/Play with python flask app/28.png">

- Thử test payload `{ { 7*7 } }` ở trên url để kiểm tra xem trang web có bị lỗi phổ biến của thằng Jinja không thì…

<img src="/assets/writeup/cookie/Play With python/Play with python flask app/29.png">

- Vậy là ta đã tìm được Flag cuối cùng là `[_h1dd3n_SSTI}]`

Kết hợp toàn bộ 8 flag ta được flag hoàn chỉnh là

`FIA{_e@sy_l0g1n_byp@$$_f@ke_b3_r1ch_@and_IDOR_ez_$$T1_cr@ck_jwt_h1dd3n_SSTI}`

DONEEEE!! bài dài vãi chuối …
