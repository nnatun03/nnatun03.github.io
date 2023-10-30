---
title: Write-Up SUPER ADMIN
date: 2023-10-4 7:55:00 +0700
categories: [CTF, UDCTF-2023, Write-Up]
tags: [web, write-up, ctf]     # TAG names should always be lowercase
---
# SUPER ADMIN

Truy cập vào trang web thì ta thấy 

<img src="/assets/writeup/cookie/SUPER ADMIN 267bf800aea44a9fbad0a1895d581b7b/Untitled.png">

- Test 1 lúc thì có vẻ như ta cần phải đăng nhập với QUYỀN admin thì mới có thể xem được flag, và flag được dấu ở /profile

<img src="/assets/writeup/cookie/SUPER ADMIN 267bf800aea44a9fbad0a1895d581b7b/Untitled 1.png">

- Dùng burp thì ta thấy được cookie, mình dùng JWT,io để xem thử định dạng của nó

<img src="/assets/writeup/cookie/SUPER ADMIN 267bf800aea44a9fbad0a1895d581b7b/Untitled 2.png">

- Việc của ta lúc này là tìm được secret-key và thay đổi lại role thành admin
- Mình sẽ dùng hashcat để tìm secret-key

payload hashcat: `hashcat -m 16500 -a 0 jwt_token.txt /usr/share/wordlists/rockyou.txt`

<img src="/assets/writeup/cookie/SUPER ADMIN 267bf800aea44a9fbad0a1895d581b7b/Untitled 3.png">

- Có secret key là password1 mình sẽ tiến hành modify lại jwt token và thay vào cookie

<img src="/assets/writeup/cookie/SUPER ADMIN 267bf800aea44a9fbad0a1895d581b7b/Untitled 4.png">

<img src="/assets/writeup/cookie/SUPER ADMIN 267bf800aea44a9fbad0a1895d581b7b/Untitled 5.png">
