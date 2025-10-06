import os
import time
from pathlib import Path
import io

from playwright.sync_api import sync_playwright
from PIL import Image
import imageio


BASE_URL = "http://localhost:8000/"
IMAGES_DIR = Path("images")


def ensure_dirs():
    IMAGES_DIR.mkdir(exist_ok=True)


def screenshot_desktop(page):
    """Captura screenshot completa da página inicial e salva como JPG."""
    page.set_viewport_size({"width": 1366, "height": 900})
    page.goto(BASE_URL + "index.html", wait_until="networkidle")
    png_path = IMAGES_DIR / "screenshot-desktop.png"
    jpg_path = IMAGES_DIR / "screenshot-desktop.jpg"
    page.screenshot(path=str(png_path), full_page=True)
    # Converter para JPG com qualidade
    with Image.open(png_path) as im:
        rgb = im.convert("RGB")
        rgb.save(jpg_path, format="JPEG", quality=85)
    try:
        png_path.unlink()
    except Exception:
        pass
    print(f"Screenshot salva em: {jpg_path}")


def gif_fab_toggle(page):
    """Gera GIF do botão FAB animando hambúrguer → X a partir da demo."""
    page.set_viewport_size({"width": 480, "height": 800})
    page.goto(BASE_URL + "index.html", wait_until="networkidle")

    # Localizar botão para clip de captura
    button = page.locator("#menu-button")
    box = button.bounding_box()
    if not box:
        raise RuntimeError("Não foi possível localizar #menu-button para captura.")

    # Adicionar padding ao clip
    pad = 8
    clip = {
        "x": max(0, box["x"] - pad),
        "y": max(0, box["y"] - pad),
        "width": box["width"] + 2 * pad,
        "height": box["height"] + 2 * pad,
    }

    frames = []

    # Estado inicial (fechado)
    frames.append(page.screenshot(type="png", clip=clip))

    # Disparar animação abrindo (click no label)
    button.click()
    # Capturar frames durante ~0.48s (8 frames a cada 60ms)
    for _ in range(8):
        time.sleep(0.06)
        frames.append(page.screenshot(type="png", clip=clip))

    # Fechar (click novamente)
    button.click()
    for _ in range(8):
        time.sleep(0.06)
        frames.append(page.screenshot(type="png", clip=clip))

    gif_path = IMAGES_DIR / "fab-toggle.gif"
    # imageio espera arrays; carregamos bytes em arrays
    imgs = [imageio.v2.imread(io.BytesIO(b)) for b in frames]
    imageio.mimsave(gif_path, imgs, duration=0.06)
    print(f"GIF salvo em: {gif_path}")


def main():
    ensure_dirs()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        screenshot_desktop(page)
        gif_fab_toggle(page)
        context.close()
        browser.close()


if __name__ == "__main__":
    main()