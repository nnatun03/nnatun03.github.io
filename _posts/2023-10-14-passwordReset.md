---
title: Write-Up Password Reset
date: 2023-10-14 6:34:01 +0700
categories: [CTF, Cookie Hân Hoan, Write-Up]
tags: [web, write-up, ctf]     # TAG names should always be lowercase
pin: true
---

# Password Reset

## **Tổng quan**

- Để giải được challenge này, ta cần vận dụng kiến thức về Host Header Poisoning và cách sử dụng BurpSuite
- công cụ: Burpsuite, Request Catcher

## Phân tích bài

- Truy cập trang web với giao diện như sau, việc cần làm là ta sẽ test tất cả các chức năng của nó.

<img src="/assets/writeup/cookie/Password Reset/Untitled.png">
- Sau khi test, mình tiến hành tạo tài khoản và đăng nhập, mình được điều hướng tới `/dashboard` , lúc này mình thấy được mail của Admin là admin@example.com

<img src="/assets/writeup/cookie/Password Reset/Untitled 1.png">

- Thử vào phần `/Forgot Password` và test với mail của mình

<img src="/assets/writeup/cookie/Password Reset/Untitled 2.png">

- Ta thấy được đường link Reset mật khẩu

<img src="/assets/writeup/cookie/Password Reset/Untitled 3.png">

- Thử truy cập vào test thì mình có thể thay đổi được mật khẩu. Mình đúc kết được như sau:
1. Người dùng truy cập chức năng lấy lại mật khẩu. Nhập email sau đó nhấn nút gửi để yêu cầu trang web cấp lại mật khẩu.
2. Nếu email tồn tại trong hệ thống cơ sở dữ liệu. Hệ thống sẽ gửi một đường Secret Link có dạng **https : //website.com/password/reset?token=0a1b2c3d4e5f6g7h8i9** đến email của người dùng để đặt lại mật khẩu.
3. Sau khi người dùng mở Secret Link. Hệ thống biết đây chính là chủ sở hữu tài khoản đó và cho phép họ nhập mật khẩu mới.
4. Sau khi mật khẩu được thay đổi, Secret Link sẽ hết hạn và người dùng không thể truy cập lại được nữa.

---

- Vậy chuyện gì sẽ xảy ra nếu như ta thao túng, hoặc kiểm soát được đoạn token đó để truy cập vào tài khoản admin? Tiến hành giả thuyết của mình, mình truy cập vào `/Forgot password` và dùng Burp để bắt lại gói tin đó.

<img src="/assets/writeup/cookie/Password Reset/Untitled 4.png">

- Mình sử dụng 1 kĩ thuật có tên là ****HTTP Host Header Attacks****

Trong quá trình phát triển ứng dụng, để trang web có thể dễ dàng tương thích với bất kỳ domain nào. Lập trình viên thường sử dụng giá trị Host trong HTTP Request Header hoặc ($_SERVER[‘Host’] trong PHP) để làm phần domain trong Secret Link.

*`<a href="https://$_SERVER['HOST']/password/reset?token=$token">Set Your Password</a>`*

Khi người dùng truy cập `http://13.229.182.110:31137/` trên trình duyệt. Nó sẽ tạo ra một HTTP Request trong đó có chứa Host Header là `http://13.229.182.110:31137/` như miêu tả hình dưới. Máy chủ Web của Cookie Arena sẽ biết người dùng yêu cầu truy cập tới battle.cookiearena.org và điều hướng tài nguyên (mã nguồn PHP, static file,..) phù hợp để phục vụ.

<img src="/assets/writeup/cookie/Password Reset/Untitled 5.png">

Nhưng sẽ thế nào nếu như phía server hoàn toàn tin tưởng vào **Host** header do người dùng cung cấp, hoặc không kiểm tra đầy đủ giá trị của các **Host** header? Hacker có thể lợi dụng điểm này để thực hiện các cuộc tấn công **HTTP Host Header Attacks**, hoặc cụ thể hơn trong trường hợp này, mở ra hướng tấn công cho kỹ thuật **Password Reset Poisoning**.

- Tiến hành khai thác, mình sẽ dùng trang web Request Catcher để bắt lấy gói tin

<img src="/assets/writeup/cookie/Password Reset/Untitled 6.png">

- Thay đổi host thành tên miền mình vừa tạo và gửi đi gói tin

<img src="/assets/writeup/cookie/Password Reset/Untitled 7.png">

- Lúc này thì ta đã lấy được secret token, thay vào và đổi lại mật khẩu của admin

<img src="/assets/writeup/cookie/Password Reset/Untitled 8.png">

- 

<img src="/assets/writeup/cookie/Password Reset/Untitled 9.png">

- Đổi mật khẩu và tiến hành đăng nhập

<img src="/assets/writeup/cookie/Password Reset/Untitled 10.png">
