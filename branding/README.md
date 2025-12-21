# The Archivist's Wheel - Branding Assets

## Overview

ASCII-rendered 3D animation of a Ramelli Book Wheel (1588) for the "data-centered" project branding. The wheel serves as a metaphor for the wise librarian/archivist who catalogs and organizes knowledge sources.

**Concept**: A Renaissance-era mechanical device that allowed scholars to consult multiple heavy books simultaneously - essentially an analog precursor to tabbed browsing.

---

## Files

| File | Type | Description |
|------|------|-------------|
| `library-wheel-ascii.html` | **Primary** | Animated 3D book wheel rendered as ASCII art via Three.js |
| `library-wheel-static.html` | Static | Pre-converted ASCII from image (higher fidelity, no animation) |
| `library-wheel.html` | Archive | Original CSS/SVG version (deprecated) |
| `bookwheel_then_and_now.png` | Reference | Ramelli 1588 illustration + RIT 2018 recreation |

### Supporting Files (in `/ascii_Files/`)

| File | Description |
|------|-------------|
| `ascii_converter.py` | Python script for image-to-ASCII conversion |
| `bookwheel_custom.txt` | Pre-converted ASCII art (clean character ramp) |
| `bookwheel_detailed.txt` | High-detail ASCII (70+ character ramp) |
| `bookwheel_standard.txt` | Standard conversion |
| `bookwheel_minimal.txt` | Minimal character set |

---

## Technical Implementation

### Stack

```
Three.js (r160)     - 3D rendering
AsciiEffect         - Real-time ASCII conversion
Vanilla HTML/CSS/JS - No build step required
```

### Viewing

```bash
# Start local server (required for ES modules)
cd /Users/kbinkly/git-repos/data-centered/branding
python3 -m http.server 8080

# Open in browser
http://localhost:8080/library-wheel-ascii.html
```

---

## 3D Scene Structure

### Camera

```javascript
// 3/4 perspective (matching Ramelli illustration)
camera.position.set(-12, 3, 16);
camera.lookAt(0, 0, 0);

// Mouse parallax (subtle)
camera.position.x = -12 + mouseX * 2;
camera.position.y = 3 + mouseY * 1.5;
```

### Scene Hierarchy

```
Scene
├── Cabinet Frame
│   ├── Left Pillar
│   ├── Right Pillar
│   ├── Top Beam + Crown
│   ├── Bottom Base
│   ├── Side Panels
│   └── Axle Brackets (brass)
│
├── Main Wheel (rotates Z-axis)
│   ├── Outer Rim (torus, wood)
│   ├── Inner Rim (torus, dark wood)
│   ├── Spokes × 10 (cylinder)
│   ├── Central Hub (brass)
│   ├── Hub Center (iron)
│   ├── Main Gear (36 teeth, brass)
│   │
│   └── Shelf Assemblies × 10
│       ├── Platform (angled lectern)
│       ├── Book Lip
│       ├── Side Supports
│       ├── Open Book
│       │   ├── Left Page (cream)
│       │   ├── Right Page (cream)
│       │   ├── Spine (leather)
│       │   └── Cover Edges
│       └── Bracket (iron)
│
├── Gear Train (stationary, rotates independently)
│   ├── Secondary Gear (24T, copper)
│   ├── Tertiary Gear (18T, brass)
│   ├── Crank Gear (12T, copper)
│   └── Crank Handle
│
└── Scholar's Station
    ├── Desk
    ├── Desk Legs × 4
    ├── Chair Seat
    └── Chair Back
```

---

## Animation System

### Rotation Speeds

```javascript
// Main wheel: slow, stately rotation
mainWheel.rotation.z += 0.006;  // ~17 seconds per revolution

// Gear train (proper meshing ratios)
// Adjacent gears counter-rotate, speed inversely proportional to teeth
secGear:   0.006 * (36/24) = 0.009    // direction: -1
tertGear:  0.006 * (36/24) * (24/18) = 0.012  // direction: +1
crankGear: 0.006 * (36/24) * (24/18) * (18/12) = 0.018  // direction: -1
```

### Epicyclic Counter-Rotation

```javascript
// The "magic" of the book wheel: shelves maintain orientation
// as the wheel rotates (books stay readable)
shelfAssemblies.forEach(shelf => {
  shelf.rotation.z = -mainWheel.rotation.z;
});
```

---

## ASCII Rendering

### Character Ramp

```javascript
// 10 characters, light → dark
' .:-=+*#%@'

// Resolution (character density)
resolution: 0.15  // Lower = more detail, higher = more abstract
```

### Styling

```css
color: #d4a855;           /* Brass/sepia tone */
backgroundColor: #0a0908; /* Near-black */
fontFamily: "Courier New", monospace;
fontSize: 10px;
lineHeight: 8px;          /* Tighter for ASCII aspect ratio */
```

---

## Materials Palette

| Material | Color | Metalness | Roughness | Use |
|----------|-------|-----------|-----------|-----|
| Brass | `#d4a855` | 0.8 | 0.2 | Hubs, brackets, main gear |
| Copper | `#cd7f32` | 0.75 | 0.3 | Secondary gears |
| Wood | `#8b6240` | 0.0 | 0.85 | Wheel rim, platforms, desk |
| Dark Wood | `#5c3d2e` | 0.0 | 0.9 | Frame, spokes, chair |
| Iron | `#4a4a4a` | 0.85 | 0.4 | Brackets, handles |
| Page | `#f5f0e0` | - | 0.9 | Open book pages |
| Leather | `#4a2c1a` | - | 0.8 | Book covers/spines |

---

## Historical Reference

### Ramelli's Original (1588)

- **Source**: *Le diverse et artificiose machine* (Plate CLXXXVIII)
- **Designer**: Agostino Ramelli, Italian military engineer
- **Purpose**: Allow scholars (especially those with gout) to consult multiple heavy volumes without moving
- **Innovation**: Epicyclic gearing from astronomical clocks keeps shelves level

### Key Design Elements

1. **Vertical wheel** rotating on horizontal axis (like Ferris wheel)
2. **8-10 lecterns** around circumference
3. **Open books** with pages facing outward toward seated reader
4. **45° reading angle** maintained during rotation
5. **Cabinet frame** with architectural details
6. **Visible gear train** on side
7. **Scholar's desk** positioned in front

---

## Customization

### Adjust Rotation Speed

```javascript
// In animate() function
mainWheel.rotation.z += 0.006;  // Increase for faster, decrease for slower
```

### Change Number of Book Shelves

```javascript
const numShelves = 10;  // Change to 8 or 12
```

### Modify Camera Angle

```javascript
// More frontal view
camera.position.set(0, 2, 20);

// More side view
camera.position.set(-18, 2, 8);

// Bird's eye
camera.position.set(-8, 15, 12);
```

### ASCII Resolution

```javascript
// More detailed (slower)
resolution: 0.1

// More abstract (faster)
resolution: 0.2
```

### Character Set

```javascript
// Detailed (more shading levels)
' .\'`^",:;Il!i><~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'

// Minimal (higher contrast)
' .-+*#@'

// Blocks (retro feel)
' ░▒▓█'
```

---

## Converting Images to ASCII

Use the included Python script:

```bash
cd /Users/kbinkly/git-repos/data-centered/ascii_Files

# Basic conversion
python3 ascii_converter.py input.jpg -w 120 -o output.txt

# With options
python3 ascii_converter.py input.png \
  --width 140 \
  --ramp detailed \
  --invert \
  --contrast 1.2 \
  --output result.txt
```

### Options

| Flag | Description | Default |
|------|-------------|---------|
| `-w, --width` | Output width in characters | 120 |
| `-r, --ramp` | Character ramp (standard/detailed/minimal/blocks/custom) | standard |
| `-i, --invert` | Invert for dark backgrounds | false |
| `-c, --contrast` | Contrast adjustment | 1.0 |
| `-o, --output` | Output file (or stdout) | stdout |

---

## Future Enhancements

### Librarian Character

- [ ] Design ASCII librarian mascot (steampunk aesthetic)
- [ ] Options: hand-crafted ASCII or 3D model → ASCII conversion
- [ ] Potential animation: librarian turning the wheel crank

### Interactive Features

- [ ] Click to stop/start rotation
- [ ] Scroll to zoom
- [ ] Click book to "open" detail view

### Export Options

- [ ] Capture single frame as PNG
- [ ] Export animation as GIF
- [ ] Generate static ASCII for terminal display

---

## Resources

### ASCII Art Tools

| Tool | URL | Use Case |
|------|-----|----------|
| TAAG | https://patorjk.com/software/taag/ | Text to ASCII banners |
| ASCII Animator | https://www.ascii-animator.com/ | Frame-by-frame animation |
| LaplASCIIan | https://github.com/zalo/LaplASCIIan | GIF → animated ASCII SVG |
| jp2a | https://github.com/cslarsen/jp2a | CLI image converter |

### Three.js References

- [AsciiEffect](https://threejs.org/examples/#webgl_effects_ascii)
- [ExtrudeGeometry](https://threejs.org/docs/#api/en/geometries/ExtrudeGeometry) (for gears)
- [TorusGeometry](https://threejs.org/docs/#api/en/geometries/TorusGeometry) (for wheel rim)

### Historical Sources

- [Wikipedia: Bookwheel](https://en.wikipedia.org/wiki/Bookwheel)
- [Science History Institute - Plate 188](https://digital.sciencehistory.org/works/w6634396g)
- [Rochester: Book Wheel as Modern Search Engine](https://www.rochester.edu/newscenter/book-wheel-modern-search-engine-364122/)

---

## Credits

- **Original Design**: Agostino Ramelli (1588)
- **Modern Reference**: Rochester Institute of Technology recreation (2018)
- **ASCII Implementation**: Claude Code + data-centered project
- **Inspiration**: Matt Bierman's ASCII portfolio (https://bierman.io/)

---

*Last updated: December 2025*
