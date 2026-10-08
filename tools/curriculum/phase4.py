"""Phase 4 - Classical machine learning with scikit-learn (days 64-84, 18 study days)."""

from helpers import day, doc, gq, phase, yt

SK = "https://scikit-learn.org/stable/"
SK_EVAL = "https://scikit-learn.org/stable/modules/model_evaluation.html"
SK_CV = "https://scikit-learn.org/stable/modules/cross_validation.html"
SK_PRE = "https://scikit-learn.org/stable/modules/preprocessing.html"
SK_PIPE = "https://scikit-learn.org/stable/modules/compose.html"
SK_TREE = "https://scikit-learn.org/stable/modules/tree.html"
SK_ENS = "https://scikit-learn.org/stable/modules/ensemble.html"
SK_SVM = "https://scikit-learn.org/stable/modules/svm.html"
SK_CLUST = "https://scikit-learn.org/stable/modules/clustering.html"
SK_DEC = "https://scikit-learn.org/stable/modules/decomposition.html"
SK_EX = "https://scikit-learn.org/stable/auto_examples/index.html"
KAGGLE_ML = "https://www.kaggle.com/learn/intro-to-machine-learning"
KAGGLE_FE = "https://www.kaggle.com/learn/feature-engineering"
ESL = "https://www.statlearning.com/"
XGB = "https://xgboost.readthedocs.io/en/stable/"
LGBM = "https://lightgbm.readthedocs.io/en/latest/"
CAT = "https://catboost.ai/docs/"
IMBL = "https://imbalanced-learn.org/stable/"
SHAP = "https://shap.readthedocs.io/en/latest/"
OPTUNA = "https://optuna.readthedocs.io/en/stable/"
MLFLOW = "https://mlflow.org/docs/latest/"
INTERP = "https://christophm.github.io/interpretable-ml-book/"
GCRASH = "https://developers.google.com/machine-learning/crash-course"

days = [
    day(
        "ML nədir: anlayışlar və iş axını",
        [
            "Supervised, unsupervised, reinforcement learning",
            "Klassifikasiya vs reqressiya",
            "Train / validation / test bölgüsü və niyə vacibdir",
            "ML layihəsinin standart iş axını",
        ],
        [
            yt("Machine Learning Full Course", "freeCodeCamp", "3s", "freecodecamp machine learning full course"),
            yt("What is Machine Learning", "StatQuest", "15 d", "statquest machine learning basics"),
        ],
        [
            doc("Google ML Crash Course", "developers.google.com", GCRASH),
            doc("scikit-learn: başlanğıc", "scikit-learn.org", SK + "getting_started.html"),
        ],
        [
            "3 ML tipini real nümunələrlə yaz",
            "Bir dataset seç və train/test bölgüsü et",
            "Data leakage nümunəsi tap və yaz",
            "ML layihəsinin 7 addımını öz sözlərinlə yaz",
        ],
        "ML iş axını qeydi (markdown) + ilk dataset hazırlığı",
        [
            "Supervised və unsupervised fərqi nədir?",
            "Validation set niyə lazımdır?",
            "Data leakage nədir?",
        ],
    ),
    day(
        "İlk model: KNN və scikit-learn API",
        [
            "sklearn API: fit, predict, score, transform",
            "K-Nearest Neighbors alqoritmi",
            "Modelin dəqiqliyi və ilk qiymətləndirmə",
            "Estimator/transformer anlayışları",
        ],
        [
            yt("scikit-learn ilk addımlar", "Krish Naik", "50 d", "sklearn tutorial krish naik"),
            yt("KNN alqoritmi izahı", "StatQuest", "20 d", "knn k nearest neighbors statquest"),
        ],
        [
            doc("Kaggle: Intro to ML", "kaggle.com", KAGGLE_ML),
            doc("scikit-learn: KNeighborsClassifier", "scikit-learn.org", SK + "modules/generated/sklearn.neighbors.KNeighborsClassifier.html"),
        ],
        [
            "Iris dataset-i yüklə və KNN modelini öyrət",
            "Fərqli k dəyərləri üçün dəqiqliyi müqayisə et",
            "Normallaşdırmanın KNN-ə təsirini göstər",
            "Nəticələri cədvəl kimi yaz",
        ],
        "KNN məşqi notebooku (k seçimi analizi ilə)",
        [
            "fit/predict/transform nə edir?",
            "KNN niyə scaling tələb edir?",
            "k dəyəri nəticəyə necə təsir edir?",
        ],
    ),
    day(
        "Xətti modellər: reqressiya və loqistik",
        [
            "Xətti və polinomial reqressiya",
            "Ridge (L2) və Lasso (L1) requlyarizasiya",
            "Logistic regression və sigmoid",
            "Xətti modellərin nə vaxt yaxşı işlədiyi",
        ],
        [
            yt("Linear and Logistic Regression", "StatQuest", "45 d", "statquest linear regression logistic regression"),
            yt("Regularization: Ridge və Lasso", "StatQuest", "30 d", "statquest ridge lasso regularization"),
        ],
        [
            doc("scikit-learn: xətti modellər", "scikit-learn.org", SK + "modules/linear_model.html"),
            doc("ISLR kitabı (fəsillər 3, 4)", "statlearning.com", ESL),
        ],
        [
            "Reqressiya modelini real dataset üzərində öyrət və MSE hesabla",
            "Ridge və Lasso-nu fərqli alpha dəyərləri ilə müqayisə et",
            "Logistic regression ilə ikili klassifikasiya et",
            "Lasso-nun hansı əmsalları sıfırladığını göstər",
        ],
        "Xətti modellərin müqayisəsi cədvəli (R², MSE, əmsallar)",
        [
            "Ridge ilə Lasso fərqi nədir?",
            "Logistic regression niyə 'reqressiya' adlanır?",
            "Requlyarizasiya overfitting-i necə azaldır?",
        ],
    ),
    day(
        "Qərar ağacları və Random Forest",
        [
            "Decision tree: split kriteriyaları (Gini, entropy)",
            "Ağacın dərinliyi və overfitting",
            "Bagging və Random Forest",
            "Feature importance-ın intuitiv mənası",
        ],
        [
            yt("Decision Trees and Random Forests", "StatQuest", "45 d", "statquest decision trees random forests"),
            yt("Random Forest dərindən", "Krish Naik", "35 d", "random forest algorithm explained"),
        ],
        [
            doc("scikit-learn: qərar ağacları", "scikit-learn.org", SK_TREE),
            doc("scikit-learn: ensemble metodlar", "scikit-learn.org", SK_ENS),
        ],
        [
            "Ağacın dərinliyini dəyişərək overfitting-i göstər",
            "Random Forest qur və ağacla müqayisə et",
            "Feature importance-ları çap edib qrafik çək",
            "max_depth və n_estimators parametrlərini sına",
        ],
        "Ağac vs Random Forest müqayisəsi + importance qrafiki",
        [
            "Gini impurity nədir?",
            "Random Forest niyə tək ağacdan yaxşıdır?",
            "Feature importance hansı hallarda yanıldır?",
        ],
    ),
    day(
        "Gradient boosting: XGBoost, LightGBM, CatBoost",
        [
            "Boosting ideyası: ardıcıl zəif modellər",
            "XGBoost-un əsas parametrləri",
            "LightGBM və CatBoost fərqləri",
            "Tabular data-da nə üçün boosting çox vaxt ən güclüdür",
        ],
        [
            yt("XGBoost dərindən izah", "StatQuest", "40 d", "statquest xgboost gradient boosting"),
            yt("LightGBM ilə təlim", "Krish Naik", "30 d", "lightgbm tutorial"),
        ],
        [
            doc("XGBoost sənədləri", "xgboost.readthedocs.io", XGB),
            doc("LightGBM sənədləri", "lightgbm.readthedocs.io", LGBM),
            doc("CatBoost sənədləri", "catboost.ai", CAT),
        ],
        [
            "Eyni dataset üzərində 3 boosting kitabxanasını müqayisə et",
            "Erkən dayanma (early stopping) istifadə et",
            "XGBoost feature importance-larını çıxart",
            "Dəqiqlik və təlim vaxtını cədvəldə göstər",
        ],
        "3 boosting modelinin müqayisə cədvəli + ən yaxşı modelin saxlanması",
        [
            "Boosting ilə bagging fərqi nədir?",
            "Early stopping nə edir?",
            "Nə vaxt XGBoost yerinə LightGBM seçərdin?",
        ],
    ),
    day(
        "SVM və kernel trick",
        [
            "Maximum margin ideyası",
            "Soft margin və C parametri",
            "Kernel funksiyaları (linear, RBF, polynomial)",
            "SVM-in kiçik və orta dataset-lərdə güclü tərəfi",
        ],
        [
            yt("Support Vector Machines", "StatQuest", "30 d", "statquest support vector machines"),
            yt("Kernel trick izahı", "MIT / Josh Starmer", "25 d", "kernel trick explained svm"),
        ],
        [
            doc("scikit-learn: SVM", "scikit-learn.org", SK_SVM),
            gq("SVM kernel seçimi", "scikit-learn.org", "svm kernel selection rbf linear"),
        ],
        [
            "İki sinifli dataset üzərində SVM öyrət",
            "C və gamma parametrlərini dəyişərək qərar sərhədini vizuallaşdır",
            "Linear və RBF kernel-i müqayisə et",
            "Kiçik dataset-də SVM vs Random Forest müqayisəsi apar",
        ],
        "SVM qərar sərhədləri vizuallaşdırması (parametr analizi ilə)",
        [
            "SVM-də C parametri nə edir?",
            "Kernel trick nəyi həll edir?",
            "SVM nə vaxt yavaş olur?",
        ],
    ),
    day(
        "Model qiymətləndirmə: metrikalar",
        [
            "Confusion matrix və ondan törəyən metrikalar",
            "Precision, recall, F1, accuracy-nin tələləri",
            "ROC-AUC və PR curve",
            "Hansı problemi hansı metriklə ölçmək",
        ],
        [
            yt("Confusion Matrix və metriklər", "StatQuest", "40 d", "statquest confusion matrix precision recall"),
            yt("ROC və AUC izahı", "StatQuest", "20 d", "statquest roc and auc"),
        ],
        [
            doc("scikit-learn: model qiymətləndirmə", "scikit-learn.org", SK_EVAL),
            gq("Classification metrics nə vaxt yanıldır", "scikit-learn.org", "classification metrics pitfalls accuracy"),
        ],
        [
            "Bir modelin confusion matrix-ini çıxart və izah et",
            "Precision, recall, F1 hesabla (əl ilə və sklearn ilə)",
            "ROC və PR əyrilərini çək",
            "Balanssız dataset-də accuracy-nin yanıldığını göstər",
        ],
        "Metrikalar hesabatı (classification_report + əyrilər)",
        [
            "Precision ilə recall fərqi nədir?",
            "ROC-AUC nəyi ölçür?",
            "Balanssız data-da hansı metriklərə baxmalı?",
        ],
    ),
    day(
        "Cross-validation və bias-variance",
        [
            "k-fold, stratified, leave-one-out CV",
            "Bias-variance tradeoff",
            "Learning curves və validation curves",
            "Nəticələrin etibarlılığı və variasiya",
        ],
        [
            yt("Cross Validation", "StatQuest", "25 d", "statquest cross validation"),
            yt("Bias-Variance Tradeoff", "StatQuest", "20 d", "statquest bias variance tradeoff"),
        ],
        [
            doc("scikit-learn: cross-validation", "scikit-learn.org", SK_CV),
            doc("scikit-learn: learning curves", "scikit-learn.org", SK + "modules/learning_curve.html"),
        ],
        [
            "5-fold CV ilə model qiymətləndir",
            "Stratified CV ilə müqayisə et",
            "Learning curve çək və overfit/underfit yoxla",
            "Bias-variance nəticəsini bir abzasda yaz",
        ],
        "CV nəticələri hesabatı + learning curve qrafiki",
        [
            "Niyə tək train/test bölgüsü kifayət deyil?",
            "Underfitting əlamətləri nədir?",
            "Stratified CV nə vaxt lazımdır?",
        ],
    ),
    day(
        "Feature engineering və data hazırlığı",
        [
            "Scaling: StandardScaler, MinMaxScaler, RobustScaler",
            "Encoding: OneHot, Ordinal, Target encoding",
            "Polinomial feature-lar və interaction-lar",
            "Feature selection: filter, wrapper, embedded",
        ],
        [
            yt("Feature Engineering Full Course", "Krish Naik", "2s", "feature engineering krish naik"),
            yt("Scaling və encoding", "StatQuest", "25 d", "feature scaling encoding machine learning"),
        ],
        [
            doc("scikit-learn: preprocessing", "scikit-learn.org", SK_PRE),
            doc("scikit-learn: feature selection", "scikit-learn.org", SK + "modules/feature_selection.html"),
            doc("Kaggle: Feature Engineering", "kaggle.com", KAGGLE_FE),
        ],
        [
            "Dataset üzərində 5 yeni feature yarat",
            "3 fərqli encoding üsulunu müqayisə et",
            "Feature selection ilə sütun sayını azalt və effekti ölç",
            "Yeni feature-ların modelə təsirini cədvəldə göstər",
        ],
        "Feature engineering nəticələri cədvəli (əvvəl/sonra müqayisə)",
        [
            "StandardScaler ilə MinMaxScaler fərqi nədir?",
            "Target encoding-in riski nədir?",
            "Hansı feature-ları sildin və niyə?",
        ],
    ),
    day(
        "Pipeline və data leakage-ın qarşısı",
        [
            "sklearn Pipeline anlayışı",
            "ColumnTransformer ilə heterogen data",
            "Cross-validation içində preprocessing",
            "Data leakage növləri və aşkarlanması",
        ],
        [
            yt("sklearn Pipeline dərsliyi", "Data School", "35 d", "sklearn pipeline tutorial"),
            yt("Data leakage izahı", "Krish Naik", "25 d", "data leakage machine learning"),
        ],
        [
            doc("scikit-learn: Pipeline", "scikit-learn.org", SK_PIPE),
            gq("Data leakage növləri", "kaggle.com", "data leakage in machine learning kaggle"),
        ],
        [
            "Sayısal və kateqorik sütunlar üçün ColumnTransformer qur",
            "Pipeline-a scaler + model əlavə et",
            "Yanlış (leaky) və düzgün pipeline-ı müqayisə et",
            "Pipeline-ı joblib ilə yadda saxla",
        ],
        "Təkrar istifadə oluna bilən tam sklearn Pipeline",
        [
            "Pipeline hansı səhvlərin qarşısını alır?",
            "Data leakage necə baş verir?",
            "Pipeline-ı necə saxlamaq olar?",
        ],
    ),
    day(
        "Hiperparametr optimizasiyası",
        [
            "GridSearchCV və RandomizedSearchCV",
            "Optuna ilə Bayesian optimizasiya",
            "Nested CV və düzgün qiymətləndirmə",
            "Nəticələrin saxlanması (experiment qeydi)",
        ],
        [
            yt("Hyperparameter Tuning", "Krish Naik", "40 d", "hyperparameter tuning grid search random search"),
            yt("Optuna ilə optimizasiya", "Optuna (rəsmi)", "30 d", "optuna hyperparameter optimization tutorial"),
        ],
        [
            doc("scikit-learn: tuning", "scikit-learn.org", SK + "modules/grid_search.html"),
            doc("Optuna sənədləri", "optuna.readthedocs.io", OPTUNA),
        ],
        [
            "GridSearchCV ilə 3 parametr üzrə axtarış apar",
            "Eyni işi RandomizedSearchCV ilə daha sürətli et",
            "Optuna ilə 20 trial işlət və ən yaxşı nəticəni tap",
            "Bütün nəticələri cədvəldə müqayisə et",
        ],
        "Optimizasiya müqayisəsi + ən yaxşı modelin parametrləri",
        [
            "GridSearch nə vaxt yararsızdır?",
            "Bayesian optimizasiya nəyi yaxşılaşdırır?",
            "Nested CV nə üçün lazımdır?",
        ],
    ),
    day(
        "Balanssız data (imbalanced learning)",
        [
            "Balanssızlığın nəticələri",
            "Class weight və threshold tuning",
            "Oversampling: SMOTE, ADASYN",
            "Undersampling və kombinə edilmiş üsullar",
        ],
        [
            yt("Imbalanced data üsulları", "Krish Naik", "30 d", "imbalanced dataset machine learning smote"),
            yt("SMOTE izahı", "StatQuest", "20 d", "statquest smote imbalanced data"),
        ],
        [
            doc("imbalanced-learn sənədləri", "imbalanced-learn.org", IMBL),
            gq("Threshold tuning f1 score", "scikit-learn.org", "tuning decision threshold classification"),
        ],
        [
            "Balanssız dataset yarat (və ya hazır tap)",
            "Naiv model ilə balanslaşdırılmış modeli müqayisə et",
            "SMOTE tətbiq edib effekti ölç",
            "Qərar həddini dəyişərək precision/recall balansını tənzimlə",
        ],
        "Balanssızlıqla mübarizə hesabatı (əvvəl/sonra metrikalar)",
        [
            "SMOTE nə edir?",
            "Class weight nə vaxt SMOTE-dan üstündür?",
            "Niyə accuracy balanssız data-da yanıltıcıdır?",
        ],
    ),
    day(
        "Clustering: k-means, hierarchical, DBSCAN",
        [
            "k-means alqoritmi və elbow metodu",
            "Hierarchical clustering və dendrogram",
            "DBSCAN və sıxlıq əsaslı klasterləmə",
            "Silhouette score və klaster keyfiyyəti",
        ],
        [
            yt("K-means clustering", "StatQuest", "25 d", "statquest k-means clustering"),
            yt("Hierarchical və DBSCAN", "StatQuest", "30 d", "statquest hierarchical clustering dbscan"),
        ],
        [
            doc("scikit-learn: clustering", "scikit-learn.org", SK_CLUST),
            gq("Silhouette score", "scikit-learn.org", "silhouette score clustering evaluation"),
        ],
        [
            "k-means ilə 3 klaster tap və vizuallaşdır",
            "Elbow və silhouette ilə optimal k-nı seç",
            "DBSCAN-ı qeyri-sferik data üzərində tətbiq et",
            "3 üsulun nəticələrini müqayisə et",
        ],
        "Klasterləmə müqayisəsi notebooku (vizual + metrikalarla)",
        [
            "k-means hansı fərziyyələrlə işləyir?",
            "DBSCAN nə vaxt üstündür?",
            "Bitərəf k-nı necə seçmək olar?",
        ],
    ),
    day(
        "Ölçü azaltma və vizualizasiya: PCA, t-SNE, UMAP",
        [
            "PCA-nın praktik tətbiqi",
            "t-SNE: qonşuluq əsaslı vizualizasiya",
            "UMAP ilə böyük dataset-lərin vizualizasiyasi",
            "Yüksək ölçülülüyün lənəti (curse of dimensionality)",
        ],
        [
            yt("t-SNE və UMAP vizuallaşdırma", "StatQuest", "30 d", "statquest t-sne umap"),
            yt("PCA praktikada", "StatQuest", "25 d", "statquest pca practical example"),
        ],
        [
            doc("scikit-learn: decomposition", "scikit-learn.org", SK_DEC),
            doc("UMAP sənədləri", "umap-learn.readthedocs.io", "https://umap-learn.readthedocs.io/en/latest/"),
        ],
        [
            "Yüksək ölçülü dataset-də PCA tətbiq et",
            "İzah olunan variasiya qrafikini çək",
            "t-SNE və UMAP nəticələrini müqayisə et",
            "Ölçü azaltmanın model performansına təsirini ölç",
        ],
        "Ölçü azaltma müqayisəsi + 2D vizualizasiyalar",
        [
            "PCA niyə sürətli və stabil seçimdir?",
            "t-SNE oxları niyə şərh olunmamalıdır?",
            "PCA feature selection-dan nə ilə fərqlənir?",
        ],
    ),
    day(
        "Anomaliya aşkarlama və qeyri-supervised tətbiqlər",
        [
            "Anomaliya vs outlier vs novelty",
            "Isolation Forest, One-Class SVM, LOF",
            "Autoencoder ilə rekonstruksiya xətası",
            "Metrikalar (supervised olmayan qiymətləndirmə)",
        ],
        [
            yt("Anomaly detection üsulları", "Krish Naik", "30 d", "anomaly detection machine learning isolation forest"),
            yt("Autoencoder ilə anomaliya", "Sentdex", "25 d", "autoencoder anomaly detection python"),
        ],
        [
            doc("scikit-learn: anomaly detection", "scikit-learn.org", SK + "modules/outlier_detection.html"),
            gq("Anomaly detection qiymətləndirmə", "scikit-learn.org", "evaluating anomaly detection models"),
        ],
        [
            "Isolation Forest ilə anomaliyaları tap",
            "LOF ilə nəticəni müqayisə et",
            "Kiçik autoencoder yaz və rekonstruksiya xətasına bax",
            "Hansı metodun daha uyğun olduğunu əsaslandır",
        ],
        "Anomaliya aşkarlama nümunəsi (3 metod müqayisəsi)",
        [
            "Anomaliya ilə outlier fərqi nədir?",
            "Isolation Forest necə işləyir?",
            "Nəticəni etiketli data olmadan necə qiymətləndirmək olar?",
        ],
    ),
    day(
        "Model izahı: SHAP və interpretasiya",
        [
            "Global vs local interpretasiya",
            "Permutation importance və partial dependence",
            "SHAP dəyərləri və intuisiya",
            "İzahın biznes/səhiyyə kimi sahələrdə əhəmiyyəti",
        ],
        [
            yt("SHAP dəyərləri izahı", "StatQuest", "30 d", "statquest shap values"),
            yt("Interpretable ML üsulları", "Christoph Molnar", "35 d", "interpretable machine learning methods"),
        ],
        [
            doc("SHAP sənədləri", "shap.readthedocs.io", SHAP),
            doc("Interpretable ML (kitab)", "christophm.github.io", INTERP),
        ],
        [
            "Model üçün permutation importance hesabla",
            "SHAP summary plot çək",
            "5 nümunə üçün lokal izah hazırla",
            "İzahdan hansı biznes qərarının çıxdığını yaz",
        ],
        "Model izahı hesabatı (SHAP qrafikləri ilə)",
        [
            "Global və lokal izah fərqi nədir?",
            "SHAP-ın üstünlüyü feature importance-dan nədir?",
            "İzah model performansına təsir edir?",
        ],
    ),
    day(
        "ML layihəsinin strukturlaşdırılması və eksperiment izləmə",
        [
            "Layihə strukturu: data, notebooks, src, models, reports",
            "Eksperimentlərin qeydə alınması (MLflow basics)",
            "Reproducibility: seed, versiya, konfiqurasiya faylları",
            "Model kartı və sənədləşdirmə",
        ],
        [
            yt("MLflow ilə eksperiment izləmə", "Krish Naik", "35 d", "mlflow experiment tracking tutorial"),
            yt("ML layihə strukturu", "Made With ML", "25 d", "machine learning project structure best practices"),
        ],
        [
            doc("MLflow sənədləri", "mlflow.org", MLFLOW),
            doc("Made With ML", "madewithml.com", "https://madewithml.com/"),
        ],
        [
            "Layihə üçün qovluq strukturu yarat",
            "`config.yaml` ilə parametrləri koddan ayır",
            "MLflow ilə 5 eksperiment qeyd et",
            "README-də nəticələr cədvəli yaz",
        ],
        "Strukturlaşdırılmış ML layihə şablonu (MLflow ilə)",
        [
            "Nəticələrin reproduksiyası üçün nə lazımdır?",
            "MLflow nəyi həll edir?",
            "Model kartı nədir?",
        ],
    ),
    day(
        "Faza 4 layihəsi: tam ML pipeline",
        [
            "Problemin sonuna qədər aparılması",
            "Model seçimi və əsaslandırma",
            "Xəta analizi (error analysis)",
            "Nəticələrin təqdimatı",
        ],
        [
            yt("Tam ML layihəsi (tabular data)", "Abhishek Thakur", "50 d", "complete machine learning project tabular data"),
            yt("Error analysis necə aparılır", "Andrew Ng", "20 d", "error analysis machine learning andrew ng"),
        ],
        [
            doc("scikit-learn: nümunələr qalereyası", "scikit-learn.org", SK_EX),
            doc("Hands-On ML kodları", "github.com/ageron", "https://github.com/ageron/handson-ml3"),
        ],
        [
            "Tabular dataset seç və problemi formalaşdır",
            "Ən azı 4 model öyrət və CV ilə müqayisə et",
            "Ən yaxşı modeli tuning et",
            "Error analysis apar və README-də nəticələri yaz",
        ],
        "GitHub-da `ml-project` reposu (pipeline + nəticələr + README)",
        [
            "Niyə bu modeli seçdin?",
            "Hansı nümunələrdə model səhv edir?",
            "Növbəti addım nə olardı?",
        ],
    ),
]

weeks = [
    {
        "focus": "Supervised learning əsasları",
        "project": "İlk ML pipeline: 4 model (KNN, linear, tree, boosting) müqayisəsi + nəticələr cədvəli",
        "quiz": "Supervised learning, KNN, xətti modellər və ağaclar üzrə 10 sual",
    },
    {
        "focus": "Qiymətləndirmə və data hazırlığı",
        "project": "Model seçimi layihəsi: cross-validation + hyperparameter tuning + error analysis hesabatı",
        "quiz": "Metrikalar, cross-validation, feature engineering və leakage üzrə 10 sual",
    },
    {
        "focus": "Unsupervised learning və izah",
        "project": "Müştəri seqmentasiyası: k-means + PCA + SHAP ilə izahlı hesabat",
        "quiz": "Clustering, ölçü azaltma, anomaliya və SHAP üzrə 10 sual",
    },
]

PHASE = phase(
    4,
    "Klassik maşın öyrənməsi (scikit-learn)",
    "Supervised və unsupervised alqoritmləri, düzgün qiymətləndirmə, feature engineering və model izahı.",
    "54-62 saat",
    weeks,
    days,
)
