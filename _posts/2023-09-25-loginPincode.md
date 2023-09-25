---
title: Write-Up PHP login pincode
date: 2023-09-17 12:34:01 +0700
categories: [CTF, Cookie Hân Hoan, Write-Up]
tags: [web, write-up, ctf]     # TAG names should always be lowercase
---
To unlock, enter the correct PIN. The PIN is a 4 digit number, ranging from 1000 to 1500. Use Burp Suite Intruder or any other tool like Hydra.

## Tổng quan

- Để giải được challenge này ta cần có kiến thức về brute-force và cách dùng intruder của burpsuite
- công cụ: burpsuite

## Phân tích bài

- Truy cập vào trang web ta thấy được giao diện nhập mã pin thông thường, không có gì đặc biệt nên ta view-source để kiếm thêm tí cháo

<img src="/assets/writeup/cookie/BABY LOGIN PINCODE/0.png">
- view source thì ta kiếm được mã nguồn ( quá đã :D )

<img src="/assets/writeup/cookie/BABY LOGIN PINCODE/1.png">

- đọc sơ qua thì thấy chả có gì đáng lưu ý, bài này giải cách đơn giản nhất là brute force cho tới khi có được mã pin chính xác mà thôi, vì số max=4 nên ta chỉ cần brute-force từ 0000-9999 :D, đọc mã nguồn thì cũng k thấy có limit range bla bla gì cả.
- Dùng burpsuite → send to intruder.
- nhớ bôi phần mình muốn brute-force sau đó chọn add thì sẽ ra được như hình ^^
 ( xóa chữ A đi nhé các cậu )

<img src="/assets/writeup/cookie/BABY LOGIN PINCODE/2.png">

- sau đó chuyển sang tab payload và chọn như hình

<img src="/assets/writeup/cookie/BABY LOGIN PINCODE/3.png">

- bấm start attack và đợi kết quả thôi!, lưu ý là nếu đăng nhập thành công thì thường length của nó sẽ nhiều hơn, vì hiển thị thêm 1 số chữ hoặc gì đó, sẽ khác nhau ở length nên hãy bấm vào để nó sort ra cái length dài nhất và nhập thôi

<img src="/assets/writeup/cookie/BABY LOGIN PINCODE/4.png">

<img src="/assets/writeup/cookie/BABY LOGIN PINCODE/5.png">

**DONEEEEE!**
