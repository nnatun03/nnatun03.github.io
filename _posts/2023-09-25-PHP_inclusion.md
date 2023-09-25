---
title: Write-Up PHP inclusion
date: 2023-09-17 12:34:01 +0700
categories: [CTF, Cookie Hân Hoan, Write-Up]
tags: [web, write-up, ctf]     # TAG names should always be lowercase
---
Flag is hidden in /www/uploads/flag.php, please find a way to read the contents of this file

## Tổng quan

- Để giải được challenge này ta cần có kiến thức về ngôn ngữ PHP cũng như LFI (Local File Inclusion) và Wrappers
- công cụ: burpsuite

## Phân tích bài

- truy cập vào trang web, đập vào mặt là cái page trống hoặc như thế này, việc đầu tiên cần làm như thường lệ, nháy view-source để kiếm ăn, và test các chức năng của web.

<img src="/assets/writeup/cookie/PHP INCLUSION/0.png">
- Vọc 1 lúc thì ở phần list, có file flag và hello.json tuy nhiên không thể xem được flag vì đã có 1 lớp filter (phần này các bạn đọc mã nguồn mà đề cung cấp giúp mình )

<img src="/assets/writeup/cookie/PHP INCLUSION/1.png">

• sau tầm nửa ngày vật vã với cái challenge này thì mình đúc kết ra được 1 điều rằng là không dùng bất kì cách path-traversal hay LFI bình thường nào mà giải được cả :) mặc dù nó đã bị path-traversal ở đoạn này.

<img src="/assets/writeup/cookie/PHP INCLUSION/2.png">

- lúc này chúng ta phải biết đến khái niệm wrappers trong PHP nói chung và linux nói riêng

<img src="/assets/writeup/cookie/PHP INCLUSION/3.png">

- vọc cheat sheet thì ta có 1 số case mẫu như sau:

<img src="/assets/writeup/cookie/PHP INCLUSION/4.png">

- áp dụng vào challenge trên, ta có payload như sau, tuy nhiên ở đây mình đã bọc thêm base64 vào

payload: `php://filter/convert.base64-encode/resource=file:///www/uploads/flag`

<img src="/assets/writeup/cookie/PHP INCLUSION/5.png">

- Lưu ý, để dùng được wrapper trong challenge này, phải sử dụng nó ở lớp `/index`

<img src="/assets/writeup/cookie/PHP INCLUSION/6.png">

- bởi vì trong mã nguồn ta có thể thấy được rằng có 1 lỗi dẫn đến LFI ở dòng 25

<img src="/assets/writeup/cookie/PHP INCLUSION/7.png">

<img src="/assets/writeup/cookie/PHP INCLUSION/8.png">

- Bạn có thể tham khảo chat GPT nếu bạn chưa hiểu bản chất của lỗi sau.
