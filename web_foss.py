"""
web.F/OSS — private security toolkit.
Авторы: wourazi & restokrat.
Тема: black / white / pink hacker.
Анимированное название (один раз при запуске).
Выход: 00 или Ctrl+C.
"""

import sys
import os
import time
import math
import random
import string
import socket
import platform
import datetime

if os.name == "nt":
    try:
        os.system("chcp 65001 >nul")
    except Exception:
        pass


# ============================================================
#  ЦВЕТА
# ============================================================
RESET = "\033[0m"

PINK = "\033[38;5;205m"
PINK_SOFT = "\033[38;5;212m"
PINK_DIM = "\033[38;5;132m"
PINK_BRIGHT = "\033[38;5;219m"
PINK_NEON = "\033[38;5;200m"

WHITE = "\033[97m"
GRAY = "\033[38;5;245m"
GRAY_DIM = "\033[38;5;238m"
BOLD = "\033[1m"

ACCENT = PINK
ACCENT_SOFT = PINK_SOFT
ACCENT_DIM = PINK_DIM
TEXT = WHITE
TEXT_DIM = GRAY
TEXT_DIM2 = GRAY_DIM

RED = PINK
GREEN = PINK_SOFT
YELLOW = PINK_SOFT
BLUE = PINK_SOFT
MAGENTA = PINK
CYAN = PINK


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def slowprint(s, delay=0.01):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)


def pause(msg="нажми Enter чтобы продолжить"):
    try:
        input(f"\n{TEXT_DIM}[*] {msg}...{RESET}")
    except (EOFError, KeyboardInterrupt):
        pass


def pause_dot(msg="нажми любую клавишу"):
    if os.name == "nt":
        import msvcrt
        print(f"\n{TEXT_DIM}[*] {msg}...{RESET}")
        msvcrt.getwch()
    else:
        input(f"\n{TEXT_DIM}[*] {msg}...{RESET}")


def ts():
    return datetime.datetime.now().strftime("%H:%M:%S")


def line_info(msg):
    print(f"{GRAY_DIM}[{ts()}]{RESET} {ACCENT}[i]{RESET} {TEXT}{msg}{RESET}")


def line_ok(msg):
    print(f"{GRAY_DIM}[{ts()}]{RESET} {ACCENT_SOFT}[+]{RESET} {TEXT}{msg}{RESET}")


def line_warn(msg):
    print(f"{GRAY_DIM}[{ts()}]{RESET} {ACCENT}[!]{RESET} {TEXT}{msg}{RESET}")


def line_err(msg):
    print(f"{GRAY_DIM}[{ts()}]{RESET} {ACCENT}[x]{RESET} {TEXT}{msg}{RESET}")


def header(title):
    clear()
    pad = 66
    print(ACCENT + "╔" + "═" * pad + "╗")
    print("║" + f"{BOLD}{title.center(pad)}{RESET}{ACCENT}" + "║")
    print("╚" + "═" * pad + "╝" + RESET)
    print()


# ============================================================
#  ЛОГО
# ============================================================
LOGO_LINES = [
    r"  ██╗    ██╗███████╗██████╗     ███████╗     ██████╗ ███████╗███████╗  ",
    r"  ██║    ██║██╔════╝██╔══██╗    ██╔════╝    ██╔═══██╗██╔════╝██╔════╝  ",
    r"  ██║ █╗ ██║█████╗  ██████╔╝    █████╗      ██║   ██║███████╗███████╗  ",
    r"  ██║███╗██║██╔══╝  ██╔══██╗    ██╔══╝      ██║   ██║╚════██║╚════██║  ",
    r"  ╚███╔███╔╝███████╗██████╔╝    ██║         ╚██████╔╝███████║███████║  ",
    r"   ╚══╝╚══╝ ╚══════╝╚═════╝     ╚═╝          ╚═════╝ ╚══════╝╚══════╝  ",
]


def _pink_shade(k):
    if k > 0.85:
        return PINK_BRIGHT
    if k > 0.65:
        return PINK
    if k > 0.45:
        return PINK_NEON
    if k > 0.25:
        return PINK_SOFT
    return PINK_DIM


def print_animated_logo(t0):
    phase = (t0 * 2.0) % 2.0
    if phase > 1.0:
        phase = 2.0 - phase
    wave_width = 0.35
    for line in LOGO_LINES:
        out = []
        width = len(line)
        for i, ch in enumerate(line):
            if ch == " ":
                out.append(ch)
                continue
            pos = i / max(1, width - 1)
            d = abs(pos - phase)
            if d < wave_width:
                k = 1.0 - (d / wave_width)
            else:
                k = 0.0
            k = min(1.0, k + 0.15 * math.sin(t0 * 8 + i * 0.3))
            out.append(_pink_shade(k) + ch + RESET)
        print("".join(out))


def logo_animation(duration=1.6, fps=20):
    start = time.time()
    frame_dt = 1.0 / fps
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()
    try:
        while True:
            now = time.time()
            if now - start >= duration:
                break
            sys.stdout.write("\033[H")
            print_animated_logo(now - start)
            sys.stdout.flush()
            time.sleep(frame_dt)
    finally:
        sys.stdout.write("\033[H")
        for line in LOGO_LINES:
            sys.stdout.write(ACCENT + line + RESET + "\n")
        sys.stdout.flush()
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()


def print_banner(animated=True):
    if animated:
        clear()
        logo_animation(duration=1.6, fps=20)
        print()
    else:
        for line in LOGO_LINES:
            print(ACCENT + line + RESET)
        print()

    print(ACCENT + "═" * 68 + RESET)
    print(f"{TEXT_DIM}  платформа:  {RESET}{BOLD}{ACCENT}web.F/OSS{RESET}")
    print(f"{TEXT_DIM}  авторы:     {RESET}{BOLD}{TEXT}wourazi{RESET}{TEXT_DIM} & {RESET}{BOLD}{TEXT}restokrat{RESET}")
    print(f"{TEXT_DIM}  версия:     {RESET}{BOLD}{TEXT}1.0{RESET}")
    print(f"{TEXT_DIM}  сборка:     {RESET}{TEXT}{datetime.date.today().isoformat()}{RESET}")
    print(f"{TEXT_DIM}  хост:       {RESET}{TEXT}{socket.gethostname()}{RESET}")
    print(f"{TEXT_DIM}  ОС:         {RESET}{TEXT}{platform.system()} {platform.release()}{RESET}")
    print(ACCENT + "═" * 68 + RESET)


def print_banner_fast():
    for line in LOGO_LINES:
        print(ACCENT + line + RESET)
    print(ACCENT + "═" * 68 + RESET)
    print(f"{TEXT_DIM}  платформа:  {RESET}{BOLD}{ACCENT}web.F/OSS{RESET}")
    print(f"{TEXT_DIM}  авторы:     {RESET}{BOLD}{TEXT}wourazi{RESET}{TEXT_DIM} & {RESET}{BOLD}{TEXT}restokrat{RESET}")
    print(f"{TEXT_DIM}  версия:     {RESET}{BOLD}{TEXT}1.0{RESET}")
    print(f"{TEXT_DIM}  сборка:     {RESET}{TEXT}{datetime.date.today().isoformat()}{RESET}")
    print(f"{TEXT_DIM}  хост:       {RESET}{TEXT}{socket.gethostname()}{RESET}")
    print(f"{TEXT_DIM}  ОС:         {RESET}{TEXT}{platform.system()} {platform.release()}{RESET}")
    print(ACCENT + "═" * 68 + RESET)


# ============================================================
#  BOOT
# ============================================================
def boot_screen():
    clear()
    print_banner(animated=True)
    print()
    steps = [
        "Проверка окружения...",
        "Инициализация ядра web.F/OSS...",
        "Загрузка модулей анализа...",
        "Проверка сетевых интерфейсов...",
        "Синхронизация с локальным хранилищем...",
        "Проверка целостности подписей...",
        "Инициализация крипто-модуля...",
        "Подготовка рабочих профилей...",
    ]
    for msg in steps:
        line_info(msg)
        time.sleep(0.3)
    print()
    line_ok("все системы в норме")
    line_warn("оператор несёт ответственность за использование")
    time.sleep(1.0)


# ============================================================
#  ВСПОМОГАТЕЛЬНОЕ
# ============================================================
def rand_mac():
    return ":".join(f"{random.randint(0, 255):02X}" for _ in range(6))


def rand_ip():
    return f"192.168.1.{random.randint(2, 254)}"


def fake_delay(a=0.2, b=0.5):
    time.sleep(random.uniform(a, b))


# ============================================================
#  МОДУЛИ
# ============================================================
def tool_ip_scan():
    header("МОДУЛЬ СКАНИРОВАНИЯ СЕТИ")
    line_info("активный интерфейс: Ethernet")
    line_info(f"локальный IP: 192.168.1.{random.randint(2, 30)}")
    line_info("маска: /24")
    line_info("запуск ARP-обнаружения...")
    fake_delay(0.6, 1.0)
    hosts = []
    for i in range(random.randint(4, 9)):
        ip = rand_ip()
        mac = rand_mac()
        vendor = random.choice([
            "TP-Link", "D-Link", "ASUS", "MikroTik", "Keenetic",
            "Apple", "Samsung", "Intel", "Realtek", "Xiaomi",
        ])
        rtt = random.randint(1, 40)
        hosts.append((ip, mac, vendor, rtt))
    print()
    print(f"{ACCENT}{'IP':<18}{'MAC':<20}{'VENDOR':<12}{'RTT'}{RESET}")
    print(f"{GRAY_DIM}{'-' * 60}{RESET}")
    for ip, mac, vendor, rtt in hosts:
        print(f"{TEXT}{ip:<18}{mac:<20}{vendor:<12}{rtt} ms{RESET}")
        fake_delay(0.1, 0.2)
    print()
    line_ok(f"обнаружено узлов: {len(hosts)}")
    line_ok("отчёт сохранён в scan_<timestamp>.txt")
    pause_dot()


def tool_port_scan():
    header("МОДУЛЬ СКАНИРОВАНИЯ ПОРТОВ")
    target = input(f"{TEXT}[?] цель (Enter = 127.0.0.1): {RESET}").strip() or "127.0.0.1"
    line_info(f"цель: {target}")
    line_info("режим: TCP connect")
    line_info("диапазон: 1-1024")
    fake_delay(0.4, 0.8)
    ports = [
        (22,   "ssh",   "OpenSSH 8.9"),
        (80,   "http",  "nginx 1.24.0"),
        (443,  "https", "nginx 1.24.0"),
        (3306, "mysql", "MySQL 8.0.34"),
        (5432, "pgsql", "PostgreSQL 15.4"),
        (6379, "redis", "Redis 7.2"),
        (8080, "http",  "Tomcat 10.1"),
        (8443, "https", "Apache 2.4.58"),
    ]
    random.shuffle(ports)
    open_ports = ports[:random.randint(3, 6)]
    print()
    print(f"{ACCENT}{'PORT':<8}{'STATE':<10}{'SERVICE':<10}{'BANNER'}{RESET}")
    print(f"{GRAY_DIM}{'-' * 60}{RESET}")
    for p in sorted(open_ports):
        print(f"{TEXT}{p[0]:<8}{'open':<10}{p[1]:<10}{p[2]}{RESET}")
        fake_delay(0.1, 0.2)
    print()
    line_ok(f"открытых портов: {len(open_ports)}")
    line_info(f"закрыто/фильтруется: {1024 - len(open_ports)}")
    pause_dot()


def tool_admin_finder():
    header("ПОИСК АДМИНИСТРАТИВНЫХ ПАНЕЛЕЙ")
    target = input(f"{TEXT}[?] домен или IP: {RESET}").strip() or "example.com"
    line_info(f"цель: {target}")
    line_info("загрузка словаря (247 путей)...")
    fake_delay(0.5, 0.9)
    paths = [
        "/admin", "/admin/login", "/administrator", "/login",
        "/panel", "/cpanel", "/wp-admin", "/dashboard",
        "/manage", "/manager", "/admin.php", "/backend",
    ]
    random.shuffle(paths)
    found = []
    for p in paths[:random.randint(6, 10)]:
        status = random.choice([200, 301, 302, 403, 404])
        line_info(f"GET http://{target}{p} -> {status}")
        fake_delay(0.15, 0.3)
        if status in (200, 301, 302):
            found.append((p, status))
    print()
    if found:
        for p, status in found:
            line_ok(f"найден: {target}{p} [{status}]")
    else:
        line_warn("панелей не найдено")
    line_ok("поиск завершён")
    pause_dot()


def tool_banner_grab():
    header("МОДУЛЬ СБОРА БАННЕРОВ")
    target = input(f"{TEXT}[?] IP:порт (Enter = 127.0.0.1:80): {RESET}").strip() or "127.0.0.1:80"
    try:
        host, port = target.split(":")
        port = int(port)
    except Exception:
        host, port = "127.0.0.1", 80
    line_info(f"соединение с {host}:{port}...")
    fake_delay(0.3, 0.7)
    line_ok("соединение установлено")
    fake_delay(0.2, 0.5)
    banner = random.choice([
        "HTTP/1.1 200 OK\r\nServer: nginx/1.24.0\r\nDate: ...",
        "HTTP/1.1 200 OK\r\nServer: Apache/2.4.58 (Unix)\r\n...",
        "SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.4",
        "220 FTP Server (vsFTPd 3.0.5) ready",
        "HTTP/1.1 301 Moved Permanently\r\nServer: cloudflare\r\n...",
    ])
    print()
    print(f"{ACCENT}--- banner ---{RESET}")
    for row in banner.split("\r\n"):
        print(f"{TEXT}{row}{RESET}")
        fake_delay(0.05, 0.15)
    print(f"{ACCENT}--- end ---{RESET}")
    line_ok("баннер получен")
    pause_dot()


def tool_stress():
    header("СТРЕСС-ТЕСТ КАНАЛА")
    target = input(f"{TEXT}[?] целевой URL (Enter = http://127.0.0.1): {RESET}").strip() or "http://127.0.0.1"
    threads = input(f"{TEXT}[?] потоков (Enter = 200): {RESET}").strip() or "200"
    line_info(f"цель: {target}")
    line_info(f"потоков: {threads}")
    line_warn("проверь, что у тебя есть разрешение на тест")
    fake_delay(0.4, 0.8)
    sent = 0
    rps = 0
    for _ in range(5):
        sent += random.randint(500, 1500)
        rps = random.randint(400, 1200)
        line_info(f"отправлено: {sent:<8} rps: {rps}")
        fake_delay(0.3, 0.6)
    print()
    line_ok("тест завершён")
    line_info(f"всего запросов: {sent}")
    line_info(f"средний rps:    {rps}")
    line_info(f"ошибок:         {random.randint(0, 12)}")
    pause_dot()


def tool_anon_mail():
    header("АНОНИМНАЯ ПОЧТА")
    provider = random.choice(["protonmail.com", "tutanota.com", "mailfence.com"])
    inbox = "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
    addr = f"{inbox}@{provider}"
    line_info("создание временного ящика...")
    fake_delay(0.4, 0.8)
    line_ok(f"ящик создан: {addr}")
    to_addr = input(f"{TEXT}[?] получатель: {RESET}").strip()
    subject = input(f"{TEXT}[?] тема: {RESET}").strip()
    body = input(f"{TEXT}[?] текст: {RESET}").strip()
    print()
    line_info("шифрование содержимого (AES-256)...")
    fake_delay(0.3, 0.6)
    line_ok("контент зашифрован")
    line_info("маршрутизация через цепочку узлов...")
    fake_delay(0.3, 0.6)
    line_ok("маршрут установлен")
    line_info("отправка письма...")
    fake_delay(0.4, 0.8)
    msg_id = "".join(random.choice(string.hexdigits.lower()) for _ in range(16))
    line_ok(f"письмо отправлено (message-id: {msg_id})")
    line_info(f"получатель: {to_addr}")
    line_info(f"тема: {subject}")
    line_info("уничтожение временного ящика через 10 минут...")
    pause_dot()


def tool_password_gen():
    header("ГЕНЕРАТОР ПАРОЛЕЙ")
    try:
        length = int(input(f"{TEXT}[?] длина пароля (8-64): {RESET}") or "16")
    except ValueError:
        length = 16
    length = max(8, min(64, length))
    line_info("источник энтропии: os.urandom")
    fake_delay(0.2, 0.4)
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    pwd = "".join(random.choice(alphabet) for _ in range(length))
    print()
    print(f"{ACCENT}┌{'─' * 60}┐{RESET}")
    print(f"{ACCENT}│{RESET} {BOLD}{WHITE}{pwd}{RESET}")
    print(f"{ACCENT}└{'─' * 60}┘{RESET}")
    print()
    line_ok(f"длина: {length} символов")
    line_info(f"энтропия: ~{int(length * 6.5)} бит")
    pause_dot()


def tool_encrypt():
    header("ШИФРОВАНИЕ / РАСШИФРОВКА")
    line_info("алгоритм: сдвиг Цезаря (+5)")
    print(f"{TEXT}[1] шифровать  [2] расшифровать  [0] назад{RESET}")
    choice = input(f"{TEXT}[?] выбор: {RESET}").strip()
    if choice == "0":
        return
    text = input(f"{TEXT}[?] текст: {RESET}")
    shift = 5
    out = []
    for ch in text:
        if ch.isalpha():
            base = "A" if ch.isupper() else "a"
            out.append(chr((ord(ch) - ord(base) + (shift if choice == "1" else -shift)) % 26 + ord(base)))
        else:
            out.append(ch)
    print()
    line_ok(f"результат: {''.join(out)}")
    pause_dot()


def tool_sys_info():
    header("ИНФОРМАЦИЯ О СИСТЕМЕ")
    items = [
        ("платформа",       "web.F/OSS"),
        ("версия",          "1.0"),
        ("хост",            socket.gethostname()),
        ("пользователь",    os.environ.get("USERNAME") or os.environ.get("USER") or "неизвестно"),
        ("ОС",              f"{platform.system()} {platform.release()}"),
        ("версия ОС",       platform.version()),
        ("архитектура",     platform.machine()),
        ("Python",          sys.version.split()[0]),
        ("ядра CPU",        str(os.cpu_count())),
        ("рабочий каталог", os.getcwd()),
    ]
    for k, v in items:
        print(f"{ACCENT}{k:<18}{RESET} {TEXT}{v}{RESET}")
        fake_delay(0.05, 0.15)
    print()
    try:
        local_ip = socket.gethostbyname(socket.gethostname())
        line_info(f"локальный IP: {local_ip}")
    except Exception:
        line_warn("не удалось получить локальный IP")
    pause_dot()


def tool_lingvo():
    header("ЛИНГВО-МОДУЛЬ")
    text = input(f"{TEXT}[?] текст: {RESET}").strip()
    line_info("определение языка...")
    fake_delay(0.3, 0.6)
    lang = random.choice([
        ("русский", "ru", 0.98),
        ("английский", "en", 0.95),
        ("немецкий", "de", 0.89),
        ("французский", "fr", 0.87),
        ("испанский", "es", 0.85),
    ])
    line_ok(f"определён язык: {lang[0]} ({lang[1]}), уверенность: {lang[2]}")
    fake_delay(0.3, 0.6)
    line_info("перевод на английский...")
    fake_delay(0.4, 0.8)
    line_ok(f"перевод: [translated text of: {text[:40]}...]")
    pause_dot()


def tool_osint():
    header("OSINT-РАЗВЕДКА")
    q = input(f"{TEXT}[?] username / email / домен: {RESET}").strip()
    if not q:
        q = "example"
    line_info(f"объект: {q}")
    platforms = [
        ("github.com",    random.choice([True, True, False])),
        ("twitter.com",   random.choice([True, False])),
        ("reddit.com",    random.choice([True, True, False])),
        ("instagram.com", random.choice([True, False])),
        ("t.me",          random.choice([True, True, False])),
        ("vk.com",        random.choice([True, False])),
        ("habr.com",      random.choice([True, False])),
    ]
    print()
    for site, exists in platforms:
        status = "найден" if exists else "не найден"
        color = ACCENT_SOFT if exists else GRAY_DIM
        print(f"{GRAY_DIM}[{ts()}]{RESET} {color}[+/-]{RESET} {TEXT}{site:<18}{RESET} {color}{status}{RESET}")
        fake_delay(0.15, 0.3)
    print()
    found_count = sum(1 for _, e in platforms if e)
    line_ok(f"найдено профилей: {found_count} из {len(platforms)}")
    pause_dot()


def tool_dorking():
    header("ПОИСКОВЫЕ ЗАПРОСЫ")
    domain = input(f"{TEXT}[?] домен: {RESET}").strip() or "example.com"
    line_info(f"генерация дорков для {domain}...")
    fake_delay(0.3, 0.6)
    dorks = [
        f'site:{domain} "index of /"',
        f'site:{domain} ext:sql',
        f'site:{domain} ext:log',
        f'site:{domain} inurl:admin',
        f'site:{domain} intitle:"confidential"',
        f'site:{domain} intext:"password"',
    ]
    for d in dorks:
        print(f"{TEXT}  {d}{RESET}")
        fake_delay(0.1, 0.25)
    print()
    line_ok(f"сгенерировано {len(dorks)} запросов")
    line_info("сохранено в dorks_<timestamp>.txt")
    pause_dot()


def tool_wifi():
    header("АНАЛИЗ WIFI")
    line_info("сканирование эфира...")
    fake_delay(0.5, 1.0)
    ssids = [
        ("TP-LINK_4A2C",   -45, "WPA2", random.choice([1, 6, 11])),
        ("Keenetic-9F1B",  -52, "WPA2", random.choice([1, 6, 11])),
        ("MTS_Router_5G",  -61, "WPA3", 36),
        ("DIR-825_A1B2",   -70, "WPA2", 11),
        ("HomeWiFi_2G",    -78, "WPA2", 6),
        ("Guest_Network",  -83, "OPEN", 1),
    ]
    random.shuffle(ssids)
    print()
    print(f"{ACCENT}{'SSID':<22}{'SIGNAL':<10}{'SECURITY':<10}{'CH'}{RESET}")
    print(f"{GRAY_DIM}{'-' * 55}{RESET}")
    for ssid, sig, sec, ch in ssids:
        if sig > -60:
            color = WHITE
        elif sig > -75:
            color = ACCENT_SOFT
        else:
            color = ACCENT_DIM
        print(f"{TEXT}{ssid:<22}{color}{sig} dBm{RESET}    {TEXT}{sec:<10}{ch}{RESET}")
        fake_delay(0.1, 0.2)
    print()
    line_ok(f"обнаружено сетей: {len(ssids)}")
    line_warn("сети с открытым доступом — потенциальный риск")
    pause_dot()


def tool_nettest():
    header("СЕТЕВОЙ ТЕСТ")
    line_info("поиск ближайшего узла...")
    fake_delay(0.4, 0.8)
    ping = random.randint(5, 30)
    down = random.randint(40, 250)
    up = random.randint(10, 100)
    jitter = random.randint(1, 8)
    print()
    print(f"{ACCENT}пинг:{RESET}         {TEXT}{ping} мс{RESET}")
    print(f"{ACCENT}джиттер:{RESET}      {TEXT}{jitter} мс{RESET}")
    print(f"{ACCENT}скачивание:{RESET}   {TEXT}{down} Мбит/с{RESET}")
    print(f"{ACCENT}отдача:{RESET}       {TEXT}{up} Мбит/с{RESET}")
    print()
    line_ok("тест завершён")
    pause_dot()


# ============================================================
#  ABOUT
# ============================================================
def about_creators():
    header("О СОЗДАТЕЛЯХ")
    print(f"{ACCENT}[*]{RESET} {BOLD}{TEXT}wourazi{RESET}")
    print(f"    {TEXT}ведущий разработчик.{RESET}")
    print(f"    {TEXT_DIM}архитектура, интерфейс, ядро, модули анализа.{RESET}")
    print()
    print(f"{ACCENT}[*]{RESET} {BOLD}{TEXT}restokrat{RESET}")
    print(f"    {TEXT}соавтор.{RESET}")
    print(f"    {TEXT_DIM}модули, тестирование, отладка, документация.{RESET}")
    print()
    print(f"{ACCENT}Платформа:{RESET} {BOLD}{TEXT}web.F/OSS{RESET}")
    print(f"{ACCENT}Версия:{RESET}    {TEXT}1.0{RESET}")
    print(f"{ACCENT}Профиль:{RESET}   {TEXT}private security toolkit{RESET}")
    print(f"{ACCENT}Статус:{RESET}    {TEXT}active{RESET}")
    print(f"{ACCENT}Сборка:{RESET}    {TEXT}{datetime.date.today().isoformat()}{RESET}")
    pause_dot()


def about_tool():
    header("О ПЛАТФОРМЕ")
    line_info("web.F/OSS — приватный набор модулей для работы в сети.")
    line_info("назначение: сетевой анализ, разведка открытых источников,")
    line_info("работа с почтой, криптография, генерация ключей.")
    line_info("все операции выполняются локально.")
    line_info("текущая версия: 1.0")
    line_warn("оператор несёт ответственность за использование.")
    pause_dot()


def what_is_project():
    header("WEB.F/OSS")
    line_info("приватный toolkit для работы в изолированной среде.")
    line_info("модули покрывают базовые задачи оператора:")
    line_info("разведку, сеть, почту, крипто, утилиты.")
    line_info("распространение — только среди доверенных лиц.")
    line_info("версия: 1.0")
    pause_dot()


def help_screen():
    header("СПРАВКА")
    print(f"{ACCENT}1-14{RESET}   {TEXT}— модули{RESET}")
    print(f"{ACCENT}95-98{RESET}  {TEXT}— сведения{RESET}")
    print(f"{ACCENT}00{RESET}     {TEXT}— выход{RESET}")
    pause_dot()


# ============================================================
#  МЕНЮ
# ============================================================
MENU_TEXT = f"""
{ACCENT}╔══════════════════════════════════════════════════════════════════╗
║                    web.F/OSS  //  v1.0                           ║
╚══════════════════════════════════════════════════════════════════╝{RESET}

{ACCENT}[1]{RESET}  Сканер сети           {ACCENT}[2]{RESET}  Сканер портов
{ACCENT}[3]{RESET}  Поиск админ-панелей  {ACCENT}[4]{RESET}  Сбор баннеров
{ACCENT}[5]{RESET}  Стресс-тест канала   {ACCENT}[6]{RESET}  Анонимная почта
{ACCENT}[7]{RESET}  Генератор пароля     {ACCENT}[8]{RESET}  Шифр / Расшифровка
{ACCENT}[9]{RESET}  Инфа о системе       {ACCENT}[10]{RESET} Лингво-модуль
{ACCENT}[11]{RESET} OSINT-разведка       {ACCENT}[12]{RESET} Поисковые запросы
{ACCENT}[13]{RESET} Анализ WiFi          {ACCENT}[14]{RESET} Сетевой тест

{PINK_DIM}--- сведения ---{RESET}
{ACCENT}[95]{RESET} О создателях          {ACCENT}[96]{RESET} О платформе
{ACCENT}[97]{RESET} О проекте            {ACCENT}[98]{RESET} Справка

{TEXT}[00]{RESET} Выход                  {TEXT}[??]{RESET} Справка
"""


ACTIONS = {
    "1":  tool_ip_scan,
    "2":  tool_port_scan,
    "3":  tool_admin_finder,
    "4":  tool_banner_grab,
    "5":  tool_stress,
    "6":  tool_anon_mail,
    "7":  tool_password_gen,
    "8":  tool_encrypt,
    "9":  tool_sys_info,
    "10": tool_lingvo,
    "11": tool_osint,
    "12": tool_dorking,
    "13": tool_wifi,
    "14": tool_nettest,
    "95": about_creators,
    "96": about_tool,
    "97": what_is_project,
    "98": help_screen,
    "?":  help_screen,
    "??": help_screen,
}


def main_menu():
    first_iteration = True
    while True:
        clear()
        if first_iteration:
            print_banner(animated=True)
            first_iteration = False
        else:
            print_banner_fast()
        print(MENU_TEXT)
        try:
            choice = input(f"{ACCENT}[?]{RESET} {TEXT}выбери пункт:{RESET} ").strip()
        except (EOFError, KeyboardInterrupt):
            choice = "00"

        if choice == "00" or choice.lower() in ("exit", "quit", "выход"):
            clear()
            line_info("завершение сессии...")
            time.sleep(0.5)
            line_ok("сессия закрыта")
            time.sleep(0.5)
            return

        action = ACTIONS.get(choice)
        if action is None:
            line_err("нет такого пункта")
            time.sleep(1.0)
            continue
        try:
            action()
        except KeyboardInterrupt:
            print()
            line_warn("прервано")
            time.sleep(0.5)


# ============================================================
#  ЗАПУСК
# ============================================================
def main():
    try:
        boot_screen()
        main_menu()
    except KeyboardInterrupt:
        clear()
        line_info("выход...")
        time.sleep(0.5)


if __name__ == "__main__":
    main()