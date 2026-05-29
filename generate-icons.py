#!/usr/bin/env python3
import struct
import zlib
import base64
import os

def create_png(width, height, color=(255, 215, 0)):
    """Create a simple solid color PNG"""
    def png_chunk(chunk_type, data):
        chunk_len = struct.pack('>I', len(data))
        chunk_crc = struct.pack('>I', zlib.crc32(chunk_type + data) & 0xffffffff)
        return chunk_len + chunk_type + data + chunk_crc

    signature = b'\x89PNG\r\n\x1a\n'

    ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)
    ihdr = png_chunk(b'IHDR', ihdr_data)

    raw_data = b''
    for y in range(height):
        raw_data += b'\x00'
        for x in range(width):
            raw_data += bytes(color)

    compressed = zlib.compress(raw_data, 9)
    idat = png_chunk(b'IDAT', compressed)

    iend = png_chunk(b'IEND', b'')

    return signature + ihdr + idat + iend

def create_icon_set():
    """Create icon set for Tauri"""
    icons_dir = 'src-tauri/icons'
    os.makedirs(icons_dir, exist_ok=True)

    sizes = {
        '32x32.png': 32,
        '128x128.png': 128,
        '128x128@2x.png': 256,
    }

    for filename, size in sizes.items():
        png_data = create_png(size, size, (255, 215, 0))
        with open(os.path.join(icons_dir, filename), 'wb') as f:
            f.write(png_data)
        print(f"Created {filename}")

    print("Icon generation complete!")
    print("Note: For production, replace with custom icons")

if __name__ == '__main__':
    create_icon_set()
