import os
import pandas as pd
from src import email_handler, resume_parser, scorer, feedback_sender

# --- Config ---
EMAIL_USER = 'Vinyaskumar11@gmail.com'
EMAIL_PASS = 'mcaw zkni gryw uioz'
RESUME_FOLDER = './data/resumes'
SENDER_EMAIL = EMAIL_USER
SENDER_PASSWORD = EMAIL_PASS

def main():
    os.makedirs(RESUME_FOLDER, exist_ok=True)
    os.makedirs('./logs', exist_ok=True)

    print("📥 Step 1: Fetching resumes...")
    email_handler.fetch_resumes(EMAIL_USER, EMAIL_PASS, RESUME_FOLDER)

    files = os.listdir(RESUME_FOLDER)
    print(f"🔍 Found {len(files)} files in resume folder.")

    processed = []
    for file in files:
        file_path = os.path.join(RESUME_FOLDER, file)
        print(f"⚙️ Processing file: {file_path}")
        
        try:
            text = resume_parser.extract_text(file_path)
            masked_text = resume_parser.mask_email(text)

            score = scorer.calculate_score(masked_text)

            name = "Candidate"
            recipient = "your_test_email@example.com"  # replace with your email for testing

            feedback_sender.send_feedback(SENDER_EMAIL, SENDER_PASSWORD, recipient, name, score)

            processed.append({'Name': name, 'Email': '[masked]', 'Score': score})
            print(f"✅ Finished: {file}")
        except Exception as e:
            print(f"❌ Error processing {file}: {e}")

    if processed:
        df = pd.DataFrame(processed)
        df.to_csv('./logs/processed_log.csv', mode='a', index=False, header=not os.path.exists('./logs/processed_log.csv'))
        print("✅ Log file written.")
    else:
        print("⚠️ No resumes were processed.")

if __name__ == '__main__':
    main()
