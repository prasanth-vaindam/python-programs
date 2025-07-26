import smtplib
from email.message import EmailMessage
import os

# CONFIGURE THESE
SENDER_EMAIL = "contactyourcomputersir@gmail.com"
APP_PASSWORD = "bcpcwqagwmvavjhf"  # App password from Google Account settings
RECEIVER_EMAIL = "abhilashvarma09@gmail.com"  # can be same as sender
SUBJECT = "📊 Weekly Math Tables Report - Geetu"
CHART_FILES = ["table_mistakes_chart.png", "slow_responses_chart.png"]


def get_report_summary():
    # Load and reuse the generator logic from previous step
    from generate_weekly_report import read_mistakes, read_slow_responses, read_player_scores

    lines = ["📊 WEEKLY MATH TABLE REPORT", "========================================"]

    # Mistakes
    mistakes = read_mistakes()
    if mistakes:
        lines.append("\n❌ Tables Most Missed:")
        for t, count in sorted(mistakes.items(), key=lambda x: -x[1]):
            lines.append(f" - Table {t}: {count} mistake(s)")
    else:
        lines.append("\n✅ No mistakes recorded.")

    # Slow responses
    slows = read_slow_responses()
    if slows:
        lines.append("\n🐢 Tables Answered Slowly:")
        for t, count in sorted(slows.items(), key=lambda x: -x[1]):
            lines.append(f" - Table {t}: {count} slow response(s)")
    else:
        lines.append("\n🚀 All answers were fast enough!")

    # Player summary
    stats = read_player_scores()
    if stats:
        lines.append("\n👤 Player Stats:")
        lines.append(f"{'Name':<12} {'Games':<6} {'Avg Stars':<10} {'Avg Time (s)':<12}")
        for player, data in stats.items():
            avg_stars = data["total_stars"] / data["games"]
            avg_time = data["total_time"] / data["games"]
            lines.append(f"{player:<12} {data['games']:<6} {avg_stars:<10.2f} {avg_time:<12.2f}")
    else:
        lines.append("\n📁 No player scores found.")

    return "\n".join(lines)


# Email sender for weekly report
def send_email():
    print("📤 Sending email report...")

    msg = EmailMessage()
    msg['Subject'] = SUBJECT
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg.set_content(get_report_summary("prasanth"))

    # Attach chart images
    for file in CHART_FILES:
        if os.path.exists(file):
            with open(file, 'rb') as f:
                file_data = f.read()
                msg.add_attachment(file_data, maintype='image', subtype='png', filename=file)
        else:
            print(f"⚠️ File not found, skipping attachment: {file}")

    # Send the email using Gmail SMTP
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER_EMAIL, APP_PASSWORD)
            smtp.send_message(msg)
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")


# Run the email sender
send_email()
