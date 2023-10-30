---
title: Write-Up Just cat the flask full
date: 2023-10-4 7:55:00 +0700
categories: [CTF, UDCTF-2023, Write-Up]
tags: [web, write-up, ctf]     # TAG names should always be lowercase
---
# Just cat the flask full

- Truy cập vào trang web và nhận thấy

<img src="/assets/writeup/cookie/Just cat the flask full 100d3d03530f466b9d49ec1174aa24b2/Untitled.png">
- Thử thay đổi hi thành một kí tự khác

<img src="/assets/writeup/cookie/Just cat the flask full 100d3d03530f466b9d49ec1174aa24b2/Untitled 1.png">

- Vì đề bài là flask python nên mình sẽ test thử lỗi SSTI

<img src="/assets/writeup/cookie/Just cat the flask full 100d3d03530f466b9d49ec1174aa24b2/Untitled 2.png">

- Khai thác RCE

<img src="/assets/writeup/cookie/Just cat the flask full 100d3d03530f466b9d49ec1174aa24b2/Untitled 3.png">

<img src="/assets/writeup/cookie/Just cat the flask full 100d3d03530f466b9d49ec1174aa24b2/Untitled 4.png">

<img src="/assets/writeup/cookie/Just cat the flask full 100d3d03530f466b9d49ec1174aa24b2/Untitled 5.png">

- Đã xong flag1
- Tiếp tục khai thác flag thứ 2, lần này ta sẽ tập trung vào file sum_suckers_cred!

<img src="/assets/writeup/cookie/Just cat the flask full 100d3d03530f466b9d49ec1174aa24b2/Untitled 6.png">

- Truy cập vào thì mình biết được rằng sum_sucker_creds còn có 1 file shadow, thử đọc file đó thì mình phát hiện được thứ có vẻ như là tài khoản và mật khẩu, tuy nhiên mật khẩu ở đây đã được mã hóa

<img src="/assets/writeup/cookie/Just cat the flask full 100d3d03530f466b9d49ec1174aa24b2/Untitled 7.png">

- Mình sẽ dùng hashcat để giải mã, ở đây mình đoán file quan trọng sẽ là vip nên lấy để giải mã

<img src="/assets/writeup/cookie/Just cat the flask full 100d3d03530f466b9d49ec1174aa24b2/Untitled 8.png">

<img src="/assets/writeup/cookie/Just cat the flask full 100d3d03530f466b9d49ec1174aa24b2/Untitled 9.png">

<img src="/assets/writeup/cookie/Just cat the flask full 100d3d03530f466b9d49ec1174aa24b2/Untitled 10.png">
