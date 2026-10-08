"""Phase 7 - Computer vision basics (days 141-154, 2 weeks, 12 study days)."""

from helpers import day, doc, gq, phase, yt

OPENCV = "https://docs.opencv.org/4.x/"
OPENCV_REPO = "https://github.com/opencv/opencv"
ULTRA = "https://docs.ultralytics.com/"
PYIMG = "https://pyimagesearch.com/"
TORCHVISION = "https://pytorch.org/vision/stable/index.html"
ONNX = "https://onnx.ai/"
VIT = "https://arxiv.org/abs/2010.11929"
CLIP = "https://arxiv.org/abs/2103.00020"
UNET = "https://arxiv.org/abs/1505.04597"
YOLO = "https://arxiv.org/abs/1506.02640"
HF_PAPERS = "https://huggingface.co/papers"
DISTILL = "https://distill.pub/"
CS231N = "https://cs231n.stanford.edu/"

days = [
    day(
        "CV əsasları: OpenCV ilə şəkil emalı",
        [
            "Şəkil yükləmə, yadda saxlama, formatlar",
            "Rəng fəzaları (RGB, BGR, HSV, grayscale)",
            "Filtrlər: blur, threshold, edge (Sobel, Canny)",
            "Morphological əməliyyatlar (erosion, dilation)",
        ],
        [
            yt("OpenCV Python Full Course", "freeCodeCamp", "3s 30d", "opencv python full course freecodecamp"),
            yt("Şəkil emalı əsasları", "Sentdex", "40 d", "opencv image processing tutorial sentdex"),
        ],
        [
            doc("OpenCV Python dərsləri", "docs.opencv.org", OPENCV),
            doc("CS231n: şəkillər üzərində iş", "cs231n.stanford.edu", CS231N),
        ],
        [
            "Şəkil oxu, ölçüsünü dəyiş, qeyd et",
            "Grayscale çevrilmə və threshold tətbiq et",
            "Canny edge detection ilə konturları çıxart",
            "Morphological əməliyyatları müqayisə et",
        ],
        "Şəkil emalı nümunələri toplusu (əvvəl/sonra şəkillərlə)",
        [
            "BGR ilə RGB fərqi nə üçün problem yaradır?",
            "Threshold necə seçilir?",
            "Edge detection nə üçün istifadə olunur?",
        ],
    ),
    day(
        "Feature detection: SIFT, ORB, matching",
        [
            "Keypoint və descriptor anlayışı",
            "SIFT, SURF, ORB müqayisəsi",
            "Feature matching və RANSAC",
            "Homography və panorama qurma",
        ],
        [
            yt("Feature detection və matching", "PyImageSearch / First Principles", "40 d", "sift orb feature matching tutorial"),
            yt("Homography izahı", "LearnOpenCV", "25 d", "homography ransac computer vision"),
        ],
        [
            doc("OpenCV: feature detection", "docs.opencv.org", OPENCV + "d7/d56/tutorial_py_table_of_contents_feature2d.html"),
            gq("SIFT ilə ORB fərqi", "pyimagesearch.com", "sift vs orb keypoint detector comparison"),
        ],
        [
            "İki şəkil arasında ORB ilə keypoint tap",
            "Descriptor-ları uyğunlaşdır (BFMatcher)",
            "RANSAC ilə yalnız düzgün uyğunluqları saxla",
            "Homography hesabla və bir şəkli digərinə çevir",
        ],
        "Feature matching + homography nümunəsi (vizual nəticə ilə)",
        [
            "Keypoint ilə descriptor fərqi nədir?",
            "RANSAC nəyi həll edir?",
            "Homography nə vaxt hesablanmır?",
        ],
    ),
    day(
        "Obyekt aşkarlamanın klassik əsasları",
        [
            "Detection vs klassifikasiya vs lokalizasiya",
            "Sliding window və HOG + SVM",
            "IoU metriki",
            "Precision/recall və mAP",
        ],
        [
            yt("Object detection əsasları", "Andrew Ng / DeepLearning.AI", "35 d", "object detection basics hog iou map"),
            yt("mAP metriki izahı", "Ultralytics", "20 d", "mean average precision map explained"),
        ],
        [
            doc("Ultralytics: metriklər", "docs.ultralytics.com", ULTRA + "guides/yolo-performance-metrics/"),
            gq("HOG + SVM ilə deteksiya", "pyimagesearch.com", "hog svm object detection tutorial"),
        ],
        [
            "IoU funksiyasını yaz",
            "İki bounding box arasında IoU hesabla",
            "Precision/recall əyrisini çək",
            "mAP-ın necə hesablandığını bir abzasda yaz",
        ],
        "IoU + mAP hesablama funksiyaları (test ilə)",
        [
            "IoU nə deməkdir?",
            "mAP nə üçün 0.5 həddi ilə hesablanır?",
            "Klassifikasiya metriklərindən fərqi nədir?",
        ],
    ),
    day(
        "Modern deteksiya: YOLO ilə praktika",
        [
            "One-stage vs two-stage detector",
            "YOLO arxitekturası və versiyaları",
            "Pretrained model ilə inference",
            "Xüsusi dataset-də yenidən öyrətmə",
        ],
        [
            yt("YOLOv8 Full Tutorial", "Nicolas Renotte", "1s", "yolov8 custom dataset training tutorial"),
            yt("Ultralytics YOLO kursu", "Ultralytics", "45 d", "ultralytics yolo python tutorial"),
        ],
        [
            doc("Ultralytics sənədləri", "docs.ultralytics.com", ULTRA),
            doc("Paper: YOLO", "arxiv.org", YOLO),
        ],
        [
            "Pretrained YOLO ilə şəkil/video üzərində deteksiya et",
            "50 şəkil annotasiya et (Roboflow)",
            "Modeli öz dataset-ində 20 epoch öyrət",
            "Nəticələri mAP cədvəlində müqayisə et",
        ],
        "Öz dataset-ində öyrədilmiş YOLO modeli + nəticələr",
        [
            "One-stage detektor niyə sürətlidir?",
            "Annotation formatı necə olmalıdır?",
            "mAP nəticəsini necə yaxşılaşdırmaq olar?",
        ],
    ),
    day(
        "Seqmentasiya: semantic və instance",
        [
            "Semantic vs instance vs panoptic seqmentasiya",
            "U-Net arxitekturası (encoder-decoder, skip connections)",
            "Mask R-CNN ideyası",
            "Seqmentasiya metrikləri (IoU, Dice)",
        ],
        [
            yt("U-Net izahı", "Yannic Kilcher / DigitalSreeni", "30 d", "u-net architecture explained segmentation"),
            yt("Seqmentasiya modelləri", "DigitalSreeni", "40 d", "image segmentation tutorial python"),
        ],
        [
            doc("Paper: U-Net", "arxiv.org", UNET),
            doc("torchvision seqmentasiya", "pytorch.org", TORCHVISION + "models.html#semantic-segmentation"),
        ],
        [
            "U-Net-i PyTorch ilə qur (kiçik versiya)",
            "Kiçik dataset-də seqmentasiya et",
            "IoU və Dice əmsalını hesabla",
            "Nəticələri maska şəkilləri ilə göstər",
        ],
        "İşləyən U-Net modeli + maska vizualizasiyaları",
        [
            "Skip connection nə üçün vacibdir?",
            "Semantic ilə instance fərqi nədir?",
            "Dice əmsalı nəyi ölçür?",
        ],
    ),
    day(
        "Praktik CV tapşırıqları: OCR, üz, pose",
        [
            "OCR: Tesseract və EasyOCR",
            "Üz aşkarlama və tanıma əsasları",
            "Pose estimation (MediaPipe)",
            "Hazır modelləri tətbiqə çevirmək vərdişi",
        ],
        [
            yt("OCR with Python", "Nicholas Renotte", "35 d", "ocr python tesseract easyocr tutorial"),
            yt("MediaPipe pose və face", "Nicholas Renotte", "40 d", "mediapipe python face pose detection"),
        ],
        [
            doc("MediaPipe", "developers.google.com", "https://ai.google.dev/edge/mediapipe/solutions/guide"),
            gq("EasyOCR istifadəsi", "github.com", "easyocr python tutorial"),
        ],
        [
            "Şəkildəki mətni OCR ilə çıxart",
            "Videoda üzləri aşkarla və say",
            "Pose estimation ilə hərəkəti izlə",
            "Nəticələri qısa videoda göstər",
        ],
        "3 praktik CV nümunəsi (OCR + face + pose) demo videoları ilə",
        [
            "OCR hansı hallarda səhv edir?",
            "Üz tanıma ilə aşkarlama fərqi nədir?",
            "Pose estimation hansı sahələrdə istifadə olunur?",
        ],
    ),
    day(
        "Vision Transformers (ViT) və CLIP",
        [
            "ViT arxitekturası: patch embedding, attention",
            "ViT vs CNN: nə vaxt hansı",
            "CLIP: kontrastiv öyrənmə",
            "Hugging Face ilə pretrained CV modelləri",
        ],
        [
            yt("Vision Transformer izahı", "Yannic Kilcher", "30 d", "vision transformer paper explained vit"),
            yt("CLIP arxitekturası", "Hugging Face", "25 d", "clip model explained hugging face"),
        ],
        [
            doc("Paper: ViT", "arxiv.org", VIT),
            doc("Paper: CLIP", "arxiv.org", CLIP),
            doc("Hugging Face CV modelləri", "huggingface.co", "https://huggingface.co/docs/transformers/tasks/image_classification"),
        ],
        [
            "ViT ilə şəkil klassifikasiyası et",
            "Eyni dataset-də CNN ilə müqayisə et",
            "CLIP ilə oxşarlıq matrisini hesabla",
            "Nəticələri cədvəldə göstər",
        ],
        "ViT vs CNN müqayisəsi + CLIP nümunəsi",
        [
            "ViT niyə böyük dataset tələb edir?",
            "CLIP necə öyrədilir?",
            "Nə vaxt CNN seçmək daha yaxşıdır?",
        ],
    ),
    day(
        "Zero-shot və open-vocabulary CV",
        [
            "Zero-shot klassifikasiya (CLIP ilə)",
            "Open-vocabulary detection (Grounding DINO, YOLO-World)",
            "Prompt-ların CV-də rolu",
            "Məhdudiyyətlər və praktik istifadə",
        ],
        [
            yt("Zero-shot CV", "Hugging Face", "30 d", "zero shot image classification clip tutorial"),
            yt("Open vocabulary detection", "Ultralytics / Roboflow", "30 d", "open vocabulary object detection yoloworld"),
        ],
        [
            doc("Hugging Face: zero-shot image classification", "huggingface.co", "https://huggingface.co/docs/transformers/tasks/zero_shot_image_classification"),
            doc("HF Papers (CV yenilikləri)", "huggingface.co", HF_PAPERS),
        ],
        [
            "CLIP ilə öz şəkillərinizi etiketsiz klassifikasiya et",
            "Prompt dəyişərək nəticəni müqayisə et",
            "Open-vocabulary deteksiya nümunəsi işlət",
            "Məhdudiyyətləri yaz",
        ],
        "Zero-shot CV təcrübəsi + prompt analizi",
        [
            "Zero-shot nə deməkdir?",
            "Prompt keyfiyyəti nəticəyə necə təsir edir?",
            "Open-vocabulary modellərin riski nədir?",
        ],
    ),
    day(
        "Video analizi və obyekt izləmə",
        [
            "Video oxuma (kadr-kadr emal)",
            "Optical flow əsasları",
            "Tracking: SORT, DeepSORT ideyası",
            "Video üzərində performans məsələləri",
        ],
        [
            yt("Object tracking tutorial", "Nicolas Renotte", "40 d", "object tracking yolo deepsort tutorial"),
            yt("Optical flow izahı", "LearnOpenCV", "25 d", "optical flow explained opencv"),
        ],
        [
            doc("OpenCV: video analizi", "docs.opencv.org", OPENCV + "d6/d00/tutorial_py_root.html"),
            doc("Ultralytics tracking", "docs.ultralytics.com", ULTRA + "modes/track/"),
        ],
        [
            "Videoda obyektləri deteksiya et",
            "Tracker əlavə et və ID-ləri izlə",
            "Kadr emal sürətini (FPS) ölç",
            "Nəticəni qeyd edilmiş videoda göstər",
        ],
        "Video analizi demo (obyekt izləmə ilə)",
        [
            "Tracking ilə detection fərqi nədir?",
            "FPS-i nə azaldır?",
            "Optical flow nə üçün istifadə olunur?",
        ],
    ),
    day(
        "CV modelini deploy etmək: ONNX və sürət",
        [
            "ONNX formatı və export",
            "ONNX Runtime ilə inference",
            "Model kvantizasiyası və sürət optimallaşdırması",
            "Real-time inference servisi",
        ],
        [
            yt("PyTorch to ONNX export", "PyTorch (rəsmi)", "25 d", "pytorch onnx export tutorial"),
            yt("ONNX Runtime ilə sürət", "Microsoft", "30 d", "onnx runtime inference optimization"),
        ],
        [
            doc("ONNX sənədləri", "onnx.ai", ONNX),
            doc("PyTorch ONNX export", "pytorch.org", "https://pytorch.org/docs/stable/onnx.html"),
        ],
        [
            "PyTorch modelini ONNX-a çevir",
            "ONNX Runtime ilə inference et",
            "Sürəti PyTorch ilə müqayisə et",
            "Kiçik FastAPI servisi qur",
        ],
        "ONNX + FastAPI ilə işləyən CV servisi (sürət müqayisəsi ilə)",
        [
            "ONNX nə qazandırır?",
            "Export zamanı hansı xətalar olur?",
            "Sürət optimallaşdırması necə ölçülür?",
        ],
    ),
    day(
        "CV layihəsi I: dataset və baseline",
        [
            "Problemin seçilməsi (klassifikasiya, deteksiya, seqmentasiya)",
            "Data toplama və annotasiya",
            "Augmentation strategiyası",
            "Baseline model",
        ],
        [
            yt("CV layihəsi planı", "Roboflow", "35 d", "computer vision project end to end tutorial"),
            yt("Data annotasiyası", "Roboflow", "25 d", "image annotation tools tutorial roboflow"),
        ],
        [
            doc("Roboflow", "roboflow.com", "https://roboflow.com/"),
            doc("torchvision augmentation", "pytorch.org", TORCHVISION + "transforms.html"),
        ],
        [
            "Layihə mövzusunu seç və sualı yaz",
            "Ən azı 100 şəkil topla/annotasiya et",
            "Augmentation pipeline qur",
            "Baseline modeli öyrət və metrikaları qeyd et",
        ],
        "Dataset + baseline modelin nəticələri",
        [
            "Dataset keyfiyyəti nəticəyə necə təsir edir?",
            "Baseline nə üçün lazımdır?",
            "Hansı augmentation-lar uyğundur?",
        ],
    ),
    day(
        "CV layihəsi II: təlim, qiymətləndirmə, demo",
        [
            "Transfer learning və hiperparametr seçimi",
            "Səhv analizi (hansı şəkillərdə səhv)",
            "Demo qurmaq (Gradio/Streamlit)",
            "Layihəni sənədləşdirmək",
        ],
        [
            yt("CV modelini yaxşılaşdırmaq", "Nicholas Renotte", "40 d", "improve computer vision model accuracy"),
            yt("CV demo qurmaq", "Roboflow", "30 d", "computer vision demo streamlit gradio"),
        ],
        [
            doc("Gradio sənədləri", "gradio.app", "https://www.gradio.app/docs"),
            doc("Papers with Code → HF Papers", "huggingface.co", HF_PAPERS),
        ],
        [
            "Modeli yaxşılaşdır (augmentation + transfer learning)",
            "Metrikaları əvvəlki nəticə ilə müqayisə et",
            "Gradio ilə demo qur və deploy et",
            "README-də nəticələr, qrafiklər və növbəti addımlar yaz",
        ],
        "Canlı CV demo + GitHub-da `computer-vision-project` reposu",
        [
            "Modeli nə qədər yaxşılaşdırdın?",
            "Hansı səhvlər qaldı?",
            "Demo-nu necə daha faydalı etmək olar?",
        ],
    ),
]

weeks = [
    {
        "focus": "Şəkil emalı və deteksiya",
        "project": "Obyekt aşkarlama layihəsi: öz dataset-ində YOLO ilə təlim (100+ annotasiya edilmiş şəkil)",
        "quiz": "OpenCV, feature matching, IoU/mAP, YOLO və seqmentasiya üzrə 10 sual",
    },
    {
        "focus": "Transformer-lər, video və deploy",
        "project": "CV demo: ONNX + FastAPI ilə real-time inference servisi və canlı demo linki",
        "quiz": "ViT, CLIP, zero-shot CV, tracking və ONNX üzrə 10 sual",
    },
]

PHASE = phase(
    7,
    "Kompüter görmə əsasları",
    "Şəkil emalı, deteksiya, seqmentasiya, ViT/CLIP və CV modelini deploy etmək bacarığı.",
    "36-41 saat",
    weeks,
    days,
)
