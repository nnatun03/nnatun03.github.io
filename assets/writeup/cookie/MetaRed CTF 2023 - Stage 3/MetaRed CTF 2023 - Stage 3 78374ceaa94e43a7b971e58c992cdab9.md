# MetaRed CTF 2023 - Stage 3

# Master JWT

[MetaRed CTF 2023 - Master JWT · Neaje](https://neaje.me/posts/metared_ctf/)

![Untitled](MetaRed%20CTF%202023%20-%20Stage%203%2078374ceaa94e43a7b971e58c992cdab9/Untitled.png)

# Baby seek and real seek

![Untitled](MetaRed%20CTF%202023%20-%20Stage%203%2078374ceaa94e43a7b971e58c992cdab9/Untitled%201.png)

# Mienteles

![Untitled](MetaRed%20CTF%202023%20-%20Stage%203%2078374ceaa94e43a7b971e58c992cdab9/Untitled%202.png)

# Extracttheflag!

![Untitled](MetaRed%20CTF%202023%20-%20Stage%203%2078374ceaa94e43a7b971e58c992cdab9/Untitled%203.png)

`Content-Type: application/x-www-form-urlencoded :` Cho biết định dạng content được gửi lên là www-form-urlencoded

Nếu không có header này, server sẽ không hiểu được rằng `_SESSION[admin]=true` là một params url encoded, và sẽ không thể parse ra key và value để set session `admin=true.`

Bài này yêu cầu bypass authentication bằng cách set giá trị admin trong session. Cần thêm `content-type` để server hiểu được dữ liệu gửi lên.