# SUPER ADMIN

Truy cập vào trang web thì ta thấy 

![Untitled](SUPER%20ADMIN%20267bf800aea44a9fbad0a1895d581b7b/Untitled.png)

- Test 1 lúc thì có vẻ như ta cần phải đăng nhập với QUYỀN admin thì mới có thể xem được flag, và flag được dấu ở /profile

![Untitled](SUPER%20ADMIN%20267bf800aea44a9fbad0a1895d581b7b/Untitled%201.png)

- Dùng burp thì ta thấy được cookie, mình dùng JWT,io để xem thử định dạng của nó

![Untitled](SUPER%20ADMIN%20267bf800aea44a9fbad0a1895d581b7b/Untitled%202.png)

- Việc của ta lúc này là tìm được secret-key và thay đổi lại role thành admin
- Mình sẽ dùng hashcat để tìm secret-key

payload hashcat: `hashcat -m 16500 -a 0 jwt_token.txt /usr/share/wordlists/rockyou.txt`

![Untitled](SUPER%20ADMIN%20267bf800aea44a9fbad0a1895d581b7b/Untitled%203.png)

- Có secret key là password1 mình sẽ tiến hành modify lại jwt token và thay vào cookie

![Untitled](SUPER%20ADMIN%20267bf800aea44a9fbad0a1895d581b7b/Untitled%204.png)

![Untitled](SUPER%20ADMIN%20267bf800aea44a9fbad0a1895d581b7b/Untitled%205.png)