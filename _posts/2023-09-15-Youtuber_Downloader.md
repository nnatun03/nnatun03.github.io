---
title: Write-Up Youtuber Downloader
date: 2023-09-17 12:34:01 +0700
categories: [CTF, Cookie Hân Hoan, Write-Up]
tags: [web, write-up, ctf]     # TAG names should always be lowercase
---
---
Youtube Downloader là công cụ giúp bạn tải video từ Youtube về máy tính miễn phí. Nếu hack được ứng dụng này, bạn sẽ nắm trong tay công nghệ tải video của các website Youtube Downloader trên thế giới.


## Tổng quan:

- bài này thuộc dạng cmd injection
- sử dụng payload ở: ` [`PayloadAllTheThings/Command_Injection`](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Command%20Injection#bypass-without-space)` (tìm kiếm ở phần bypass without space ^^)
- công cụ: Burpsuite

## Phân tích bài

- khi vào bài, ta thấy được trang web này chỉ có chức năng duy nhất là curl, check viewsource thì cũng ko có thêm thông tin hay mã nguồn gì.

<img src="/assets/writeup/cookie/Youtube Downloader/0.png">

- thử curl bất kì, mình thường dùng google.com =))

<img src="/assets/writeup/cookie/Youtube Downloader/1.png">

- sau khi curl xong ta cũng không có thêm nhiều thông tin gì, vì goal của bài này là command injection, ta thử test 1 số payload vào xem như thế nào, có thể test nhiều payload như:
    
    `original_cmd_by_server; ls`
    
    `original_cmd_by_server && ls`
    
    `original_cmd_by_server | ls`
    
    `original_cmd_by_server || ls`
    
- test được 1 lúc thì mình phát hiện ra rằng bài này đã filter mất dấu “space” (khoảng trắng ấy), nên mục tiêu tối thượng bây giờ là làm cách nào để bypass được filter?, vì không đọc được mã nguồn nên mình thử nhiều cách như dùng URL encode, base64, decode…. sau 1 lúc tra cứu thì mình tìm được 1 cách đó là ${IFS}
    
<img src="/assets/writeup/cookie/Youtube Downloader/2.png">
    
- hiểu nôm na thì ${IFS} dùng để thay kí tự khoảng trắng, từ lúc này thì ta dùng payload sau để bypass được bài này
    
    `?url=https://www.google.com/;ls${IFS}/`
    

<img src="/assets/writeup/cookie/Youtube Downloader/3.png">

    `?url=https://www.google.com/;cat${IFS}/flag.txt`

<img src="/assets/writeup/cookie/Youtube Downloader/4.png">

- Vậy là xong bài rồi đóa 🕺🏼
