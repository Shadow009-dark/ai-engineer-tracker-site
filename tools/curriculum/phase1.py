"""Phase 1 - Python for AI, Git/GitHub and Linux (days 1-21, 3 weeks, 18 study days)."""

from helpers import day, doc, gq, phase, yt

PY_TUT = "https://docs.python.org/3/tutorial/"
PEP8 = "https://peps.python.org/pep-0008/"
VENV = "https://docs.python.org/3/library/venv.html"
GIT_BOOK = "https://git-scm.com/book/en/v2"
GIT_BRANCHING = "https://learngitbranching.js.org/"
GH_START = "https://docs.github.com/en/get-started"
GH_SKILLS = "https://github.com/skills"
MISSING_SEM = "https://missing.csail.mit.edu/"
PYTEST = "https://docs.pytest.org/en/stable/"
RUFF = "https://docs.astral.sh/ruff/"
REQUESTS = "https://requests.readthedocs.io/en/latest/"
GH_ACTIONS = "https://docs.github.com/en/actions"
COLAB = "https://colab.research.google.com/"

days = [
    day(
        "Mühit qurulumu: Python, VS Code, terminal",
        [
            "Python interpreter, versiya yoxlama (python --version)",
            "VS Code + Python və Jupyter extension-ları",
            "Terminalda qovluq naviqasiyası (cd, ls, pwd)",
            "İlk skript: python main.py",
        ],
        [
            yt("Python for Beginners - Full Course", "freeCodeCamp", "4s 26d", "freeCodeCamp python for beginners full course"),
            yt("VS Code ilə Python qurulumu",  "Visual Studio Code", "12 d", "setup python in visual studio code"),
        ],
        [
            doc("Python rəsmi təlimatı (bölmə 1-3)", "docs.python.org", PY_TUT),
            doc("İnterpretatoru necə işə salmaq olar", "docs.python.org", "https://docs.python.org/3/using/index.html"),
        ],
        [
            "Python 3.12+ quraşdır və `python --version` çıxışını yoxla",
            "VS Code-da Python və Jupyter extension-larını quraşdır",
            "Terminalda `ai-journey` adlı qovluq yarat və ora `main.py` faylı qoy",
            "`print('Salam, AI Engineer!')` yazıb skripti işə sal",
        ],
        "İşləyən mühit + ilk Python skripti",
        [
            "Skript ilə interaktiv interpreter arasında fərq nədir?",
            "Niyə Python 3.12+ versiyasını seçirik?",
            "`cd` və `ls` nə edir?",
        ],
    ),
    day(
        "Python təkrarı I: dəyişənlər, şərtlər, dövrlər, funksiyalar",
        [
            "Dinamik tiplər: int, float, str, bool, None",
            "if / elif / else, müqayisə və məntiqi operatorlar",
            "for və while dövrləri, range(), break/continue",
            "Funksiyalar: parametrlər, qaytarılan dəyər, scope",
        ],
        [
            yt("Python Basics Crash Course", "freeCodeCamp", "1s 30d", "python basics crash course freecodecamp"),
            yt("Funksiyalar və scope izahı", "Corey Schafer", "20 d", "corey schafer python functions scope"),
        ],
        [
            doc("Rəsmi təlimat: idarəetmə axını", "docs.python.org", PY_TUT + "#more-control-flow-tools"),
            gq("PEP 8 üslub qaydaları", "peps.python.org", "PEP 8 python style guide"),
        ],
        [
            "FizzBuzz-u 2 fərqli üsulla yaz (dövr və list comprehension)",
            "Funksiya yaz: verilmiş tam ədədin sadə olub-olmadığını yoxlasın",
            "Funksiya yaz: sıralanmamış ədədlər siyahısının medianını hesablasın",
            "Bütün kodunu `pep8` qaydalarına uyğunlaşdır",
        ],
        "10 kiçik Python alqoritmi bir faylda (algorithms.py)",
        [
            "Python-da siyahı ilə tuple fərqi nədir?",
            "`for` dövrü içində `else` nə vaxt işə düşür?",
            "Funksiya daxilində dəyişənin scope-u necə işləyir?",
        ],
    ),
    day(
        "Python təkrarı II: kolleksiyalar və comprehension",
        [
            "list, tuple, dict, set və hansını nə vaxt seçmək",
            "Slicing, sort/sorted, key funksiyaları",
            "List/dict/set comprehension",
            "Kolleksiyaların time complexity-ə təsiri (O(n) intuition)",
        ],
        [
            yt("Python Data Structures", "Corey Schafer", "1s", "corey schafer python data structures playlist"),
            yt("Comprehensions və generatorlar", "Sentdex", "25 d", "python list comprehension sentdex"),
        ],
        [
            doc("Daxili tiplər", "docs.python.org", "https://docs.python.org/3/library/stdtypes.html"),
            doc("`collections` modulu", "docs.python.org", "https://docs.python.org/3/library/collections.html"),
        ],
        [
            "Sözlər tezliyini hesablayan funksiya yaz (dict ilə)",
            "Eyni hesablamanı `collections.Counter` ilə yaz və müqayisə et",
            "10 elementli siyahını comprehension ilə filtrələ",
            "İki siyahının kəsişməsini set ilə tap",
        ],
        "Klassik LeetCode asan səviyyəli 3 məsələ həlli",
        [
            "dict və set-də axtarış niyə O(1)-dir?",
            "List comprehension ilə generator expression fərqi nədir?",
            "`sorted()` nə vaxt `sort()`-dan üstündür?",
        ],
    ),
    day(
        "Fayllar, JSON və xəta idarəsi",
        [
            "open(), `with` bloku, encoding='utf-8' niyə vacibdir",
            "Fayl oxuma/yazma rejimləri (r, w, a)",
            "json.load / json.dump ilə struktur data",
            "try / except / finally, xüsusi exception-lar",
        ],
        [
            yt("Python File Objects və JSON", "Corey Schafer", "35 d", "corey schafer python files json"),
            yt("Exception handling ən yaxşı təcrübələr", "ArjanCodes", "18 d", "arjancodes exception handling python"),
        ],
        [
            doc("`json` modulu", "docs.python.org", "https://docs.python.org/3/library/json.html"),
            doc("Xətalar və exception-lar", "docs.python.org", "https://docs.python.org/3/tutorial/errors.html"),
        ],
        [
            "Proqram yaz: `notes.json` faylına qeyd əlavə et, oxu və sil",
            "Fayl tapılmadıqda xəta mesajı göstər (exception ilə)",
            "Encoding xətası yaratmaq üçün qəsdən səhv encoding istifadə et və düzəlt",
            "Bütün fayl əməliyyatlarını try/except ilə əhatə et",
        ],
        "Fayl əsaslı kiçik Notes CLI (əlavə et / siyahıla / sil)",
        [
            "Niyə `with open(...)` istifadə edirik?",
            "`except ValueError` ilə `except Exception` fərqi nədir?",
            "JSON ilə CSV fərqi nə vaxt önəmli olur?",
        ],
    ),
    day(
        "OOP əsasları: class, metodlar, inheritance",
        [
            "class, __init__, self, atribut və metodlar",
            "Encapsulation: _protected, __private konvensiyaları",
            "Inheritance və polymorphism",
            "Nə vaxt OOP, nə vaxt sadə funksiya (over-engineering-dən qaçın)",
        ],
        [
            yt("Python OOP Full Course", "Corey Schafer", "1s 30d", "corey schafer python oop tutorial"),
            yt("OOP dizayn prinsipləri", "ArjanCodes", "25 d", "arjancodes python oop design principles"),
        ],
        [
            doc("Siniflər haqqında təlimat", "docs.python.org", "https://docs.python.org/3/tutorial/classes.html"),
            gq("SOLID prinsipləri Python-da", "realpython.com", "SOLID principles python"),
        ],
        [
            "`Model` adlı əsas sinif yarat: `fit`, `predict` metodları olan sadə quruluş",
            "`LinearModel` sinfini `Model`-dən miras al və metodlarını override et",
            "`__repr__` və `__str__` metodlarını yaz",
            "Kiçik data pipeline-ı OOP ilə yaz (Reader -> Cleaner -> Writer)",
        ],
        "Miras və polimorfizm nümayiş etdirən ML-ə bənzər sinif iyerarxiyası",
        [
            "`self` nədir və niyə lazımdır?",
            "Method overriding ilə overloading fərqi nədir?",
            "Kompozisiya nə vaxt mirasdan daha yaxşıdır?",
        ],
    ),
    day(
        "Type hints, dataclass, generator, decorator",
        [
            "Type hints: List[int], Optional, Union, Callable",
            "dataclass ilə data saxlama sinifləri",
            "Generator funksiyalar və `yield`",
            "Decorator mexanizmi (funksiyanı funksiyaya ötürmək)",
        ],
        [
            yt("Python Type Hints tam kurs", "ArjanCodes", "40 d", "arjancodes python type hints"),
            yt("Generators və decorators", "Corey Schafer", "45 d", "corey schafer python generators decorators"),
        ],
        [
            doc("`typing` modulu", "docs.python.org", "https://docs.python.org/3/library/typing.html"),
            doc("`dataclasses` modulu", "docs.python.org", "https://docs.python.org/3/library/dataclasses.html"),
        ],
        [
            "Bütün əvvəlki gün alqoritmlərinə type hint əlavə et",
            "`Experiment` dataclass-ı yarat (model adı, parametrlər, nəticə, tarix)",
            "Böyük faylı sətir-sətir oxuyan generator yaz",
            "Funksiya çağırışını ölçən `@timer` decorator yaz",
        ],
        "Type hint-lı, dataclass istifadə edən təmiz kod nümunəsi",
        [
            "Type hint runtime-da nə edir?",
            "Generator niyə yaddaşa qənaət edir?",
            "Decorator necə işləyir (sintaktik şəkər)?",
        ],
    ),
    day(
        "Layihə strukturu və asılılıq idarəsi",
        [
            "venv ilə izolyasiya olunmuş mühit",
            "pip, requirements.txt, versiya pinning",
            "Layihə strukturu: src/, tests/, data/, README.md, .gitignore",
            ".env faylları və konfiqurasiyanın koddan ayrılması",
        ],
        [
            yt("Virtual Environments", "Corey Schafer", "15 d", "corey schafer python virtual environment venv"),
            yt("Python layihə strukturu", "ArjanCodes", "22 d", "python project structure best practices"),
        ],
        [
            doc("`venv` rəsmi sənədi", "docs.python.org", VENV),
            doc("requirements faylları", "pip docs", "https://pip.pypa.io/en/stable/reference/requirements-file-format/"),
        ],
        [
            "Yeni layihə qovluğu yarat və venv qur",
            "requirements.txt yarat və 3 paketi pin et",
            "`.gitignore` faylı yaz (venv, __pycache__, .env, .ipynb_checkpoints)",
            "README.md yaz: layihə nədir, necə quraşdırılır, necə işə salınır",
        ],
        "Git-ə hazır, təmiz Python layihə skeleti",
        [
            "venv mühiti hansı problemin həllidir?",
            "Niyə versiyaları pin edirik?",
            "`.env` faylı niyə Git-ə əlavə olunmamalıdır?",
        ],
    ),
    day(
        "Git I: versiya nəzarətinin əsasları",
        [
            "git init, add, commit, status, log, diff",
            "Working directory / staging / repository üçlüyü",
            "Yaxşı commit mesajı yazma qaydaları",
            "gitignore və böyük fayllar (Git LFS-ə qısa baxış)",
        ],
        [
            yt("Git and GitHub for Beginners", "freeCodeCamp", "1s 10d", "freecodecamp git and github for beginners"),
            yt("Git əsasları izahı", "Corey Schafer", "35 d", "corey schafer git tutorial"),
        ],
        [
            doc("Pro Git kitabı (bölmə 1-2)", "git-scm.com", GIT_BOOK),
            gq("Yaxşı commit mesajı necə yazılır", "conventionalcommits.org", "conventional commits guide"),
        ],
        [
            "Layihəni git repo-ya çevir və ilk commit-i et",
            "3 fərqli dəyişiklik edib 3 ayrı commit yaz",
            "`git log --oneline --graph` çıxışını oxu",
            "Səhv commit mesajını `git commit --amend` ilə düzəlt",
        ],
        "Tarixçəsi təmiz, mənalı commit-ləri olan repo",
        [
            "Staging area nə üçün lazımdır?",
            "`git diff` ilə `git diff --staged` fərqi nədir?",
            "Commit mesajı niyə vacibdir?",
        ],
    ),
    day(
        "Git II: branch, merge, konflikt, remote",
        [
            "Branch yaratmaq, keçmək, silmək",
            "Merge və merge conflict-in həlli",
            "Remote: origin, push, pull, fetch",
            "Rebase nədir və nə vaxt istifadə olunur",
        ],
        [
            yt("Git Branching and Merging", "freeCodeCamp", "50 d", "git branching merging tutorial"),
            yt("Learn Git Branching (interaktiv)", "learngitbranching.js.org", "45 d", "learn git branching interactive"),
        ],
        [
            doc("Pro Git: Branching", "git-scm.com", GIT_BOOK + "/v2/Git-Branching-Branches-in-a-Nutshell"),
            doc("İnteraktiv Git məşqi", "learngitbranching.js.org", GIT_BRANCHING),
        ],
        [
            "`feature/notes-cli` branch-ı yarat və dəyişiklik et",
            "Qəsdən merge konflikti yarat və həll et",
            "Bütün branch-ları `main`-ə merge et",
            "GitHub-da boş repo yarat və `git push -u origin main` et",
        ],
        "GitHub-da push olunmuş repo + ən azı 2 branch tarixçəsi",
        [
            "Merge ilə rebase fərqi nədir?",
            "Merge konflikti nə vaxt yaranır?",
            "`git fetch` ilə `git pull` fərqi nədir?",
        ],
    ),
    day(
        "GitHub: profil, PR axını, ilk açıq mənbə addımı",
        [
            "GitHub profili və README (profile README)",
            "Issue, Pull Request, review axını",
            "Fork və açıq mənbə layihələrə töhfə vermək",
            "GitHub CLI (gh) əsas əmrləri",
        ],
        [
            yt("GitHub Pull Request axını", "GitHub", "20 d", "github pull request workflow tutorial"),
            yt("GitHub profili necə güclü olur", "Fireship", "12 d", "how to make github profile stand out"),
        ],
        [
            doc("GitHub rəsmi başlanğıc sənədləri", "docs.github.com", GH_START),
            doc("GitHub Skills (praktiki kurslar)", "github.com/skills", GH_SKILLS),
        ],
        [
            "`Shadow009-dark` profil README-ni yarat və doldur",
            "Repo-da issue aç, branch-da işlə, PR aç və merge et",
            "`.github/ISSUE_TEMPLATE` və PR template əlavə et",
            "`gh repo create` ilə bir repo-nu komanda sətrindən yarat",
        ],
        "Peşəkar görünüşlü GitHub profili və bir tamamlanmış PR",
        [
            "Fork ilə branch fərqi nədir?",
            "PR review zamanı nəyə baxılır?",
            "Profil README niyə faydalıdır?",
        ],
    ),
    day(
        "Linux I: terminal, fayl sistemi, icazələr",
        [
            "Fayl sistemi iyerarxiyası (/home, /etc, /usr, /tmp)",
            "Əsas əmrlər: ls, cd, cp, mv, rm, mkdir, find",
            "İcazələr: chmod, chown, rwx",
            "Proseslər: ps, top, kill, nohup",
        ],
        [
            yt("Linux Command Line Full Course", "freeCodeCamp", "5s", "freecodecamp linux command line full course"),
            yt("Missing Semester: Shell", "MIT Missing Semester", "1s", "missing semester shell lecture"),
        ],
        [
            doc("Missing Semester (MIT kursu)", "missing.csail.mit.edu", MISSING_SEM),
            doc("Ubuntu CLI təlimatı", "ubuntu.com", "https://ubuntu.com/tutorials/command-line-for-beginners"),
        ],
        [
            "WSL2 və ya Linux VM qur (Windows-da)",
            "10 fayllı qovluq yarat, kopyala, adını dəyiş, sil",
            "Fayl icazələrini `chmod 644` və `chmod 755` edərək müqayisə et",
            "Arxa fonda işləyən prosesi tap və dayandır",
        ],
        "Komanda sətrində fayl sistemi ilə sərbəst işləmək bacarığı",
        [
            "`/etc` qovluğunda nə saxlanılır?",
            "`chmod 755` nə deməkdir?",
            "`kill -9` nə edir?",
        ],
    ),
    day(
        "Linux II: pipe, grep, mühit dəyişənləri, SSH",
        [
            "Pipe (|), redirection (>, >>), tee",
            "grep, find, xargs, wc, sort, uniq",
            "Mühit dəyişənləri və PATH",
            "SSH açarları və remote serverə qoşulma",
        ],
        [
            yt("Linux Text Processing: grep, sed, awk", "DistroTube", "40 d", "grep sed awk tutorial linux"),
            yt("SSH və SSH açarları", "NetworkChuck", "25 d", "ssh keys explained networkchuck"),
        ],
        [
            doc("GNU Coreutils sənədi", "gnu.org", "https://www.gnu.org/software/coreutils/manual/"),
            gq("Linux-da awk ilə data emalı", "gnu.org", "awk tutorial linux data processing"),
        ],
        [
            "Böyük log faylı yarat və `grep` + `wc -l` ilə filtrlə",
            "`sort | uniq -c | sort -rn` zəncirini data saymaq üçün istifadə et",
            "PATH-ə yeni qovluq əlavə et və effektini göstər",
            "SSH açarı yarat və GitHub-a əlavə et (parolsuz push)",
        ],
        "Terminalda log analizi edən 3 əmr zənciri (qeyd et, README-yə əlavə et)",
        [
            "Pipe nə edir?",
            "`>` ilə `>>` fərqi nədir?",
            "SSH açarı paroldan niyə daha təhlükəsizdir?",
        ],
    ),
    day(
        "Bash skriptləri və Makefile",
        [
            "Bash dəyişənləri, if, for, funksiyalar",
            "Skript icazələri və shebang (#!)",
            "Cron ilə avtomatik işlər",
            "Makefile ilə təkrarlanan əmrləri qısaltmaq",
        ],
        [
            yt("Bash Scripting Full Course", "freeCodeCamp", "1s 30d", "bash scripting full course freecodecamp"),
            yt("Makefile-lar ağrısız izah", "DistroTube", "25 d", "makefile tutorial beginners"),
        ],
        [
            doc("Bash manual", "gnu.org", "https://www.gnu.org/software/bash/manual/bash.html"),
            doc("Makefile Tutorial", "makefiletutorial.com", "https://makefiletutorial.com/"),
        ],
        [
            "`backup.sh` yaz: data qovluğunu tarixli zip edib başqa qovluğa atsın",
            "`activate.sh` yaz: venv-i aktivləşdirib skripti işə salsın",
            "Makefile yaz: `make setup`, `make test`, `make run` hədəfləri ilə",
            "Skriptlərdə xəta olsa dayanmağı təmin et (`set -e`)",
        ],
        "Layihədə işləyən Makefile + 2 bash skripti",
        [
            "Shebang sətri nə edir?",
            "`set -euo pipefail` nəyi təmin edir?",
            "Makefile nə üçün faydalıdır?",
        ],
    ),
    day(
        "Testlər, logging və kod keyfiyyəti",
        [
            "pytest: assert, fixture, parametrize",
            "logging modulu (səviyyələr, format, fayl)",
            "argparse ilə CLI interfeys",
            "ruff/black ilə avtomatik formatlama və linting",
        ],
        [
            yt("pytest tam kurs", "mCoding", "35 d", "pytest full tutorial python testing"),
            yt("Logging ən yaxşı təcrübələri", "ArjanCodes", "20 d", "arjancodes python logging best practices"),
        ],
        [
            doc("pytest sənədləri", "docs.pytest.org", PYTEST),
            doc("ruff (linter + formatter)", "astral.sh", RUFF),
        ],
        [
            "Əvvəlki günlərin funksiyaları üçün 10 pytest testi yaz",
            "`parametrize` ilə test hallarını cədvəl kimi yaz",
            "`print` yerinə logging istifadə et",
            "`ruff check .` və `ruff format .` işlədin, xətaları düzəlt",
        ],
        "Testləri keçən, formatlanmış, logging-li Python modulu",
        [
            "Unit test ilə integration test fərqi nədir?",
            "Fixture nə üçün istifadə olunur?",
            "Logging `print`-dən niyə üstündür?",
        ],
    ),
    day(
        "HTTP, JSON API-lər, .env və secret idarəsi",
        [
            "HTTP metodları, status kodları, başlıqlar",
            "requests ilə API çağırışı, timeout, retry",
            "Token/API key saxlama qaydaları (.env, .gitignore)",
            "REST API dizaynının əsasları",
        ],
        [
            yt("HTTP və REST API izahı", "Web Dev Simplified", "25 d", "http rest api explained beginners"),
            yt("Python requests kitabxanası", "Corey Schafer", "25 d", "python requests library tutorial"),
        ],
        [
            doc("requests sənədləri", "requests.readthedocs.io", REQUESTS),
            doc("12-Factor App: konfiqurasiya", "12factor.net", "https://12factor.net/config"),
        ],
        [
            "Açıq API-dən (məs. GitHub API) data çəkən skript yaz",
            "Timeout, status yoxlaması və retry əlavə et",
            "Token-i `.env` faylından oxu (`python-dotenv`), koda yazma",
            "Xəta hallarını (404, 401, 500) simulyasiya et və idarə et",
        ],
        "API-dən data çəkib yadda saxlayan təhlükəsiz skript",
        [
            "401 ilə 403 fərqi nədir?",
            "API açarı niyə koda yazılmamalıdır?",
            "Retry zamanı nəyə diqqət etmək lazımdır?",
        ],
    ),
    day(
        "GitHub Actions ilə ilk CI pipeline",
        [
            "Workflow, job, step, runner anlayışları",
            "YAML sintaksisi və `on:` trigger-ləri",
            "Python layihəsi üçün test işlədən workflow",
            "Badge-lər (build status) README-də",
        ],
        [
            yt("GitHub Actions Full Course", "TechWorld with Nana", "1s", "github actions tutorial beginners techworld with nana"),
            yt("CI/CD nədir", "Fireship", "10 d", "ci cd explained fireship"),
        ],
        [
            doc("GitHub Actions sənədləri", "docs.github.com", GH_ACTIONS),
            doc("Workflow sintaksisi", "docs.github.com", GH_ACTIONS + "/workflows-and-actions/workflow-syntax"),
        ],
        [
            "`.github/workflows/tests.yml` yaz: push-da pytest işlətsin",
            "Matrix ilə 2 Python versiyasında test et",
            "Ruff lint addımını workflow-a əlavə et",
            "Yeşil badge-i README-yə əlavə et",
        ],
        "Push edəndə avtomatik test işlədən CI pipeline",
        [
            "CI nədir və nə problemi həll edir?",
            "Workflow hansı hadisələrlə tetiklenir?",
            "Test uğursuz olsa nə baş verir?",
        ],
    ),
    day(
        "Notebook mühiti: Colab, Jupyter, ilk GPU təcrübəsi",
        [
            "Jupyter notebook vs .py skript: nə vaxt hansı",
            "Google Colab: GPU/TPU, fayl saxlama, davamlılıq",
            "Notebook təmizliyi: xanaların sırası, təkrar işə salma probleminin qarşısı",
            "Reproducibility: seed, versiya qeydi",
        ],
        [
            yt("Jupyter Notebook tam təlimat", "Corey Schafer", "35 d", "jupyter notebook tutorial corey schafer"),
            yt("Google Colab GPU istifadəsi", "Nicholas Renotte", "20 d", "google colab gpu tutorial"),
        ],
        [
            doc("Google Colab", "colab.research.google.com", COLAB),
            gq("Notebook ən yaxşı təcrübələri", "jupyter.org", "jupyter notebook best practices reproducibility"),
        ],
        [
            "Colab-da notebook aç, GPU-nu aktivləşdir və yoxla",
            "Noutbukda 3 xanalı mini analiz yaz (data yüklə, hesabla, qrafik çək)",
            "Noutbuku `Restart and run all` edərək xətasız işlədiyini təsdiqlə",
            "Noutbuku GitHub-a `.ipynb` kimi push et",
        ],
        "Başdan sona işləyən, GitHub-da olan ilk notebook",
        [
            "Notebook-un əsas riski nədir (gizli vəziyyət)?",
            "Colab sessiyası niyə itə bilər?",
            "`Restart and run all` niyə vacibdir?",
        ],
    ),
    day(
        "Faza 1 layihəsi: Python CLI + testlər + CI",
        [
            "Bütün faza biliklərinin tətbiqi",
            "Layihə planlaşdırma: tələblər, strukturu, README",
            "Kodun modullara bölünməsi",
            "Öz işini özün qiymətləndirmə",
        ],
        [
            yt("Kiçik Python layihəsi necə qurulur", "ArjanCodes", "30 d", "build small python project structure arjancodes"),
            yt("CLI alətini paylaşıla bilən etmək", "mCoding", "20 d", "python cli tool packaging tutorial"),
        ],
        [
            doc("Python Packaging təlimatı", "packaging.python.org", "https://packaging.python.org/en/latest/tutorials/packaging-projects/"),
            gq("Layihə README şablonu", "github.com", "github readme template for python projects"),
        ],
        [
            "`study-tracker-cli` layihəsini qur: öyrənmə qeydlərini CLI-dan idarə etsin",
            "Ən azı 8 pytest testi yaz",
            "GitHub Actions ile testləri avtomatlaşdır",
            "README-də skrinşot və istifadə nümunələri əlavə et",
        ],
        "GitHub-da tamamlanmış `study-tracker-cli` layihəsi (yaşıl CI badge ilə)",
        [
            "Layihə strukturu necə olmalıdır və niyə?",
            "Testlər kodun hansı hissəsini əhatə edir?",
            "Növbəti dəfə nəyi daha yaxşı edərdin?",
        ],
    ),
]

weeks = [
    {
        "focus": "Python əsasları",
        "project": "Python əsasları: fayldan sual oxuyan CLI quiz proqramı (10 sual, hesab toplama)",
        "quiz": "Python tipləri, dövrlər, funksiyalar və kolleksiyalar üzrə 10 sual",
    },
    {
        "focus": "Git, GitHub və alət zənciri",
        "project": "Şəxsi repo: öyrəndiklərini README-də sənədləşdir, ilk PR aç, `.gitignore` və issue template qur",
        "quiz": "Git əmrləri, branch/merge axını və PR prosesi üzrə 10 sual",
    },
    {
        "focus": "Linux, test və CI",
        "project": "Repo şablonu: pytest + ruff + GitHub Actions CI işləyən başlanğıc şablonu",
        "quiz": "Terminal, icazələr, pytest və CI anlayışları üzrə 10 sual",
    },
]

PHASE = phase(
    1,
    "Python, Git/GitHub və Linux əsasları",
    "AI üçün lazım olan Python mühəndisliyi təməlini qurmaq: təmiz kod, test, versiya nəzarəti və terminal.",
    "54-62 saat",
    weeks,
    days,
)
