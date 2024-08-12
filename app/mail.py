import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    # Mailpit サーバーの情報
    smtp_server = "mail"
    smtp_port = 1025  # MailpitのデフォルトのSMTPポート

    from_email = "your_email@example.com"  # 送信元のメールアドレス

    # メールの作成
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        # SMTPサーバーに接続
        server = smtplib.SMTP(smtp_server, smtp_port)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        print("メールが送信されました")
    except Exception as e:
        print(f"メール送信中にエラーが発生しました: {e}")
    finally:
        server.quit()


if __name__ == "__main__":
    # 使用例
    send_email("Test Subject", "This is the body of the email", "recipient@example.com")
