# Kuri

## Bagian 1
## Latar Belakang
[What is encryption](https://danielmiessler.com/study/encoding-encryption-hashing-obfuscation/):
> Encryption transforms data into another format in such a way that only specific individual(s) can reverse the transformation. It uses a key, which is kept secret, in conjunction with the plaintext and the algorithm, in order to perform the encryption operation. As such, the ciphertext, algorithm, and key are all required to return to the plaintext.

[Why it matters](https://danielmiessler.com/study/encoding-encryption-hashing-obfuscation/):
> The purpose of encryption is to transform data in order to keep it secret from others, e.g. sending someone a secret letter that only they should be able to read, or securely sending a password over the Internet. Rather than focusing on usability, the goal is to ensure the data cannot be consumed by anyone other than the intended recipient(s).

## Teknologi yang digunakan
1. Python
2. Flask

## Cipher yang diimplementasikan
1. Vigenere Cipher
2. Caesar Cipher

## Cara Penggunaan
1. Untuk enkripsi Vigenere cipher, kirim JSON dengan request POST ke [cryptoirk.herokuapp.com/crypto/1](cryptoirk.herokuapp.com/crypto/1)
2. Untuk dekripsi Vigenere cipher, kirim JSON dengan request POST ke [cryptoirk.herokuapp.com/crypto/2](cryptoirk.herokuapp.com/crypto/2)
3. Untuk enkripsi Caesar cipher, kirim JSON dengan request POST ke [cryptoirk.herokuapp.com/crypto/3](cryptoirk.herokuapp.com/crypto/3)
4. Untuk dekripsi Caesar cipher, kirim JSON dengan request POST ke [cryptoirk.herokuapp.com/crypto/4](cryptoirk.herokuapp.com/crypto/4)

## Spesifikasi API
1. Terdapat sebuah _endpoint_ yang akan menerima _plaintext_, lalu mengubahnya menjadi _ciphertext_. _Endpoint_ akan menerima **POST** _request_ dengan _payload_:
```JSON
{
  "plaintext": "Insert plaintext here"
}
```

2. Terdapat sebuah _endpoint_ yang akan menerima _ciphertext_, lalu mengubahnya menjadi _plaintext_. _Endpoint_ akan menerima **POST** _request_ dengan _payload_:
```JSON
{
  "ciphertext": "Insert ciphertext here"
}
```

3. [API dapat diakses melalui internet](https://cryptoirk.herokuapp.com/crypto)
