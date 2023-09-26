---
title: Write-Up Go around a Webpage
date: 2023-09-26 3:55:00 +0700
categories: [CTF, FIA-FPTU, Write-Up]
tags: [web, write-up, ctf]     # TAG names should always be lowercase
---
# Go around a Webpage

A simple website to go around and learn the basics

## Tổng quan

- Để giải được bài này ta cần kiến thức về Recon
- công cụ: Burpsuite, FFUF ( hoặc công cụ scan dirb ẩn bất kì )

## Phân tích bài

- Truy cập vào trang web việc đầu ta làm là test các chức năng của nó ( ở đây chả có vẹo gì :)) )

<img src="/assets/writeup/cookie/Go around a Webpage/0.png">
- Thử view-source xem có gì không

<img src="/assets/writeup/cookie/Go around a Webpage/1.png">

- cũng không có gì để khai thác ở đây, có vẻ như trang này chỉ dùng để giới thiệu và vẽ vẽ đẹp đẹp các kiểu 😀, vì vậy lúc này ta cần phải kiểm tra xem liệu rằng trang web này có đường dẫn nào khác sau nó không? truy tìm các subdomain hoặc parameter hay dirb ẩn.
- mình sử dụng FFUF

Payload: `ffuf -w common.txt.1 -u https://hackerpage.fiahackingisfun.id.vn/FUZZ -fc 403`

<img src="/assets/writeup/cookie/Go around a Webpage/2.png">

- phát hiện ra thư mục robots.txt, thử truy cập vào thì ta được thêm 1 dirb ẩn đó chính là `/Super_Secret_Page/`

<img src="/assets/writeup/cookie/Go around a Webpage/3.png">

- thử truy cập vào `/Super_Secret_Page/` thì ta biết được rằng trang web chỉ có thể truy cập được khi bạn đã login, và 1 dòng command có liên quan đến backup.

<img src="/assets/writeup/cookie/Go around a Webpage/4.png">

- lúc này ta có thêm 2 hướng để tiếp tục khai thác bài này
    1. tìm form login để đăng nhập và vào được `/Super_Secret_Page/`
    2. tìm server backup của trang web

---

1. **Tìm form login để đăng nhập và vào được `/Super_Secret_Page/`**
- Mình bắt đầu với hướng 1 trước, mình sẽ tìm form login của bài này, chúng ta tiếp tục sử dụng FFUF, tuy nhiên lần này ta sẽ không scan ở [`https://hackerpage.fiahackingisfun.id.vn/`](https://hackerpage.fiahackingisfun.id.vn/FUZZ)
- mà thay vào đó ta scan tiếp ở `https://hackerpage.fiahackingisfun.id.vn/Super_Secret_Page/FUZZ`

<img src="/assets/writeup/cookie/Go around a Webpage/5.png">

- tìm được `/development` thử truy cập vào thì hiện ra thông báo như sau

<img src="/assets/writeup/cookie/Go around a Webpage/6.png">

- ta F12 và chỉnh sửa cookies thành 1 là sẽ vào được form login.

<img src="/assets/writeup/cookie/Go around a Webpage/7.png">

<img src="/assets/writeup/cookie/Go around a Webpage/8.png">

- nhìn form login mình liên tưởng đến phương pháp như SQLi hay XSS… tuy nhiên trong bài này vì được hint là không có database nên mình tiếp tục đánh vào ý 2, đó là server backup, khả năng cao là tài khoản và mật khẩu đăng nhập sẽ ở đó.

1. **Tìm form server backup của trang web**
- mình đã thử dirb scan nhiều đường dẫn như
    - `/Super_Secret_Page/development/FUZZ`
    - `/Super_Secret_Page/FUZZ/`
    - etc
- nhưng vẫn không tìm được, lúc này mình searching trên google về backup file thì biết được rằng server sẽ có lưu 1 dạng file backup dưới dạng `.bak` hoặc `~`

<img src="/assets/writeup/cookie/Go around a Webpage/9.png">

- thử test trên đường dẫn

`https://hackerpage.fiahackingisfun.id.vn/Super_Secret_Page/index.html.bak`

<img src="/assets/writeup/cookie/Go around a Webpage/10.png">

- tìm được tài khoản và mật khẩu, tuy nhiên mật khẩu đã bị mã hóa, lúc này ta chỉ cần giải ra thì sẽ được tài khoản và mật khẩu là `whoami/admin`
- tiến hành đăng nhập và mình nhận được thông báo như sau

<img src="/assets/writeup/cookie/Go around a Webpage/11.png">

- có vẻ như trình duyệt đã giớn hạn chỉ có FIA_Member browser mới được truy cập vào site này.
- ta sử dụng burpsuite và chức năng send to repeater của nó để thay đổi nội dung gói tin chuyển đi, ta tận dụng field `User-Agent` chứa **untrusted data** để thay đổi nội dung của nó thành `FIA_Member`

<img src="/assets/writeup/cookie/Go around a Webpage/12.png">

- cuối cùng ta nhận được 1 đoạn mã base64, nhưng nội dung lại là final part của flag? vậy phần đầu nó nằm ở đâu?
- đoạn này loay hoay khá lâu, tuy nhiên nếu ta check kĩ tab network thì sẽ thấy được rằng thông qua phương thức GET server đã nhận về 1 gói tin chứa đoạn base64 đầu tiên.

<img src="/assets/writeup/cookie/Go around a Webpage/13.png">

- kết hợp 2 đoạn base 64 đó ta sẽ lấy được flag

<img src="/assets/writeup/cookie/Go around a Webpage/14.png">

- **DONEEEEE!**
