# Just cat the flask full

- Truy cập vào trang web và nhận thấy

![Untitled](Just%20cat%20the%20flask%20full%20100d3d03530f466b9d49ec1174aa24b2/Untitled.png)

- Thử thay đổi hi thành một kí tự khác

![Untitled](Just%20cat%20the%20flask%20full%20100d3d03530f466b9d49ec1174aa24b2/Untitled%201.png)

- Vì đề bài là flask python nên mình sẽ test thử lỗi SSTI

![Untitled](Just%20cat%20the%20flask%20full%20100d3d03530f466b9d49ec1174aa24b2/Untitled%202.png)

- Khai thác RCE

![Untitled](Just%20cat%20the%20flask%20full%20100d3d03530f466b9d49ec1174aa24b2/Untitled%203.png)

![Untitled](Just%20cat%20the%20flask%20full%20100d3d03530f466b9d49ec1174aa24b2/Untitled%204.png)

![Untitled](Just%20cat%20the%20flask%20full%20100d3d03530f466b9d49ec1174aa24b2/Untitled%205.png)

- Đã xong flag1
- Tiếp tục khai thác flag thứ 2, lần này ta sẽ tập trung vào file sum_suckers_cred!

![Untitled](Just%20cat%20the%20flask%20full%20100d3d03530f466b9d49ec1174aa24b2/Untitled%206.png)

- Truy cập vào thì mình biết được rằng sum_sucker_creds còn có 1 file shadow, thử đọc file đó thì mình phát hiện được thứ có vẻ như là tài khoản và mật khẩu, tuy nhiên mật khẩu ở đây đã được mã hóa

![Untitled](Just%20cat%20the%20flask%20full%20100d3d03530f466b9d49ec1174aa24b2/Untitled%207.png)

- Mình sẽ dùng hashcat để giải mã, ở đây mình đoán file quan trọng sẽ là vip nên lấy để giải mã

![Untitled](Just%20cat%20the%20flask%20full%20100d3d03530f466b9d49ec1174aa24b2/Untitled%208.png)

![Untitled](Just%20cat%20the%20flask%20full%20100d3d03530f466b9d49ec1174aa24b2/Untitled%209.png)

![Untitled](Just%20cat%20the%20flask%20full%20100d3d03530f466b9d49ec1174aa24b2/Untitled%2010.png)