---
title: Write-Up File Download
date: 2023-09-17 12:34:01 +0700
categories: [CTF, Cookie Hân Hoan, Write-Up]
tags: [web, write-up, ctf]     # TAG names should always be lowercase
---
You can upload and download file. Try to get the /flag.txt

## Tổng quan

- Để giải được challenge này, ta cần vận dụng kiến thức về pathtraversal
- công cụ: trình duyệt thông thường

## Phân tích bài

- Truy cập vào trang web ta thấy trang web chỉ có chức năng upload

<img src="/assets/writeup/cookie/FILE DOWNLOAD/0.png">
- truy cập vào phần upload, ta thấy 1 số field để điền, lúc này mình thử test XSS hoặc HTML injection nhưng có vẻ như config của server sẽ auto chuyển nó thành dạng txt

<img src="/assets/writeup/cookie/FILE DOWNLOAD/1.png">

- đã bị convert thành txt, tuy nhiên ta thấy parameter của trang web nhìn rất là ảo, khả năng cao bị path traversal nên ta thử khai thác

<img src="/assets/writeup/cookie/FILE DOWNLOAD/2.png">

- thử payload: `../../../etc/passwd`

<img src="/assets/writeup/cookie/FILE DOWNLOAD/3.png">

- vậy là đã bị lỗi path trarvelsal, lúc này ta chỉ cần đổi payload thành `../../../flag.txt`

<img src="/assets/writeup/cookie/FILE DOWNLOAD/4.png">

- Bài nhẹ nhàng giải trí ăn sáng cho ae <(”)
