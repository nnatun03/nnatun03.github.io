# PHP có làm em lo lắng

## **Tổng quan**

- Để giải được challenge này, ta cần vận dụng kiến thức về ngôn ngữ PHP và cách dùng BurpSuite
- công cụ: Burpsuite

## Phân tích bài

- Truy cập trang web, ta thấy được form login, có chức năng đăng kí tài khoản.

![Untitled](PHP%20co%CC%81%20la%CC%80m%20em%20lo%20la%CC%86%CC%81ng%2075ac733245b6458daccaba64c492cffc/Untitled.png)

- Sau khi tạo tài khoản và đăng nhập vào, chúng ta sẽ được điều hướng đến trang /index.php

![Untitled](PHP%20co%CC%81%20la%CC%80m%20em%20lo%20la%CC%86%CC%81ng%2075ac733245b6458daccaba64c492cffc/Untitled%201.png)

- Trang có chức năng export to CVS với định dạng là đuôi `.cvs`, khi ta chọn export thì trang web sẽ tải lên file kèm theo đường dẫn đến file như hình bên dưới.

![Untitled](PHP%20co%CC%81%20la%CC%80m%20em%20lo%20la%CC%86%CC%81ng%2075ac733245b6458daccaba64c492cffc/Untitled%202.png)

- Thử truy cập vào, lúc này mình liên tưởng tới Path-Traversal, tuy nhiên sau một lúc test thử thì có vẻ bài này không bị lỗi ấy.
    
    ![Untitled](PHP%20co%CC%81%20la%CC%80m%20em%20lo%20la%CC%86%CC%81ng%2075ac733245b6458daccaba64c492cffc/Untitled%203.png)
    
- Tuy nhiên lúc này mình để ý được rằng tên đăng nhập của mình đã được export xuống như hình bên dưới, nên mình đã nghĩ tới 1 hướng đó chính là mình thử chèn một đoạn code PHP vào xem sao.
- Tạo tài khoản với tên đăng nhập là `<?php phpinfo();?>`

![Untitled](PHP%20co%CC%81%20la%CC%80m%20em%20lo%20la%CC%86%CC%81ng%2075ac733245b6458daccaba64c492cffc/Untitled%204.png)

- Tuy nhiên bài này ở đây đã filter cụm `<?php`, tức mỗi lần xuất hiện `<?php` thì bạn sẽ luôn bị chèn dấu `#` vào sau.

![Untitled](PHP%20co%CC%81%20la%CC%80m%20em%20lo%20la%CC%86%CC%81ng%2075ac733245b6458daccaba64c492cffc/Untitled%205.png)

- Tuy nhiên mình để ý rằng bài này chỉ filter chính xác cụm `<?php`  làm thẻ mở đầu , tức là nếu mình các thẻ khác thì sẽ không bị chèn `#` vào. Lúc này mình thử search google xem có cách nào khác để mở thẻ không thì có một số cách như sau.

```php
<?
echo "Hello World";
?>
```

hoặc 

```php
<?= "Hello World" ?>
```

và 

```php
<%
  echo "Hello World";
%>
```

- Thử test với tên đăng nhập là `<?= system('ls -la /') ?>` thì có vẻ như ta đã bypass được filter của bài, tuy nhiên lúc này đoạn mã php của ta vẫn chưa được thực thi vì đuôi file vẫn đang là .cvs

![Untitled](PHP%20co%CC%81%20la%CC%80m%20em%20lo%20la%CC%86%CC%81ng%2075ac733245b6458daccaba64c492cffc/Untitled%206.png)

- Lúc này mình tận dụng chức năng Intercep của BurpSuite để thay đổi đuôi tệp tin thành .php

![Untitled](PHP%20co%CC%81%20la%CC%80m%20em%20lo%20la%CC%86%CC%81ng%2075ac733245b6458daccaba64c492cffc/Untitled%207.png)

- Sau khi click lại Forward thì các bạn có thể thấy đuôi file của ta đã trở thành .php

![Untitled](PHP%20co%CC%81%20la%CC%80m%20em%20lo%20la%CC%86%CC%81ng%2075ac733245b6458daccaba64c492cffc/Untitled%208.png)

- DONEEEE, việc còn lại là đổi payload để cat flag thôi ^^

![Untitled](PHP%20co%CC%81%20la%CC%80m%20em%20lo%20la%CC%86%CC%81ng%2075ac733245b6458daccaba64c492cffc/Untitled%209.png)