import imaplib
import email
import os

def fetch_resumes(email_user, email_pass, output_folder):
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(email_user, email_pass)
    imap.select("INBOX")

    status, messages = imap.search(None, 'ALL')
    for num in messages[0].split():
        typ, msg_data = imap.fetch(num, '(RFC822)')
        msg = email.message_from_bytes(msg_data[0][1])

        for part in msg.walk():
            if part.get_content_maintype() == 'multipart': continue
            if part.get('Content-Disposition') is None: continue

            filename = part.get_filename()
            if filename and (filename.endswith('.pdf') or filename.endswith('.docx')):
                filepath = os.path.join(output_folder, filename)
                with open(filepath, 'wb') as f:
                    f.write(part.get_payload(decode=True))

    imap.logout()
