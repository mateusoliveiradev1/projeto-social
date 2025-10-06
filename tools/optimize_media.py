from pathlib import Path
import imageio
import numpy as np
from PIL import Image, ImageOps


IMAGES_DIR = Path("images")
GIF_PATH = IMAGES_DIR / "fab-toggle.gif"
GIF_300_PATH = IMAGES_DIR / "fab-toggle-300.gif"
SHOT_PATH = IMAGES_DIR / "screenshot-desktop.jpg"


def optimize_gif_open_only():
    if not GIF_PATH.exists():
        print("GIF não encontrado, pulando otimização.")
        return
    frames = imageio.mimread(GIF_PATH)
    if not frames:
        print("Sem frames no GIF, pulando.")
        return
    # Usar apenas primeira metade dos frames (abertura)
    half = max(1, len(frames) // 2 + len(frames) % 2)
    open_frames = frames[:half]
    imageio.mimsave(GIF_PATH, open_frames, duration=0.08)
    print(f"GIF otimizado (apenas abertura) com {len(open_frames)} frames.")


def to_sepia(img: Image.Image) -> Image.Image:
    if img.mode != "RGB":
        img = img.convert("RGB")
    width, height = img.size
    pixels = img.load()
    for py in range(height):
        for px in range(width):
            r, g, b = pixels[px, py]
            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)
            pixels[px, py] = (min(255, tr), min(255, tg), min(255, tb))
    return img


def generate_gif_300_sepia():
    if not GIF_PATH.exists():
        print("GIF base não encontrado, pulando geração 300px.")
        return
    frames = imageio.mimread(GIF_PATH)
    if not frames:
        print("Sem frames no GIF base, pulando.")
        return
    out_arrays = []
    for fr in frames:
        im = Image.fromarray(fr)
        im = ImageOps.contain(im, (300, 300), method=Image.LANCZOS)
        im = to_sepia(im)
        out_arrays.append(np.array(im))
    imageio.mimsave(GIF_300_PATH, out_arrays, duration=0.08)
    print(f"GIF 300px com sépia gerado em: {GIF_300_PATH}")


def resize_screenshot(max_width=1600, quality=80):
    if not SHOT_PATH.exists():
        print("Screenshot não encontrada, pulando redimensionamento.")
        return
    im = Image.open(SHOT_PATH)
    w, h = im.size
    if w <= max_width:
        print("Screenshot já está menor ou igual ao alvo, mantendo.")
        return
    new_h = int(h * (max_width / w))
    im = im.resize((max_width, new_h), Image.LANCZOS)
    im.save(SHOT_PATH, format="JPEG", quality=quality, optimize=True)
    print(f"Screenshot redimensionada para {max_width}x{new_h} (qualidade {quality}).")


def main():
    optimize_gif_open_only()
    resize_screenshot()
    generate_gif_300_sepia()


if __name__ == "__main__":
    main()