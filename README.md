# Elliptic Curve Parameter Extractor

This project demonstrates how to extract elliptic curve parameters (`a`, `b`, `p`) and the finite field characteristic directly from an SSL/TLS certificate that uses **Elliptic Curve Digital Signature Algorithm (ECDSA)**.  

It combines the [`cryptography`](https://cryptography.io/en/latest/) library (to parse certificates and identify the curve) with [`tinyec`](https://pypi.org/project/tinyec/) (to retrieve the actual mathematical parameters of the curve).

---

## 📌 Features
- Load a website’s certificate (`.pem` format).
- Identify the elliptic curve used (e.g., `secp256r1`, `secp384r1`, `secp521r1`).
- Extract the curve equation in the form:

  

\[
  y^2 = x^3 + ax + b \pmod{p}
  \]



- Print the finite field characteristic (`p` for prime curves, `2` for binary curves).

---

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/ec-parameter-extractor.git
cd ec-parameter-extractor
pip install cryptography tinyec
