#!/usr/bin/env python3
"""Generate a WiFi QR code image from the command line."""

import argparse
import sys

try:
    import qrcode
except ImportError:
    print("Missing dependency. Install it with:  pip install qrcode[pil]")
    sys.exit(1)


def escape_special(value: str) -> str:
    """Escape special characters per the WiFi QR code spec."""
    for ch in ("\\", ";", ",", '"', ":"):
        value = value.replace(ch, f"\\{ch}")
    return value


def build_wifi_string(ssid: str, password: str, encryption: str, hidden: bool) -> str:
    ssid = escape_special(ssid)
    hidden_flag = "H:true;" if hidden else ""
    if encryption == "nopass":
        return f"WIFI:T:nopass;S:{ssid};{hidden_flag};"
    password = escape_special(password)
    return f"WIFI:T:{encryption};S:{ssid};P:{password};{hidden_flag};"


def generate(ssid: str, password: str, encryption: str, hidden: bool,
             size: int, output: str) -> None:
    wifi_string = build_wifi_string(ssid, password, encryption, hidden)

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=max(1, size // 33),
        border=2,
    )
    qr.add_data(wifi_string)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img = img.resize((size, size))
    img.save(output)
    print(f"Saved {size}x{size} QR code to {output}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate a WiFi QR code image.",
        epilog="Example:  wifi_qr.py -s MyNetwork -p s3cret -o wifi.png",
    )
    parser.add_argument("-s", "--ssid", required=True, help="WiFi network name (SSID)")
    parser.add_argument("-p", "--password", default="", help="WiFi password")
    parser.add_argument("-e", "--encryption", default="WPA",
                        choices=["WPA", "WEP", "nopass"],
                        help="Security type (default: WPA)")
    parser.add_argument("--hidden", action="store_true", help="Hidden network")
    parser.add_argument("--size", type=int, default=400,
                        help="Image size in pixels (default: 400)")
    parser.add_argument("-o", "--output", default="wifi-qr.png",
                        help="Output file path (default: wifi-qr.png)")

    args = parser.parse_args()

    if args.encryption != "nopass" and not args.password:
        parser.error("Password is required for WPA/WEP networks")

    generate(args.ssid, args.password, args.encryption,
             args.hidden, args.size, args.output)


if __name__ == "__main__":
    main()
