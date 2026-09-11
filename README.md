<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=6,11,20&height=120&animation=fadeIn" width="100%"/>

<div align="center">

# Md Rayyan

**Machine Learning Engineer in training** — Applied ML Systems · Deep Learning · MLOps

Building ML systems that hold up past the notebook: a retrieval pipeline that checks its own claims, training infrastructure that survives cloud interruptions, and a diagnostic ML pipeline built specifically to avoid the data-leakage mistakes that inflate most student results.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/md-rayyan/)
[![Email](https://img.shields.io/badge/Email-8B5CF6?style=flat-square&logo=gmail&logoColor=white)](mailto:rayyan1652@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Rayyan-mohammed)
&nbsp;&nbsp;📍 Hyderabad, India

</div>

<br/>

## 👋 About

Final-year B.Tech CSE (Data Science) student at NMIMS University, Hyderabad (2023–2027). I spend more time in `model.py` and `docker-compose.yml` than in lecture slides.

My focus is applied ML engineering — not just training a model that scores well offline, but building the retrieval, evaluation, and serving layer around it that makes it trustworthy somewhere other than a notebook. Recent work spans retrieval-augmented generation with claim-level faithfulness checking, ML training infrastructure that survives AWS Spot interruptions, and a diagnostic pipeline built around getting cross-validation right.

I lead the **Code IT Club at NMIMS**, serve as a **Google Cloud Student Ambassador**, and was part of the winning team at **TechFest 2025**.

---

## 🧠 Stack

**AI / ML**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-1a1a2e?style=flat-square)
![SHAP](https://img.shields.io/badge/SHAP-8B5CF6?style=flat-square)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=black)

**LLM / RAG**

![LangGraph](https://img.shields.io/badge/LangGraph-1a1a2e?style=flat-square)
![FAISS](https://img.shields.io/badge/FAISS-1a1a2e?style=flat-square)
![ChromaDB](https://img.shields.io/badge/ChromaDB-1a1a2e?style=flat-square)
![Claude API](https://img.shields.io/badge/Claude%20API-8B5CF6?style=flat-square)

**Backend & Serving**

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white)

**Cloud & Infrastructure**

![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonaws&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=flat-square&logo=googlecloud&logoColor=white)

**MLOps & Tooling**

![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)

---

## 🚀 Featured Projects

### 🗣️ CodeSwitch-Verify — Faithfulness-Checked RAG
**[Repository](https://github.com/Rayyan-mohammed/HinglishRAG-Faith)**

![Python](https://img.shields.io/badge/Python-8B5CF6?style=flat-square) ![FAISS](https://img.shields.io/badge/FAISS-8B5CF6?style=flat-square) ![Claude API](https://img.shields.io/badge/Claude%20API-8B5CF6?style=flat-square) ![RAG](https://img.shields.io/badge/RAG-8B5CF6?style=flat-square)

![“](https://img.shields.io/badge/%E2%80%9C-8B5CF6?style=flat-square)
> RAG chatbots answering Hinglish questions about government schemes sound confident — but nothing checks whether each claim is actually true, in a domain where a wrong eligibility answer has real consequences.

- **Built:** decomposes every answer into atomic claims and verifies each independently against retrieved evidence — supported / contradicted / unverifiable — via LLM-as-judge (3-sample majority vote). `bge-m3` + FAISS retrieval, Claude Haiku 4.5, design decisions tracked in ADRs.

---

### 🏥 BharatHealth Analyst — LLM Agent over National Health Survey Data
**[Repository](https://github.com/Rayyan-mohammed/aarogya-lens)**

![Python](https://img.shields.io/badge/Python-0EA5E9?style=flat-square) ![LangGraph](https://img.shields.io/badge/LangGraph-0EA5E9?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-0EA5E9?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-0EA5E9?style=flat-square) ![ChromaDB](https://img.shields.io/badge/ChromaDB-0EA5E9?style=flat-square)

![“](https://img.shields.io/badge/%E2%80%9C-0EA5E9?style=flat-square)
> India's NFHS-5 health survey (706 districts × 448 indicators) needs SQL and an analyst to query today — public health questions shouldn't require that.

- **Built:** a LangGraph ReAct agent with 7 tools (semantic search, SQL/pandas query, charting, trend & correlation analysis) over a merged NFHS-5 + NFHS-4 dataset in ChromaDB. FastAPI backend, Next.js frontend, CI at 93% coverage.
- **Honestly:** the full accuracy benchmark isn't finished yet — blocked twice by rate limits. Said plainly rather than rounded up.

---

### 🎙️ Parkinson's Detection via Acoustic Biomarkers
**[Repository](https://github.com/Rayyan-mohammed/Parkinson)**

![Python](https://img.shields.io/badge/Python-F43F5E?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F43F5E?style=flat-square) ![XGBoost](https://img.shields.io/badge/XGBoost-F43F5E?style=flat-square) ![SHAP](https://img.shields.io/badge/SHAP-F43F5E?style=flat-square) ![HuggingFace](https://img.shields.io/badge/HuggingFace-F43F5E?style=flat-square)

![“](https://img.shields.io/badge/%E2%80%9C-F43F5E?style=flat-square)
> Most student medical-ML projects inflate accuracy via subject-level data leakage — a single patient's samples land on both sides of the train/test split.

- **Built:** strict subject-level `GroupKFold` cross-validation, hyperparameter search bounded to inner folds, SMOTE applied only within training folds, `wav2vec2` embeddings + SHAP explainability (global + per-patient).

| Model | Accuracy | ROC-AUC |
|---|---|---|
| MLP | 0.756 ± 0.057 | 0.851 ± 0.116 |
| XGBoost | 0.760 ± 0.114 | 0.793 ± 0.204 |

*(subject-isolated CV — wide confidence intervals reported honestly rather than hidden)*

---

### ☁️ Argus — Spot-Resilient ML Training Orchestrator *(team project)*
**[Repository](https://github.com/Rayyan-mohammed/Argus-Spot_Resilient_ML_Training_Orchestrator)**

![Kubernetes](https://img.shields.io/badge/Kubernetes-F59E0B?style=flat-square) ![PyTorch](https://img.shields.io/badge/PyTorch-F59E0B?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-F59E0B?style=flat-square) ![Terraform](https://img.shields.io/badge/Terraform-F59E0B?style=flat-square) ![AWS EKS](https://img.shields.io/badge/AWS%20EKS-F59E0B?style=flat-square) ![Grafana](https://img.shields.io/badge/Grafana-F59E0B?style=flat-square)

![“](https://img.shields.io/badge/%E2%80%9C-F59E0B?style=flat-square)
> AWS Spot instances are 70–90% cheaper than on-demand but reclaimable with 2 minutes' notice — a long training job loses everything since its last checkpoint.

- **Built:** a Transformer predicts interruption risk from Spot price history; a `kopf` Kubernetes operator checkpoints and reschedules the training pod before the interruption lands; the job resumes automatically.
- **Result:** validated on a real AWS EKS cluster — survived a live Spot drain with a ~75s recovery. Predictive approach: **zero wasted compute** vs. 202s unprotected, **~12× faster** recovery than reactive. Honest limitations documented. Targeting a NeurIPS ML4Sys 2026 workshop poster.
- **My part:** built with a teammate — Helm chart deployment, stress testing & cost analysis, risk-threshold bug fixes.

---

### 💰 OptiPrice — Dynamic Pricing Engine
**[Repository](https://github.com/Rayyan-mohammed/OptiPrice)** · **[Live App ↗](https://optiprice-dynamic-pricing-agent.streamlit.app/)**

![Python](https://img.shields.io/badge/Python-10B981?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-10B981?style=flat-square) ![SciPy](https://img.shields.io/badge/SciPy-10B981?style=flat-square) ![SHAP](https://img.shields.io/badge/SHAP-10B981?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-10B981?style=flat-square)

![“](https://img.shields.io/badge/%E2%80%9C-10B981?style=flat-square)
> Retail pricing is often static or rule-based, ignoring price elasticity, competitor moves, and margin trade-offs.

- **Built:** a SciPy-constrained profit/revenue optimizer, a Monte Carlo 30-day A/B test simulator, SHAP-explained pricing recommendations, and live competitor pricing via the Mercado Libre API.

---

## 🧩 Additional Work

| Project | What it is | Stack |
|---|---|---|
| [ApplyForge](https://github.com/Rayyan-mohammed/ApplyForge) | Human-in-the-loop AI agent that discovers internships, ranks them against a resume, and drafts applications for review over Telegram. Deployed on EC2, running continuously. | Python · LLM agents |
| [DNA Sequence Compression](https://github.com/Rayyan-mohammed/DNA-sequence-compression) ([live](https://dna-sequence-compression.streamlit.app/)) | Genomic data compression via LZ77, Burrows-Wheeler Transform, and suffix trees, with live NCBI data pulls and 3D protein structure rendering. | Python · Streamlit |
| [Route Resilience](https://github.com/Rayyan-mohammed/Urban-Route-Resilience) *(team, ISRO hackathon)* | Occlusion-robust road extraction from satellite imagery (SegFormer) plus graph-theoretic network resilience analysis. | Python · PyTorch · NetworkX |
| [Traffic Sign Recognition](https://github.com/Rayyan-mohammed/Traffic-Sign-Recognition-System) | Real-time 43-class CNN traffic sign classifier with webcam inference. | TensorFlow/Keras · OpenCV · Streamlit |
| [Phishing URL Detector](https://github.com/Rayyan-mohammed/Phishing-Attack-Detection-System) | Random Forest classifier over 15+ URL features, served via Flask. | scikit-learn · Flask |

---

## 🎯 How I Approach ML Problems

- **Leakage is the default failure mode.** The Parkinson's project exists specifically to get subject-level cross-validation right, because most student medical-ML projects don't.
- **An unverified result isn't a result.** Argus documents its limitations next to its wins. aarogya-lens says plainly which benchmark isn't finished instead of skipping it.
- **Explainability isn't optional.** SHAP shows up wherever a model makes a decision that needs to be justified — diagnosis, pricing.
- **Decisions get written down.** ADRs in CodeSwitch-Verify and Argus record *why* a design changed, not just what it is now.

---

## 🔭 Currently Exploring

- Production ML infrastructure — extending Argus toward real (not injected) Spot interruption testing
- Evaluation methodology for RAG and multi-agent LLM systems
- PyTorch and deep learning beyond transfer learning

---

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/md-rayyan/)
[![Email](https://img.shields.io/badge/Email-8B5CF6?style=flat-square&logo=gmail&logoColor=white)](mailto:rayyan1652@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Rayyan-mohammed)

<br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Rayyan-mohammed/Rayyan-mohammed/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Rayyan-mohammed/Rayyan-mohammed/output/github-contribution-grid-snake.svg" />
  <img alt="" src="https://raw.githubusercontent.com/Rayyan-mohammed/Rayyan-mohammed/output/github-contribution-grid-snake.svg" width="80%" />
</picture>

</div>

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=6,11,20&height=60" width="100%"/>
