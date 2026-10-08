"""Phase 2 - Mathematics for machine learning (days 22-42, 3 weeks, 18 study days)."""

from helpers import day, doc, gq, phase, yt

MML = "https://mml-book.github.io/"
OCW_LA = "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"
STATQUEST = "https://statquest.org/"
SEEING_THEORY = "https://seeing-theory.brown.edu/"
KHAN_STATS = "https://www.khanacademy.org/math/statistics-probability"
DLB = "https://www.deeplearningbook.org/"
NUMPY = "https://numpy.org/doc/stable/"
AUTOGRAD = "https://pytorch.org/docs/stable/notes/autograd.html"
RUDER = "https://ruder.io/optimizing-gradient-descent/"
SETOSA = "https://setosa.io/ev/conditional-probability/"

days = [
    day(
        "Vektorlar: əsas anlayışlar",
        [
            "Vektor nədir, ML-də nəyi təmsil edir (feature vektoru)",
            "Vektor əməliyyatları: toplama, skalyar vurma",
            "Norm (L1, L2) və məsafə anlayışı",
            "Dot product və oxşarlıq (cosine similarity)",
        ],
        [
            yt("Essence of Linear Algebra (bölmə 1-3)", "3Blue1Brown", "35 d", "3blue1brown essence of linear algebra vectors"),
            yt("Vektorlar və vektor fəzaları", "MIT OCW / Gilbert Strang", "50 d", "gilbert strang vectors linear algebra lecture"),
        ],
        [
            doc("Mathematics for ML (bölmə 2-3)", "mml-book.github.io", MML),
            gq("Cosine similarity nədir", "towardsdatascience.com", "cosine similarity explained"),
        ],
        [
            "NumPy ilə iki vektorun dot productunu əl ilə (dövrlə) və `np.dot` ilə hesabla",
            "L1 və L2 normlarını hər iki üsulla hesabla",
            "Cosine similarity funksiyası yaz",
            "İki sənəd arasında oxşarlığı vektorlarla ölçən nümunə hazırla",
        ],
        "Vektor əməliyyatlarını əl ilə implement edən `vectors.py`",
        [
            "Dot product həndəsi olaraq nə deməkdir?",
            "L1 və L2 norm fərqi nədir?",
            "Cosine similarity 0 və 1 arasında nəyi göstərir?",
        ],
    ),
    day(
        "Matrislər və matris əməliyyatları",
        [
            "Matris nədir, ölçü (shape) anlayışı",
            "Toplama, skalyar vurma, matris vurma",
            "Transpozisiya, identiklik, tərs matris",
            "Matris vurmanın ML-də rolu (xətti transformasiya)",
        ],
        [
            yt("Matris vurma və xətti çevrilmələr", "3Blue1Brown", "20 d", "3blue1brown linear transformations matrices"),
            yt("Matris əməliyyatları", "Khan Academy", "25 d", "khan academy matrix operations"),
        ],
        [
            doc("MML: şərh və matris əməliyyatları", "mml-book.github.io", MML),
            doc("NumPy: xətti cəbr", "numpy.org", NUMPY + "reference/routines.linalg.html"),
        ],
        [
            "Matris vurmanı yalnız Python dövrləri ilə implement et",
            "Nəticəni `np.matmul` ilə yoxla",
            "Tərs matrisi hesabla və A @ A_inv ≈ I olduğunu göstər",
            "Matrisi koordinat çevrilməsi kimi tətbiq edib nöqtələri fırlat",
        ],
        "Əl ilə yazılmış matris əməliyyatları kitabxanası (test ilə)",
        [
            "Matris vurma niyə kommutativ deyil?",
            "Tərs matris nə vaxt mövcud olmur?",
            "Transpozisiya nə üçün lazımdır?",
        ],
    ),
    day(
        "Xətti tənliklər, rank, determinant",
        [
            "Xətti tənliklər sistemi (Ax = b)",
            "Gauss elimination və pivot anlayışı",
            "Rank, linear independence, span",
            "Determinant və onun mənası (həcm miqyası)",
        ],
        [
            yt("Gaussian Elimination", "MIT OCW / Gilbert Strang", "45 d", "gaussian elimination mit 18.06"),
            yt("Determinant və rank", "Khan Academy", "25 d", "khan academy determinant rank linear algebra"),
        ],
        [
            doc("MML: xətti tənliklər sistemləri", "mml-book.github.io", MML),
            gq("Rank və həllərin sayı", "mathinsight.org", "matrix rank solutions linear system"),
        ],
        [
            "Kiçik tənlik sistemini əl ilə Gauss elimination ilə həll et",
            "Eyni sistemi `np.linalg.solve` ilə həll et və müqayisə et",
            "Rank-ı az olan (singular) matris yarat və xətanı izah et",
            "Determinantı hesabla və həndəsi mənasını yaz",
        ],
        "İşləyən Gauss elimination implementasiyası",
        [
            "Xətti asılılıq nə deməkdir?",
            "Rank matris haqqında nə deyir?",
            "Həll yoxdursa bunu necə başa düşürük?",
        ],
    ),
    day(
        "Eigenvalue, eigenvector, SVD və PCA",
        [
            "Eigenvektor və eigenvalue intuisiya",
            "Spectral decomposition, symmetric matrislər",
            "Singular Value Decomposition (SVD)",
            "PCA-nın riyazi əsası: covariasiya matrisi + eigenvektorlar",
        ],
        [
            yt("Eigenvectors and eigenvalues", "3Blue1Brown", "17 d", "3blue1brown eigenvectors eigenvalues"),
            yt("SVD izahı", "Steve Brunton", "20 d", "steve brunton singular value decomposition"),
            yt("PCA əl ilə hesablama", "StatQuest", "25 d", "statquest PCA step by step"),
        ],
        [
            doc("MML: matris parçalanmaları", "mml-book.github.io", MML),
            doc("scikit-learn: PCA", "scikit-learn.org", "https://scikit-learn.org/stable/modules/decomposition.html"),
        ],
        [
            "NumPy ilə kiçik matrisin eigenvalue-larını hesabla",
            "SVD-ni tətbiq et və A ≈ U S V^T olduğunu təsdiqlə",
            "PCA-nı 2D dataset üzərində əl ilə implement et",
            "Nəticəni sklearn PCA ilə müqayisə et",
       ],
        "Sıfırdan yazılmış PCA notebooku (sklearn ilə müqayisəli)",
        [
            "Eigenvektor nəyi göstərir?",
            "SVD PCA-dan necə üstündür?",
            "PCA hansı məlumatı itirir?",
        ],
    ),
    day(
        "Törəmə və qradiyent",
        [
            "Törəmə anlayışı və qaydalar (power, product, chain rule)",
            "Partial törəmə və qradiyent",
            "Jacobian və Hessian (tanışlıq səviyyəsində)",
            "Qradiyentin ən böyük artım istiqaməti olması",
        ],
        [
            yt("Essence of Calculus (bölmə 1-6)", "3Blue1Brown", "1s 40d", "3blue1brown essence of calculus"),
            yt("Qradiyent və istiqamətli törəmə", "Khan Academy", "30 d", "khan academy gradient partial derivatives"),
        ],
        [
            doc("MML: diferensial hesab", "mml-book.github.io", MML),
            gq("Numerik törəmə (finite difference)", "en.wikipedia.org", "finite difference derivative approximation"),
        ],
        [
            "Analitik olaraq bir funksiyanın qradiyentini tap (kağızda)",
            "Numerik (finite difference) qradiyent funksiyası yaz",
            "Analitik və numerik nəticələri müqayisə et",
            "Chain rule-u kodla nümayiş etdir (kompozisiya funksiyası)",
        ],
        "Analitik vs numerik qradiyent müqayisəsi olan notebook",
        [
            "Qradiyent nəyi göstərir?",
            "Chain rule niyə backpropagation-un əsasıdır?",
            "Partial törəmə nədir?",
        ],
    ),
    day(
        "Qradiyent enişi (əl ilə)",
        [
            "Optimizasiya məsələsi: minimumu tapmaq",
            "Gradient descent düsturu və learning rate",
            "Convergence, diverge və yaxşı learning rate seçimi",
            "Loss funksiyası və loss landshaftı",
        ],
        [
            yt("Gradient Descent əl ilə nümunə", "StatQuest", "30 d", "statquest gradient descent"),
            yt("Gradient descent vizual izah", "3Blue1Brown", "20 d", "gradient descent neural network 3blue1brown"),
        ],
        [
            doc("Deep Learning Book: optimizasiya", "deeplearningbook.org", DLB),
            gq("Learning rate seçimi", "towardsdatascience.com", "choosing learning rate gradient descent"),
        ],
        [
            "Sadə funksiya (f(x) = x^2) üçün gradient descent implement et",
            "Fərqli learning rate dəyərlərini sına və nəticələri qrafikdə göstər",
            "Çox böyük learning rate ilə divergensiyanı nümayiş etdir",
            "İki parametrli funksiya üçün qradiyent addımlarını kontur qrafikdə çək",
        ],
        "Learning rate müqayisəsi olan gradient descent notebooku",
        [
            "Learning rate çox böyük olsa nə olur?",
            "Lokal minimum problemi nədir?",
            "Convergence necə ölçülür?",
        ],
    ),
    day(
        "Ehtimala giriş: hadisələr və Bayes",
        [
            "Ehtimal aksiomaları, hadisə və nümunə fəzası",
            "Birləşmə, kəsişmə, asılılıq",
            "Şərti ehtimal",
            "Bayes teoremi və intuitiv izahı",
        ],
        [
            yt("Bayes teoremi izahı", "3Blue1Brown", "15 d", "3blue1brown bayes theorem"),
            yt("Probability əsasları", "StatQuest", "50 d", "statquest probability basics"),
        ],
        [
            doc("Seeing Theory: Probability", "seeing-theory.brown.edu", SEEING_THEORY),
            doc("Şərti ehtimalın vizual izahı", "setosa.io", SETOSA),
        ],
        [
            "Bayes düsturunu real nümunə ilə (xəstəlik testi) hesabla",
            "Monte Carlo simulyasiyası ilə nəticəni yoxla",
            "Şərti ehtimalın iki tərifini kod ilə uyğunlaşdır",
            "Naive Bayes-in niyə 'naive' olduğunu bir abzasda yaz",
        ],
        "Bayes teoreminin simulyasiya ilə təsdiqi (notebook)",
        [
            "Şərti ehtimal nədir?",
            "Bayes teoremi necə oxunur?",
            "Niyə 'prior' vacibdir?",
        ],
    ),
    day(
        "Təsadüfi dəyişənlər və paylanmalar",
        [
            "Diskret və davamlı təsadüfi dəyişənlər",
            "PMF/PDF/CDF anlayışları",
            "Bernoulli, binomial, Poisson, uniform",
            "Normal (Gauss) paylanması və mərkəzi rolu",
        ],
        [
            yt("StatQuest: Probability Distributions", "StatQuest", "1s", "statquest probability distributions normal binomial poisson"),
            yt("Normal paylanma izahı", "Khan Academy", "25 d", "khan academy normal distribution"),
        ],
        [
            doc("MML: ehtimal paylanmaları", "mml-book.github.io", MML),
            doc("SciPy statistik paylanmalar", "scipy.org", "https://docs.scipy.org/doc/scipy/reference/stats.html"),
        ],
        [
            "Hər 4 paylanma üçün simulyasiya edib histoqram çək",
            "NumPy `random` ilə normal paylanma yarat və parametrlərini dəyiş",
            "PDF-i əl ilə hesablayıb SciPy nəticəsi ilə müqayisə et",
            "Real dataset-də paylanma formasını yoxla",
        ],
        "4 paylanmanın simulyasiya + nəzəri müqayisəsi notebooku",
        [
            "Diskret və davamlı fərqi nədir?",
            "Normal paylanma niyə bu qədər istifadə olunur?",
            "Poisson nə vaxt uyğun modeldir?",
        ],
    ),
    day(
        "Gözləmə, dispersiya, kovariasiya, korrelyasiya",
        [
            "Gözləmə (expected value) və xassələri",
            "Dispersiya və standart sapma",
            "Kovariasiya və korrelyasiya",
            "Asılılıq vs korrelyasiya (və 'korrelyasiya bərabərlik deyil')",
        ],
        [
            yt("StatQuest: Expected value & Variance", "StatQuest", "35 d", "statquest expected value variance covariance"),
            yt("Kovariasiya və korrelyasiya", "Josh Starmer / StatQuest", "25 d", "covariance correlation explained"),
        ],
        [
            doc("MML: gözləmə və kovariasiya", "mml-book.github.io", MML),
            doc("pandas: korrelyasiya", "pandas.pydata.org", "https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html"),
        ],
        [
            "Verilmiş dataset üçün gözləmə və dispersiyanı yalnız NumPy ilə hesabla",
            "Kovariasiya matrisini əl ilə qur və `np.cov` ilə yoxla",
            "Pearson və Spearman korrelyasiyasını müqayisə et",
            "Korrelyasiya olub səbəb əlaqəsi olmayan nümunə tap",
        ],
        "Statistik hesablamaları əl ilə edən modul + müqayisə notebooku",
        [
            "Dispersiya nəyi ölçür?",
            "Kovariasiya vahiddən asılıdır, korrelyasiya?",
            "Korrelyasiya niyə səbəbi sübut etmir?",
        ],
    ),
    day(
        "Böyük ədədlər qanunu və Mərkəzi Limit Teoremi",
        [
            "Nümunə (sample) vs populyasiya",
            "Böyük ədədlər qanunu (LLN)",
            "Mərkəzi Limit Teoremi (CLT)",
            "Standart xəta və nümunə ölçüsünün rolu",
        ],
        [
            yt("Central Limit Theorem", "StatQuest", "25 d", "statquest central limit theorem"),
            yt("Law of Large Numbers simulyasiya", "Khan Academy", "15 d", "law of large numbers simulation"),
        ],
        [
            doc("CLT interaktiv izah", "seeing-theory.brown.edu", SEEING_THEORY),
            gq("Standart xəta nədir", "towardsdatascience.com", "standard error explained"),
        ],
        [
            "Sikkə atma simulyasiyası ilə LLN-i göstər",
            "Qeyri-normal paylanmadan nümunələr götürüb ortalamanın paylanmasını çək",
            "Nümunə ölçüsünü 10, 100, 1000 edərək CLT-ni nümayiş etdir",
            "Nəticələri histoqram şəbəkəsində yaz",
        ],
        "CLT və LLN simulyasiya notebooku (vizual sübut)",
        [
            "CLT nə deyir?",
            "Nümunə ölçüsü artdıqca nə yaxşılaşır?",
            "Standart xəta ilə standart sapma fərqi nədir?",
        ],
    ),
    day(
        "Statistik nəticə: hipotez testi, p-value, etibar intervalı",
        [
            "Boş hipotez (H0) və alternativ (H1)",
            "t-test, chi-square test (tanışlıq)",
            "p-value nədir və nə DEYİL",
            "Etibar intervalı (confidence interval)",
        ],
        [
            yt("StatQuest: Hypothesis Testing and p-values", "StatQuest", "40 d", "statquest hypothesis testing p value"),
            yt("A/B testinin əsasları", "StatQuest", "25 d", "statquest a b testing statistics"),
        ],
        [
            doc("SciPy: statistik testlər", "scipy.org", "https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html"),
            gq("p-value səhv anlayışları", "en.wikipedia.org", "misuse of p-values"),
        ],
        [
            "İki qrupun ortalamasını t-test ilə müqayisə et",
            "Ki-kvadrat testini kateqorik data üzərində tətbiq et",
            "Etibar intervalını əl ilə hesabla",
            "Süni A/B test nəticəsi yaradıb qərar ver (və Type I/II xətanı izah et)",
        ],
        "A/B test nəticələrini analiz edən notebook (qərar ilə)",
        [
            "p-value nə deməkdir?",
            "Type I və Type II xəta nədir?",
            "Etibar intervalı nə üçün p-value-dan daha informativdir?",
        ],
    ),
    day(
        "MLE, MAP və Bayes nəticəsi",
        [
            "Likelihood və log-likelihood",
            "Maximum Likelihood Estimation (MLE)",
            "MAP və prior-un rolu",
            "MLE-nin loss funksiyaları ilə əlaqəsi (MSE, cross-entropy)",
        ],
        [
            yt("Maximum Likelihood əl ilə", "StatQuest", "30 d", "maximum likelihood estimation statquest"),
            yt("MLE və MAP fərqi", "Mutual Information", "20 d", "maximum likelihood vs maximum a posteriori"),
        ],
        [
            doc("MML: parametr qiymətləndirməsi", "mml-book.github.io", MML),
            gq("MSE niyə MLE-dən gəlir", "towardsdatascience.com", "mse derived from maximum likelihood gaussian"),
        ],
        [
            "Normal paylanmanın parametrlərini MLE ilə əl ilə tap",
            "Log-likelihood funksiyasını kodla hesabla və qrafikdə maksimumu göstər",
            "Gaussian fərziyyəsi altında MSE-nin MLE olduğunu göstər",
            "Kiçik nümunədə prior-un nəticəni necə dəyişdiyini yaz",
        ],
        "Sıfırdan yazılmış MLE implementasiyası (vizual optimizasiya ilə)",
        [
            "Likelihood ilə ehtimal fərqi nədir?",
            "Niyə log-likelihood istifadə olunur?",
            "MSE hansı fərziyyədən doğur?",
        ],
    ),
    day(
        "İnformasiya nəzəriyyəsi: entropiya və cross-entropy",
        [
            "İnformasiya və bit anlayışı",
            "Entropiya",
            "Cross-entropy və KL divergensiya",
            "Cross-entropy loss-un ML-də rolu",
        ],
        [
            yt("Entropy, Cross-Entropy, KL Divergence", "StatQuest", "25 d", "statquest entropy cross entropy kl divergence"),
            yt("Information theory for machine learning", "Mutual Information", "20 d", "information theory machine learning entropy"),
        ],
        [
            doc("MML: informasiya nəzəriyyəsi", "mml-book.github.io", MML),
            doc("PyTorch: CrossEntropyLoss", "pytorch.org", "https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html"),
        ],
        [
            "Entropiyanı sıfırdan implement et",
            "Cross-entropy-ni implement edib PyTorch nəticəsi ilə müqayisə et",
            "KL divergensiyanı iki paylanma arasında hesabla",
            "Verilmiş dataset-də hansı modelin daha yaxşı olduğunu cross-entropy ilə müqayisə et",
        ],
        "Entropiya/cross-entropy implementasiyası + PyTorch müqayisəsi",
        [
            "Entropiya nəyi ölçür?",
            "Cross-entropy loss niyə klassifikasiyada istifadə olunur?",
            "KL divergensiya niyə simmetrik deyil?",
        ],
    ),
    day(
        "Hesablama qrafiki və autograd",
        [
            "Forward pass və computation graph",
            "Chain rule-un qrafik üzərində tətbiqi (backpropagation)",
            "PyTorch autograd: requires_grad, backward(), .grad",
            "Gradient accumulation və zero_grad() səhvləri",
        ],
        [
            yt("Neural Networks: Zero to Hero - micrograd", "Andrej Karpathy", "2s 25d", "karpathy micrograd backpropagation"),
            yt("PyTorch autograd dərindən", "PyTorch (rəsmi)", "20 d", "pytorch autograd tutorial"),
        ],
        [
            doc("PyTorch: autograd mexaniki", "pytorch.org", AUTOGRAD),
            doc("Karpathy micrograd repo", "GitHub", "https://github.com/karpathy/micrograd"),
        ],
        [
            "Karpathy-nin micrograd videosunu izləyib öz versiyanı yaz",
            "3 dəyişənli funksiya üçün əl ilə backprop hesabla",
            "PyTorch autograd ilə nəticəni yoxla",
            "Eyni hesablamanı iki dəfə aparıb gradient-lərin toplanmasını müşahidə et",
        ],
        "Sıfırdan yazılmış kiçik autograd engine (micrograd üslubunda)",
        [
            "Computation graph nədir?",
            "Backpropagation chain rule-dan necə gəlir?",
            "`zero_grad()` olmasa nə baş verir?",
        ],
    ),
    day(
        "Optimizasiya alqoritmləri: SGD, Momentum, Adam",
        [
            "Batch, mini-batch və stochastic gradient descent",
            "Momentum və Nesterov",
            "RMSProp və Adam",
            "Learning rate schedule-ları",
        ],
        [
            yt("Stochastic Gradient Descent izahı", "StatQuest", "30 d", "statquest stochastic gradient descent"),
            yt("Adam optimizer", "DeepLearning.AI", "20 d", "adam optimizer explained deeplearning ai"),
        ],
        [
            doc("Optimizing Gradient Descent (blog)", "ruder.io", RUDER),
            doc("PyTorch: optimizer-lər", "pytorch.org", "https://pytorch.org/docs/stable/optim.html"),
        ],
        [
            "Sadə 2D funksiyada SGD, Momentum və Adam-ı müqayisə et",
            "Hər optimizatorun trayektoriyasını kontur qrafikdə çək",
            "Learning rate schedule tətbiq et və effektini göstər",
            "Nəticələri cədvəl şəklində yaz",
        ],
        "Optimizatorların vizual müqayisəsi notebooku",
        [
            "Mini-batch niyə tam batch-dan üstündür?",
            "Momentum nəyi həll edir?",
            "Adam hansı iki metodu birləşdirir?",
        ],
    ),
    day(
        "Riyaziyyatı NumPy ilə kodlaşdırma",
        [
            "NumPy xətti cəbr modulu (\u0060linalg\u0060)",
            "Broadcasting ilə matris əməliyyatları",
            "Statistik funksiyalar və axis anlayışı",
            "Vektorlaşdirmə ilə Python dövrlərindən 100x sürət",
        ],
        [
            yt("NumPy Linear Algebra", "Keith Galli", "40 d", "numpy linear algebra tutorial"),
            yt("Vectorization və performans", "mCoding", "20 d", "numpy vectorization performance python"),
        ],
        [
            doc("NumPy istifadəçi təlimatı", "numpy.org", NUMPY + "user/index.html"),
            gq("NumPy performans məsləhətləri", "numpy.org", "numpy performance best practices vectorization"),
        ],
        [
            "Əvvəlki günlərin 3 funksiyasını vektorlaşdırılmış formaya çevir",
            "Dövr vs vektorlaşdırılmış versiyanın vaxtını ölç (timeit)",
            "Xətti cəbr funksiyaları üçün unit test yaz",
            "Nəticələri README-də qeyd et",
        ],
        "Vektorlaşdırılmış, test edilmiş `linalg_utils.py` modulu",
        [
            "Broadcasting nədir?",
            "Niyə NumPy dövrlərdən sürətlidir?",
            "`axis` parametri nə edir?",
        ],
    ),
    day(
        "Riyaziyyatın ML-də birləşməsi və riyazi notasiya oxumaq",
        [
            "Paper-lərdə notasiya: sütun vektoru, matris, toplama simvolu",
            "Ehtimal və xətti cəbrin birlikdə istifadəsi",
            "İsbatları oxumaq: kifayət səviyyəsində anlama",
            "Riyazi ifadəni koda çevirmək vərdişi",
        ],
        [
            yt("ML paper-lərində riyaziyyatı oxumaq", "Yannic Kilcher", "25 d", "how to read machine learning papers math"),
            yt("Riyazi notasiyaya baxış", "DeepLearning.AI", "20 d", "linear algebra notation machine learning review"),
        ],
        [
            doc("Deep Learning Book: riyazi ön biliklər (fəsil 2-4)", "deeplearningbook.org", DLB),
            gq("ML üçün riyazi notasiya", "wikipedia.org", "mathematical notation machine learning"),
        ],
        [
            "Bir ML paper seç və notasiyanı öz sözlərinlə izah et",
            "Paper-dəki 3 tənliyi NumPy koduna çevir",
            "Likelihood ifadəsini bir abzasda izah et",
            "Öyrəndiyin notasiyaları şəxsi lüğətə əlavə et",
        ],
        "Riyazi notasiya lüğəti + 3 tənliyin kod versiyası",
        [
            "Toplama simvolu ilə yazılmış ifadəni koda necə çevirirsən?",
            "Sütun vektoru konvensiyası nə üçün vacibdir?",
            "Likelihood ifadəsini oxuyub izah edə bilirsənmi?",
        ],
    ),
    day(
        "Faza 2 layihəsi: sıfırdan xətti reqressiya",
        [
            "Bütün faza riyaziyyatının birləşdirilməsi",
            "Normal equation vs gradient descent",
            "Modelin qiymətləndirilməsi (MSE, R²)",
            "Nəticələrin vizual və yazılı təqdimatı",
        ],
        [
            yt("Linear Regression from scratch", "Andrew Ng / DeepLearning.AI", "25 d", "linear regression from scratch numpy"),
            yt("Gradient descent for linear regression", "StatQuest", "25 d", "statquest linear regression gradient descent"),
        ],
        [
            doc("scikit-learn: LinearRegression", "scikit-learn.org", "https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html"),
            doc("Karpathy: neural networks zero to hero", "YouTube/Karpathy", "https://karpathy.ai/zero-to-hero.html"),
        ],
        [
            "Xətti reqressiyanı yalnız NumPy ilə implement et (fit/predict)",
            "Normal equation ilə də həll et və nəticələri müqayisə et",
            "sklearn ilə müqayisə edib fərqi ölç",
            "Loss-un iterasiya üzrə azalma qrafikini çək",
        ],
        "Tam işləyən, sənədləşdirilmiş xətti reqressiya layihəsi (GitHub repo)",
        [
            "Normal equation nə vaxt gradient descent-dən sürətlidir?",
            "R² nəyi ölçür?",
            "Loss əyriniz necə görünməlidir?",
        ],
    ),
]

weeks = [
    {
        "focus": "Xətti cəbr",
        "project": "NumPy ilə xətti cəbr kitabxanası: matris vurma, transpozisiya, Gauss elimination və testlər",
        "quiz": "Vektor, matris, eigen, SVD üzrə 10 sual",
    },
    {
        "focus": "Ehtimal və statistika",
        "project": "Ehtimal notebooku: paylanmaların simulyasiyası + Mərkəzi Limit Teoreminin vizual sübutu",
        "quiz": "Ehtimal, paylanmalar, CLT və hipotez testi üzrə 10 sual",
    },
    {
        "focus": "Optimizasiya və informasiya nəzəriyyəsi",
        "project": "Sıfırdan gradient descent + xətti reqressiya notebooku (yalnız NumPy, sklearn ilə müqayisəli)",
        "quiz": "Törəmə, gradient descent, MLE, entropiya və autograd üzrə 10 sual",
    },
]

PHASE = phase(
    2,
    "Riyaziyyat: xətti cəbr, hesab, ehtimal və statistika",
    "ML modellərinin arxasındakı riyaziyyatı intuisiya səviyyəsində anlamaq və NumPy ilə kodlaşdırmaq.",
    "54-62 saat",
    weeks,
    days,
)
