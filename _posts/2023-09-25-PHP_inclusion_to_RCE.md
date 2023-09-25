---
title: PHP inclusion to RCE
categories: [CTF, Cookie Hân Hoan, Write-Up]
tags: [web, write-up, ctf]     # TAG names should always be lowercase
---
## Tổng quan

- Để giải được bài này ta cần kiến thức về log poisoning, path traversal
- [`Kỹ thuật Log poisoning để khai thác lỗ hổng File Inclusion (securitydaily.net)`](https://securitydaily.net/0x03-file-inclusion-log-poisoning-code-execution/#:~:text=B%C3%A0i%20vi%E1%BA%BFt%20s%E1%BA%BD%20tr%C3%ACnh%20b%C3%A0y,v%C3%A0o%20t%E1%BB%87p%20tin%20nh%E1%BA%ADt%20k%C3%BD.)
- công cụ: burpsuite

## Phân tích bài

- Khi truy cập vào trang web, như thường lệ, ta test hết các chức năng của nó và nháy view-source, nhưng có vẻ không có thêm được thông tin gì.
- Ta biết được rằng khi bấm vào nút “what is ctf” ta thấy được trên url có 1 tham số là 
`?file=ctf.txt` đảo quanh lại thì chỉ có mỗi thằng này là khai thác được.
- đề cũng hint cho chúng ta là `../` đã bị filter thành `“”`
- dễ thôi, ta dùng `..././` là có thể bypass filter được.

<img src="/assets/writeup/cookie/PHP Inclusion to RCE/0.png">

- Sau khi biết trang web bị lỗi path-traversal ta tiếp tục khai thác nhưng có vẻ hơi bí, vì mục tiêu của bài này là RCE, chứ ko hẳn đơn thuần là tìm flag.txt được giấu.
- Trang web không có chỗ up file, không có thực thi được lệnh để curl ra ngoài cũng như không có thêm chỗ nào có thể khai thác được trừ url bị LFI.
- Lúc này đảo qua 1 chút khái niệm về `untrusted data` và kiến thức về `var/log/nginx/access.log`, áp dụng 2 cái này chúng ta sẽ sử dụng 1 kỹ thuật có tên là **Log Poisoning**
- chúng ta cần biết một chút về máy chủ và cơ chế ghi log của chúng. Một máy chủ web thường chứa một vài dịch vụ khác nhau như SSH, Apache, MySQL, FTP … Hầu hết các dịch vụ này đều có các tệp tin log và được lưu trữ ngay tại máy chủ. Đường dẫn và tên file log tùy thuộc vào hệ điều hành mà máy chủ đang chạy
- Làm thế nào để có thể khai thác các tệp tin nhật ký này? Tất cả các tệp tin nhật ký sẽ đều chứa thông tin về các hoạt động khác nhau, được thực hiện bởi một dịch vụ đang chạy trên hệ thống. Và nếu chúng ta có thể kiểm soát một vài thông tin trong đó, chúng ta có thể tiêm nhiễm các mã độc tùy ý. Việc chèn các mã độc từ xa kết hợp với lỗ hổng Local File Inclusion có thể dẫn đến hậu quả rất nghiêm trọng

<img src="/assets/writeup/cookie/PHP Inclusion to RCE/1.png">

- như hình trên, mình đã tận dũng lỗi LFI đễ có thể vào được thư mục varlog của web, sau đó mình tiến hành thực thi lệnh bằng cụm `&ext=&cmd=ls`
- mình tiêm untrusted data vào trường User-Agent `<?php system($_GET[’cmd’]) ?>`
- lúc này hàm var.log sẽ ghi phiên đăng nhập vào và thực thi mã php

<img src="/assets/writeup/cookie/PHP Inclusion to RCE/2.png">

- payload hoàn chỉnh lấy flag

`?file=ctf.txt..././..././..././..././..././var/log/nginx/access.log&ext&cmd=cat /flag91rEr.txt`

<img src="/assets/writeup/cookie/PHP Inclusion to RCE/3.png">
