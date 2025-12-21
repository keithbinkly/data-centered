#!/usr/bin/env python3
"""
ASCII Art Converter - Density-mapped image to ASCII conversion
"""

from PIL import Image
import argparse

# Character ramps from sparse (light) to dense (dark)
RAMPS = {
    'standard': ' .,-~:;=!*#$@',
    'detailed': ' .\'`^",:;Il!i><~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$',
    'blocks': ' ░▒▓█',
    'minimal': ' .-+*#@',
    'dots': ' .·:░▒▓█',
}

def image_to_ascii(
    image_path: str,
    width: int = 120,
    ramp: str = 'standard',
    invert: bool = False,
    contrast: float = 1.0,
) -> str:
    """
    Convert an image to ASCII art using density mapping.
    
    Args:
        image_path: Path to input image
        width: Output width in characters
        ramp: Character ramp name or custom string
        invert: Invert brightness (for dark backgrounds)
        contrast: Contrast adjustment (1.0 = normal)
    
    Returns:
        ASCII art as string
    """
    # Get character ramp
    chars = RAMPS.get(ramp, ramp)
    if invert:
        chars = chars[::-1]
    
    # Load and convert to grayscale
    img = Image.open(image_path).convert('L')
    
    # Calculate height (characters are ~2x taller than wide)
    aspect_ratio = img.height / img.width
    height = int(width * aspect_ratio * 0.55)
    
    # Resize
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    
    # Apply contrast
    if contrast != 1.0:
        from PIL import ImageEnhance
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(contrast)
    
    # Convert pixels to characters
    pixels = list(img.getdata())
    ascii_chars = []
    
    for pixel in pixels:
        # Map 0-255 to character index
        char_idx = int(pixel / 256 * len(chars))
        char_idx = min(char_idx, len(chars) - 1)
        ascii_chars.append(chars[char_idx])
    
    # Split into lines
    lines = []
    for i in range(0, len(ascii_chars), width):
        lines.append(''.join(ascii_chars[i:i + width]))
    
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='Convert images to ASCII art')
    parser.add_argument('image', help='Input image path')
    parser.add_argument('-w', '--width', type=int, default=120, help='Output width (default: 120)')
    parser.add_argument('-r', '--ramp', default='standard', 
                       help=f'Character ramp: {list(RAMPS.keys())} or custom string')
    parser.add_argument('-i', '--invert', action='store_true', help='Invert for dark backgrounds')
    parser.add_argument('-c', '--contrast', type=float, default=1.0, help='Contrast (default: 1.0)')
    parser.add_argument('-o', '--output', help='Output file (default: stdout)')
    
    args = parser.parse_args()
    
    result = image_to_ascii(
        args.image,
        width=args.width,
        ramp=args.ramp,
        invert=args.invert,
        contrast=args.contrast,
    )
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(result)
        print(f'Saved to {args.output}')
    else:
        print(result)


if __name__ == '__main__':
    main()
