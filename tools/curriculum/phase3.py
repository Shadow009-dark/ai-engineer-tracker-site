"""Phase 3 - Data analysis: NumPy, Pandas, visualization, SQL (days 43-63, 18 study days)."""

from helpers import day, doc, gq, phase, yt

NUMPY = "https://numpy.org/doc/stable/"
PANDAS = "https://pandas.pydata.org/docs/"
PANDAS_UG = "https://pandas.pydata.org/docs/user_guide/index.html"
MPL = "https://matplotlib.org/stable/"
SEABORN = "https://seaborn.pydata.org/"
PLOTLY = "https://plotly.com/python/"
W3SQL = "https://www.w3schools.com/sql/"
SQLBOLT = "https://sqlbolt.com/"
MODE_SQL = "https://mode.com/sql-tutorial/"
PGEX = "https://pgexercises.com/"
KAGGLE_LEARN = "https://www.kaggle.com/learn"
KAGGLE_PANDAS = "https://www.kaggle.com/learn/pandas"
PDH = "https://jakevdp.github.io/PythonDataScienceHandbook/"
WES = "https://wesmckinney.com/book/"
SQLITE = "https://docs.python.org/3/library/sqlite3.html"
SQLALCHEMY = "https://docs.sqlalchemy.org/en/20/"

days = [
    day(
        "NumPy I: ndarray, shape, indexing, broadcasting",
        [
            "ndarray nədir, shape/dtype/ndim",
            "Indexing, slicing, boolean masking, fancy indexing",
            "Broadcasting qaydaları",
            "Views vs copies (performans və səhvlər)",
        ],
        [
            yt("NumPy Full Course", "Keith Galli", "1s 30d", "keith galli complete numpy tutorial"),
            yt("NumPy əsasları", "freeCodeCamp", "1s", "freecodecamp numpy tutorial"),
        ],
        [
            doc("NumPy: quickstart", "numpy.org", NUMPY + "user/absolute_beginners.html"),
            doc("Python Data Science Handbook: NumPy", "jakevdp.github.io", PDH),
        ],
        [
            "0-99 arası ədədlərdən 10x10 matris yarat",
            "Şərt əsasında boolean maskə ilə filtrələ",
            "Broadcasting davranışını 4 fərqli nümunədə göstər",
            "View vs copy fərqini `np.shares_memory` ilə təsdiqlə",
        ],
        "NumPy əsaslarını əhatə edən məşq notebooku",
        [
            "`shape` və `reshape` necə işləyir?",
            "Broadcasting hansı qaydalarla genişlənir?",
            "View və copy fərqi nə vaxt problem yaradır?",
        ],
    ),
    day(
        "NumPy II: aqreqasiya, eksenlər, matris əməliyyatları",
        [
            "sum, mean, std, min, max və axis parametri",
            "Matris vurma, transpozisiya, stacking/splitting",
            "Universal funksiyalar (ufunc)",
            "NaN-ların idarəsi (nanmean, isnan)",
        ],
        [
            yt("NumPy aggregations and axis", "Keith Galli", "35 d", "numpy axis aggregation tutorial"),
            yt("NumPy matrix operations", "Codebasics", "30 d", "numpy matrix operations tutorial"),
        ],
        [
            doc("NumPy: sıralama və aqreqasiya", "numpy.org", NUMPY + "reference/routines.statistics.html"),
            gq("NumPy axis anlayışı", "numpy.org", "numpy axis explained"),
        ],
        [
            "İki matrisi üfüqi və şaquli birləşdir (hstack/vstack)",
            "Axis=0 və axis=1 ilə eyni hesablamanı aparıb fərqi izah et",
            "NaN olan array üzərində `np.nanmean` istifadə et",
            "Stack/split əməliyyatlarını nümunələrlə göstər",
        ],
        "NumPy aqreqasiya və matris məşqləri notebooku",
        [
            "`axis=0` nə deməkdir?",
            "NaN dəyərlər ortalamanı necə təhrif edir?",
            "ufunc nədir?",
        ],
    ),
    day(
        "NumPy III: random, şəkillər, fayl I/O",
        [
            "`np.random` və seed ilə reproduktivlik",
            "Şəkilləri array kimi oxumaq (shape, kanallar)",
            "Fayl I/O: npy, npz, text fayllar",
            "Sadə şəkil əməliyyatları (crop, flip, filter)",
        ],
        [
            yt("NumPy random və seed", "Corey Schafer", "20 d", "numpy random seed tutorial"),
            yt("Şəkillər NumPy array kimi", "Sentdex", "25 d", "images as numpy arrays python"),
        ],
        [
            doc("NumPy: təsadüfi ədədlər", "numpy.org", NUMPY + "reference/random/index.html"),
            doc("NumPy fayl formatları", "numpy.org", NUMPY + "reference/routines.io.html"),
        ],
        [
            "Seed təyin edib eyni datanı iki dəfə yarat və eyni olduğunu təsdiqlə",
            "Bir şəkil yükləyib array formasını çap et",
            "Şəkli kəs, çevir və qeyd et",
            "Array-ı npy faylına yaz və geri oxu",
        ],
        "Şəkil emalı nümunələri olan notebook (npy saxlanması ilə)",
        [
            "Seed niyə vacibdir (reproducibility)?",
            "Şəkil array-ında kanallar necə saxlanılır?",
            "npy ilə csv arasında fərq nədir?",
        ],
    ),
    day(
        "Pandas I: Series, DataFrame, seçim",
        [
            "Series və DataFrame anlayışları",
            "Index, columns, dtypes",
            "read_csv/read_excel və böyük parametrlər",
            "loc, iloc, at, iat ilə seçim",
        ],
        [
            yt("Pandas Full Course", "Keith Galli", "1s 30d", "keith galli pandas tutorial"),
            yt("Pandas ilk addımlar", "Kaggle / freeCodeCamp", "45 d", "pandas getting started tutorial"),
        ],
        [
            doc("Pandas: 10 dəqiqədə", "pandas.pydata.org", PANDAS + "user_guide/10min.html"),
            doc("Kaggle: Pandas kursu", "kaggle.com", KAGGLE_PANDAS),
        ],
        [
            "CSV fayl oxu və ilk 5 sətri göstər",
            "Sütun və sətir seçimini `loc` və `iloc` ilə et",
            "Index-i sütuna çevir və əksinə",
            "Sütun tiplərini yoxla və dəyişdir",
        ],
        "Pandas əsas əməliyyatları üzrə məşq notebooku (real dataset ilə)",
        [
            "loc ilə iloc fərqi nədir?",
            "Index nə üçün istifadə olunur?",
            "read_csv hansı problemli halları yaradır?",
        ],
    ),
    day(
        "Pandas II: filtr, sıralama, groupby",
        [
            "Şərtli filtrələmə və query()",
            "sort_values, rank, nlargest",
            "groupby + agg + transform",
            "Value counts və kateqorik analiz",
        ],
        [
            yt("Pandas GroupBy", "Corey Schafer", "45 d", "corey schafer pandas groupby aggregation"),
            yt("Pandas filtrləmə məşqləri", "Keith Galli", "30 d", "pandas filtering data tutorial"),
        ],
        [
            doc("Pandas user guide: groupby", "pandas.pydata.org", PANDAS_UG + "/groupby.html"),
            doc("Pandas: indexing", "pandas.pydata.org", PANDAS_UG + "/indexing.html"),
        ],
        [
            "Dataset-i 3 fərqli şərtlə filtrlə",
            "groupby ilə 3 fərqli aqreqasiya apar",
            "Nəticəni sütun adları ilə təmizlə (rename, reset_index)",
            "Ən çox 10 kateqoriyanı tap və göstər",
        ],
        "Data aqreqasiyası və qruplaşdırma notebooku",
        [
            "groupby ilə pivot_table fərqi nədir?",
            "transform nə vaxt lazımdır?",
            "`query()` niyə bəzən daha oxunaqlıdır?",
        ],
    ),
    day(
        "Pandas III: merge, join, pivot",
        [
            "merge: inner, left, right, outer",
            "join və concat (sətir/sütun üzrə)",
            "pivot_table, crosstab, melt",
            "MultiIndex nə vaxt lazımdır",
        ],
        [
            yt("Pandas Merge, Join, Concat", "Corey Schafer", "40 d", "pandas merge join concat tutorial"),
            yt("Pivot tables Pandas", "Keith Galli", "25 d", "pandas pivot table tutorial"),
        ],
        [
            doc("Pandas: merge/join/concat", "pandas.pydata.org", PANDAS_UG + "/merging.html"),
            doc("Pandas: reshape", "pandas.pydata.org", PANDAS_UG + "/reshaping.html"),
        ],
        [
            "İki fərqli CSV faylı yaradıb merge et",
            "4 merge tipini (inner/left/right/outer) müqayisə et",
            "Uzun formadan geniş formaya çevir (pivot)",
            "crosstab ilə kateqorik əlaqəni göstər",
        ],
        "İki dataset-i birləşdirən tam analiz notebooku",
        [
            "Merge zamanı sətir sayı niyə arta bilər?",
            "Inner və left join fərqi nədir?",
            "Pivot ilə groupby necə əlaqəlidir?",
        ],
    ),
    day(
        "Pandas IV: boş dəyərlər, tiplər, datetime",
        [
            "Missing data: isnull, dropna, fillna (strategiyalar)",
            "Dtype çevrilmələri, category tipi, memory azaldılması",
            "apply, map, applymap və vektorlaşdırılmış alternativlər",
            "Datetime: to_datetime, resample, rolling",
        ],
        [
            yt("Pandas missing data", "Corey Schafer", "30 d", "corey schafer pandas missing data"),
            yt("Pandas time series əsasları", "Data School", "35 d", "pandas time series tutorial"),
        ],
        [
            doc("Pandas: missing data", "pandas.pydata.org", PANDAS_UG + "/missing_data.html"),
            doc("Pandas: time series", "pandas.pydata.org", PANDAS_UG + "/timeseries.html"),
        ],
        [
            "Dataset-dəki boş dəyərləri analiz et və 2 strategiya ilə doldur",
            "Datetime sütunu yaradıb ay üzrə qruplaşdır",
            "Rolling average hesabla və qrafikdə göstər",
            "apply ilə yazdığın funksiyanı vektorlaşdırılmış versiyaya çevir",
        ],
        "Time series və data təmizləmə notebooku",
        [
            "Boş dəyəri silmək nə vaxt səhvdir?",
            "category tipi yaddaşa necə qənaət edir?",
            "apply nə vaxt yavaşdır?",
        ],
    ),
    day(
        "Pandas V: string əməliyyatları, böyük fayllar, performans",
        [
            "`.str` aksessoru ilə mətn əməliyyatları",
            "Regex ilə təmizləmə",
            "Chunks ilə böyük fayl oxuma",
            "Performans: dtype optimizasiyası, parquet formatı",
        ],
        [
            yt("Pandas string operations", "Data School", "25 d", "pandas string methods str accessor"),
            yt("Böyük dataset-ləri Pandas ilə emal etmək", "mCoding", "20 d", "pandas large dataset memory performance"),
        ],
        [
            doc("Pandas: mətn əməliyyatları", "pandas.pydata.org", PANDAS_UG + "/text.html"),
            doc("Parquet vs CSV", "pandas.pydata.org", PANDAS + "reference/api/pandas.read_parquet.html"),
        ],
        [
            "Mətn sütununu regex ilə təmizlə",
            "Böyük CSV-ni chunk ilə oxuyub aqreqasiya et",
            "CSV və parquet fayl ölçülərini müqayisə et",
            "Oxuma vaxtını `%timeit` ilə ölç",
        ],
        "Performans müqayisəsi cədvəli olan notebook (CSV vs Parquet)",
        [
            "Niyə parquet CSV-dən üstündür?",
            "Chunk-lar nə vaxt lazımdır?",
            "`.str` əməliyyatları hansı hallarda yavaş olur?",
        ],
    ),
    day(
        "Matplotlib: vizualizasiyanın əsasları",
        [
            "Figure və axes anlayışları",
            "plot, scatter, bar, hist, imshow",
            "Başlıq, ox etiketləri, legend, stil",
            "Yadda saxlama (savefig) və DPI",
        ],
        [
            yt("Matplotlib Full Tutorial", "Corey Schafer", "1s 30d", "corey schafer matplotlib tutorial"),
            yt("Matplotlib ən yaxşı təcrübələri", "Sentdex", "40 d", "matplotlib tutorial sentdex"),
        ],
        [
            doc("Matplotlib: rəsmi təlimat", "matplotlib.org", MPL + "users/getting-started/index.html"),
            doc("Matplotlib: pyplot dərsliyi", "matplotlib.org", MPL + "tutorials/introductory/pyplot.html"),
        ],
        [
            "Eyni datanı 4 fərqli qrafik tipi ilə göstər",
            "2x2 subplot şəbəkəsi qur",
            "Bütün qrafiklərə başlıq və ox etiketləri əlavə et",
            "Qrafikləri PNG kimi yadda saxla (dpi=150)",
        ],
        "4 qrafik tipli, səliqəli vizualizasiya fiquresi",
        [
            "Figure ilə axes fərqi nədir?",
            "Histoqram üçün bin sayı necə seçilir?",
            "savefig hansı parametrlərlə keyfiyyətli olur?",
        ],
    ),
    day(
        "Seaborn və Plotly: statistik və interaktiv vizualizasiya",
        [
            "Seaborn: histplot, boxplot, violinplot, heatmap, pairplot",
            "Kateqorik və ədədi dəyişənlərin birlikdə vizualizasiyasi",
            "Plotly ilə interaktiv qrafiklər",
            "Qrafik seçimi qaydaları (hansı data üçün hansı qrafik)",
        ],
        [
            yt("Seaborn Full Course", "Kimberly Fessel", "1s", "seaborn tutorial kimberly fessel"),
            yt("Plotly Python əsasları", "Plotly / Charming Data", "40 d", "plotly python tutorial"),
        ],
        [
            doc("Seaborn: rəsmi API", "seaborn.pydata.org", SEABORN + "tutorial.html"),
            doc("Plotly Python", "plotly.com", PLOTLY),
        ],
        [
            "Dataset üçün pairplot qur",
            "Korrelyasiya matrisini heatmap kimi göstər",
            "Seaborn ilə kateqorik analiz apar (box + violin)",
            "Bir qrafiki Plotly ilə interaktiv edib HTML kimi saxla",
        ],
        "Seaborn + Plotly əsaslı vizualizasiya toplusu",
        [
            "Boxplot nə cəhətdən faydalıdır?",
            "Pairplot böyük dataset-lərdə niyə problemlidir?",
            "İnteraktiv qrafik nə vaxt statikdən yaxşıdır?",
        ],
    ),
    day(
        "EDA: metodologiya və data təmizləmə",
        [
            "EDA-nın addımları: strukturu, keyfiyyət, paylanma, əlaqələr",
            "Data keyfiyyəti yoxlamaları (duplikat, outlier, tip xətaları)",
            "Outlier aşkarlama üsulları (IQR, z-score)",
            "Nəticələri yazılı formada ifadə etmək",
        ],
        [
            yt("EDA Full Course", "Krish Naik", "1s 30d", "krish naik exploratory data analysis"),
            yt("Data cleaning ən yaxşı təcrübələri", "Ken Jee", "30 d", "data cleaning techniques ken jee"),
        ],
        [
            doc("Kaggle: EDA nümunə notebookları", "kaggle.com", "https://www.kaggle.com/code"),
            doc("Pandas: EDA üçün faydalı funksiyalar", "pandas.pydata.org", PANDAS + "reference/frame.html"),
        ],
        [
            "Yeni dataset seç və ilk 10 saniyədə baş verən yoxlamaları yaz",
            "Duplikat və outlier-ları tap",
            "5 fərqli vizualizasiya ilə dataset-i təsvir et",
            "Hər qrafik altına 1-2 cümlə nəticə yaz",
        ],
        "EDA mərhələsi tamamlanmış notebook (nəticələrlə)",
        [
            "EDA-da ilk 3 yoxlama nədir?",
            "Outlier həmişə silinməlidir?",
            "EDA nəticələri modelin qurulmasına necə təsir edir?",
        ],
    ),
    day(
        "EDA layihəsi: real dataset üzərində tam analiz",
        [
            "Layihə planı: sual qoymaq -> analiz -> nəticə",
            "Vizualizasiya cədvəlinin qurulması",
            "Nəticələrin hesabat kimi yazılması",
            "Notebook-un paylaşıla bilən formata salınması",
        ],
        [
            yt("EDA real layihə nümunəsi", "Ken Jee", "45 d", "end to end data analysis project python"),
            yt("Kaggle notebook yazma strategiyası", "Abhishek Thakur", "30 d", "how to write kaggle notebook"),
        ],
        [
            doc("Kaggle dataset-ləri", "kaggle.com", "https://www.kaggle.com/datasets"),
            gq("Data analizi hesabat şablonu", "github.com", "data analysis report template markdown"),
        ],
        [
            "Dataset üçün 3 biznes sual qoy",
            "Hər sual üçün analiz və qrafik hazırla",
            "Nəticələri markdown xanalarında yaz",
            "Noutbuku GitHub-a push et",
        ],
        "Tam sənədləşdirilmiş EDA layihəsi (GitHub-da)",
        [
            "Hansı sualı cavablandırdın?",
            "Hansı fərziyyə səhv çıxdı?",
            "Hansı analiz gələcəkdə lazım olacaq?",
        ],
    ),
    day(
        "SQL I: SELECT, WHERE, ORDER BY",
        [
            "Relyasion model: cədvəl, sətir, sütun, açar",
            "SELECT, DISTINCT, WHERE, ORDER BY, LIMIT",
            "AND/OR/NOT, LIKE, IN, BETWEEN, NULL",
            "SQL-in ML-də yeri (feature hazırlama)",
        ],
        [
            yt("SQL for Data Analysis", "freeCodeCamp", "4s", "freecodecamp sql full course beginners"),
            yt("SQL əsasları", "Alex The Analyst", "40 d", "alex the analyst sql basics"),
        ],
        [
            doc("W3Schools SQL təlimi", "w3schools.com", W3SQL),
            doc("SQLBolt interaktiv dərslər", "sqlbolt.com", SQLBOLT),
        ],
        [
            "DB Browser for SQLite quraşdır və nümunə bazanı yüklə",
            "10 SELECT sorğusu yaz (WHERE + ORDER BY ilə)",
            "NULL dəyərləri olan sütunlarda filtrləmə apar",
            "LIKE ilə mətn axtarışı et",
        ],
        "10 sorğudan ibarət SQL məşq faylı (şərhlərlə)",
        [
            "WHERE ilə HAVING fərqi nədir?",
            "NULL ilə müqayisə niyə `=` ilə işləmir?",
            "ORDER BY olmadan LIMIT niyə riskli?",
        ],
    ),
    day(
        "SQL II: JOIN, GROUP BY, subquery",
        [
            "INNER/LEFT/RIGHT/FULL JOIN",
            "GROUP BY, HAVING və aqreqat funksiyalar",
            "Subquery və EXISTS",
            "Set əməliyyatları: UNION, INTERSECT, EXCEPT",
        ],
        [
            yt("SQL JOINs izahı", "Alex The Analyst", "45 d", "sql joins tutorial"),
            yt("GROUP BY və aqreqasiya", "Mode Analytics", "30 d", "sql group by aggregation tutorial"),
        ],
        [
            doc("Mode SQL təlimatı", "mode.com", MODE_SQL),
            doc("PostgreSQL dərsliyi", "postgresql.org", "https://www.postgresql.org/docs/current/tutorial.html"),
        ],
        [
            "3 cədvəlli bazada JOIN sorğuları yaz",
            "GROUP BY ilə 5 fərqli aqreqasiya apar",
            "Subquery ilə filtrləmə et",
            "4 JOIN tipini müqayisə edən sorğular yaz",
        ],
        "JOIN və aqreqasiya sorğuları toplusu + nəticələrin izahı",
        [
            "LEFT JOIN nə vaxt NULL qaytarır?",
            "HAVING niyə lazımdır?",
            "Subquery ilə JOIN nə vaxt bir-birini əvəz edir?",
        ],
    ),
    day(
        "SQL III: CTE, window functions, index",
        [
            "Common Table Expressions (WITH)",
            "Window functions: ROW_NUMBER, RANK, LAG/LEAD, running totals",
            "Index nədir və sorğu sürətinə təsiri",
            "Sorğu planı (EXPLAIN) oxumaq",
        ],
        [
            yt("Window Functions SQL", "Alex The Analyst", "35 d", "sql window functions tutorial"),
            yt("SQL sorğu optimizasiyası", "Hussein Nasser", "30 d", "sql query optimization indexing performance"),
        ],
        [
            doc("PostgreSQL: window functions", "postgresql.org", "https://www.postgresql.org/docs/current/tutorial-window.html"),
            doc("Use The Index, Luke (index bələdçisi)", "use-the-index-luke.com", "https://use-the-index-luke.com/"),
        ],
        [
            "CTE ilə çoxmərhələli sorğu yaz",
            "ROW_NUMBER ilə hər qrupda ilk sətri tap",
            "Running total hesabla (window ilə)",
            "Eyni sorğunu index əlavə etməzdən əvvəl/sonra müqayisə et",
        ],
        "Analitik SQL sorğuları toplusu (CTE + window functions)",
        [
            "CTE subquery-dan niyə oxunaqlıdır?",
            "ROW_NUMBER ilə RANK fərqi nədir?",
            "Index nə vaxt kömək etmir?",
        ],
    ),
    day(
        "SQL + Python birlikdə",
        [
            "sqlite3 modulu ilə bazaya qoşulma",
            "Cədvəl yaratma, data yazma, oxuma",
            "pandas.read_sql ilə sorğu nəticəsi",
            "SQLAlchemy (ORM) əsasları",
        ],
        [
            yt("Python SQLite tutorial", "Corey Schafer", "35 d", "python sqlite3 tutorial corey schafer"),
            yt("SQLAlchemy əsasları", "Pretty Printed", "30 d", "sqlalchemy tutorial beginners"),
        ],
        [
            doc("Python sqlite3", "docs.python.org", SQLITE),
            doc("pandas.read_sql", "pandas.pydata.org", PANDAS + "reference/api/pandas.read_sql.html"),
        ],
        [
            "SQLite bazası yarat və 2 cədvəl doldur",
            "Sorğu nəticəsini pandas DataFrame kimi oxu",
            "DataFrame-i bazaya geri yaz",
            "SQLAlchemy ilə eyni əməliyyatı ORM şəklində yaz",
        ],
        "Python + SQL inteqrasiyalı mini pipeline",
        [
            "Niye Pandas-a keçməzdən əvvəl SQL-də filtr etmək daha səmərəlidir?",
            "ORM nə vaxt artıq yüktür?",
            "SQL injection nədir və necə qarşısı alınır?",
        ],
    ),
    day(
        "Kaggle-a başlanğıc və ilk notebook",
        [
            "Kaggle profili, dataset-lər, notebook-lar, competitions",
            "Notebook yazma strukturu (sual -> data -> analiz -> nəticə)",
            "Kaggle API ilə dataset yükləmək",
            "Upvote və community əlaqələri",
        ],
        [
            yt("Kaggle əsasları", "Abhishek Thakur", "30 d", "kaggle beginner guide notebook"),
            yt("İlk Kaggle notebook", "Ken Jee", "40 d", "how to do your first kaggle notebook"),
        ],
        [
            doc("Kaggle Learn kursları", "kaggle.com", KAGGLE_LEARN),
            doc("Kaggle API", "github.com/Kaggle", "https://github.com/Kaggle/kaggle-api"),
        ],
        [
            "Kaggle profili yarat/optimallaşdır (bio, foto, linklər)",
            "3 dataset seç və nə üçün seçdiyini yaz",
            "Kaggle API ilə dataset yüklə",
            "İlk notebook-u yazıb yayımla",
        ],
        "Yayımlanmış ilk Kaggle notebooku",
        [
            "Yaxşı Kaggle notebook-un 3 xüsusiyyəti nədir?",
            "Dataset lisenziyası nə üçün vacibdir?",
            "Kaggle API token-i necə təhlükəsiz saxlanılır?",
        ],
    ),
    day(
        "Faza 3 layihəsi: tam data analizi pipeline-ı",
        [
            "Faza biliklərinin tam tətbiqi",
            "Pipeline addımları: yüklə, təmizlə, birləşdir, analiz et, vizuallaşdır",
            "Kodun funksiyalara bölünməsi",
            "Analizin biznes/mənalı nəticəyə çevrilməsi",
        ],
        [
            yt("End-to-end data analysis project", "Krish Naik", "1s", "end to end data analytics project python"),
            yt("Notebook-dan təmiz kod ayrılması", "ArjanCodes", "20 d", "refactor jupyter notebook into python module"),
        ],
        [
            doc("Pandas: data təmizləmə bələdçisi", "pandas.pydata.org", PANDAS_UG),
            doc("Kaggle dataset-ləri", "kaggle.com", "https://www.kaggle.com/datasets"),
        ],
        [
            "Layihə üçün dataset seç və sual müəyyən et",
            "SQL və ya Pandas ilə data hazırla",
            "Ən azı 8 vizualizasiya hazırla",
            "Notebook + README + nəticələr bölməsi yaz",
        ],
        "GitHub-da `data-analysis-project` reposu (notebook + README + qrafiklər)",
        [
            "Pipeline-ın hansı addımı ən çox vaxt apardı?",
            "Hansı statistik metoddan istifadə etdin?",
            "Nəticənin ən vacib 3 məqamı nədir?",
        ],
    ),
]

weeks = [
    {
        "focus": "NumPy və Pandas əsasları",
        "project": "Data pipeline: dataset yüklə -> təmizlə -> aqreqasiya et -> nəticəni qrafiklərlə göstər",
        "quiz": "NumPy broadcasting, Pandas loc/iloc, groupby üzrə 10 sual",
    },
    {
        "focus": "Vizualizasiya və EDA",
        "project": "EDA notebooku: 10 fərqli qrafik + hər biri üçün yazılı nəticə",
        "quiz": "Vizualizasiya tipləri, data keyfiyyəti və EDA metodologiyası üzrə 10 sual",
    },
    {
        "focus": "SQL və Kaggle",
        "project": "SQL + Python: SQLite bazası qur, analitik sorğular yaz, nəticəni Kaggle notebook kimi yayımla",
        "quiz": "JOIN, GROUP BY, window functions və index üzrə 10 sual",
    },
]

PHASE = phase(
    3,
    "Data analizi: NumPy, Pandas, Matplotlib və SQL",
    "Real dataset-ləri oxumaq, təmizləmək, analiz etmək və SQL ilə sorğulamaq bacarığı.",
    "54-62 saat",
    weeks,
    days,
)
