from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from tinyec import registry

# Load certificate
with open("wikipedia.crt", "rb") as f:
    cert_data = f.read()

cert = x509.load_pem_x509_certificate(cert_data, default_backend())
public_key = cert.public_key()

if isinstance(public_key, ec.EllipticCurvePublicKey):
    curve_name = public_key.curve.name
    print("Curve Name:", curve_name)

    # Use tinyec to get parameters
    try:
        curve = registry.get_curve(curve_name)
        p = curve.field.p
        a = curve.a
        b = curve.b

        # print("\nElliptic Curve Equation:")
        # print(f"y^2 = x^3 + {a}x + {b} (mod {p})")

        print(f"a = {a}")
        print(f"b = {b}")
        print(f"p = {p}")
    except Exception as e:
        print("Curve not found in tinyec registry:", e)
