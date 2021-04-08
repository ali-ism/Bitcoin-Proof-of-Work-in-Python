# Bitcoin-Proof-of-Work-in-Python

Assignment 2

In this assignment, you will simulate “mining” your personal information (full name, email,
and AUB ID number) using SHA-256 and Bitcoin-style Proof-of-Work.

Your personal information block consists of the following bytes:

• Previous block hash: 32 bytes
• Nonce: 4 bytes
• Timestamp: 4 bytes
This is a Unix epoch timestamp, which is based on the number of seconds elapsed
since midnight UTC, Thursday, January 1, 1970. For example, the timestamp
1612888888 corresponds to Tuesday, February 9, 2021 6:41:28 PM GMT+02:00. This
timestamp would be represented in the block by 0x6022bb38

• Data:
- AUB ID number: 4 bytes. The ID number is treated like a 32-bit unsigned
integer. For example, 202212345 is represented by 0x0c0d83f9 in the
block.
- Email address: abc12@mail.aub.edu, 18 or 19 bytes, ASCII-encoded. The
shown email address would be represented by
0x6162633132406d61696c2e6175622e656475 in the block.
- Full name: First_Name Last_Name, variable number of bytes, ASCIIencoded.
For example, John Smith is represented by 0x4a6f686e20536d697468 in the block.

Use a previous block hash value from the actual Bitcoin blockchain at
https://www.blockchain.com/btc/blocks

Use the hash of block number 650000 + last four digits of your ID number.
For example, if your ID number is 202212345, the Bitcoin block number is 652345, and your
previous hash value would be the following, as obtained from
https://www.blockchain.com/btc/block/652345:
0x0000000000000000000901f6897513af92b66173f5bbd13a2f336bcd925a1b69

Objective: Find a nonce value that results in a SHA-256 hash for your personal block with 24
leftmost 0 bits, 25 leftmost 0 bits, 26 leftmost 0 bits, 27 leftmost 0 bits, etc.

Submit:
1. Your source code in Python.
2. Your personal block information in hex: previous block hash, nonce that corresponds
to 24 zero bits, timestamp, ID number, email, and full name.
3. A table that shows the number of zero bits (24, 25, 26, 27,..), the nonce value in hex,
the hash value in hex of your personal block (for 24, 25, 26, 27,.. bits), and the
(elapsed) time it took your computer to find the nonce. See format on next page.
4. Comment on the relationship between number of zero bits, elapsed time, available
computation rate, and energy spent.
