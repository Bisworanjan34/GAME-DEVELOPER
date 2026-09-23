import pygame


def render_gradient_text(font, text, color1, color2):
    # Step 1: Text ko white color mein render karo (Yeh text ki shape dega)
    text_surface = font.render(text, True, (255, 255, 255))
    width, height = text_surface.get_size()

    # Step 2: Ek gradient box banao (Left color se Right color ka shade)
    gradient_surface = pygame.Surface((width, height), pygame.SRCALPHA)

    for x in range(width):
        # Math logic: X position ke hisaab se color1 aur color2 ko mix karna
        r = color1[0] + (color2[0] - color1[0]) * x / width
        g = color1[1] + (color2[1] - color1[1]) * x / width
        b = color1[2] + (color2[2] - color1[2]) * x / width

        # Uss vertical line par gradient color draw kar do
        pygame.draw.line(
            gradient_surface, (int(r), int(g), int(b)), (x, 0), (x, height)
        )

    # Step 3: Gradient ko text surface ke sath multiply (blend) kar do
    gradient_surface.blit(text_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    return gradient_surface
