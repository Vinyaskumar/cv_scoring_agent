import smtplib
from email.mime.text import MIMEText

def send_feedback(sender_email, sender_password, recipient, name, score):
    feedback = f"""
    Dear {name},

    ✅ Your CV Score: {score}/30

    {score >= 20 and 'Excellent profile for AI roles!' or 'Consider improving your AI project portfolio.'}

    Regards,
    AI Recruitment Bot
    """
    msg = MIMEText(feedback)
    msg['Subject'] = "Your Resume Evaluation Result"
    msg['From'] = sender_email
    msg['To'] = recipient

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient, msg.as_string())
    server.quit()
