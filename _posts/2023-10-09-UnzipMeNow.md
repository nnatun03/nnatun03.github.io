---
title: Write-Up Unzip me now
date: 2023-10-09 2:44:01 +0700
categories: [CTF, Cookie Hân Hoan, Write-Up]
tags: [web, write-up, ctf]     # TAG names should always be lowercase
---
# Unzip me now

## **Tổng quan**

- Để giải được challenge này, ta cần vận dụng kiến thức về lỗi bảo mật Path-Traversal hoặc sử dụng Symlink
- công cụ: Burpsuite, Kali linux

## Phân tích bài

- Truy cập và test thử chức năng của bài mình đúc kết được một số ý như sau
    - Chỉ có thể up file với đuôi là .zip
    - Trừ code php ra thì các đuôi như txt, .py , pdf đều sẽ được giải nén và hoạt động bình thường

<img src="/assets/writeup/cookie/Unzip me now/Unzip me now/0.png">
- Lúc này mình thử zip đoạn code python lại và up lên và mình phát hiện trang web đang có đường dẫn lưu tệp tin như sau
    
    `/view_folder/1696759588/mona.py`
    

<img src="/assets/writeup/cookie/Unzip me now/Unzip me now/1.png">

- Mình thử test với payload `/view_folder/1696759588/../../../../../etc/passwd` xem có bị pathTraversal không thì có vẻ không hiệu quả

<img src="/assets/writeup/cookie/Unzip me now/Unzip me now/2.png">

- Trang web sẽ ngay lập tức điều hướng về như ảnh trên, tuy nhiên nếu như mình test ở trong BurpSuite thì mới phát hiện ra trang web bị pathTraversal, điều này làm mình bị chệch hướng @@ dẫn đến việc mình làm bằng cách 2 đó là symlink sẽ đề cập bên dưới.

<img src="/assets/writeup/cookie/Unzip me now/Unzip me now/3.png">

- Không hiểu bài lỗi hay sao nhưng mình dùng lỗi pathTraversal để đọc flag luôn vẫn được @@ vì đề cho biết flag được cất ở `/flag.txt`
- payload: `/view_folder/1696759588/../../../../../flag.txt`

<img src="/assets/writeup/cookie/Unzip me now/Unzip me now/4.png">

- Cách 2 mình sử dụng đó là symlink hay còn gọi là kĩ thuật symbolic link attack.
- Để giải thích nhanh thì:
    - Liên kết mềm (symbolic link) là một loại file đặc biệt trỏ tới một file hoặc thư mục khác trong hệ thống. ( khá giống cách mà shortcut hoạt động)
    - Kẻ tấn công có thể tạo liên kết mềm trỏ tới các file/thư mục nhạy cảm mà họ không có quyền truy cập bình thường.
    - Sau đó họ sử dụng liên kết mềm này để đọc/ghi trái phép vào file hoặc thư mục mục tiêu.
    - Điều này cho phép họ lách qua cơ chế phân quyền của hệ thống.
- Mình sẽ dùng kali linux để tạo 1 symbolic link

<img src="/assets/writeup/cookie/Unzip me now/Unzip me now/5.png">

- `ln -s /flag.txt link_to_flag` dùng để tạo 1 symbolic link tới thư mục `/flag.txt`
- `zip -y hack.zip link_to_flag` dùng để nén lại thành file zip.
- Sau đó ta tiến hành gửi file zip này lên hệ thống, lúc này hệ thống sẽ giải nén thư mục này và thực thi symlink mà ta gửi đến, thứ mà đang trỏ tới `/flag.txt`
- Sau khi upload,  ta bấm vào và tải về file flag.txt

<img src="/assets/writeup/cookie/Unzip me now/Unzip me now/6.png">

<img src="/assets/writeup/cookie/Unzip me now/Unzip me now/7.png">

Done 2 cách xD
