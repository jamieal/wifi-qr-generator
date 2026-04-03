# WiFi QR Code Generator

Generate a QR code for your WiFi network so anyone can connect by scanning it with their phone. Free, open source, and your credentials never leave your browser.

**[Use it now](https://jamieal.github.io/wifi-qr-generator)** (update link after deploy)

## Features

- Enter your WiFi SSID, password, and security type
- Instantly generates a scannable QR code
- Test it live — point your phone camera at the screen
- Download in multiple print-ready sizes (200px–1200px or custom)
- Works offline — everything runs client-side in your browser
- Supports WPA/WPA2/WPA3, WEP, and open networks
- Hidden network support

## Download Sizes

| Size | Use Case |
|------|----------|
| 200 x 200 | Fridge magnet, business card |
| 400 x 400 | Sticker, small print |
| 800 x 800 | Standard poster print |
| 1200 x 1200 | Large poster |
| Custom | Enter any dimensions |

## CLI Tool

There's also a Python command-line tool for generating QR codes programmatically.

```bash
cd cli
pip install -r requirements.txt
python wifi_qr.py -s "MyNetwork" -p "mypassword" -o wifi.png
```

### CLI Options

```
-s, --ssid        WiFi network name (required)
-p, --password    WiFi password
-e, --encryption  Security type: WPA, WEP, nopass (default: WPA)
--hidden          Mark as hidden network
--size            Image size in pixels (default: 400)
-o, --output      Output file (default: wifi-qr.png)
```

## Self-Hosting

It's a single HTML file with no build step. Clone it and open `index.html`, or deploy anywhere that serves static files.

```bash
git clone https://github.com/jamieal/wifi-qr-generator.git
open wifi-qr-generator/index.html
```

GitHub Pages deployment is included — just push to `main` and it deploys automatically.

## Privacy

Your WiFi details are processed entirely in your browser. Nothing is sent to any server.

## License

MIT
