"""Generate dated, hyperlinked planners for Supernote and other PDF readers.

Uses vector text and lines, internal PDF destinations, and no network services.
"""
import argparse
import calendar
from datetime import date, timedelta
from pathlib import Path
from reportlab.pdfgen import canvas

def generate_planner(year, output_dir, author='Randeep Gupta'):
    """Write one year and validate page counts and all generated link targets."""
    W, H = (600, 800)
    output_dir.mkdir(parents=True, exist_ok=True)
    out = str(output_dir / f'{year}_Supernote_Planner.pdf')
    c = canvas.Canvas(out, pagesize=(W, H), pageCompression=1)
    c.setTitle(f'{year} Hyperlinked Planner')
    c.setAuthor(author)
    start = date(year, 1, 1)
    end = date(year, 12, 31)
    weeks = [start - timedelta(days=start.weekday()) + timedelta(weeks=i) for i in range((end - (start - timedelta(days=start.weekday()))).days // 7 + 1)]
    manifest = {}
    links = []

    def federal_dates(year):
        result = set()

        def nth(y, m, weekday, n):
            first = date(y, m, 1)
            return first + timedelta(days=(weekday - first.weekday()) % 7 + 7 * (n - 1))
        for yy in range(year - 1, year + 2):
            fixed = [date(yy, 1, 1), date(yy, 6, 19), date(yy, 7, 4), date(yy, 11, 11), date(yy, 12, 25)]
            days = fixed + [nth(yy, 1, 0, 3), nth(yy, 2, 0, 3), nth(yy, 9, 0, 1), nth(yy, 10, 0, 2), nth(yy, 11, 3, 4)]
            last = date(yy, 5, 31)
            days.append(last - timedelta(days=last.weekday()))
            for d in fixed:
                if d.weekday() == 5:
                    days.append(d - timedelta(days=1))
                if d.weekday() == 6:
                    days.append(d + timedelta(days=1))
            result.update((d for d in days if d.year == year))
        return result
    holidays = federal_dates(start.year)

    def txt(x, y, s, size=10, bold=False, gray=0.12, align='left'):
        c.setFillGray(gray)
        c.setFont('Helvetica-Bold' if bold else 'Helvetica', size)
        getattr(c, {'left': 'drawString', 'center': 'drawCentredString', 'right': 'drawRightString'}[align])(x, H - y, s)

    def line(x, y, x2, y2, g=0.65):
        c.setStrokeGray(g)
        c.setLineWidth(0.5)
        c.line(x, H - y, x2, H - y2)

    def box(x, y, w, h, g=0.96):
        c.setFillGray(g)
        c.setStrokeGray(0.55)
        c.setLineWidth(0.5)
        c.rect(x, H - y - h, w, h, fill=1, stroke=1)

    def link(key, x, y, w, h):
        c.linkRect('', key, (x, H - y - h, x + w, H - y), relative=0, thickness=0)
        links.append((c.getPageNumber(), key))

    def btn(label, key, x, y, w=70, h=22, active=False):
        box(x, y, w, h, 0.22 if active else 1)
        txt(x + w / 2, y + h / 2 + 3, label, 8, gray=1 if active else 0.1, align='center')
        link(key, x, y, w, h)

    def dk(d):
        return 'd' + d.isoformat()

    def wk(d):
        return 'w' + (d - timedelta(days=d.weekday())).isoformat()

    def ruled(x, y, w, bottom, step=20):
        while y <= bottom:
            line(x, y, x + w, y)
            y += step

    def base(key, title, sub='', m=None, q=None):
        c.bookmarkPage(key)
        manifest[key] = c.getPageNumber()
        txt(70, 43, title, 20, True)
        txt(70, 63, sub, 10, gray=0.4)
        btn('YEAR', 'year', 504, 24, 72)
        for i in range(4):
            btn('Q' + str(i + 1), 'q' + str(i + 1), 22, 164 + i * 30, 28, 27, q == i + 1)
        for i in range(12):
            btn(calendar.month_abbr[i + 1].upper(), 'm' + str(i + 1), 22, 296 + i * 35, 28, 32, m == i + 1)
        line(70, 116, 576, 116, 0.25)
        txt(70, 775, f'{year}  /  PLANNER', 7, gray=0.5)
        txt(576, 775, str(c.getPageNumber()), 7, gray=0.5, align='right')

    def finish():
        c.showPage()

    def mini(m, x, y, w=154, h=135, overview=False):
        txt(x + w / 2, y + 11, calendar.month_name[m].upper(), 10, True, align='center')
        link('m' + str(m), x, y, w, 20)
        ww = 28 if overview else w / 8
        cw = (w - ww) / 7
        rh = (h - 40) / 6
        txt(x + ww / 2, y + 31, 'WK' if overview else 'W', 7, gray=0.4, align='center')
        for j, s in enumerate(['M', 'T', 'W', 'T', 'F', 'S', 'S']):
            txt(x + ww + (j + 0.5) * cw, y + 31, s, 7, gray=0.4, align='center')
        line(x, y + 36, x + w, y + 36)
        for r, week in enumerate(calendar.Calendar(0).monthdatescalendar(year, m)):
            yy = y + 40 + r * rh
            if overview:
                btn(f'W{week[0].isocalendar().week:02}', wk(week[0]), x, yy, ww - 3, rh - 2)
            else:
                txt(x + ww / 2, yy + rh * 0.7, f'{week[0].isocalendar().week:02}', 7, gray=0.4, align='center')
                link(wk(week[0]), x, yy, ww, rh)
            for j, d in enumerate(week):
                if d.month == m:
                    dx = x + ww + j * cw
                    if d in holidays:
                        c.setFillGray(0.82)
                        c.rect(dx + 0.5, H - yy - rh + 1, cw - 1, rh - 2, fill=1, stroke=0)
                    txt(dx + cw / 2, yy + rh * 0.7, str(d.day), 8, align='center')
                    link(dk(d), dx, yy, cw, rh)
    base('year', f'{year}', 'A year of space to think, plan, and follow through.')
    for q in range(4):
        y = 140 + q * 150
        for j in range(3):
            mini(q * 3 + j + 1, 78 + j * 168, y, overview=True)
    c.setFillGray(0.82)
    c.rect(70, H - 740, 9, 9, fill=1, stroke=0)
    txt(85, 739, 'U.S. federal holidays, including observed dates', 8, gray=0.4)
    txt(70, 756, 'Tap a month, date, week button, or side tab to navigate.', 8, gray=0.4)
    finish()
    for q in range(1, 5):
        base('q' + str(q), 'Quarter ' + str(q), f'{year}  /  QUARTERLY NOTES', q=q)
        ruled(70, 143, 506, 283)
        for i in range(3):
            y = 310 + i * 145
            mini((q - 1) * 3 + i + 1, 70, y, 174, 130)
            ruled(264, y + 18, 312, y + 130)
        finish()
    for m in range(1, 13):
        base('m' + str(m), calendar.month_name[m], f'{year}  /  MONTHLY CALENDAR', m=m, q=(m - 1) // 3 + 1)
        btn('Month notes', 'mn' + str(m), 478, 77, 98)
        rows = calendar.Calendar(0).monthdatescalendar(year, m)
        top = 155
        rh = 580 / len(rows)
        cw = 68
        for j, s in enumerate(['W', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']):
            txt(84 if j == 0 else 100 + (j - 0.5) * cw, 143, s, 9, align='center')
        for r, week in enumerate(rows):
            y = top + r * rh
            box(70, y, 30, rh, 0.94)
            txt(85, y + 23, str(week[0].isocalendar().week), 10, align='center')
            link(wk(week[0]), 70, y, 30, rh)
            for j, d in enumerate(week):
                x = 100 + j * cw
                box(x, y, cw, rh, 1 if d.month == m else 0.97)
                if d in holidays:
                    c.setFillGray(0.82)
                    c.rect(x + cw - 30, H - y - 28, 28, 26, fill=1, stroke=0)
                txt(x + cw - 9, y + 22, str(d.day), 11, gray=0.1 if d.month == m else 0.55, align='right')
                if d.year == year:
                    link(dk(d), x + cw - 32, y + 2, 30, 30)
        finish()
        base('mn' + str(m), calendar.month_name[m], f'{year}  /  MONTHLY NOTES', m=m, q=(m - 1) // 3 + 1)
        btn('Calendar', 'm' + str(m), 478, 77, 98)
        ruled(70, 144, 506, 744)
        finish()
    for i, mon in enumerate(weeks):
        sun = mon + timedelta(days=6)
        anchor = max(start, mon)
        m = anchor.month
        sub = f'{mon:%b %d, %Y} - {sun:%b %d, %Y}'
        for extra in [False, True]:
            base(wk(mon) + ('x' if extra else ''), f'Week {mon.isocalendar().week:02}', sub, m=m, q=(m - 1) // 3 + 1)
            txt(285, 43, 'EXTRA WEEKLY NOTES' if extra else 'WEEKLY NOTES', 10)
            if i:
                btn('< Week', wk(weeks[i - 1]), 70, 80, 66)
            if i < len(weeks) - 1:
                btn('Week >', wk(weeks[i + 1]), 142, 80, 66)
            btn('Weekly plan' if extra else 'Extra notes', wk(mon) + ('' if extra else 'x'), 478, 77, 98)
            if extra:
                ruled(70, 144, 506, 744)
            else:
                txt(70, 137, "THIS WEEK'S PRIORITIES", 10, True)
                for x, y, w, h, rows, label in [(70, 155, 249, 213, 9, 'Do first'), (327, 155, 249, 236, 10, 'Schedule'), (70, 380, 249, 103, 4, 'Delegate'), (327, 403, 249, 80, 3, 'Eliminate')]:
                    box(x, y, w, h, 1)
                    c.setFont('Helvetica', 8)
                    lw = c.stringWidth(label, 'Helvetica', 8) + 10
                    c.setFillGray(1)
                    c.rect(x + 9, H - y - 5, lw, 11, fill=1, stroke=0)
                    txt(x + 14, y + 3, label, 8, gray=0.35)
                    for row in range(rows):
                        yy = y + 20 + row * 22
                        c.setStrokeGray(0.55)
                        c.setLineWidth(0.5)
                        c.rect(x + 12, H - yy + 1, 6, 6, fill=0, stroke=1)
                        line(x + 28, yy + 2, x + w - 12, yy + 2)
                txt(70, 511, 'DAY-SPECIFIC TASKS', 10, True)
                for j in range(7):
                    d = mon + timedelta(days=j)
                    y = 531 + j * 31
                    if d in holidays:
                        c.setFillGray(0.82)
                        c.rect(67, H - y - 17, 108, 24, fill=1, stroke=0)
                    txt(70, y + 10, d.strftime('%a').upper(), 9, True)
                    txt(167, y + 10, d.strftime('%b %d'), 9, align='right')
                    if d.year == year:
                        link(dk(d), 70, y - 5, 105, 27)
                    line(179, y - 5, 179, y + 18, 0.7)
                    line(70, y + 21, 576, y + 21)
            finish()
    for n in range((end - start).days + 1):
        d = start + timedelta(days=n)
        mon = d - timedelta(days=d.weekday())
        for extra in [False, True]:
            base(dk(d) + ('x' if extra else ''), d.strftime('%B %d'), d.strftime(f'%A  /  {year}'), m=d.month, q=(d.month - 1) // 3 + 1)
            if d in holidays:
                c.setFillGray(0.82)
                c.rect(70, H - 47, 205, 25, fill=1, stroke=0)
                txt(70, 43, d.strftime('%B %d'), 20, True)
            txt(285, 43, 'EXTRA DAILY NOTES' if extra else 'DAILY NOTES', 10)
            btn('Daily plan' if extra else 'Extra notes', dk(d) + ('' if extra else 'x'), 478, 77, 98)
            btn('Week ' + str(d.isocalendar().week), wk(d), 478, 51, 98, 20)
            for delta in range(-7, 8):
                target = d + timedelta(days=delta)
                idx = delta + 7
                x = 70 + idx * 26.4
                if target.year == year:
                    box(x, 80, 25, 28, 0.22 if delta == 0 else 0.82 if target in holidays else 1)
                    txt(x + 12.5, 90, target.strftime('%a')[:2], 6, gray=1 if delta == 0 else 0.4, align='center')
                    txt(x + 12.5, 102, str(target.day), 9, bold=delta == 0, gray=1 if delta == 0 else 0.1, align='center')
                    link(dk(target) + ('x' if extra else ''), x, 80, 25, 28)
                else:
                    box(x, 80, 25, 28, 0.97)
                    txt(x + 12.5, 90, target.strftime('%a')[:2], 6, gray=0.65, align='center')
                    txt(x + 12.5, 102, str(target.day), 9, gray=0.65, align='center')
            first = max(start, d - timedelta(days=7))
            last = min(end, d + timedelta(days=7))
            txt(285, 64, first.strftime('%b %d') + ' - ' + last.strftime('%b %d'), 8, gray=0.4)
            if extra:
                ruled(70, 144, 506, 744)
            else:
                txt(70, 142, 'TASK PRIORITIES', 10, True)
                txt(210, 166, 'URGENT', 9, True, align='center')
                txt(455, 166, 'NOT URGENT', 9, True, align='center')
                for x, y, w, h, rows, title in [(90, 178, 239, 101, 3, '1  DO FIRST'), (337, 178, 239, 122, 4, '2  SCHEDULE'), (90, 287, 239, 80, 2, '3  DELEGATE'), (337, 308, 239, 59, 1, '4  ELIMINATE')]:
                    box(x, y, w, h, 1)
                    txt(x + 12, y + 21, title, 11, True)
                    for row in range(rows):
                        yy = y + 43 + row * 22
                        c.setStrokeGray(0.55)
                        c.setLineWidth(0.5)
                        c.rect(x + 12, H - yy - 1, 6, 6, fill=0, stroke=1)
                        line(x + 28, yy + 2, x + w - 12, yy + 2)
                for x, y, h, label in [(90, 178, 101, 'IMPORTANT'), (337, 178, 122, 'IMPORTANT'), (90, 287, 80, 'NOT IMPORTANT'), (337, 308, 59, 'NOT IMPORTANT')]:
                    txt(x + 227, y + 21, label, 6, gray=0.45, align='right')
                txt(70, 391, 'NOTES', 10, True)
                ruled(70, 407, 506, 747)
            finish()
    c.save()
    assert len(manifest) == 29 + 2 * len(weeks) + 2 * ((end - start).days + 1)
    assert all((key in manifest for _, key in links))
    print(f'{out}: {len(manifest)} pages, {len(links)} internal links')
    return Path(out)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('years', nargs='*', type=int, default=list(range(2026, 2031)), help='Years to generate; default: 2026 through 2030')
    parser.add_argument('--output-dir', type=Path, default=Path('planners'), help='Output folder; existing same-named files are overwritten')
    parser.add_argument('--author', default='Randeep Gupta', help='PDF author metadata')
    args = parser.parse_args()
    for year in args.years:
        if not 2026 <= year <= 9998:
            parser.error('Years must be between 2026 and 9998')
    for year in dict.fromkeys(args.years):
        generate_planner(year, args.output_dir, args.author)
if __name__ == '__main__':
    main()
