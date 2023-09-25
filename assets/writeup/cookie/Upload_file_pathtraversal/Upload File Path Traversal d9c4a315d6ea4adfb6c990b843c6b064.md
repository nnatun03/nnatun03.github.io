# Upload File Path Traversal

## Tổng quan

- Để giải được challenge này ta cần có kiến thức về file upload và path traversal, encoding.
- công cụ: burpsuite

## Phân tích bài

- truy cập vào trang web, ta thấy được rằng trang web này chỉ có duy nhất 1 chức năng là upload file, sau khi test up 1 số file bình thường như gif,jpg,... thì upload thoải mái.

![Untitled](Upload%20File%20Path%20Traversal%20d9c4a315d6ea4adfb6c990b843c6b064/Untitled.png)

- tuy nhiên khi ta thử up file php thì sẽ bị báo là file ko hợp lệ

![Untitled](Upload%20File%20Path%20Traversal%20d9c4a315d6ea4adfb6c990b843c6b064/Untitled%201.png)

- lúc này ta thử view-source xem có thông tin gì hữu ích ko thì tìm được 1 đoạn mã nguồn của code như sau:

![Untitled](Upload%20File%20Path%20Traversal%20d9c4a315d6ea4adfb6c990b843c6b064/Untitled%202.png)

- đọc thì có vẻ như chỉ có thể upload được file với các định dạng như (gif,jpg,png). Sau đó sẽ được upload lên /upload.php với format là
    
    [`http://13.215.248.36:32716/upload/example.gif`](http://13.215.248.36:32716/upload/example.gif)
    
- mình thử sử dụng 1 file gif up lên, sau đó dùng burpsuite và send to repeater.

![Untitled](Upload%20File%20Path%20Traversal%20d9c4a315d6ea4adfb6c990b843c6b064/Untitled%203.png)

- Lúc này mình sẽ xóa hết phần định danh của thằng gif đi (màu đỏ) và thay bằng `code php` + đổi tên filename thành đuôi `.php` luôn nhé :D, vì thằng coder nó chả filter đoạn đấy nên mình có thể khai thác được (1 phần vì bài này dễ )
- vì bài này ở đây có 1 lớp filter là nó chỉ lấy những kí tự sau dấu `/` cuối cùng, ví dụ bạn để input là `aa / bb` thì khi upload nó chỉ nhận `/bb`.
- tuy nhiên nếu chúng ta encode dấu `/` thành `%2f` thì có thể bypass được

![Untitled](Upload%20File%20Path%20Traversal%20d9c4a315d6ea4adfb6c990b843c6b064/Untitled%204.png)

- payload sẽ được tô đậm màu đỏ

```visual-basic
-----WebKitFormBoundarycQPvCLj26757rBVu

Content-Disposition: form-data; name="file"; filename="`..%2fshell3.php`"

Content-Type: image/gif

`<?php phpinfo();?>`

-----WebKitFormBoundarycQPvCLj26757rBVu--
```

- Sau khi upload thành công, ta truy cập thử /shell3.php vừa upload để kiểm tra

![Untitled](Upload%20File%20Path%20Traversal%20d9c4a315d6ea4adfb6c990b843c6b064/Untitled%205.png)

- **DONE, việc còn lại ae cat /flag.txt thôi nhé ^^**