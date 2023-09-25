---
title: Write-Up Be Positive
date: 2023-09-17 12:34:01 +0700
categories: [CTF, Cookie Hân Hoan, Write-Up]
tags: [web, write-up, ctf]     # TAG names should always be lowercase
---
Libra Dnuf Marketplace
Libra Dnuf is known underground as a marketplace to sell sensitive information and lost secrets. This place has long closed registration but only allows reputable members to exchange items. During a reconnaissance, 0x1115 team caught the exchange of two members codenamed alice and bob.
After analyzing the packets, 0x1115 was able to decrypt the passwords for alice and bob that matched the usernames. With this loophole, the analysis team continues to detect the Transfer Function between users after passing the authentication portal.
To avoid wake a sleeping dog, 0x1115 quickly took a snapshot of Libra Dnuf market and transferred it to CookieArena for investigation to find the important file in the flag package. We also recommend to be careful with the rollback option, because using this function all data will be reset to its original state.

## Tổng quan

- Để giải được challenge này không khó, vấn đề là mình có nhìn ra được bản chất không :D, xưa làm bài này mình cứ đâm đầu vào SQLi, hay fileupload để kiếm tài khoản admin chuyển tiền thêm =)))
- công cụ: burpsuite

## Phân tích bài

- Truy cập vào trang web, ta thấy được 1 form login, đề bài đã cho ta 2 account là bob và alice, thử đăng nhập vào xem có gì hay :D

<img src="/assets/writeup/cookie/Be Positive/0.png">
- sau khi đăng nhập vào (alice) ta thấy được rằng có 1 số chức năng…. ( đọc đề đi lười ghi quá)

<img src="/assets/writeup/cookie/Be Positive/1.png">

- mục tiêu của bài này có vẻ như là ta phải mua được flag ( giá 3001$), tuy nhiên cả 2 account của ta chỉ có tổng cộng 3000$? , thôi thì thử chuyển tiền sang bob xem sao

<img src="/assets/writeup/cookie/Be Positive/2.png">

- sau khi chuyển tiền xong, ta dùng burpsuite bắt lại gói tin, thật ra bài này đọc đề bài là mình đã liên tưởng đến việc dùng số âm rồi ( be positive mà), nên ta dùng chức năng Repeater của burp để chuyển lại thêm lần nữa

<img src="/assets/writeup/cookie/Be Positive/3.png">

- thử chuyển bằng số âm thì BOMMM, vẫn chuyển được :D, lúc này có vẻ như bob mất -99999

<img src="/assets/writeup/cookie/Be Positive/4.png">

- Sau đó thì mua flag thôi :D, bài này khá dễ nếu nhìn đúng trọng tâm

<img src="/assets/writeup/cookie/Be Positive/5.png">
