from io import BytesIO
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader



from io import BytesIO

from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader


def create_printable_pdf(
    cards: list[Image.Image],
    output_path: str,
    cards_per_row: int,
    margin_mm: float = 10,
    gap_mm: float = 5,
    back: bool = False,
    back_image_path: str | None = None,
):
    if not cards:
        raise ValueError("No cards provided.")

    if back and back_image_path is None:
        raise ValueError(
            "A back image path must be provided when back=True."
        )

    page_width, page_height = A4

    margin = margin_mm * mm
    gap = gap_mm * mm

    available_width = page_width - 2 * margin

    # -------------------------
    # Card dimensions
    # -------------------------

    card_width = (
        available_width
        - gap * (cards_per_row - 1)
    ) / cards_per_row

    image_width, image_height = cards[0].size
    aspect_ratio = image_height / image_width

    card_height = card_width * aspect_ratio

    available_height = page_height - 2 * margin

    rows_per_page = int(
        (available_height + gap)
        // (card_height + gap)
    )

    if rows_per_page < 1:
        raise ValueError(
            "Cards are too large to fit vertically on an A4 page."
        )

    cards_per_page = cards_per_row * rows_per_page

    # -------------------------
    # Validate aspect ratios
    # -------------------------

    expected_ratio = cards[0].height / cards[0].width

    for card in cards:
        ratio = card.height / card.width

        if abs(ratio - expected_ratio) > 0.01:
            raise ValueError(
                "All cards must have the same aspect ratio."
            )

    # -------------------------
    # Load backside
    # -------------------------

    back_image = None

    if back:
        back_image = Image.open(
            back_image_path
        ).convert("RGB")

    # -------------------------
    # PDF
    # -------------------------

    pdf = canvas.Canvas(
        output_path,
        pagesize=A4,
    )

    # Process cards page by page
    for page_start in range(
        0,
        len(cards),
        cards_per_page,
    ):
        page_cards = cards[
            page_start:page_start + cards_per_page
        ]

        # =========================
        # FRONT PAGE
        # =========================

        for index, card in enumerate(page_cards):
            row = index // cards_per_row
            column = index % cards_per_row

            x = margin + column * (
                card_width + gap
            )

            y = (
                page_height
                - margin
                - card_height
                - row * (card_height + gap)
            )

            buffer = BytesIO()

            card.convert("RGB").save(
                buffer,
                format="PNG",
            )

            buffer.seek(0)

            pdf.drawImage(
                ImageReader(buffer),
                x,
                y,
                width=card_width,
                height=card_height,
            )

        # Finish front page
        pdf.showPage()

        # =========================
        # BACK PAGE
        # =========================

        if back:
            for index in range(len(page_cards)):
                row = index // cards_per_row
                column = index % cards_per_row

                x = margin + column * (
                    card_width + gap
                )

                y = (
                    page_height
                    - margin
                    - card_height
                    - row * (card_height + gap)
                )

                buffer = BytesIO()

                back_image.save(
                    buffer,
                    format="PNG",
                )

                buffer.seek(0)

                pdf.drawImage(
                    ImageReader(buffer),
                    x,
                    y,
                    width=card_width,
                    height=card_height,
                )

            # Finish backside page
            pdf.showPage()

    pdf.save()


def create_printable_pokemon_pdf(
    cards: list[Image.Image],
    output_path: str,
    back: bool = True,
):
    create_printable_pdf(
        cards=cards,
        output_path=output_path,
        cards_per_row=3,
        margin_mm=4,
        gap_mm=2,
        back=back,
        back_image_path="card_backside.png" if back else None,
    )


def create_printable_tokens_pdf(
    cards: list[Image.Image],
    output_path: str,
):
    create_printable_pdf(
        cards=cards,
        output_path=output_path,
        cards_per_row=5,
        margin_mm=4,
        gap_mm=2,
        back=False,
    )


def create_printable_moves_pdf(
    cards: list[Image.Image],
    output_path: str,
):
    create_printable_pdf(
        cards=cards,
        output_path=output_path,
        cards_per_row=4,
        margin_mm=4,
        gap_mm=2,
        back=False,
    )