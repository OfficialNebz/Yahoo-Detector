import datetime
import time
import sys
import json

def save_json_log(score, evidence):
    log_data = {
        'timestamp': str(datetime.datetime.now()),
        "threat_level": score,
        "triggers": evidence
    }
    with open('security_audit.log', 'a') as json_file:
        json_file.write(json.dumps(log_data) + '\n')

def scan_effect():
    print("\n[+]INITIALIZING NEURAL SCAN\n", end="")

    for i in range(4):
        time.sleep(0.5)
        print('.', end="")
        sys.stdout.flush()
    time.sleep(1)
    print('\nACCESS GRANTED')

#Group 1: The Bait (Lures the target in)
bait_words = ['congratulations', 'promo', 'winner', 'cash', 'gift', 'lottery', 'inheritance', 'fund', 'prize']

#Group 2: The "Fear" (Makes you panic)
urgency_words = ['blocked', 'deactivate', 'suspended', 'unauthorized', 'urgent', 'immediately', 'expires','24 hours']

#Group 3: What they want to steal
sensitive_words = ['bvn', 'pin', 'otp', 'password', 'token', 'ssn', 'login', 'verify']

#Group 4: The "Authority" (Fake senders)
authority_words = ['cbn', 'efcc', 'irs', 'police', 'customer care', 'admin']

all_words = authority_words + urgency_words + sensitive_words + bait_words

def calculate_risk(message):
    evidence = []
    risk_score = 0

    for word in bait_words:
        if word in message:
            risk_score += 10
            evidence.append(word)

    for word in urgency_words:
        if word in message:
            risk_score += 20
            evidence.append(word)

    for word in sensitive_words:
        if word in message:
            risk_score += 50
            evidence.append(word)

    for word in authority_words:
        if word in message:
            risk_score += 70
            evidence.append(word)

    return risk_score, evidence


def save_log(score, evidence):
    timestamp = datetime.datetime.now()
    with open('scam_log.txt', 'a') as log:
        log_entry = f"[{timestamp}]. RISK: {score}% | Evidence: {evidence}\n"
        log.write(log_entry)
    print("💾 EVIDENCE SAVED to scam_log.txt and security_audit.log")

def start_app():
    print(f"\n--- 🛡️ NIGERIAN CYBER DEFENSE CONSOLE V3.1 🛡️ ---")
    while True:
        user_input = input('Enter SMS to scan: ').lower()

        if user_input == 'exit':
            print('Shutting down...')
            break
        total_risk, found_evidence= calculate_risk(user_input)
        scan_effect()
        if total_risk > 0:
            if total_risk >= 100:
                total_risk = 100
                print(f"\n ---RISK REPORT: {total_risk}%! \nCRITICAL THREAT: IMMEDIATE ACTION IS REQUIRED---")
                print(f"\n TRIGGER WORDS FOUND: {found_evidence}")

            elif total_risk >= 80:
                print(f"\n ---RISK REPORT: {total_risk}%! \nCRITICAL THREAT: IMMEDIATE ACTION IS REQUIRED---")
                print(f"\n TRIGGER WORDS FOUND: {found_evidence}")

            elif total_risk >= 50:
                print(f"\n ---RISK REPORT: {total_risk}%! \nHIGH RISK: DO NOT CLICK LINKS---")
                print(f"\n TRIGGER WORDS FOUND: {found_evidence}")

            elif total_risk >= 20:
                print(f"\n ---RISK REPORT: {total_risk}%! \nMODERATE RISK: BE CAUTIOUS---")
                print(f"\n TRIGGER WORDS FOUND: {found_evidence}")

            save_log(total_risk, found_evidence)
            save_json_log(total_risk, found_evidence)
        else:
            print('System Clean')

        print('-' * 40)

start_app()