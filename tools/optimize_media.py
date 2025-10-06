from pathlib import Path
import imageio
from PIL import Image


IMAGES_DIR = Path("images")
GIF_PATH = IMAGES_DIR / "fab-toggle.gif"
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


if __name__ == "__main__":
    main()