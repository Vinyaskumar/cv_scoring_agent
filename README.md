# CV Scoring Agent 🧒📄

An automated Python-based tool that fetches resumes from your email inbox, parses their content, scores them against a defined set of criteria, and optionally sends feedback — all without manual intervention!

---

## 💡 Features

- 📥 **Email Integration:**  
  Automatically fetches resumes from your email account using IMAP.

- 🔍 **Resume Parsing:**  
  Extracts structured information from PDF resumes for easy evaluation.

- ✅ **Scoring System:**  
  Assigns scores to resumes based on your pre-configured rules and templates.

- 💌 **Feedback Automation:**  
  Sends feedback emails directly to candidates (optional).

---

## ⚙️ Setup

1. Clone this repo:

```bash
git clone https://github.com/your-username/cv_scoring_agent.git
cd cv_scoring_agent
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure your environment:

- Create a `.env` file or securely set the following:
    ```bash
    EMAIL_USER=your_email@gmail.com
    EMAIL_PASS=your_app_password
    RESUME_FOLDER="target_folder"
    ```
> ⚠️ If you use Gmail:  
> Enable **2-Step Verification** and generate an **App Password** to avoid authentication issues.

4. Run the program:

```bash
python main.py
```

---

## 🗃️ Project Structure

```
cv_scoring_agent/
├── data/
│   └── resumes/
├── src/
│   ├── email_handler.py
│   ├── resume_parser.py
│   ├── scorer.py
│   └── feedback_sender.py
└── main.py
```

---

## 🚀 Usage

1. Place resumes in your email (or manually in `data/resumes/`).
2. Run the script — it will:
   - Fetch resumes
   - Parse and score them
   - Output results
   - Optionally send feedback.

---

## 💪 Contributing

PRs and suggestions are always welcome!  
Fork it, create a feature branch, and submit a pull request.

---

## ⚠️ Disclaimer

This project is intended for educational and personal recruitment assistance only.  
Handle personal data responsibly and ensure GDPR compliance when using real candidate data.

> ‼️ **Note:**
> The resumes uploaded and used in this project are **my personal resumes** and are strictly not to be used for any other purpose.
> The email ID configured is **my personal email** and should not be used or accessed for any other purpose.

---

## 📬 Contact

Created by [Vinyas Kumar](https://github.com/Vinyaskumar) — feel free to reach out!

