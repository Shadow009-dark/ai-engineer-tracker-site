# AI Engineer Tracker — 180 günlük yol xəritəsi 🚀

Sıfırdan **AI Engineer** səviyyəsinə aparan **180 günlük (6 aylıq)** şəxsi öyrənmə izləyicisi.
Statik sayt (HTML + CSS + vanilla JS, build addımı yoxdur), GitHub Pages-də pulsuz yerləşir,
gedişatı **GitHub REST API** ilə öz reponuzda saxlayır və hər günü avtomatik commit + log faylına çevirir.

> Hazırdır: 9 faza · 180 gün · 746 tapşırıq · 335 video · 338 oxu materialı · 566 özünüyoxlama sualı · 26 təkrar günü
> Ümumi gündəlik yük: 2-4 saat (plan üzrə ümumi ~514 saat).

---

## 📋 Xüsusiyyətlər

**Gündəlik dashboard (əsas xüsusiyyət)**
- Bugün nə etməliyəm: mövzu, öyrəniləcək anlayışlar, tapşırıqlar, videolar, oxu materialları, günün nəticəsi
- Bugün nə öyrəndim: tamamlanmış elementlər və faiz (üzük göstəricisi + progress bar)
- Nə qaldı: bugün, bu həftə və ümumilikdə qalan elementlər
- İndiyə qədər bilməli olduğun suallar: bugünə qədər bütün günlərin özünüyoxlama sualları
- Gecikmiş günlər və "başqa günə köçür" düyməsi
- Streak, tamamlanmış günlər, ümumi və faza üzrə gedişat barları
- Həftəlik (7 gün) və aylıq (30 gün) qrafiklər — yalnız canvas, heç bir kitabxana yoxdur
- GitHub üslubunda contribution heatmap (son 26 həftə)
- Düymələr: ✅ Tamamlandı · ⏭️ Keç · 📝 Qeyd əlavə et · 📆 Köçür
- Günün refleksiyası: "Bu gün nə öyrəndim?", "Nə çətin oldu?", "Sabah nə edəcəm?"
- Təqvim: tamamlanmış / qismən / buraxılmış / gələcək / təkrar günləri

**GitHub inteqrasiyası**
- Hər əməliyyatdan sonra `data/progress.json` yenilənir və `logs/YYYY-MM-DD.md` yaranır
- Commit mesajı formatı: `Day 12: completed 4/5 tasks - Pandas basics`
- Token yalnız brauzerdə saxlanılır (localStorage), repoya **heç vaxt** düşmür
- Offline-first: internet yoxdursa və ya token yoxdursa, hər şey yerli saxlanılır və "sinxronla" düyməsi ilə sonra göndərilir
- GitHub Actions workflow README-də "Gün 45/180, 25% tamamlandı, 12 günlük streak" blokunu avtomatik yeniləyir

**Digər**
- Bütün planda axtarış və filtrləmə (faza, status, tip)
- Progress ixracı (JSON + Markdown hesabat) və JSON idxalı (heç bir element itmir)
- Planı sayt içindən redaktə etmək: gün əlavə et / sil / yuxarı-aşağı köçür / məzmunu dəyiş
- Klaviatura qısayolları (<kbd>D</kbd> <kbd>S</kbd> <kbd>R</kbd> <kbd>N</kbd> <kbd>/</kbd> <kbd>T</kbd> <kbd>1-6</kbd> <kbd>?</kbd> <kbd>Ctrl+S</kbd>)
- Dark/light rejim, mobil-uyğun (responsive) dizayn
- **Mentor Məsləhəti** bölməsi: necə öyrənmək, hansı portfolio layihələri, GitHub/Kaggle/LinkedIn, müsahibə, tipik səhvlər, nə overhyped-dir

---

## 📁 Qovluq strukturu

```
ai-engineer-tracker/
├── index.html                  # Bütün UI (Azerbaycan dilində)
├── style.css                   # Dark/light tema, responsive dizayn
├── app.js                      # Dashboard, təqvim, qrafiklər, plan redaktəsi, ixrac/idxal
├── github-sync.js              # GitHub Contents API + sha idarəsi + offline növbə
├── data/
│   ├── plan.json               # 180 günlük tam plan (9 faza, bütün günlər)
│   ├── progress.json           # Sizin gedişatınız (repo-da saxlanılır, repo-dan sinxronlanır)
│   └── mentor.json             # Mentor məsləhətləri + həftəlik məsləhətlər
├── logs/                       # Gündəlik jurnallar: logs/YYYY-MM-DD.md (avtomatik yaranır)
├── tests/
│   ├── sync-tests.html         # GitHub sync testləri (mock API, brauzerdə işləyir)
│   └── sync-tests.js           # 59 test: sha, konflikt, offline növbə, UTF-8 base64, merge
├── tools/
│   ├── generate_plan.py        # plan.json generatoru (fazaları günlərə çevirir)
│   ├── validate_plan.py        # plan.json struktur/ link yoxlaması
│   └── curriculum/             # Faza məzmunu (phase1.py ... phase9.py) + notes.py (AZ resurs izahları)
├── scripts/
│   └── update_readme.py        # README gedişat blokunu yeniləyir (Actions daxilində)
├── .github/workflows/
│   └── update-progress.yml     # Hər commit-də + hər gün README-ni yeniləyir
└── README.md
```

---

## 1️⃣ Quraşdırma: reponu yaratmaq və yerləşdirmək

### Lokal test (mütləq ilk addım)

Sayt `data/*.json` fayllarını `fetch` ilə oxuyur, ona görə onu birbaşa fayl kimi (`file://`) açmaq
brauzerdə bloklanır. Layihə qovluğunda sadə HTTP server işə salın:

```bash
cd ai-engineer-tracker
python -m http.server 8000
# brauzerdə aç: http://localhost:8000
```

### GitHub-da repo yaratmaq

1. GitHub-da sağ yuxarıdaki **+** → **New repository**.
2. **Repository name**: `ai-engineer-tracker` (adı fərqli olsa da olar — sonra Ayarlarda dəyişəcəksiniz).
3. **Public** seçin (GitHub Pages pulsuz yalnız public repolarda işləyir).
4. **Add a README file**, `.gitignore`, lisenziya — heç birini seçməyin (artıq hazırdır).
5. **Create repository**.

### Faylları push etmək

```bash
cd ai-engineer-tracker
git init -b main
git add .
git commit -m "İlk commit: 180 günlük AI Engineer planı"
git remote add origin https://github.com/Shadow009-dark/ai-engineer-tracker.git
git push -u origin main
```

> `gh` CLI varsa: `gh repo create Shadow009-dark/ai-engineer-tracker --public --source . --push`

---

## 2️⃣ GitHub Pages-də yerləşdirmək

1. Repo → **Settings** → sol menyuda **Pages**.
2. **Source**: `Deploy from a branch` → **Branch**: `main`, qovluq: `/ (root)` → **Save**.
3. 1-2 dəqiqə gözləyin. Saytın ünvanı:
   `https://shadow009-dark.github.io/ai-engineer-tracker/`
4. Saytı telefonda da açıb "Ana ekrana əlavə et" edə bilərsiniz (PWA kimi işləyir).

Sayt Pages-də işlədikdən sonra bütün sinxronizasiya da işləyir, çünki `fetch` üçün HTTPS lazımdır.

---

## 3️⃣ GitHub token necə yaradılır (təhlükəsiz, addım-addım)

Token yalnız sizin brauzerinizdə saxlanılır. Koda, repoya, ekran şəklinə **heç vaxt** düşməməlidir.

1. GitHub-da sağ yuxarıdaki profil şəklinə bas → **Settings**.
2. Sol menyunun ən aşağısında **Developer settings** → **Personal access tokens** → **Fine-grained tokens**.
3. **Generate new token** düyməsinə bas.
4. **Token name**: `ai-engineer-tracker`
5. **Expiration**: 90 gün (və ya 1 il). Vaxtı bitəndə yenisini yaradacaqsınız — bu normaldır.
6. **Repository access**: **Only select repositories** → yalnız `ai-engineer-tracker` seçin.
7. **Permissions** → **Repository permissions** → **Contents** → **Read and write**.
   Başqa heç bir icazə verməyin (bu, minimum zəruri icazədir).
8. **Generate token** → `github_pat_...` ilə başlayan açarı kopyalayın.
9. Saytda **⚙️ Ayarlar** → *Fine-grained Personal Access Token* sahəsinə yapışdırın →
   **🔑 Tokeni yadda saxla** → **🧪 Bağlantını yoxla**.
   "✅ Bağlantı uğurludur" mesajını görməlisiniz.

**Təhlükəsizlik qaydaları**
- Token-i heç vaxt fayla yazıb commit etməyin (sayt bunu etmir).
- Ekran şəklində, mesajda və ya chat-da paylaşmayın.
- Şübhələnsəniz: GitHub → **Revoke** → yenisini yaradın və saytda yeniləyin.
- Reponu `private` etsəniz də sayt işləyəcək (token Contents icazəsi ilə oxuyub yazır).

---

## 4️⃣ Başlanğıc tarixini təyin etmək

Sayt **Ayarlar → Başlanğıc tarixi** bölməsindən idarə olunur:

1. **⚙️ Ayarlar** → *Başlanğıc tarixi* → məsələn `2026-10-15`.
2. Gündəlik hədəf (dəqiqə) sahəsini də tənzimləyə bilərsiniz (standart 180 dəqiqə).
3. **💾 Yadda saxla** — bütün 180 günün tarixləri dərhal yenidən hesablanır.
   (Yalnız plan faylını yenidən yaratmaq istəyirsinizsə: `python tools/generate_plan.py --start 2026-10-15`)

Hər günün plan tarixi `başlanğıc tarixi + (sıra nömrəsi - 1)` düsturu ilə hesablanır.
Bir günü başqa tarixə köçürsəniz, yalnız o günün tarixi dəyişir.

---

## 5️⃣ Gündəlik istifadə (5 dəqiqəlik rutin)

| Vaxt | Nə etməli |
| --- | --- |
| Səhər (1 dəq) | Saytı aç → **📅 Bugün** → hero kartında günün mövzusunu oxu |
| İş zamanı | Tapşırıqları yerinə yetirdikcə checkbox-ları işarələ (<kbd>D</kbd> qısayolu növbəti tapşırığı işarələyir) |
| Video/oxu | Videoları izləyəndə və oxu materiallarını oxuyanda onların checkbox-unu da işarələ (gedişat faizi buna görə artır) |
| Sonda (3 dəq) | **Refleksiya** xanalarını doldur → **💾 Refleksiyanı yadda saxla** → bu `logs/YYYY-MM-DD.md` faylını GitHub-a göndərir |
| Günü bitir | **✅ Tamamlandı (D)** düyməsi və ya <kbd>D</kbd> — gün 100% olur və commit gedir |
| Gecikmə | **📆 Köçür (R)** ilə günü başqa tarixə keçir (gedişat itmir) |

**Klaviatura qısayolları**: <kbd>D</kbd> növbəti tapşırıq · <kbd>S</kbd> keç · <kbd>R</kbd> köçür ·
<kbd>N</kbd> qeyd · <kbd>/</kbd> axtarış · <kbd>T</kbd> tema · <kbd>1</kbd>-<kbd>6</kbd> bölmələr ·
<kbd>?</kbd> kömək · <kbd>Ctrl</kbd>+<kbd>S</kbd> sinxronla.

**Sinxronizasiya necə işləyir**
- Token varsa: hər əməliyyatdan ~2.5 saniyə sonra avtomatik sinxronlaşır (progress.json + bugünkü log).
- Token yoxdursa: hər şey yerli işləyir, şəbəkəyə heç bir sorğu getmir.
- GitHub əlçatmazsa (offline, limit, xəta): əməliyyat **növbəyə** düşür, yuxarıdaki status çipində
  "N gözləyən sinxronizasiya" yazır; **Ayarlar → 🔁 Növbəni boşalt** ilə sonra göndərilir.
- Hər sinxron iki fayl yaradır: `data/progress.json` (bütün gedişat) və `logs/YYYY-MM-DD.md`
  (həmin günün jurnalı). Contents API bir commit-də bir fayl yazdığı üçün bu, **iki commit** deməkdir
  (biri progress, biri log) — bu normaldır.

---

## 6️⃣ GitHub Actions: README-də avtomatik gedişat

`.github/workflows/update-progress.yml` faylı hər `data/progress.json` dəyişikliyindən sonra,
hər gün saat 06:00 UTC-də və əl ilə işə salındıqda `scripts/update_readme.py` skriptini işlədir və
README-dəki bu bloku yeniləyir:

<!-- PROGRESS:START -->

### 📊 Gedişat (avtomatik yenilənir)

![Progress](https://img.shields.io/badge/Gün_2%2F180-0%25-green?style=flat-square)

**Gün 2/180 · 0% tamamlandı · 0 günlük streak**

`░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░`

| Göstərici | Dəyər |
| --- | --- |
| Bugünkü mövzu | Gün 2 — Python təkrarı I: dəyişənlər, şərtlər, dövrlər, funksiyalar |
| Tamamlanmış gün | 0 (keçilmiş: 0) |
| Tamamlanmış element | 0 / 1985 |
| Ümumi öyrənmə vaxtı | 0 saat |
| Başlanğıc tarixi | 2026-10-08 |
| Son yenilənmə | 2026-10-09 |

#### Faza gedişatı

| Faza | Gedişat | Günlər |
| --- | --- | --- |
| 1. Python, Git/GitHub və Linux əsasları | 0% (0/231) | 0/21 |
| 2. Riyaziyyat: xətti cəbr, hesab, ehtimal və statistika | 0% (0/232) | 0/21 |
| 3. Data analizi: NumPy, Pandas, Matplotlib və SQL | 0% (0/231) | 0/21 |
| 4. Klassik maşın öyrənməsi (scikit-learn) | 0% (0/233) | 0/21 |
| 5. Dərin öyrənmə: PyTorch, CNN, RNN, Transformer | 0% (0/308) | 0/28 |
| 6. NLP və Böyük Dil Modelləri (LLM) | 0% (0/309) | 0/28 |
| 7. Kompüter görmə əsasları | 0% (0/155) | 0/14 |
| 8. MLOps və deployment | 0% (0/154) | 0/14 |
| 9. Portfolio, CV və müsahibə hazırlığı | 0% (0/132) | 0/12 |

<!-- PROGRESS:END -->

- Heç bir xarici action istifadə olunmur (yalnız `actions/checkout` + adi `git` əmrləri).
- Badge-i istəmirsinizsə `scripts/update_readme.py` faylında `badge` sətrini silin.
- Actions **Settings → Actions → General → Workflow permissions** bölməsində
  "Read and write permissions" seçilməlidir (workflow özü `permissions: contents: write` istəyir).

---

## 7️⃣ Planı dəyişmək və yenidən yaratmaq

Saytın içindən: **Plan** bölməsi → **✏️ Planı redaktə et** → günü redaktə et ✏️, sil 🗑️, yerini dəyiş ↑↓,
yeni gün əlavə et ➕. Dəyişikliklər `progress.json` içindəki `planOverrides` bölməsində saxlanılır və
sinxronlaşdırılır (yəni başqa cihazda da görünür).

**Statistika → ⬇️ Plan (JSON)** düyməsi redaktə olunmuş tam planı yükləyir; onu `data/plan.json` ilə
əvəz edib commit etsəniz, dəyişikliklər daimi plan olur.

Məzmunu koddan dəyişmək (tövsiyə olunan üsul):

```bash
# tools/curriculum/phaseN.py fayllarında günləri düzəldin, sonra:
python tools/generate_plan.py --start 2026-10-15
python tools/validate_plan.py       # struktur, link və say yoxlaması
```

---

## 8️⃣ Testlər

**GitHub sinxronizasiya testləri** (mock API — real token və şəbəkə lazım deyil):

```
http://localhost:8000/tests/sync-tests.html
```

Yoxlanılanlar: UTF-8/base64 çevrilməsi (Azərbaycan hərfləri daxil), yeni/mövcud fayl üçün `sha` davranışı,
409 konflikt zamanı yeni `sha` ilə təkrar cəhd, 401/403/rate-limit xəta tipləri, offline növbə və
`flush` bərpası, remote+yerli progress birləşməsi (heç bir tamamlanmış element itmir), commit mesajı formatı,
`logs/YYYY-MM-DD.md` məzmunu, `syncAll` ilə çoxlu log faylının göndərilməsi. **59 test — hamısı keçir.**

**Plan yoxlaması**: `python tools/validate_plan.py` — 180 gün, hər 7-ci gün təkrar, hər gündə 3-5 tapşırıq /
3-5 sual / 1-3 video, bütün video linkləri YouTube axtarış linki (uydurma video ID yoxdur).

---

## 9️⃣ 180 günün strukturu

| Faza | Günlər | Mövzu |
| --- | --- | --- |
| 1 | 1-21 | Python, Git/GitHub və Linux əsasları |
| 2 | 22-42 | Riyaziyyat: xətti cəbr, hesab, ehtimal və statistika |
| 3 | 43-63 | Data analizi: NumPy, Pandas, Matplotlib və SQL |
| 4 | 64-84 | Klassik maşın öyrənməsi (scikit-learn) |
| 5 | 85-112 | Dərin öyrənmə: PyTorch, CNN, RNN, Transformer |
| 6 | 113-140 | NLP və Böyük Dil Modelləri (prompt, RAG, agent, fine-tuning) |
| 7 | 141-154 | Kompüter görmə əsasları |
| 8 | 155-168 | MLOps və deployment (FastAPI, Docker, CI/CD, monitorinq) |
| 9 | 169-180 | Portfolio, CV və müsahibə hazırlığı |

Hər 7-ci gün **təkrar/istirahət günüdür** (120 dəqiqə): həftənin suallarını təkrar, quiz, gecikmiş
tapşırıqlar və **həftəlik layihə addımı**. Hər faza 2-4 həftədir və fazanın sonunda portfolio layihəsi var.

---

## 🔟 Gələcəkdə əlavə edilə biləcək təkmilləşdirmələr

1. **Service worker + PWA** — saytı tamamilə offline açmaq və telefonda native kimi istifadə etmək.
2. **Bildirişlər** — hər gün saat 20:00-da "bugünkü tapşırıqları bağla" xatırlatması (Web Push).
3. **Git Data API ilə tək commit** — progress.json + log faylını bir atomik commit-də göndərmək.
4. **Anki ixracı** — hər günün suallarını `.csv`/`.apkg` kimi Android Anki-yə ötürmək (spaced repetition avtomatik).
5. **Focus/vaxt izləyicisi** — Pomodoro sayğacı və real vaxt qeydi (indiki `minutes` sahəsi əl ilə doldurulur).
6. **AI köməkçi** — öz RAG-ınızı (Faza 6 layihəsi) sayta qoşub "bu mövzunu 3 sualla yoxla" funksiyası.
7. **Kaggle/LeetCode inteqrasiyası** — həmin günlərin hesab statistikasını avtomatik çəkmək.
8. **Çoxlu istifadəçi / şablon rejimi** — planı dostla paylaşmaq və leaderboard (GitHub OAuth ilə).
9. **iCal ixracı** — günləri Google Calendar-a abunə etmək.
10. **Xərc və GPU izləmə** — cloud xərcini qeyd edib hesabat çıxarmaq (Faza 8 üçün).
11. **Test əhatəsini artırmaq** — `app.js` üçün DOM testləri (JSDOM/Playwright) və plan generatoru üçün pytest.
12. **Çap/PDF hesabat** — 6 ayın sonunda avtomatik "yekun portfolio hesabatı".

---

## ℹ️ Qeydlər

- Bütün UI və plan məzmunu **Azərbaycan dilindədir**; kod, fayl adları və dəyişənlər **ingilis dilindədir**.
- Video linkləri **uydurulmamışdır**: hamısı `youtube.com/results?search_query=...` formatındadır (kanal + mövzu),
  beləliklə link heç vaxt "ölü" olmur. Oxu materialları tanınmış rəsmi sənədlərə və ya Google axtarışına yönəlir.
- İngilis dilli hər resursun altında **qısa Azərbaycanca izah** var ("nə verir və necə istifadə etməli"):
  məsələn *freeCodeCamp → "Sıfırdan başlayanlar üçün uzun, praktik kurs — özün də eyni vaxtda kod yaz."*.
  Bunlar kanal/mənbə tipini izah edir, konkret video məzmunu haqqında uydurma iddia etmir; 673 resursun
  hamısı üçün `tools/curriculum/notes.py` daxilindəki qaydalarla generasiya olunur.
- `data/plan.json` hər açılışda şəbəkədən yenidən oxunur (yenilənmiş plan dərhal görünsün); brauzerdəki kopya
  yalnız offline halda ehtiyat variant kimi istifadə olunur.
- Sənədlərdəki element ID sxemi: `d{ɡün}-t{task}`, `d{ɡün}-v{video}`, `d{ɡün}-r{reading}`, `d{ɡün}-m{mustKnow}`
  (məsələn `d12-t3` = 12-ci günün 3-cü tapşırığı).
- Gedişat brauzerdə (localStorage) və repo-da (`data/progress.json`) saxlanılır. Brauzer məlumatlarını
  təmizləsəniz də repo-dan geri gəlir — **Statistika → ⬆️ Progress idxal et** ilə də bərpa edə bilərsiniz.

Uğurlar! 180 gün sonra bu repo sizin ən güclü CV-niz olacaq. 💪
