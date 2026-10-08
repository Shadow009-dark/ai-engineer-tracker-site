"""Phase 9 - Portfolio, CV and interview preparation (days 169-180, 2 weeks, 10 study days)."""

from helpers import day, doc, gq, phase, yt

INTERVIEWS_BOOK = "https://huyenchip.com/ml-interviews-book/"
CHIP_BLOG = "https://huyenchip.com/blog/"
MADE = "https://madewithml.com/"
GH_PROFILE = "https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/about-your-profile"
GH_SKILLS = "https://github.com/skills"
KAGGLE = "https://www.kaggle.com/competitions"
ESL = "https://www.statlearning.com/"
SK = "https://scikit-learn.org/stable/"
LEETCODE = "https://leetcode.com/"
ROADMAP = "https://roadmap.sh/ai-engineer"
HF_PAPERS = "https://huggingface.co/papers"
DESIGN_ML = "https://github.com/chiphuyen/machine-learning-systems-design"
CRACK_ML = "https://github.com/khangich/machine-learning-interview"
STAR = "https://www.themuse.com/advice/star-interview-method"

days = [
    day(
        "Portfolio strategiyası: hansı layihələr işə götürənləri inandırır",
        [
            "İşə götürənin AI Engineer-dən gözlədikləri",
            "3 layihə qaydası: dərinlik, ölçü, təsir",
            "Zəif və güclü layihə nümunələri",
            "Portfolio-nun strukturlaşdırılması",
        ],
        [
            yt("Portfolio layihələri necə seçilir", "Ken Jee", "30 d", "data science portfolio projects hire"),
            yt("AI Engineer rol və tələblər", "AI Engineer (Latent Space)", "35 d", "ai engineer role requirements portfolio"),
        ],
        [
            doc("AI Engineer roadmap", "roadmap.sh", ROADMAP),
            doc("Chip Huyen bloqu", "huyenchip.com", CHIP_BLOG),
        ],
        [
            "Vakansiya elanlarını analiz et və 10 tələb çıxart",
            "Öz 5 layihəni siyahıya al və güclü/zəif tərəflərini yaz",
            "3 layihə seç (biri LLM, biri CV/klasik ML, biri MLOps)",
            "Hər biri üçün təkmilləşdirmə planı yaz",
        ],
        "Layihə seçimi + təkmilləşdirmə planı (bacarıq boşluqları ilə)",
        [
            "Hansı layihə ən çox təsir bağışlayır?",
            "Portfolio-da hansı bacarıq çatışmır?",
            "Nəyi silmək lazımdır?",
        ],
    ),
    day(
        "Portfolio cilalama I: kod və README keyfiyyəti",
        [
            "Repo gigiyenası: struktur, lisenziya, .gitignore",
            "README strukturu (problem, yanaşma, nəticə, necə işə salınır)",
            "Testlər və təkrar işlədilə bilənlik",
            "Kod oxunaqlılığı və tipik səhvlər",
        ],
        [
            yt("Layihə README necə yazılır", "Krish Naik", "25 d", "how to write a great readme machine learning"),
            yt("Kodu portfolioda necə göstərmək", "ArjanCodes", "30 d", "clean code portfolio project python"),
        ],
        [
            doc("GitHub profil sənədləri", "docs.github.com", GH_PROFILE),
            doc("Make a README", "makeareadme.com", "https://www.makeareadme.com/"),
        ],
        [
            "Bir layihəni tam yenidən sənədləşdir",
            "Test əhatəsini artır (ən azı 5 test)",
            "requirements faylını təmizlə və versiyaları pin et",
            "Lisenziya və .gitignore əlavə et",
        ],
        "Cilalanmış repo: README + testlər + təmiz struktur",
        [
            "README-də hansı 3 sual cavablanmalıdır?",
            "Testlər niyə işə götürəni inandırır?",
            "Repo-da nə artıq yükdür?",
        ],
    ),
    day(
        "Portfolio cilalama II: demo, video və canlı link",
        [
            "Canlı demo (HF Spaces, Streamlit Cloud, Vercel)",
            "2 dəqiqəlik demo videosu ssenarisi",
            "Arxitektura diaqramı",
            "Nəticələrin rəqəmlərlə təqdimatı",
        ],
        [
            yt("Layihə demo videosu necə çəkilir", "Ken Jee", "25 d", "project demo video data science portfolio"),
            yt("Streamlit ilə UI qurmaq", "Streamlit / Data Professor", "35 d", "streamlit app tutorial data science"),
        ],
        [
            doc("Streamlit sənədləri", "docs.streamlit.io", "https://docs.streamlit.io/"),
            doc("Hugging Face Spaces", "huggingface.co", "https://huggingface.co/docs/hub/spaces"),
        ],
        [
            "Bir layihə üçün canlı demo yayımla",
            "Demo videosu çək (2 dəqiqə, problem -> nəticə)",
            "Arxitektura diaqramını README-yə əlavə et",
            "Nəticələri rəqəmlərlə cədvəldə ver",
        ],
        "Canlı demo + video + diaqram (bir layihə tam hazır)",
        [
            "Demo videoda ilk 15 saniyədə nə göstərmək lazımdır?",
            "Canlı link nə üçün vacibdir?",
            "Hansı rəqəm ən güclü təsir bağışlayır?",
        ],
    ),
    day(
        "GitHub profili və README ekosistemi",
        [
            "Profil README dizaynı",
            "Pinned repos və təşkilatlanma",
            "Contribution graph-a baxış",
            "Profilin rekruiter üçün optimallaşdırılması",
        ],
        [
            yt("GitHub profili necə gücləndirilir", "Fireship", "12 d", "github profile readme ideas"),
            yt("Portfolio GitHub-da necə qurulur", "Krish Naik", "25 d", "github portfolio for data science jobs"),
        ],
        [
            doc("GitHub Skills", "github.com/skills", GH_SKILLS),
            doc("GitHub profil sənədləri", "docs.github.com", GH_PROFILE),
        ],
        [
            "Profil README-i yaz (kim olduğun, nə edirsən, layihələr)",
            "6 repo-nu pin et və başlıqları aydın et",
            "Hər pin edilmiş reponun README-sini yoxla",
            "Profili yeni istifadəçi gözü ilə qiymətləndir (30 saniyə testi)",
        ],
        "Rekruiter üçün optimallaşdırılmış GitHub profili",
        [
            "30 saniyədə profildən nə oxunur?",
            "Hansı repo pin edilməlidir?",
            "Problemli repo-lar necə arxivlənməlidir?",
        ],
    ),
    day(
        "LinkedIn və CV optimallaşdırması",
        [
            "AI Engineer CV strukturur (təcrübə, layihələr, bacarıqlar)",
            "Nəticə əsaslı bullet-lar (rəqəmlərlə)",
            "LinkedIn profili və şəbəkə",
            "ATS (avtomatik filtr) üçün açarlar sözlər",
        ],
        [
            yt("CV necə yazılır (texniki vəzifə)", "Ken Jee", "35 d", "data science resume tips"),
            yt("LinkedIn optimallaşdırma", "Alex The Analyst", "30 d", "linkedin profile optimization data"),
        ],
        [
            doc("STAR metodu", "themuse.com", STAR),
            doc("Chip Huyen: müsahibə kitabı", "huyenchip.com", INTERVIEWS_BOOK),
        ],
        [
            "CV-ni 1 səhifəyə sal və layihələri nəticə ilə yaz",
            "LinkedIn başlığını və bio-nu yenilə",
            "5 vakansiya elanı ilə CV-ni müqayisə et (açar sözlər)",
            "2 təcrübə bullet-unu rəqəmlərlə yenidən yaz",
        ],
        "Yenilənmiş CV + LinkedIn profili (açar sözlərlə uyğunlaşdırılmış)",
        [
            "Bullet-larda nəticə necə göstərilir?",
            "ATS filtri nəyi axtarır?",
            "CV-də nəyi çıxarmaq lazımdır?",
        ],
    ),
    day(
        "Kaggle və açıq mənbə strategiyası",
        [
            "Kaggle competitions-da iştirak strategiyası",
            "Notebook-ları ictimaiyə faydalı etmək",
            "Açıq mənbə layihələrə ilk töhfələr",
            "Icma qurmaq və görünmək",
        ],
        [
            yt("Kaggle competition strategiyası", "Abhishek Thakur", "40 d", "kaggle competition strategy tips"),
            yt("Açıq mənbəyə necə töhfə vermək", "Fireship", "20 d", "contributing to open source first pull request"),
        ],
        [
            doc("Kaggle competitions", "kaggle.com", KAGGLE),
            doc("Hugging Face Papers", "huggingface.co", HF_PAPERS),
        ],
        [
            "Bir Kaggle competition seç və qoşul",
            "Notebook yazıb yayımla (kamida 5 upvote almağa çalış)",
            "Kiçik açıq mənbə töhfəsi et (sənəd düzəlişi və ya test)",
            "Öyrəndiklərini LinkedIn-də paylaş",
        ],
        "Kaggle notebooku + 1 açıq mənbə töhfəsi (PR)",
        [
            "Kaggle-da dərəcə necə qazanılır?",
            "Açıq mənbə töhfəsi niyə CV-də dəyərlidir?",
            "Necə davamlı öyrənmə vərdişi qurmaq olar?",
        ],
    ),
    day(
        "Müsahibə hazırlığı II: ML nəzəriyyəsi",
        [
            "Supervised learning sualları",
            "Model qiymətləndirmə və metrikalar",
            "Overfitting/underfitting və regulyarizasiya",
            "Tipik ML sualları və cavab strukturu",
        ],
        [
            yt("Machine Learning müsahibə sualları", "Krish Naik", "1s", "machine learning interview questions answers"),
            yt("ML nəzəriyyəsi müsahibə hazırlığı", "Andrew Ng / DeepLearning.AI", "40 d", "machine learning theory interview prep"),
        ],
        [
            doc("ML Interviews Book (Chip Huyen)", "huyenchip.com", INTERVIEWS_BOOK),
            doc("ISLR (təkrar bölmələr)", "statlearning.com", ESL),
        ],
        [
            "100 ML sualı siyahısı hazırla və 50-nə yazılı cavab ver",
            "Bias-variance-ı 2 dəqiqədə izah et",
            "Metrikaları hansı halda seçəcəyini yaz",
            "Zəif mövzular üçün təkrar planı qur",
        ],
        "50 sual-cavab ML müsahibə qeydi",
        [
            "Bias-variance tradeoff-u necə izah edərdin?",
            "Precision/recall balansını necə seçərdin?",
            "Hansı mövzularda zəifsən?",
        ],
    ),
    day(
        "Müsahibə hazırlığı III: kodlaşdırma və SQL",
        [
            "Alqoritmik suallar (array, string, dict)",
            "Pandas/SQL müsahibə tapşırıqları",
            "Data emalı sualları (canlı kodlaşdırma)",
            "Kod yazarkən danışma texnikası",
        ],
        [
            yt("LeetCode strategiyası", "NeetCode", "40 d", "leetcode patterns coding interview strategy"),
            yt("SQL müsahibə sualları", "Alex The Analyst", "40 d", "sql interview questions solutions"),
        ],
        [
            doc("LeetCode", "leetcode.com", LEETCODE),
            doc("ML coding interview materialları", "github.com", CRACK_ML),
        ],
        [
            "Asan səviyyədə 10 LeetCode məsələsi həll et",
            "5 SQL müsahibə sualını yaz və izah et",
            "Pandas ilə 3 data emalı tapşırığı həll et",
            "Hər həlli səsli izah et (yarım saat)",
        ],
        "30 kodlaşdırma/SQL həlli + izahlar",
        [
            "Hansı pattern-ləri bilmək lazımdır?",
            "Canlı kodlaşdırmada necə düşünməyi izah edirsən?",
            "SQL-də ən çox hansı suallar verilir?",
        ],
    ),
    day(
        "Müsahibə hazırlığı IV: ML system design",
        [
            "System design sualının strukturu",
            "Data, model, xidmət və monitorinq hissələri",
            "Tövsiyə sistemi / axtarış / RAG dizaynı nümunələri",
            "Miqyas və xərc mülahizələri",
        ],
        [
            yt("ML system design müsahibəsi", "Exponent", "45 d", "machine learning system design interview"),
            yt("RAG sistemi dizaynı", "AI Engineer", "30 d", "designing rag system architecture interview"),
        ],
        [
            doc("Machine Learning Systems Design", "github.com/chiphuyen", DESIGN_ML),
            doc("Chip Huyen bloqu", "huyenchip.com", CHIP_BLOG),
        ],
        [
            "3 system design sualını tam yazılı cavablandır",
            "Bir RAG sisteminin arxitekturasını çək",
            "Miqyas (1K -> 1M istifadəçi) fərqini yaz",
            "Monitoring və xərc planını əlavə et",
        ],
        "3 ML system design cavabı (diaqramlarla)",
        [
            "System design cavabını necə strukturlaşdırırsan?",
            "Hansı hissələri əvvəlcə müəyyən edirsən?",
            "Miqyas artımı nəyi dəyişir?",
        ],
    ),
    day(
        "Müsahibə simulyasiyası və 6 aylıq yekun",
        [
            "Mock müsahibə keçirmə",
            "Zəif yerlərin son qiymətləndirilməsi",
            "Növbəti 6 ayın planı",
            "Davamlı öyrənmə vərdişləri (spaced repetition, icma)",
        ],
        [
            yt("Mock müsahibə nümunəsi", "Exponent", "40 d", "mock machine learning interview example"),
            yt("6 aylıq ML yol xəritəsi yekunu", "Ken Jee", "30 d", "machine learning career roadmap after 6 months"),
        ],
        [
            doc("ML Interviews Book (son fəsillər)", "huyenchip.com", INTERVIEWS_BOOK),
            doc("roadmap.sh: növbəti addımlar", "roadmap.sh", ROADMAP),
        ],
        [
            "2 dostla və ya özünlə mock müsahibə keçir (kamera ilə)",
            "30 zəif sualı təkrar et",
            "Növbəti 6 ay üçün 3 hədəf yaz (vakansiya, layihə, icma)",
            "6 aylıq nəticələri rəqəmlərlə hesabla (günlər, layihələr, sətir kod)",
        ],
        "Mock müsahibə qeydi + növbəti 6 ay planı + 6 aylıq yekun hesabat",
        [
            "Müsahibədə özünü necə qiymətləndirirsən?",
            "Ən böyük böyümə hansı sahədə oldu?",
            "Növbəti 3 addım nədir?",
        ],
    ),
]

weeks = [
    {
        "focus": "Portfolio və şəxsi brendinq",
        "project": "Portfolio paketi: 3 cilalanmış layihə (kod + README + canlı demo), GitHub profili və CV",
        "quiz": "Portfolio, README, CV və LinkedIn strategiyası üzrə 10 sual",
    },
    {
        "focus": "Müsahibə hazırlığı və yekun",
        "project": "Müsahibə dəsti: 100 sual-cavab, 2 mock müsahibə və 6 aylıq yekun hesabat",
        "quiz": "ML nəzəriyyəsi, kodlaşdırma, SQL və system design üzrə 10 sual",
    },
]

PHASE = phase(
    9,
    "Portfolio, CV və müsahibə hazırlığı",
    "Görülən işi göstərə bilən portfolio, peşəkar profil və müsahibə hazırlığı.",
    "30-34 saat",
    weeks,
    days,
)
